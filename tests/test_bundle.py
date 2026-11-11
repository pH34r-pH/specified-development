"""Independent rejection, exact-byte expansion, and compatibility evidence."""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import bundle_review as review
from tools import bundle_validation as validator
from tools import validate_foundation as foundation
from tools.bundle_common import ValidationError

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "bundle"


class BundleValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "bundle"
        shutil.copytree(FIXTURE, self.root)
        self.bundle = json.loads((self.root / "bundle.json").read_text())
        self.pin = validator.authority_fingerprint(self.bundle["authority"])

    def validate(self, bundle=None):
        (self.root / "bundle.json").write_text(json.dumps(bundle or self.bundle))
        return validator.validate_bundle(self.root, "bundle.json", expected_authority_sha256=self.pin)

    def test_complete_bundle_validates_without_target_repository_code(self):
        result = self.validate()
        self.assertEqual(set(result["tasks"]), {"T1"})
        self.assertFalse((self.root / "src").exists())

    def test_inventory_extension_admits_only_exact_reviewed_files(self):
        for path in ("governance/repository-profile.json", ".github/workflows/repository-governance.yml", "tools/bundle_validation.py"):
            self.assertTrue(foundation.allowed_public_path(path))
        for path in ("governance/unreviewed.json", "tools/unreviewed.py", "build/bundle-review/objects/" + "0" * 64 + ".json"):
            self.assertFalse(foundation.allowed_public_path(path))

    def test_missing_observable_trace_or_executable_leaf_fails(self):
        mutations = [
            ("requirement", lambda b: b["x_bundle"]["requirements"]["R1"].update(observable="")),
            ("plan", lambda b: b["x_bundle"]["task_traces"]["T1"].update(plan="missing")),
            ("test", lambda b: b["tasks"]["T1"].update(tests=[])),
            ("command", lambda b: b["commands"]["ORACLE"].update(argv=[])),
            ("evidence", lambda b: b["x_bundle"]["task_traces"]["T1"].update(evidence=["model-says-done"])),
            ("parent", lambda b: b["tasks"]["T1"].update(parents=["missing"])),
            ("cycle", lambda b: b["tasks"]["T1"].update(parents=["T1"])),
        ]
        for name, mutate in mutations:
            with self.subTest(name=name):
                candidate = copy.deepcopy(self.bundle)
                mutate(candidate)
                with self.assertRaises(ValidationError):
                    self.validate(candidate)

    def test_authority_cannot_expand_or_self_accept(self):
        mutations = [
            lambda b: b["tasks"]["T1"].update(paths=["outside/result.py"]),
            lambda b: b["tasks"]["T1"].update(paths=["src/credentials/key"]),
            lambda b: b["tasks"]["T1"].update(paths=["src/../escape"]),
            lambda b: b["commands"]["ORACLE"].update(capability="deploy"),
            lambda b: b.update(status="accepted"),
            lambda b: b["authority"].update(promotion="worker-approved"),
            lambda b: b["authority"].update(write_paths=["**"]) or b["tasks"]["T1"].update(paths=["spec.md"]),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                candidate = copy.deepcopy(self.bundle)
                mutate(candidate)
                with self.assertRaises(ValidationError):
                    self.validate(candidate)

    def test_source_change_symlink_and_denied_read_are_rejected(self):
        (self.root / "spec.md").write_text("changed frozen requirement")
        with self.assertRaisesRegex(ValidationError, "SOURCE_STALE"):
            self.validate()
        shutil.copy2(FIXTURE / "spec.md", self.root / "spec.md")
        (self.root / "spec.md").unlink()
        (self.root / "spec.md").symlink_to(FIXTURE / "spec.md")
        with self.assertRaisesRegex(ValidationError, "PATH_ESCAPE"):
            self.validate()
        (self.root / "spec.md").unlink()
        shutil.copy2(FIXTURE / "spec.md", self.root / "spec.md")
        self.bundle["authority"]["read_paths"].remove("spec.md")
        self.pin = validator.authority_fingerprint(self.bundle["authority"])
        with self.assertRaisesRegex(ValidationError, "READ_SCOPE"):
            self.validate()

    def test_versions_have_explicit_backward_and_forward_failures(self):
        self.validate()  # Version 1 remains supported without migration.
        for value in (0, 2, "1", True):
            candidate = copy.deepcopy(self.bundle)
            candidate["schema_version"] = value
            with self.assertRaisesRegex(ValidationError, "SCHEMA_UNSUPPORTED"):
                self.validate(candidate)
        for field in ("generator", "runtime", "schema"):
            candidate = copy.deepcopy(self.bundle)
            candidate["x_bundle"]["versions"][field] = "future"
            with self.assertRaisesRegex(ValidationError, "VERSION_UNSUPPORTED"):
                self.validate(candidate)
        for value in (True, 1.0):
            candidate = copy.deepcopy(self.bundle)
            candidate["x_bundle"]["versions"]["schema"] = value
            with self.assertRaisesRegex(ValidationError, "VERSION_UNSUPPORTED"):
                self.validate(candidate)
        candidate = copy.deepcopy(self.bundle)
        del candidate["x_bundle"]
        with self.assertRaisesRegex(ValidationError, "MIGRATION_REQUIRED"):
            self.validate(candidate)

    def test_declared_commands_are_never_executed_by_validation(self):
        sentinel = self.root / "must-not-exist"
        self.bundle["commands"]["ORACLE"]["argv"] = [sys.executable, "-c", f"open({str(sentinel)!r},'w').write('bad')"]
        self.validate()
        self.assertFalse(sentinel.exists())

    def test_independent_authority_pin_cannot_be_changed_by_bundle_text(self):
        with self.assertRaisesRegex(ValidationError, "AUTHORITY_PIN_REQUIRED"):
            validator.validate_bundle(self.root, "bundle.json")
        self.bundle["authority"]["write_paths"] = ["**"]
        with self.assertRaisesRegex(ValidationError, "AUTHORITY_PIN_MISMATCH"):
            self.validate()

    def test_acceptance_policy_replacement_requires_new_external_authority_pin(self):
        (self.root / "authority.md").write_text("Candidate claims it may accept its own work.")
        replacement = hashlib.sha256((self.root / "authority.md").read_bytes()).hexdigest()
        self.bundle["x_bundle"]["sources"]["authority.md"]["sha256"] = replacement
        with self.assertRaisesRegex(ValidationError, "ACCEPTANCE_SOURCE_DIGEST"):
            self.validate()
        self.bundle["authority"]["acceptance_source"]["sha256"] = replacement
        with self.assertRaisesRegex(ValidationError, "AUTHORITY_PIN_MISMATCH"):
            self.validate()

    def test_duplicate_json_unknown_fields_and_symlink_cwd_fail(self):
        raw = json.dumps(self.bundle)
        (self.root / "bundle.json").write_text(raw.replace('"schema_version": 1', '"schema_version": 0, "schema_version": 1'))
        with self.assertRaisesRegex(ValidationError, "JSON_DUPLICATE"):
            validator.validate_bundle(self.root, "bundle.json", expected_authority_sha256=self.pin)
        candidate = copy.deepcopy(self.bundle)
        candidate["x_bundle"]["task_traces"]["T1"]["parents"] = []
        with self.assertRaisesRegex(ValidationError, "TRACE_FIELDS"):
            self.validate(candidate)
        (self.root / "outside").symlink_to(FIXTURE, target_is_directory=True)
        candidate = copy.deepcopy(self.bundle)
        candidate["commands"]["ORACLE"]["cwd"] = "outside"
        with self.assertRaisesRegex(ValidationError, "PATH_ESCAPE"):
            self.validate(candidate)

    def test_fixture_oracle_independently_observes_red_and_green(self):
        command = [sys.executable, "checks/oracle.py"]
        self.assertNotEqual(subprocess.run(command, cwd=self.root, capture_output=True, check=False).returncode, 0)
        (self.root / "src").mkdir()
        (self.root / "src/add.py").write_text("def add(a, b):\n    return a - b\n")
        self.assertNotEqual(subprocess.run(command, cwd=self.root, capture_output=True, check=False).returncode, 0)
        (self.root / "src/add.py").write_text("def add(a, b):\n    return a + b\n")
        self.assertEqual(subprocess.run(command, cwd=self.root, capture_output=True, check=False).returncode, 0)

    def test_same_sources_tools_and_runtime_regenerate_exactly(self):
        first = review.generate(self.root, "bundle.json", expected_authority_sha256=self.pin)
        elsewhere = Path(self.temporary.name) / "independent-workspace"
        shutil.copytree(self.root, elsewhere)
        self.assertEqual(first, review.generate(elsewhere, "bundle.json", expected_authority_sha256=self.pin))
        output = Path(self.temporary.name) / "rendered"
        review.write_or_check(output, first, check=False)
        review.write_or_check(output, first, check=True)
        (output / "README.md").write_text("tampered summary")
        with self.assertRaisesRegex(ValidationError, "REGENERATION_DRIFT"):
            review.write_or_check(output, first, check=True)

    def test_expansion_is_lossless_and_tampered_or_escaping_detail_fails(self):
        files = review.generate(self.root, "bundle.json", expected_authority_sha256=self.pin)
        name = next(name for name in files if name.startswith("objects/"))
        detail = Path(self.temporary.name) / "detail.json"
        detail.write_bytes(files[name])
        identity = hashlib.sha256(detail.read_bytes()).hexdigest()
        expanded = Path(self.temporary.name) / "expanded"
        review.expand(detail, identity, expanded)
        for source in ("bundle.json", *self.bundle["authority"]["read_paths"]):
            self.assertEqual((self.root / source).read_bytes(), (expanded / source).read_bytes())
        validator.validate_bundle(expanded, "bundle.json", expected_authority_sha256=self.pin)
        with self.assertRaisesRegex(ValidationError, "DETAIL_TAMPERED"):
            review.expand(detail, "0" * 64, Path(self.temporary.name) / "bad")
        payload = json.loads(detail.read_bytes())
        payload["inputs"][0]["path"] = "../escape"
        detail.write_bytes(review.canonical(payload))
        with self.assertRaisesRegex(ValidationError, "PATH_INVALID"):
            review.expand(detail, review.digest(detail.read_bytes()), Path(self.temporary.name) / "escape-root")

    def test_cli_runs_from_a_bundle_without_sibling_repository_modules(self):
        portable = Path(self.temporary.name) / "portable"
        portable.mkdir()
        for name in ("bundle_common.py", "bundle_validation.py", "bundle_review.py"):
            shutil.copy2(ROOT / "tools" / name, portable / name)
        run = subprocess.run([sys.executable, str(portable / "bundle_validation.py"), "bundle.json", "--root", str(self.root), "--authority-sha256", self.pin], cwd=portable, capture_output=True, text=True, check=False)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn('"target_acceptance": "not-granted"', run.stdout)

    def test_expansion_rejects_nonempty_and_symlink_output_roots(self):
        files = review.generate(self.root, "bundle.json", expected_authority_sha256=self.pin)
        name = next(name for name in files if name.startswith("objects/"))
        detail = Path(self.temporary.name) / "detail.json"
        detail.write_bytes(files[name])
        identity = review.digest(detail.read_bytes())
        with self.assertRaisesRegex(ValidationError, "OUTPUT_NOT_EMPTY"):
            review.expand(detail, identity, self.root)
        linked = Path(self.temporary.name) / "linked"
        linked.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValidationError, "OUTPUT_SYMLINK"):
            review.expand(detail, identity, linked / "child")
        self.assertFalse((self.root / "child").exists())

    def test_legacy_view_preserves_source_graph_without_claiming_migration(self):
        generated = review.generate(ROOT, "build/execution-contract.yaml", legacy=True)
        self.assertIn(b"legacy view; migration and generic validation required", generated["README.md"])
        self.assertLess(len(generated["README.md"]), 30000)
        with self.assertRaisesRegex(ValidationError, "MIGRATION_REQUIRED"):
            validator.validate_bundle(ROOT, "build/execution-contract.yaml")


if __name__ == "__main__":
    unittest.main()
