"""Independent adoption-kit and layout-check cases (TST-033)."""
from __future__ import annotations

import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.bundle_common import ValidationError
from tools.gaps import build_report
from tools.layout import check_layout
from tools.onboarding import validate_record

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kit"
EXAMPLE = ROOT / "tests" / "fixtures" / "onboarding" / "tally"
PLACEHOLDERS = {"PROJECT_ID": "acme", "PROJECT_TITLE": "Acme service", "FEATURE_ID": "orders",
                "FEATURE_TITLE": "Orders", "BASELINE_COMMIT": "a" * 40, "CURRENT_COMMIT": "b" * 40,
                "OWNER/REPOSITORY": "acme/service"}


def instantiate(target: Path) -> Path:
    """Apply the kit README's documented copy-and-replace steps to an empty project."""
    target.mkdir(parents=True)
    shutil.copytree(KIT / "templates" / "spec", target / "spec")
    shutil.copytree(KIT / "templates" / "build", target / "build")
    for name in ("onboarding.json", "evidence.json"):
        shutil.copyfile(KIT / "templates" / name, target / name)
    (target / "spec/features/FEATURE_ID").rename(target / "spec/features/orders")
    (target / "build/FEATURE_ID").rename(target / "build/orders")
    (target / "src/orders").mkdir(parents=True)
    for path in target.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for placeholder, value in PLACEHOLDERS.items():
                text = text.replace(placeholder, value)
            path.write_bytes(text.encode("utf-8"))
    return target


class AdoptionKitTests(unittest.TestCase):
    def project(self) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return instantiate(Path(temporary.name) / "project")

    def test_instantiated_kit_passes_layout_onboarding_and_gap_checks(self) -> None:
        root = self.project()
        summary = check_layout(root)
        self.assertEqual(summary["features"]["orders"], {"cases": 2, "requirements": 3, "scenarios": 2, "untested": []})
        self.assertEqual(validate_record(root, json.loads((root / "onboarding.json").read_text()))["state"],
                         "candidate")
        report = build_report(root, json.loads((root / "evidence.json").read_text()))
        self.assertEqual(report["gaps"], ["orders#FR-001", "orders#FR-002", "orders#SC-001"])

    def test_brownfield_example_passes_layout_check(self) -> None:
        self.assertEqual(check_layout(EXAMPLE)["features"]["tally"]["untested"], [])

    def test_untested_requirement_is_a_reported_gap_not_an_error(self) -> None:
        root = self.project()
        tests = root / "build/orders/tests.md"
        tests.write_bytes(tests.read_bytes().replace(b"| CASE-002 | FR-002, SC-001 |", b"| CASE-002 | SC-001 |"))
        self.assertEqual(check_layout(root)["features"]["orders"]["untested"], ["orders#FR-002"])

    def test_invalid_layouts_fail_with_stable_diagnostics(self) -> None:
        def unregistered(root: Path) -> None:
            (root / "spec/notes.md").write_text("# Notes\n", encoding="utf-8")

        def frontmatter(root: Path) -> None:
            path = root / "spec/index.md"
            path.write_bytes(path.read_bytes().replace(b"schema_version: 1\n", b"", 1))

        def targets(root: Path) -> None:
            path = root / "build/orders/plan.md"
            path.write_bytes(path.read_bytes().replace(b"## Implementation targets and direct path", b"## Targets"))

        def unknown(root: Path) -> None:
            path = root / "build/orders/tests.md"
            path.write_bytes(path.read_bytes().replace(b"| CASE-001 | FR-001, SC-001 |", b"| CASE-001 | FR-009, SC-001 |"))

        def missing(root: Path) -> None:
            (root / "build/orders/tests.md").unlink()

        for mutate, code in ((unregistered, "SPEC_SOURCE_CLOSURE"), (frontmatter, "LAYOUT_FRONTMATTER"),
                             (targets, "LAYOUT_PLAN_TARGETS"), (unknown, "LAYOUT_TEST_REFERENCE"),
                             (missing, "LAYOUT_TESTS_MISSING")):
            with self.subTest(code=code):
                root = self.project()
                mutate(root)
                with self.assertRaisesRegex(ValidationError, code):
                    check_layout(root)

    def test_kit_ci_pins_every_action_and_the_tool_revision(self) -> None:
        workflow = (KIT / "ci/specified-development.yml").read_text(encoding="utf-8")
        uses = re.findall(r"uses:\s*(\S+)", workflow)
        self.assertTrue(uses)
        for reference in uses:
            self.assertRegex(reference, r"@[0-9a-f]{40}$")
        self.assertIn("specified-development@${SPECIFIED_DEVELOPMENT_REVISION}", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)

    def test_kit_relative_links_resolve(self) -> None:
        for document in KIT.rglob("*.md"):
            if "templates" in document.parts:
                continue
            for target in re.findall(r"\]\((?!https?:)([^)#]+)", document.read_text(encoding="utf-8")):
                with self.subTest(document=document.name, target=target):
                    self.assertTrue((document.parent / target).exists())


if __name__ == "__main__":
    unittest.main()
