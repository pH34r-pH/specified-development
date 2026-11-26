"""Independent malformed-input checks for canonical spec review and coverage."""
from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.bundle_common import ValidationError
from tools.spec_validation import (
    REVIEW_PATH,
    feature_requirements,
    frontmatter,
    validate_coverage,
    validate_metadata,
    validate_repository,
)

ROOT = Path(__file__).resolve().parents[1]


class SpecValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = (ROOT / "spec/features/distribution/index.md").read_text()
        self.tests = (ROOT / "build/distribution/tests.md").read_text()

    def review_copy(self) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        for directory in ("spec", "schemas", "docs"):
            shutil.copytree(ROOT / directory, root / directory)
        for feature in ("distribution", "directory-specs"):
            target = root / "build" / feature
            target.mkdir(parents=True)
            shutil.copyfile(ROOT / "build" / feature / "tests.md", target / "tests.md")
        return root

    def test_current_repository_and_both_existing_matrices(self) -> None:
        self.assertEqual(validate_repository(ROOT)["requirement_and_scenario_ids"], 80)
        self.assertEqual(len(validate_coverage(self.spec, self.tests)), 46)
        directory = (ROOT / "spec/features/directory-specs/index.md").read_text()
        cases = (ROOT / "build/directory-specs/tests.md").read_text()
        self.assertEqual(len(validate_coverage(directory, cases)), 34)

    def test_duplicate_missing_and_empty_requirement_ids(self) -> None:
        for modified, code in (
            (self.spec.replace("| FR-002 |", "| FR-001 |"), "REQUIREMENT_DUPLICATE"),
            (self.spec.replace("| FR-001 |", "| unnamed |"), "REQUIREMENT_ID"),
        ):
            with self.subTest(code=code), self.assertRaisesRegex(ValidationError, code):
                feature_requirements(modified)
        empty = self.spec.replace(next(line for line in self.spec.splitlines() if line.startswith("| FR-001 |")), "| FR-001 | |")
        with self.assertRaisesRegex(ValidationError, "REQUIREMENT_EMPTY"):
            feature_requirements(empty)

    def test_uncovered_requirement_and_unknown_reference(self) -> None:
        extra = self.spec.replace("| FR-001 |", "| FR-099 | A reviewed extra obligation. |\n| FR-001 |", 1)
        with self.assertRaisesRegex(ValidationError, "REQUIREMENT_UNCOVERED"):
            validate_coverage(extra, self.tests)
        with self.assertRaisesRegex(ValidationError, "REQUIREMENT_REFERENCE"):
            validate_coverage(self.spec, self.tests.replace("FR-001/002", "FR-099/002", 1))

    def test_duplicate_orphan_and_unknown_tests(self) -> None:
        with self.assertRaisesRegex(ValidationError, "TEST_DUPLICATE"):
            validate_coverage(self.spec, self.tests.replace("| TST-002 |", "| TST-001 |", 1))
        line = next(line for line in self.tests.splitlines() if line.startswith("| TST-001 |"))
        cells = line.split("|")
        cells[2] = " no requirement references "
        with self.assertRaisesRegex(ValidationError, "TEST_ORPHAN"):
            validate_coverage(self.spec, self.tests.replace(line, "|".join(cells), 1))
        with self.assertRaisesRegex(ValidationError, "TEST_REFERENCE"):
            validate_coverage(self.spec, self.tests.replace("| FR-001 | TST-001 |", "| FR-001 | TST-999 |"))

    def test_missing_and_inconsistent_matrix_rows(self) -> None:
        with self.assertRaisesRegex(ValidationError, "COVERAGE_MATRIX_MISSING"):
            validate_coverage(self.spec, self.tests.replace("| FR-001 | TST-001 |\n", ""))
        with self.assertRaisesRegex(ValidationError, "COVERAGE_MATRIX_DRIFT"):
            validate_coverage(self.spec, self.tests.replace("| FR-002 | TST-001, TST-002 |", "| FR-002 | TST-001 |"))
        with self.assertRaisesRegex(ValidationError, "SCENARIO_UNCOVERED"):
            validate_coverage(self.spec, self.tests.replace("| US1-AS1 / AS2 | TST-001 / TST-002 |\n", ""))

    def test_reference_cells_reject_unparsed_tokens_and_suffixes(self) -> None:
        for original, replacement, code in (
            ("| FR-001 | TST-001 |", "| FR-001 | TST-001-MISSING |", "TEST_REFERENCE"),
            ("| FR-001 | TST-001 |", "| FR-001 | TST-001, TST-UNKNOWN |", "TEST_REFERENCE"),
            ("| US1-AS1 / AS2 |", "| US1-AS1-MISSING / AS2 |", "SCENARIO_REFERENCE"),
            ("FR-001/002, SC-001", "FR-001/002, FR-UNKNOWN, SC-001", "REQUIREMENT_REFERENCE"),
        ):
            with self.subTest(replacement=replacement), self.assertRaisesRegex(ValidationError, code):
                validate_coverage(self.spec, self.tests.replace(original, replacement, 1))

    def test_malformed_id_examples_in_general_prose_are_not_references(self) -> None:
        modified = self.tests.replace("Mature full-product fixture plus idea/POC record.",
                                      "Examples mention malformed FR-UNKNOWN, US1-AS1-MISSING and TST-NOT-A-CASE.")
        self.assertEqual(validate_coverage(self.spec, modified), validate_coverage(self.spec, self.tests))

    def test_duplicate_yaml_keys_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_DUPLICATE"):
            frontmatter("---\ndocument_id: first\ndocument_id: second\n---\n# Title\n")

    def test_legacy_unknown_values_types_and_feature_fields(self) -> None:
        metadata, _ = frontmatter(self.spec)
        for change, code in (
            ({"architecture_approval": "automatically-approved"}, "FRONTMATTER_LEGACY"),
            ({"revision": "one"}, "FRONTMATTER_LEGACY"),
            ({"delivery_status": "shipped"}, "FRONTMATTER_LEGACY"),
            ({"document_id": "wrong"}, "FRONTMATTER_IDENTITY"),
        ):
            with self.subTest(change=change), self.assertRaisesRegex(ValidationError, code):
                validate_metadata(ROOT, metadata | change, "specified-development/distribution", "feature")
        del metadata["feature_id"]
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_SCHEMA"):
            validate_metadata(ROOT, metadata, "specified-development/distribution", "feature")

    def test_compound_legacy_state_does_not_accept_artifact(self) -> None:
        text = (ROOT / "spec/index.md").read_text()
        metadata, _ = frontmatter(text)
        result = validate_metadata(ROOT, metadata, "specified-development/overview", "overview")
        self.assertEqual(result["approval_status"], "architecture-approved")
        self.assertEqual(result["artifact_acceptance"], "unspecified")
        self.assertEqual(result["delivery_status"], "designed-only")
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_LEGACY"):
            validate_metadata(ROOT, metadata | {"approval_status": "architecture-approevd"}, "specified-development/overview", "overview")

    def test_current_states_require_independent_evidence_kinds(self) -> None:
        metadata, _ = frontmatter((ROOT / "docs/specification/execution-capabilities-v2.md").read_text())
        for state, kinds in (("implemented", ["source"]), ("qualified", ["source", "test"]), ("deployed", ["source", "test", "deployment"])):
            candidate = metadata | {"delivery_status": state, "delivery_evidence": [{"kind": kind, "reference": "https://example.invalid/observed-evidence"} for kind in kinds]}
            self.assertEqual(validate_metadata(ROOT, candidate, metadata["document_id"], "contract")["delivery_status"], state)
            with self.assertRaisesRegex(ValidationError, "FRONTMATTER_EVIDENCE"):
                validate_metadata(ROOT, candidate | {"delivery_evidence": []}, metadata["document_id"], "contract")
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_SCHEMA"):
            validate_metadata(ROOT, metadata | {"artifact_acceptance": "accepted", "approval_status": "proposed"}, metadata["document_id"], "contract")
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_SCHEMA"):
            validate_metadata(ROOT, metadata | {"artifact_acceptance": "accepted", "approval_status": "architecture-approved"}, metadata["document_id"], "contract")

    def test_evidence_https_syntax_is_checked_without_fetching(self) -> None:
        metadata, _ = frontmatter((ROOT / "docs/specification/execution-capabilities-v2.md").read_text())
        for reference in ("https://", "https://\ninvalid host", "https://bad host/path",
                          "https://example.invalid:broken/path", "https://[invalid/path"):
            with self.subTest(reference=reference), self.assertRaisesRegex(ValidationError, "FRONTMATTER_EVIDENCE"):
                validate_metadata(ROOT, metadata | {
                    "delivery_status": "implemented",
                    "delivery_evidence": [{"kind": "source", "reference": reference}],
                }, metadata["document_id"], "contract")
        for reference in ("https://example.invalid:8443/a%20b?kind=test#evidence",
                          "HTTPS://example.invalid/record", "https://[::1]:443/record",
                          "https://例え.example/記録", "docs/specification-review.md"):
            with self.subTest(reference=reference):
                result = validate_metadata(ROOT, metadata | {
                    "delivery_status": "implemented",
                    "delivery_evidence": [{"kind": "source", "reference": reference}],
                }, metadata["document_id"], "contract")
                self.assertEqual(result["delivery_status"], "implemented")

    def test_acceptance_evidence_uses_the_same_url_guard(self) -> None:
        metadata, _ = frontmatter((ROOT / "docs/specification/execution-capabilities-v2.md").read_text())
        with self.assertRaisesRegex(ValidationError, "FRONTMATTER_EVIDENCE"):
            validate_metadata(ROOT, metadata | {
                "artifact_acceptance": "accepted", "approval_status": "architecture-approved",
                "acceptance_evidence": {"actor": "independent fixture reviewer", "at": "2026-11-26T00:00:00Z",
                                        "reference": "https://"},
            }, metadata["document_id"], "contract")

    def test_unclassified_and_changed_prose_requires_review(self) -> None:
        root = self.review_copy()
        path = root / "docs/specification/execution-capabilities-v2.md"
        path.write_text(path.read_text() + "\n## Another obligation\n\nA new obligation applied.\n")
        with self.assertRaisesRegex(ValidationError, "SPEC_SECTION_(STALE|UNCLASSIFIED)"):
            validate_repository(root)
        root = self.review_copy()
        path = root / "docs/specification/execution-capabilities-v2.md"
        path.write_text(path.read_text().replace("never silently substituted", "always silently substituted"))
        with self.assertRaisesRegex(ValidationError, "SPEC_SECTION_STALE"):
            validate_repository(root)

    def test_cross_document_trace_and_exclusion_rejection(self) -> None:
        for mutate, code in (
            (lambda data: data["section_traces"][1].update(requirements=["unknown/document#FR-001"]), "SPEC_TRACE_REFERENCE"),
            (lambda data: data["section_traces"][1].update(kind="normative", requirements=[]), "SPEC_OBLIGATION_UNCOVERED"),
            (lambda data: data.update(coverage_exclusions=["FR-001"]), "SPEC_REVIEW_SCHEMA"),
        ):
            with self.subTest(code=code):
                root = self.review_copy()
                path = root / REVIEW_PATH
                data = json.loads(path.read_text())
                mutate(data)
                path.write_text(json.dumps(data))
                with self.assertRaisesRegex(ValidationError, code):
                    validate_repository(root)

    def test_successor_is_bound_to_exact_predecessor(self) -> None:
        root = self.review_copy()
        path = root / "docs/specification/execution-capabilities-v2.md"
        text = path.read_text()
        metadata, _ = frontmatter(text)
        digest = metadata["supersedes"]["sha256"]
        path.write_text(text.replace(digest, "e" * 64))
        with self.assertRaisesRegex(ValidationError, "SPEC_SUCCESSOR_SOURCE"):
            validate_repository(root)
        original = ROOT / "spec/contracts/execution-capabilities.md"
        self.assertEqual((root / "spec/contracts/execution-capabilities.md").read_bytes(), original.read_bytes())

    def test_default_metadata_mapping_is_not_mutated(self) -> None:
        metadata, _ = frontmatter(self.spec)
        before = copy.deepcopy(metadata)
        validate_metadata(ROOT, metadata, "specified-development/distribution", "feature")
        self.assertEqual(metadata, before)


if __name__ == "__main__":
    unittest.main()
