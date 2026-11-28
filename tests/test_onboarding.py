"""Independent onboarding-record cases (TST-029, TST-030) on a synthetic brownfield repository."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any

from tools.bundle_common import ValidationError
from tools.onboarding import validate_record

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "tests" / "fixtures" / "onboarding" / "tally"
RUNNER = """
import json, sys, unittest
suite = unittest.defaultTestLoader.discover("tests")
outcomes = {}
class Collect(unittest.TestResult):
    def addSuccess(self, test):
        outcomes[test.id().rsplit(".", 1)[1]] = "pass"
    def addFailure(self, test, err):
        outcomes[test.id().rsplit(".", 1)[1]] = "fail"
    def addError(self, test, err):
        outcomes[test.id().rsplit(".", 1)[1]] = "fail"
suite.run(Collect())
print(json.dumps(outcomes))
"""


def example_record() -> dict[str, Any]:
    return json.loads((EXAMPLE / "onboarding.json").read_text(encoding="utf-8"))


def run_example_cases() -> dict[str, str]:
    """Run the example's independent cases against its code; outcomes are evidence, not expectations."""
    completed = subprocess.run([sys.executable, "-I", "-c", f"import sys; sys.path[:0] = ['src', 'tests']\n{RUNNER}"],
                               cwd=EXAMPLE, capture_output=True, text=True, check=True, timeout=60)
    raw = json.loads(completed.stdout)
    return {name.removeprefix("test_").replace("_", "-"): outcome for name, outcome in raw.items()}


class OnboardingExampleTests(unittest.TestCase):
    def test_accepted_record_validates_with_unspecified_remainder(self) -> None:
        summary = validate_record(EXAMPLE, example_record())
        self.assertEqual(summary["areas"], ["tally"])
        self.assertEqual(summary["requirements"], 4)
        self.assertEqual(summary["initial_gaps"], ["tally#TAL-FR-002", "tally#TAL-SC-001"])

    def test_declared_gaps_equal_requirements_without_passing_evidence(self) -> None:
        record = example_record()
        outcomes = run_example_cases()
        self.assertEqual(outcomes, {"TAL-001": "pass", "TAL-002": "fail"})
        results = {"revision": record["baseline_revision"], "cases": outcomes}
        self.assertTrue(validate_record(EXAMPLE, record, results)["evidence_checked"])
        wrong = copy.deepcopy(record)
        wrong["initial_gaps"] = ["tally#TAL-FR-002"]
        with self.assertRaisesRegex(ValidationError, "ONBOARDING_GAP_MISMATCH"):
            validate_record(EXAMPLE, wrong, results)
        with self.assertRaisesRegex(ValidationError, "ONBOARDING_RESULTS"):
            validate_record(EXAMPLE, record, results | {"revision": "f" * 40})

    def test_candidate_may_omit_oracle_but_never_uses_implementation_output(self) -> None:
        record = example_record()
        record["acceptance"] = {"state": "candidate"}
        record["oracle"] = []
        self.assertEqual(validate_record(EXAMPLE, record)["state"], "candidate")
        record["oracle"] = [{"case": "TAL-009", "requirements": ["tally#TAL-FR-001"], "expected_source": "implementation-output"}]
        with self.assertRaisesRegex(ValidationError, "ONBOARDING_ORACLE_CIRCULAR"):
            validate_record(EXAMPLE, record)

    def test_existing_spec_kit_layout_must_preserve_history_and_constitution(self) -> None:
        record = example_record()
        record["spec_kit_layout"] = {"source": "specs/", "features": {"001-tally": "tally"},
                                     "history_preserved": True, "constitution_preserved": True}
        validate_record(EXAMPLE, record)
        for field in ("history_preserved", "constitution_preserved"):
            changed = copy.deepcopy(record)
            changed["spec_kit_layout"][field] = False
            with self.subTest(field=field), self.assertRaisesRegex(ValidationError, "ONBOARDING_LAYOUT"):
                validate_record(EXAMPLE, changed)
        changed = copy.deepcopy(record)
        changed["spec_kit_layout"]["features"] = {"001-tally": "reports"}
        with self.assertRaisesRegex(ValidationError, "ONBOARDING_LAYOUT"):
            validate_record(EXAMPLE, changed)


class OnboardingRecordMutationTests(unittest.TestCase):
    def assert_rejects(self, mutate, code: str) -> None:
        record = example_record()
        mutate(record)
        with self.assertRaisesRegex(ValidationError, code):
            validate_record(EXAMPLE, record)

    def test_each_named_mutation_fails_closed(self) -> None:
        cases = [
            ("untraced requirement", lambda r: r["requirements"].pop("tally#TAL-FR-003"), "ONBOARDING_UNTRACED"),
            ("empty sources", lambda r: r["requirements"]["tally#TAL-FR-003"].update(sources=[]), "ONBOARDING_UNTRACED"),
            ("unknown requirement", lambda r: r["requirements"].update({"tally#TAL-FR-099": {"sources": []}}),
             "ONBOARDING_UNKNOWN_REQUIREMENT"),
            ("undecided defect", lambda r: r["known_defects"][0].pop("decision"), "ONBOARDING_DEFECT_UNDECIDED"),
            ("intended not in gaps", lambda r: r.update(initial_gaps=["tally#TAL-SC-001"]), "ONBOARDING_GAP_MISSING"),
            ("actual without follow-up", lambda r: r["known_defects"][0].update(decision="specify-actual"),
             "ONBOARDING_DEFECT_FOLLOW_UP"),
            ("implementation-derived oracle", lambda r: r["oracle"][0].update(expected_source="implementation-output"),
             "ONBOARDING_ORACLE_CIRCULAR"),
            ("adopted test without reference", lambda r: r["oracle"][0].update(expected_source="adopted-existing-test"),
             "ONBOARDING_ORACLE_SOURCE"),
            ("uncovered accepted requirement", lambda r: r["oracle"][0].update(requirements=["tally#TAL-FR-001"]),
             "ONBOARDING_ORACLE_UNCOVERED"),
            ("accepted without actor", lambda r: r["acceptance"].pop("actor"), "ONBOARDING_ACCEPTANCE"),
            ("accepted without zoned time", lambda r: r["acceptance"].update(at="2026-11-27"), "ONBOARDING_ACCEPTANCE"),
            ("gap outside onboarded areas", lambda r: r["initial_gaps"].append("reports#REP-FR-001"),
             "ONBOARDING_UNKNOWN_REQUIREMENT"),
            ("code source in unspecified path", lambda r: r["requirements"]["tally#TAL-FR-001"]["sources"].append(
                {"kind": "code", "reference": "src/report.py"}), "ONBOARDING_SCOPE"),
            ("area that is not a specified feature", lambda r: r["areas"].append({"feature_id": "reports", "paths": ["src/report.py"]}),
             "ONBOARDING_SCOPE"),
            ("inexact baseline", lambda r: r.update(baseline_revision="main"), "ONBOARDING_REVISION"),
            ("unknown field", lambda r: r.update(extra=True), "ONBOARDING_SHAPE"),
        ]
        for name, mutate, code in cases:
            with self.subTest(name=name):
                self.assert_rejects(mutate, code)


if __name__ == "__main__":
    unittest.main()
