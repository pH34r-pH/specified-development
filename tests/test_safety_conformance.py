"""Shared vectors with optional adapters to exact local consumer checkouts.

Set SPECIFIED_EXPERIMENT_COMPILER_ROOT and SPECIFIED_LONG_HAUL_ROOT to run the
cross-repository checks. The test never downloads or modifies those repositories.
"""
from __future__ import annotations

import hashlib
import importlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import bundle_common as common
from tools import bundle_review as review

ROOT = Path(__file__).resolve().parents[1]
CORPUS = json.loads((ROOT / "tests/fixtures/safety/conformance.json").read_text())


def accepts(function, value, errors):
    try:
        function(value)
    except errors:
        return False
    return True


def expand_names(names):
    """Exercise actual materialization preflight rather than a copied matcher."""
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        payload = {"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [
            {"path": name, "sha256": hashlib.sha256(b"").hexdigest(), "base64": ""}
            for name in names
        ]}
        raw = json.dumps(payload).encode()
        detail = root / "detail.json"
        detail.write_bytes(raw)
        review.expand(detail, hashlib.sha256(raw).hexdigest(), root / "expanded")


class LocalSafetyVectors(unittest.TestCase):
    def test_strict_json_vectors(self):
        for case in CORPUS["json"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(accepts(common.parse_json, case["text"], common.ValidationError), case["accept"])
        with self.assertRaisesRegex(common.ValidationError, "JSON_INVALID"):
            common.parse_json(b"\xff")

    def test_relative_path_vectors(self):
        for case in CORPUS["paths"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(accepts(common.safe_relative_path, case["path"], common.ValidationError), case["specified"])

    def test_collection_vectors_use_actual_expansion_preflight(self):
        for case in CORPUS["collections"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(accepts(expand_names, case["paths"], common.ValidationError), case["accept"])

    def test_confined_files_reject_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "real").write_text("safe")
            (root / "link").symlink_to(root / "real")
            with self.assertRaisesRegex(common.ValidationError, "PATH_ESCAPE"):
                common.confined_file(root, "link")


@unittest.skipUnless(os.environ.get("SPECIFIED_EXPERIMENT_COMPILER_ROOT")
                     and os.environ.get("SPECIFIED_LONG_HAUL_ROOT"), "supply exact local consumer checkouts for cross-repository conformance")
class CrossRepositorySafetyVectors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler_root = Path(os.environ["SPECIFIED_EXPERIMENT_COMPILER_ROOT"]).resolve(strict=True)
        cls.long_haul_root = Path(os.environ["SPECIFIED_LONG_HAUL_ROOT"]).resolve(strict=True)
        for name, root in (("experiment_compiler", cls.compiler_root), ("long_haul", cls.long_haul_root)):
            revision = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                      capture_output=True, text=True, check=True).stdout.strip()
            if revision != CORPUS["sources"][name]["commit"]:
                raise AssertionError(f"{name}: expected the exact reviewed source revision")
            subprocess.run(["git", "-C", str(root), "diff", "--quiet", "HEAD", "--"], check=True)
        cls.original_path = sys.path[:]
        sys.path[:0] = [str(cls.compiler_root), str(cls.long_haul_root / "src")]
        original_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            cls.compiler = importlib.import_module("experiment_compiler.core")
            cls.repository_models = importlib.import_module("long_haul.work.repository_models")
            cls.repository_git = importlib.import_module("long_haul.work.repository_git")
        finally:
            sys.dont_write_bytecode = original_bytecode
        if Path(cls.compiler.__file__).resolve() != cls.compiler_root / "experiment_compiler/core.py":
            raise AssertionError("experiment_compiler import did not use the supplied checkout")
        if Path(cls.repository_git.__file__).resolve() != cls.long_haul_root / "src/long_haul/work/repository_git.py":
            raise AssertionError("long_haul import did not use the supplied checkout")

    @classmethod
    def tearDownClass(cls):
        sys.path[:] = cls.original_path

    def test_compiler_json_vectors(self):
        for case in CORPUS["json"]:
            if case.get("known_gap") == "experiment_compiler":
                continue  # The independent expected-failure test below records this gap.
            with self.subTest(case=case["id"]):
                self.assertEqual(accepts(self.compiler.json_value, case["text"].encode(), self.compiler.PackageError), case["accept"])

    @unittest.expectedFailure
    def test_compiler_numeric_overflow_gap_is_owned_by_155(self):
        case = next(case for case in CORPUS["json"] if case["id"] == "numeric-overflow")
        self.assertFalse(accepts(self.compiler.json_value, case["text"].encode(), self.compiler.PackageError))

    def test_each_consumer_retains_its_path_policy(self):
        for case in CORPUS["paths"]:
            with self.subTest(case=case["id"], consumer="experiment_compiler"):
                self.assertEqual(accepts(self.compiler.safe_path, case["path"], self.compiler.PackageError), case["experiment_compiler"])
            with self.subTest(case=case["id"], consumer="long_haul"):
                self.assertEqual(accepts(self.repository_models.repository_path, case["path"], ValueError), case["long_haul"])

    def test_compiler_collection_vectors(self):
        for case in CORPUS["collections"]:
            if case.get("known_gap") == "experiment_compiler":
                continue
            with self.subTest(case=case["id"]):
                self.assertEqual(accepts(self.compiler.unique_paths, case["paths"], self.compiler.PackageError), case["accept"])

    @unittest.expectedFailure
    def test_compiler_normalization_gap_is_owned_by_155(self):
        case = next(case for case in CORPUS["collections"] if case["id"] == "normalization-collision")
        self.assertFalse(accepts(self.compiler.unique_paths, case["paths"], self.compiler.PackageError))

    def test_compiler_and_git_readers_reject_links_at_their_own_boundary(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "real").write_text("safe")
            (root / "link").symlink_to(root / "real")
            with self.assertRaises(self.compiler.PackageError):
                self.compiler.bounded_read(root / "link")
            reader = self.repository_git._GitObjects(root)
            for mode in ("120000", "160000"):
                with self.subTest(mode=mode), self.assertRaises(PermissionError):
                    reader.blob((mode, "0" * 40))


if __name__ == "__main__":
    unittest.main()
