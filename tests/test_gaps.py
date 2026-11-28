"""Independent requirement-status and gap-report cases (TST-031, TST-032)."""
from __future__ import annotations

import copy
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tools.bundle_common import ValidationError
from tools.gaps import build_report, canonical, requirement_texts

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "tests" / "fixtures" / "onboarding" / "tally"
FEATURE_DOC = Path("spec/features/tally/index.md")
BASE = "1111111111111111111111111111111111111111"
NEXT = "2222222222222222222222222222222222222222"
FR1, FR2, FR3, SC1 = "tally#TAL-FR-001", "tally#TAL-FR-002", "tally#TAL-FR-003", "tally#TAL-SC-001"


def evidence(root: Path, revision: str, outcomes: dict[str, str] | None,
             run_hashes: dict[str, str] | None = None) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "kind": "requirement-evidence",
        "revision": revision,
        "features": ["tally"],
        "cases": {"TAL-001": {"requirements": [FR1, FR3, SC1]}, "TAL-002": {"requirements": [FR2, SC1]}},
        "tasks": {"T001": {"cases": ["TAL-001"]}, "T002": {"cases": ["TAL-002"]}},
        "results": None if outcomes is None else {
            "revision": revision,
            "requirement_hashes": run_hashes if run_hashes is not None else requirement_texts(root, ["tally"]),
            "cases": outcomes,
        },
    }


class GapReportTests(unittest.TestCase):
    def workspace(self) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name) / "tally"
        shutil.copytree(EXAMPLE, root, ignore=shutil.ignore_patterns("__pycache__"))
        return root

    def edit_spec(self, root: Path, old: str, new: str) -> None:
        path = root / FEATURE_DOC
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_bytes(text.replace(old, new).encode("utf-8"))

    def test_untested_stale_and_satisfied_statuses_without_previous_report(self) -> None:
        report = build_report(EXAMPLE, evidence(EXAMPLE, BASE, None))
        self.assertEqual({entry["status"] for entry in report["requirements"].values()}, {"stale"})
        self.assertEqual(report["gaps"], sorted([FR1, FR2, FR3, SC1]))
        self.assertEqual(report["changed"], [])
        passing = build_report(EXAMPLE, evidence(EXAMPLE, BASE, {"TAL-001": "pass", "TAL-002": "pass"}))
        self.assertEqual(passing["gaps"], [])
        failing = build_report(EXAMPLE, evidence(EXAMPLE, BASE, {"TAL-001": "pass", "TAL-002": "fail"}))
        self.assertEqual(failing["gaps"], [FR2, SC1])
        self.assertEqual(failing["requirements"][FR2]["status"], "failing")

    def test_spec_change_reports_only_its_gap_and_stale_descendants(self) -> None:
        root = self.workspace()
        before_hashes = requirement_texts(root, ["tally"])
        previous = build_report(root, evidence(root, BASE, {"TAL-001": "pass", "TAL-002": "pass"}))
        self.assertEqual(previous["gaps"], [])
        # Spec-first change: add one requirement and change another, written as already true.
        self.edit_spec(root, "| TAL-FR-003 | A new tally has a total of zero. |",
                       "| TAL-FR-003 | A new tally has a total of zero. |\n"
                       "| TAL-FR-004 | Resetting a tally returns its total to zero. |")
        self.edit_spec(root, "Adding a negative amount raises ValueError and leaves the total unchanged.",
                       "Adding a negative amount raises ValueError naming the amount and leaves the total unchanged.")
        current = requirement_texts(root, ["tally"])
        self.assertNotEqual(current[FR2], before_hashes[FR2])
        # Cases re-run at the new revision; TAL-002 only ran against the old FR-002 text.
        run_hashes = dict(current, **{FR2: before_hashes[FR2]})
        report = build_report(root, evidence(root, NEXT, {"TAL-001": "pass", "TAL-002": "pass"}, run_hashes), previous)
        self.assertEqual(report["changed"], [FR2, "tally#TAL-FR-004"])
        self.assertEqual(report["requirements"]["tally#TAL-FR-004"]["status"], "untested")
        self.assertEqual(report["requirements"][FR2]["status"], "stale")
        self.assertEqual(report["gaps"], [FR2, "tally#TAL-FR-004"])
        for unchanged in (FR1, FR3, SC1):
            self.assertEqual(report["requirements"][unchanged]["status"], "satisfied")
        self.assertEqual(report["stale"], {"cases": ["TAL-002"], "tasks": ["T002"],
                                           "plan_sections": ["build/tally/plan.md#Input validation"]})
        again = build_report(root, evidence(root, NEXT, {"TAL-001": "pass", "TAL-002": "pass"}, run_hashes), previous)
        self.assertEqual(canonical(report), canonical(again))

    def test_previously_satisfied_failure_is_regressed(self) -> None:
        previous = build_report(EXAMPLE, evidence(EXAMPLE, BASE, {"TAL-001": "pass", "TAL-002": "pass"}))
        report = build_report(EXAMPLE, evidence(EXAMPLE, NEXT, {"TAL-001": "fail", "TAL-002": "pass"}), previous)
        for requirement in (FR1, FR3, SC1):
            self.assertEqual(report["requirements"][requirement]["status"], "regressed")
        self.assertEqual(report["requirements"][FR2]["status"], "satisfied")
        self.assertEqual(report["changed"], [])
        self.assertEqual(report["stale"], {"cases": [], "tasks": [], "plan_sections": []})

    def test_prose_and_document_fields_never_mark_satisfied(self) -> None:
        root = self.workspace()
        self.edit_spec(root, "delivery_status: designed-only", "delivery_status: deployed")
        self.edit_spec(root, "Negative amounts are rejected.", "Negative amounts are rejected. Every requirement is delivered and satisfied.")
        report = build_report(root, evidence(root, BASE, None))
        self.assertEqual(report["gaps"], sorted([FR1, FR2, FR3, SC1]))

    def test_invalid_evidence_fails_closed(self) -> None:
        base = evidence(EXAMPLE, BASE, {"TAL-001": "pass", "TAL-002": "pass"})
        cases = [
            ("unknown requirement", lambda e: e["cases"]["TAL-001"]["requirements"].append("tally#TAL-FR-099"),
             "GAP_UNKNOWN_REQUIREMENT"),
            ("case tracing nothing", lambda e: e["cases"].update({"TAL-003": {"requirements": []}}), "GAP_ORPHAN_CASE"),
            ("task naming unknown case", lambda e: e["tasks"].update({"T009": {"cases": ["TAL-404"]}}), "GAP_UNKNOWN_CASE"),
            ("results from another revision", lambda e: e["results"].update(revision=NEXT), "GAP_RESULTS_REVISION"),
            ("undeclared outcome", lambda e: e["results"]["cases"].update({"TAL-404": "pass"}), "GAP_UNKNOWN_CASE"),
            ("invalid outcome", lambda e: e["results"]["cases"].update({"TAL-001": "skipped"}), "GAP_OUTCOME"),
            ("inexact revision", lambda e: e.update(revision="main"), "GAP_REVISION"),
            ("unknown feature", lambda e: e.update(features=["reports"]), "GAP_SPEC"),
            ("unknown field", lambda e: e.update(extra=True), "GAP_SHAPE"),
        ]
        for name, mutate, code in cases:
            with self.subTest(name=name):
                changed = copy.deepcopy(base)
                mutate(changed)
                with self.assertRaisesRegex(ValidationError, code):
                    build_report(EXAMPLE, changed)


if __name__ == "__main__":
    unittest.main()
