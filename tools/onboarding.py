"""Validate a brownfield onboarding record against a repository's accepted specification.

The validator checks traceability and the characterization-mode rules. It does
not judge whether a characterization is correct; that remains a review decision.
It never executes project code or computes expected values from implementation.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING or __package__:
    from .bundle_common import (
        ValidationError,
        confined_file,
        read_json,
        require,
        safe_relative_path,
    )
    from .spec_validation import MANIFEST_PATH, feature_requirements, frontmatter
else:
    from bundle_common import (
        ValidationError,
        confined_file,
        read_json,
        require,
        safe_relative_path,
    )
    from spec_validation import MANIFEST_PATH, feature_requirements, frontmatter

RECORD_KIND = "brownfield-onboarding-record"
RECORD_KEYS = {"schema_version", "kind", "repository", "baseline_revision", "areas", "requirements",
               "known_defects", "oracle", "acceptance", "initial_gaps", "spec_kit_layout"}
SOURCE_KINDS = {"code", "documentation", "test", "observed"}
ORACLE_SOURCES = {"accepted-spec", "adopted-existing-test"}
DECISIONS = {"specify-actual", "specify-intended"}
REVISION_RE = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")
RESULT_STATES = {"pass", "fail"}


def _object(value: Any, code: str, context: str, keys: set[str], optional: frozenset[str] = frozenset()) -> dict[str, Any]:
    require(isinstance(value, dict), code, f"{context} must be an object")
    value = cast(dict[str, Any], value)
    missing = keys - optional - value.keys()
    unknown = value.keys() - keys
    require(not missing and not unknown, code, f"{context}: missing={sorted(missing)} unknown={sorted(unknown)}")
    return value


def _text(value: Any, code: str, context: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), code, f"{context} must be nonempty text")
    return cast(str, value)


def _list(value: Any, code: str, context: str) -> list[Any]:
    require(isinstance(value, list), code, f"{context} must be a list")
    return cast(list[Any], value)


def _within(path: str, areas: list[str]) -> bool:
    candidate = PurePosixPath(path).parts
    return any(candidate[:len(PurePosixPath(area).parts)] == PurePosixPath(area).parts for area in areas)


def specified_requirements(root: Path, feature_ids: list[str]) -> dict[str, set[str]]:
    """Return the accepted functional requirement and success criterion IDs per onboarded feature."""
    manifest = read_json(confined_file(root, MANIFEST_PATH))
    require(isinstance(manifest, dict) and isinstance(manifest.get("features"), dict)
            and isinstance(manifest.get("documents"), dict), "ONBOARDING_SPEC", "spec manifest is malformed")
    result: dict[str, set[str]] = {}
    for feature in feature_ids:
        record = manifest["features"].get(feature)
        require(isinstance(record, dict), "ONBOARDING_SCOPE", f"area is not a specified feature: {feature}")
        document = manifest["documents"].get(record.get("root"))
        require(isinstance(document, dict), "ONBOARDING_SPEC", f"feature root is not a registered document: {feature}")
        text = confined_file(root, "spec/" + document["path"]).read_text(encoding="utf-8")
        _, body = frontmatter(text)
        requirements, _scenarios = feature_requirements(body)
        result[feature] = requirements
    return result


def _qualified(value: Any, known: set[str], context: str) -> str:
    identifier = _text(value, "ONBOARDING_SHAPE", context)
    require(identifier in known, "ONBOARDING_UNKNOWN_REQUIREMENT", f"{context}: {identifier}")
    return identifier


def validate_record(root: Path, record: Any, results: Any | None = None) -> dict[str, Any]:
    """Validate an onboarding record; return a summary including the computed gap list."""
    record = _object(record, "ONBOARDING_SHAPE", "record", RECORD_KEYS)
    require(record["schema_version"] == 1 and record["kind"] == RECORD_KIND, "ONBOARDING_SHAPE",
            "record must be a version 1 brownfield onboarding record")
    _text(record["repository"], "ONBOARDING_SHAPE", "repository")
    baseline = record["baseline_revision"]
    require(isinstance(baseline, str) and REVISION_RE.fullmatch(baseline) is not None,
            "ONBOARDING_REVISION", "baseline_revision must be an exact commit identity")

    areas = _list(record["areas"], "ONBOARDING_SHAPE", "areas")
    require(bool(areas), "ONBOARDING_SCOPE", "at least one onboarded area is required")
    feature_ids: list[str] = []
    area_paths: list[str] = []
    for index, area in enumerate(areas):
        area = _object(area, "ONBOARDING_SHAPE", f"areas[{index}]", {"feature_id", "paths"})
        feature = _text(area["feature_id"], "ONBOARDING_SHAPE", f"areas[{index}].feature_id")
        require(feature not in feature_ids, "ONBOARDING_SCOPE", f"duplicate area: {feature}")
        feature_ids.append(feature)
        paths = _list(area["paths"], "ONBOARDING_SHAPE", f"areas[{index}].paths")
        require(bool(paths), "ONBOARDING_SCOPE", f"area {feature} needs source paths")
        for path in paths:
            area_paths.append(str(safe_relative_path(path, code="ONBOARDING_SCOPE")))

    by_feature = specified_requirements(root, feature_ids)
    known = {f"{feature}#{identifier}" for feature, ids in by_feature.items() for identifier in ids}

    require(isinstance(record["requirements"], dict), "ONBOARDING_SHAPE", "requirements must be an object")
    traced = cast(dict[str, Any], record["requirements"])
    for identifier, entry in traced.items():
        _qualified(identifier, known, "requirements")
        entry = _object(entry, "ONBOARDING_SHAPE", f"requirements[{identifier}]", {"sources"})
        sources = _list(entry["sources"], "ONBOARDING_SHAPE", f"requirements[{identifier}].sources")
        require(bool(sources), "ONBOARDING_UNTRACED", f"no characterization sources: {identifier}")
        for source in sources:
            source = _object(source, "ONBOARDING_SHAPE", f"{identifier} source", {"kind", "reference"})
            require(source["kind"] in SOURCE_KINDS, "ONBOARDING_SOURCE", f"{identifier}: unknown source kind")
            reference = _text(source["reference"], "ONBOARDING_SOURCE", f"{identifier} source reference")
            if source["kind"] == "code":
                path = str(safe_relative_path(reference, code="ONBOARDING_SOURCE"))
                require(_within(path, area_paths), "ONBOARDING_SCOPE",
                        f"{identifier}: code source is outside onboarded areas: {path}")
    untraced = sorted(known - traced.keys())
    require(not untraced, "ONBOARDING_UNTRACED", f"accepted requirements without sources: {untraced}")

    gaps_list = _list(record["initial_gaps"], "ONBOARDING_SHAPE", "initial_gaps")
    gaps = {_qualified(item, known, "initial_gaps") for item in gaps_list}
    require(len(gaps) == len(gaps_list), "ONBOARDING_SHAPE", "initial_gaps contains duplicates")

    for index, defect in enumerate(_list(record["known_defects"], "ONBOARDING_SHAPE", "known_defects")):
        require(isinstance(defect, dict), "ONBOARDING_SHAPE", f"known_defects[{index}] must be an object")
        defect = cast(dict[str, Any], defect)
        identifier = _qualified(defect.get("requirement"), known, f"known_defects[{index}]")
        _text(defect.get("observed"), "ONBOARDING_SHAPE", f"known_defects[{index}].observed")
        decision = defect.get("decision")
        require(decision in DECISIONS, "ONBOARDING_DEFECT_UNDECIDED",
                f"known defect needs specify-actual or specify-intended: {identifier}")
        allowed = {"requirement", "observed", "decision"} | ({"follow_up"} if decision == "specify-actual" else set())
        require(set(defect) <= allowed, "ONBOARDING_SHAPE", f"known_defects[{index}] has unexpected fields")
        if decision == "specify-actual":
            require(isinstance(defect.get("follow_up"), str) and bool(defect["follow_up"].strip()),
                    "ONBOARDING_DEFECT_FOLLOW_UP", f"specified actual behavior needs a follow-up change: {identifier}")
        else:
            require(identifier in gaps, "ONBOARDING_GAP_MISSING",
                    f"specified intended behavior must start in the gap list: {identifier}")

    oracle_cases: dict[str, set[str]] = {}
    for index, case in enumerate(_list(record["oracle"], "ONBOARDING_SHAPE", "oracle")):
        require(isinstance(case, dict), "ONBOARDING_SHAPE", f"oracle[{index}] must be an object")
        case = cast(dict[str, Any], case)
        require(case.get("expected_source") != "implementation-output", "ONBOARDING_ORACLE_CIRCULAR",
                f"oracle[{index}] derives expectations from implementation output")
        case = _object(case, "ONBOARDING_SHAPE", f"oracle[{index}]", {"case", "requirements", "expected_source", "reference"},
                       frozenset({"reference"}))
        require(case["expected_source"] in ORACLE_SOURCES, "ONBOARDING_ORACLE_SOURCE",
                f"oracle[{index}] has an unknown expected-value source")
        if case["expected_source"] == "adopted-existing-test":
            _text(case.get("reference"), "ONBOARDING_ORACLE_SOURCE", f"oracle[{index}] adopted test reference")
        name = _text(case["case"], "ONBOARDING_SHAPE", f"oracle[{index}].case")
        require(name not in oracle_cases, "ONBOARDING_SHAPE", f"duplicate oracle case: {name}")
        traced_requirements = _list(case["requirements"], "ONBOARDING_SHAPE", f"oracle[{index}].requirements")
        require(bool(traced_requirements), "ONBOARDING_ORACLE_SOURCE", f"oracle case {name} traces no requirement")
        oracle_cases[name] = {_qualified(item, known, f"oracle case {name}") for item in traced_requirements}

    acceptance = record["acceptance"]
    require(isinstance(acceptance, dict), "ONBOARDING_ACCEPTANCE", "acceptance must be an object")
    acceptance = cast(dict[str, Any], acceptance)
    state = acceptance.get("state")
    require(state in {"candidate", "accepted"}, "ONBOARDING_ACCEPTANCE", "acceptance state must be candidate or accepted")
    if state == "accepted":
        _object(acceptance, "ONBOARDING_ACCEPTANCE", "acceptance", {"state", "actor", "at"})
        _text(acceptance["actor"], "ONBOARDING_ACCEPTANCE", "acceptance actor")
        require(isinstance(acceptance["at"], str) and TIMESTAMP_RE.fullmatch(acceptance["at"]) is not None,
                "ONBOARDING_ACCEPTANCE", "acceptance time must be an ISO 8601 timestamp with zone")
        covered = set().union(*oracle_cases.values()) if oracle_cases else set()
        uncovered = sorted(known - covered)
        require(not uncovered, "ONBOARDING_ORACLE_UNCOVERED", f"accepted requirements without independent cases: {uncovered}")
    else:
        _object(acceptance, "ONBOARDING_ACCEPTANCE", "acceptance", {"state"})

    layout = record["spec_kit_layout"]
    if layout is not None:
        layout = _object(layout, "ONBOARDING_LAYOUT", "spec_kit_layout",
                         {"source", "features", "history_preserved", "constitution_preserved"})
        _text(layout["source"], "ONBOARDING_LAYOUT", "spec_kit_layout.source")
        require(layout["history_preserved"] is True and layout["constitution_preserved"] is True, "ONBOARDING_LAYOUT",
                "an existing Spec Kit mapping must preserve feature history and constitutions")
        mapping = layout["features"]
        require(isinstance(mapping, dict) and bool(mapping)
                and all(isinstance(target, str) and target in feature_ids for target in mapping.values()),
                "ONBOARDING_LAYOUT", "every mapped Spec Kit feature must target an onboarded feature")

    summary: dict[str, Any] = {"areas": feature_ids, "requirements": len(known), "state": state,
                               "initial_gaps": sorted(gaps)}
    if results is not None:
        computed = baseline_gaps(baseline, known, oracle_cases, results)
        require(computed == gaps, "ONBOARDING_GAP_MISMATCH",
                f"declared gaps differ from evidence: missing={sorted(computed - gaps)} extra={sorted(gaps - computed)}")
        summary["evidence_checked"] = True
    return summary


def baseline_gaps(baseline: str, known: set[str], cases: dict[str, set[str]], results: Any) -> set[str]:
    """Requirements without passing evidence at the baseline: no case, or any traced case not passing."""
    results = _object(results, "ONBOARDING_RESULTS", "results", {"revision", "cases"})
    require(results["revision"] == baseline, "ONBOARDING_RESULTS", "results must come from the baseline revision")
    outcomes = results["cases"]
    require(isinstance(outcomes, dict) and all(value in RESULT_STATES for value in outcomes.values()),
            "ONBOARDING_RESULTS", "results must map case names to pass or fail")
    unknown = sorted(set(outcomes) - set(cases))
    require(not unknown, "ONBOARDING_RESULTS", f"results for undeclared cases: {unknown}")
    satisfied = set()
    for requirement in known:
        traced = [name for name, requirements in cases.items() if requirement in requirements]
        if traced and all(outcomes.get(name) == "pass" for name in traced):
            satisfied.add(requirement)
    return known - satisfied


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="onboarding record JSON")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="onboarded repository root")
    parser.add_argument("--results", type=Path, help="independent test results at the baseline revision")
    args = parser.parse_args()
    try:
        results = read_json(args.results) if args.results else None
        summary = validate_record(args.root, read_json(args.record), results)
        print(f"Onboarding record valid: {summary}. Characterization correctness is a review decision.")
        return 0
    except (ValidationError, OSError) as exc:
        print(f"ONBOARDING invalid: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
