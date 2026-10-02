"""Independent malformed-input and capability-profile tests for the scaffold."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from tools import validate_foundation as vf


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "foundation"


def load_fixture(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ManifestAndNavigationTests(unittest.TestCase):
    def test_real_design_manifest_navigation_and_links_validate(self):
        vf.validate_spec(ROOT)

    def test_malformed_manifest_fixtures_reject(self):
        for fixture in load_fixture("malformed_manifest_cases.json"):
            with self.subTest(fixture=fixture["name"]):
                with self.assertRaises(vf.ValidationError):
                    vf.validate_manifest_shape(fixture["manifest"], set(fixture["available_paths"]))

    def test_malformed_navigation_fixtures_reject(self):
        document_ids = {"specified-development/overview"}
        for fixture in load_fixture("malformed_navigation_cases.json"):
            with self.subTest(fixture=fixture["name"]):
                with self.assertRaises(vf.ValidationError):
                    vf.validate_navigation_shape(fixture["navigation"], document_ids)

    def test_malformed_markdown_links_reject(self):
        for fixture in load_fixture("malformed_link_cases.json"):
            with self.subTest(fixture=fixture["name"]):
                with tempfile.TemporaryDirectory() as temporary:
                    spec_root = Path(temporary)
                    for relative, content in fixture["files"].items():
                        path = spec_root / relative
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(content, encoding="utf-8")
                    with self.assertRaises(vf.ValidationError):
                        vf.validate_markdown_links(spec_root, {"fixture": fixture["source"]})

    def test_valid_local_fragment_is_accepted(self):
        with tempfile.TemporaryDirectory() as temporary:
            spec_root = Path(temporary)
            (spec_root / "start.md").write_text("[target](target.md#known)\n", encoding="utf-8")
            (spec_root / "target.md").write_text("# Known\n", encoding="utf-8")
            vf.validate_markdown_links(spec_root, {"start": "start.md"})


class NativeProjectionTests(unittest.TestCase):
    def setUp(self):
        self.metadata, self.records = vf.load_authoring_tasks(ROOT)
        self.bindings = vf.read_json(ROOT / "build" / "native-bindings.json")
        self.contract = vf.read_json(ROOT / "build" / "execution-contract.yaml")

    def test_full_native_projection_and_all_task_records_validate(self):
        vf.validate_native_projection(self.metadata, self.records, self.bindings, self.contract)
        self.assertEqual(60, len(self.records))

    def test_independent_native_mutations_reject(self):
        cases = load_fixture("native_mutations.json")
        for fixture in cases:
            with self.subTest(fixture=fixture["name"]):
                metadata = copy.deepcopy(self.metadata)
                records = copy.deepcopy(self.records)
                bindings = copy.deepcopy(self.bindings)
                contract = copy.deepcopy(self.contract)
                target = next(item for item in records if item["qualified_id"].endswith("/foundation/T002"))
                if fixture["name"] == "extra-edge":
                    contract["tasks"]["T002"]["parents"].append("T003")
                elif fixture["name"] == "unknown-parent":
                    target["parents"] = ["T999"]
                elif fixture["name"] == "duplicate-identity":
                    other = next(item for item in records if item is not target)
                    other["qualified_id"] = target["qualified_id"]
                elif fixture["name"] == "omitted-metadata":
                    del contract["x_distribution"]["task_metadata"]["T002"]
                with self.assertRaises(vf.ValidationError):
                    vf.validate_native_projection(metadata, records, bindings, contract)


class CapabilityProfileTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = load_fixture("capability_profiles.json")

    def test_ordinary_profile_accepts_admitted_selection_with_unexposed_effective_values(self):
        result = vf.validate_capability_record(self.fixtures["ordinary_unexposed"])
        self.assertEqual("ordinary-behavior-eligible", result)

    def test_rejected_selection_and_unknown_correctness_capability_block(self):
        for name in ("rejected_selection", "unknown_correctness_capability"):
            with self.subTest(fixture=name), self.assertRaises(vf.ValidationError):
                vf.validate_capability_record(self.fixtures[name])

    def test_hard_limit_fails_without_a_verified_control_for_the_operation(self):
        with self.assertRaises(vf.ValidationError):
            vf.validate_capability_record(self.fixtures["hard_limit_unverified"])
        self.assertEqual(
            "hard-limits-verified-for-declared-operations",
            vf.validate_capability_record(self.fixtures["hard_limit_verified"]),
        )
        mismatched = copy.deepcopy(self.fixtures["hard_limit_verified"])
        mismatched["verified_controls"][0]["value"] = 999
        with self.assertRaises(vf.ValidationError):
            vf.validate_capability_record(mismatched)
        with self.assertRaises(vf.ValidationError):
            vf.validate_capability_record(self.fixtures["ordinary_hard_limit_downgrade"])

    def test_measurement_profile_requires_every_declared_observation(self):
        with self.assertRaises(vf.ValidationError):
            vf.validate_capability_record(self.fixtures["measurement_incomplete"])
        complete = self.fixtures["measurement_complete"]
        self.assertEqual(
            "measurement-fields-complete-for-declared-claim",
            vf.validate_capability_record(complete),
        )
        # Independent synthetic Decimal oracle. Cached input and reasoning are
        # subsets; they are not added to inclusive input/output a second time.
        usage, rates = complete["usage"], complete["rates"]
        total = (
            Decimal(usage["input_tokens"]) * Decimal(rates["input_per_million"])
            + Decimal(usage["output_tokens"]) * Decimal(rates["output_per_million"])
        ) / Decimal(1_000_000)
        self.assertEqual(Decimal("0.45"), total)
        self.assertLessEqual(usage["cached_input_tokens"], usage["input_tokens"])
        self.assertLessEqual(usage["reasoning_tokens"], usage["output_tokens"])


class InventoryPrivacyAndRetentionTests(unittest.TestCase):
    def test_only_scoped_public_paths_are_admitted(self):
        fixtures = load_fixture("privacy_cases.json")
        for relative in fixtures["private_paths"]:
            with self.subTest(path=relative):
                self.assertFalse(vf.allowed_public_path(relative))
        self.assertTrue(vf.allowed_public_path("tests/fixtures/foundation/capability_profiles.json"))
        self.assertFalse(vf.allowed_public_path("build/foundation/accepted/receipts/T001/bootstrap.json"))

    def test_public_structured_data_rejects_credential_fields_and_signed_urls(self):
        with self.assertRaises(vf.ValidationError):
            vf.validate_public_json_privacy({"access_token": "fixture-value"})
        constructed = "https://example.invalid/download?token=" + "fixture" + "signature"
        with self.assertRaises(vf.ValidationError):
            vf.validate_public_json_privacy({"url": constructed})
        credential = "ghp_" + "A" * 30
        with self.assertRaises(vf.ValidationError):
            vf.validate_public_json_privacy({"value": credential})

    def test_real_public_inventory_and_retention_rules_validate(self):
        vf.check_public_inventory(ROOT)
        vf.validate_retention(ROOT)


class WholeScaffoldTests(unittest.TestCase):
    def test_complete_workspace_validator(self):
        vf.validate_workspace(ROOT)


if __name__ == "__main__":
    unittest.main()
