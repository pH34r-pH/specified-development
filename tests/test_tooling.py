"""Independent diagnostics, byte-contract and invocation checks."""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import bundle_common as common
from tools import bundle_review as review
from tools import bundle_validation as validator
from tools import validate_foundation as foundation

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "tests/fixtures/tooling/authority-serialization-v1.json"


class FingerprintContractTests(unittest.TestCase):
    def test_fixed_authority_vectors_bind_exact_bytes(self):
        vectors = json.loads(VECTORS.read_text())["vectors"]
        for vector in vectors:
            with self.subTest(vector=vector["id"]):
                raw = vector["serialized_utf8"].encode("utf-8")
                self.assertFalse(raw.endswith(b"\n"))
                self.assertEqual(hashlib.sha256(raw).hexdigest(), vector["sha256"])
                self.assertEqual(validator.authority_fingerprint(vector["value"]), vector["sha256"])
        authority = json.loads((ROOT / "tests/fixtures/bundle/bundle.json").read_text())["authority"]
        self.assertEqual(authority, vectors[0]["value"])

    def test_review_bytes_have_explicit_utf8_and_newline(self):
        self.assertEqual(review.canonical({"z": ["é", "a"], "a": "☃"}),
                         '{"a":"☃","z":["é","a"]}\n'.encode())


class ToolDiagnosticsTests(unittest.TestCase):
    def run_main(self, main, argv, function, exception):
        stdout, stderr = io.StringIO(), io.StringIO()
        with (patch.object(sys, "argv", argv), patch(function, side_effect=exception),
              contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr)):
            result = main()
        return result, stdout.getvalue(), stderr.getvalue()

    def test_bundle_input_failure_keeps_typed_diagnostic(self):
        result, stdout, stderr = self.run_main(
            validator.main, ["validator", "bundle.json", "--authority-sha256", "0" * 64],
            "tools.bundle_validation.validate_bundle", common.ValidationError("SOURCE_FIELDS: malformed source"))
        self.assertEqual(result, 2)
        self.assertEqual(stdout, "")
        self.assertIn("SOURCE_FIELDS", stderr)
        self.assertNotIn("INTERNAL_ERROR", stderr)

    def test_internal_fault_is_distinct_and_debug_exposes_traceback(self):
        for debug in (False, True):
            with self.subTest(debug=debug):
                args = ["validator", "bundle.json", "--authority-sha256", "0" * 64]
                if debug:
                    args.append("--debug")
                result, stdout, stderr = self.run_main(
                    validator.main, args, "tools.bundle_validation.validate_bundle", KeyError("programming-defect"))
                self.assertEqual(result, 3)
                self.assertEqual(stdout, "")
                self.assertIn("INTERNAL_ERROR", stderr)
                self.assertEqual("Traceback" in stderr, debug)
                self.assertNotIn("BUNDLE invalid", stderr)

    def test_review_debug_supports_global_and_subcommand_positions(self):
        for args in (
            ["review", "--debug", "render", "bundle.json", "--output", "unused"],
            ["review", "render", "bundle.json", "--output", "unused", "--debug"],
        ):
            result, _, stderr = self.run_main(
                review.main, args, "tools.bundle_review.generate", AttributeError("broken invariant"))
            self.assertEqual(result, 3)
            self.assertIn("INTERNAL_ERROR", stderr)
            self.assertIn("Traceback", stderr)

    def test_foundation_keeps_input_exit_and_marks_internal_fault(self):
        result, _, stderr = self.run_main(
            foundation.main, ["foundation", str(ROOT)], "tools.validate_foundation.validate_workspace",
            common.ValidationError("SOURCE_STALE: fixture"))
        self.assertEqual(result, 1)
        self.assertIn("SOURCE_STALE", stderr)
        result, _, stderr = self.run_main(
            foundation.main, ["foundation", str(ROOT), "--debug"], "tools.validate_foundation.validate_workspace",
            TypeError("implementation fault"))
        self.assertEqual(result, 3)
        self.assertIn("Traceback", stderr)

    def test_io_failure_is_not_classified_as_programming_fault(self):
        result, _, stderr = self.run_main(
            review.main, ["review", "expand", "missing.json", "--sha256", "0" * 64, "--output", "unused"],
            "tools.bundle_review.expand", FileNotFoundError("missing input"))
        self.assertEqual(result, 2)
        self.assertIn("IO_ERROR", stderr)
        self.assertNotIn("INTERNAL_ERROR", stderr)


class UntrustedShapeTests(unittest.TestCase):
    def test_unpaired_surrogates_are_typed_input_errors(self):
        for text in ('{"path":"\\ud800"}', '{"\\udfff":"value"}', '["\\ud800"]'):
            with self.subTest(text=text), self.assertRaisesRegex(common.ValidationError, "JSON_UNICODE"):
                common.parse_json(text)
        self.assertEqual(common.parse_json('"\\ud83d\\ude80"'), "🚀")
        with self.assertRaisesRegex(common.ValidationError, "PATH_INVALID"):
            common.safe_relative_path("src/\ud800")

    def test_legacy_review_shapes_fail_with_specific_input_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "spec.md"
            source.write_bytes(b"accepted historical source")
            authority = {"sha256": {"spec.md": hashlib.sha256(source.read_bytes()).hexdigest()}}
            cases = [
                ({"tasks": {}, "authority": []}, "LEGACY_SOURCES"),
                ({"tasks": {}, "authority": None}, "LEGACY_SOURCES"),
                ({"tasks": {"T1": []}, "authority": authority}, "LEGACY_TASK"),
                ({"tasks": {"T1": {"parents": [1]}}, "authority": authority}, "LEGACY_TASK"),
                ({"tasks": {}, "authority": authority, "x_distribution": []}, "LEGACY_METADATA"),
                ({"tasks": {"T1": {}}, "authority": authority, "x_distribution": {"task_metadata": {"T1": {"title": []}}}}, "LEGACY_METADATA"),
            ]
            for payload, code in cases:
                with self.subTest(code=code, payload=payload):
                    (root / "legacy.json").write_text(json.dumps(payload))
                    with self.assertRaisesRegex(common.ValidationError, code):
                        review.generate(root, "legacy.json", legacy=True)

    def test_lossless_detail_shapes_fail_before_output_creation(self):
        cases = [
            ([], "DETAIL_SHAPE"),
            ({"schema_version": True, "kind": "lossless-bundle-inputs"}, "DETAIL_VERSION"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [None]}, "DETAIL_RECORD"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [{"path": "a"}]}, "DETAIL_RECORD"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [{"path": [], "sha256": "0" * 64, "base64": ""}]}, "PATH_INVALID"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [{"path": "a", "sha256": [], "base64": ""}]}, "DETAIL_DIGEST"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [{"path": "a", "sha256": "0" * 64, "base64": 3}]}, "DETAIL_BASE64"),
            ({"schema_version": 1, "kind": "lossless-bundle-inputs", "inputs": [{"path": "a", "sha256": "0" * 64, "base64": "not base64!"}]}, "DETAIL_BASE64"),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            detail, output = root / "detail.json", root / "output"
            for value, code in cases:
                with self.subTest(code=code, value=value):
                    raw = json.dumps(value).encode()
                    detail.write_bytes(raw)
                    with self.assertRaisesRegex(common.ValidationError, code):
                        review.expand(detail, hashlib.sha256(raw).hexdigest(), output)
                    self.assertFalse(output.exists())

    def test_bundle_malformed_records_receive_input_errors(self):
        fixture = ROOT / "tests/fixtures/bundle-v2"
        if not fixture.exists():
            fixture = ROOT / "tests/fixtures/bundle"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "input"
            shutil.copytree(fixture, root)
            bundle = json.loads((root / "bundle.json").read_text())
            if bundle["schema_version"] == 1:
                # A newly authored diagnostic fixture, not a historical-byte check.
                bundle["x_bundle"]["versions"]["runtime"] = validator.runtime_identity()
            mutations = [
                lambda b: b["x_bundle"]["sources"]["authority.md"].pop("kind"),
                lambda b: b["x_bundle"]["sources"]["spec.md"].update(path=[]),
                lambda b: b["x_bundle"]["sources"]["spec.md"].update(kind=[]),
                lambda b: b["x_bundle"]["tests"]["CASE1"].update(command=[]),
                lambda b: b["x_bundle"]["task_traces"]["T1"].update(plan=[]),
            ]
            for index, mutate in enumerate(mutations):
                with self.subTest(mutation=index):
                    candidate = copy.deepcopy(bundle)
                    mutate(candidate)
                    (root / "bundle.json").write_text(json.dumps(candidate))
                    pin = (validator.reviewed_fingerprint(candidate) if candidate["schema_version"] == 2
                           else validator.authority_fingerprint(candidate["authority"]))
                    with self.assertRaises(common.ValidationError):
                        validator.validate_bundle(root, "bundle.json", expected_authority_sha256=pin)


class InvocationTests(unittest.TestCase):
    def test_import_error_inside_package_is_not_retried_as_top_level_import(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "tools"
            package.mkdir()
            (package / "__init__.py").write_text("")
            shutil.copy2(ROOT / "tools/bundle_validation.py", package / "bundle_validation.py")
            (package / "bundle_common.py").write_text("raise ImportError('inside-module-failure')\n")
            (root / "bundle_common.py").write_text("raise RuntimeError('wrong-fallback-import')\n")
            result = subprocess.run([sys.executable, "-m", "tools.bundle_validation", "--help"],
                                    cwd=root, capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inside-module-failure", result.stderr)
            self.assertNotIn("wrong-fallback-import", result.stderr)

    def test_portable_three_file_copy_runs_without_site_packages(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("bundle_common.py", "bundle_validation.py", "bundle_review.py"):
                shutil.copy2(ROOT / "tools" / name, root / name)
            for name in ("bundle_validation.py", "bundle_review.py"):
                result = subprocess.run([sys.executable, "-S", str(root / name), "--help"],
                                        cwd=root, capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("--debug", result.stdout)


if __name__ == "__main__":
    unittest.main()
