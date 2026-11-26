"""Review-field mutations must fail without changing historical authoring bytes."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.bundle_common import ValidationError
from tools.task_review import OUTPUT, check, generate

ROOT = Path(__file__).resolve().parents[1]


class TaskReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for directory in ("spec", "build"):
            shutil.copytree(ROOT / directory, self.root / directory)
        # Frozen authoring inputs include the original README and these controls.
        for relative in ("README.md", "LICENSE", ".gitignore", "payload-inventory.json"):
            shutil.copyfile(ROOT / relative, self.root / relative)
        for relative in ("tools", ".github", "governance"):
            shutil.copytree(ROOT / relative, self.root / relative)
        (self.root / "docs").mkdir()
        (self.root / OUTPUT).write_bytes(generate(self.root))

    def test_repeated_generation_is_identical(self) -> None:
        before = (self.root / "build/execution-contract.yaml").read_bytes()
        expected = (self.root / OUTPUT).read_bytes()
        self.assertEqual(generate(self.root), expected)
        check(self.root)
        self.assertEqual((self.root / "build/execution-contract.yaml").read_bytes(), before)

    def test_each_displayed_field_and_task_inventory_is_checked(self) -> None:
        path = self.root / OUTPUT
        original = path.read_text()
        for old, new in (("Native parents:", "Hidden parents:"), ("Output scope:", "Output scope: /"),
                         ("Acceptance:", "Acceptance: waived"), ("&quot;argv&quot;", "&quot;ignored_argv&quot;"),
                         ("<details>", ""), ("</details>", "</details>\nExtra task")):
            with self.subTest(field=old):
                self.assertIn(old, original)
                path.write_text(original.replace(old, new, 1))
                with self.assertRaisesRegex(ValidationError, "TASK_REVIEW_DRIFT"):
                    check(self.root)
        path.unlink()
        with self.assertRaisesRegex(ValidationError, "TASK_REVIEW_DRIFT"):
            check(self.root)

    def test_native_command_definition_drift_is_rejected(self) -> None:
        path = self.root / "build/execution-contract.yaml"
        contract = json.loads(path.read_text())
        command = next(iter(contract["commands"].values()))
        command["argv"] = ["inert", "changed-command"]
        path.write_text(json.dumps(contract))
        with self.assertRaisesRegex(ValidationError, "TASK_REVIEW_COMMAND_MISMATCH"):
            generate(self.root)

    def test_native_edge_drift_is_still_rejected(self) -> None:
        path = self.root / "build/execution-contract.yaml"
        contract = json.loads(path.read_text())
        contract["tasks"]["T001"]["parents"] = ["T002"]
        path.write_text(json.dumps(contract))
        with self.assertRaisesRegex(ValidationError, "NATIVE_EDGE_MISMATCH"):
            generate(self.root)


if __name__ == "__main__":
    unittest.main()
