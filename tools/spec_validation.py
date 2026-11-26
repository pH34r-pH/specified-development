"""Check current specification metadata and independently authored coverage.

Historical sources are read unchanged. A small review overlay selects explicit
successors and traces shared prose sections to existing feature requirements.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from markdown_it import MarkdownIt

if TYPE_CHECKING or __package__:
    from .bundle_common import ValidationError, confined_file, read_json, require
else:
    from bundle_common import ValidationError, confined_file, read_json, require

REVIEW_PATH = "docs/specification-review.json"
MANIFEST_PATH = "spec/manifest.json"
MARKDOWN = MarkdownIt("commonmark").enable("table")
REQUIREMENT = re.compile(r"(?:[A-Z]+-)?(?:FR|SC)-\d{3}")
CASE = re.compile(r"(?:TST|DIR|FND)-\d{3}")
LEGACY_APPROVAL = {
    "architecture-approved": "architecture-approved",
    "architecture-approved-directory-enhancement-specified": "architecture-approved",
    "user-requested-enhancement-design-candidate": "proposed",
    "enhancement-design-candidate": "proposed",
    "distribution-choice-approved": "decision-approved",
    "proposed-contract-repair-parent-review-required": "review-required",
}


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML with duplicate-key rejection rather than last-value wins."""


def _mapping(loader: UniqueSafeLoader, node: yaml.MappingNode) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        require(isinstance(key, str), "FRONTMATTER_KEY", "keys must be strings")
        require(key not in result, "FRONTMATTER_DUPLICATE", key)
        result[key] = loader.construct_object(value_node)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def frontmatter(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines(keepends=True)
    require(bool(lines) and lines[0].strip() == "---", "FRONTMATTER_MISSING", "expected YAML frontmatter")
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    require(end is not None, "FRONTMATTER_MISSING", "unterminated frontmatter")
    assert end is not None
    try:
        value = yaml.load("".join(lines[1:end]), Loader=UniqueSafeLoader)
    except yaml.YAMLError as exc:
        raise ValidationError("FRONTMATTER_YAML: invalid YAML") from exc
    require(isinstance(value, dict), "FRONTMATTER_SHAPE", "metadata must be an object")
    return value, "".join(lines[end + 1:])


def _schema(root: Path, name: str, value: Any, code: str) -> None:
    schema = read_json(confined_file(root, f"schemas/{name}.schema.json"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(value), key=lambda error: str(list(error.path)))
    require(not errors, code, str(errors[0].message) if errors else "")


def _evidence_reference(root: Path, reference: str, document_id: str) -> None:
    """Validate a pointer's syntax/existence, never the referenced claim."""
    try:
        parsed = urlsplit(reference)
        if parsed.scheme.lower() == "https":
            require(not any(character.isspace() or ord(character) < 32 or ord(character) == 127
                            for character in reference),
                    "FRONTMATTER_EVIDENCE", f"invalid HTTPS evidence reference: {document_id}")
            require(bool(parsed.netloc) and bool(parsed.hostname), "FRONTMATTER_EVIDENCE",
                    f"missing HTTPS evidence host: {document_id}")
            _ = parsed.port  # urlsplit checks a malformed or out-of-range port here.
            return
    except ValueError as exc:
        if isinstance(exc, ValidationError):
            raise
        raise ValidationError(f"FRONTMATTER_EVIDENCE: invalid evidence URL: {document_id}") from exc
    require(not parsed.scheme and confined_file(root, reference).is_file(),
            "FRONTMATTER_EVIDENCE", f"missing local evidence reference: {document_id}")


def validate_metadata(root: Path, metadata: dict[str, Any], document_id: str, role: str) -> dict[str, Any]:
    if "schema_version" in metadata:
        current = dict(metadata)
    else:
        _schema(root, "spec-frontmatter-legacy", metadata, "FRONTMATTER_LEGACY")
        legacy = metadata.get("approval_status")
        current = {
            "schema_version": 1,
            "document_id": metadata["document_id"],
            "role": role,
            "revision": metadata.get("revision", 1),
            "target_status": metadata.get("target_status", "unspecified"),
            "approval_status": LEGACY_APPROVAL.get(str(legacy), "unspecified"),
            "artifact_acceptance": metadata.get("artifact_acceptance", "unspecified"),
            "delivery_status": metadata["delivery_status"],
            "delivery_evidence": metadata.get("delivery_evidence", []),
            "qualifiers": [legacy] if legacy else [],
        }
        if metadata.get("architecture_approval") == "delegated-user-directive":
            current["approval_status"] = "architecture-approved"
            current["qualifiers"].append("delegated-user-directive")
        if "feature_id" in metadata:
            current["feature_id"] = metadata["feature_id"]
    _schema(root, "spec-frontmatter-v1", current, "FRONTMATTER_SCHEMA")
    require(current["document_id"] == document_id and current["role"] == role,
            "FRONTMATTER_IDENTITY", document_id)
    kinds = {item["kind"] for item in current["delivery_evidence"]}
    expected = {"implemented": {"source"}, "qualified": {"source", "test"},
                "deployed": {"source", "test", "deployment"}}
    require(expected.get(current["delivery_status"], set()) <= kinds,
            "FRONTMATTER_EVIDENCE", f"missing delivery evidence kinds: {document_id}")
    for item in current["delivery_evidence"]:
        _evidence_reference(root, item["reference"], document_id)
    if current["artifact_acceptance"] == "accepted":
        _evidence_reference(root, current["acceptance_evidence"]["reference"], document_id)
    return current


@dataclass
class Table:
    heading: str
    headers: list[str]
    rows: list[list[str]]


def tables(text: str) -> list[Table]:
    result: list[Table] = []
    heading = ""
    in_table = False
    row: list[str] = []
    table: Table | None = None
    tokens = MARKDOWN.parse(text)
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            heading = tokens[i + 1].content
        elif token.type == "table_open":
            table = Table(heading, [], [])
            result.append(table)
            in_table = True
        elif token.type == "table_close":
            in_table = False
        elif in_table and token.type == "tr_open":
            row = []
        elif in_table and token.type == "inline":
            row.append(token.content)
        elif in_table and token.type == "tr_close":
            assert table is not None
            if not table.headers:
                table.headers = row
            else:
                table.rows.append(row)
    return result


def sections(text: str) -> dict[str, str]:
    """Return exact source slices by heading; code-block headings are ignored."""
    lines = text.splitlines(keepends=True)
    tokens = MARKDOWN.parse(text)
    starts: list[tuple[str, int]] = []
    for i, token in enumerate(tokens):
        if token.type == "heading_open" and token.map is not None:
            starts.append((tokens[i + 1].content, token.map[0]))
    require(bool(starts), "SPEC_HEADINGS", "document has no headings")
    require(not "".join(lines[:starts[0][1]]).strip(), "SPEC_PREAMBLE", "unclassified prose before first heading")
    result: dict[str, str] = {}
    for i, (heading, start) in enumerate(starts):
        require(heading not in result, "SPEC_HEADING_DUPLICATE", heading)
        end = starts[i + 1][1] if i + 1 < len(starts) else len(lines)
        result[heading] = "".join(lines[start:end])
    return result


def _requirements(text: str) -> set[str]:
    """Read only a declared requirement-list cell, including FR-001/002."""
    result: set[str] = set()
    for token in re.split(r"\s*,\s*", text.strip()):
        match = re.fullmatch(r"((?:[A-Z]+-)?(?:FR|SC)-)(\d{3}(?:/\d{3})*)", token)
        require(match is not None, "REQUIREMENT_REFERENCE", token)
        assert match is not None
        result.update(match[1] + number for number in match[2].split("/"))
    return result


def _scenarios(text: str) -> list[str]:
    """Read only a scenario-list cell; AS2 inherits the preceding story."""
    result: list[str] = []
    story = ""
    for token in re.split(r"\s*[/,]\s*", text.strip()):
        match = re.fullmatch(r"(?:(?P<story>(?:[A-Z]+-)?US\d+)-)?AS(?P<number>\d+)", token)
        require(match is not None, "SCENARIO_REFERENCE", token)
        assert match is not None
        if match["story"]:
            story = match["story"]
        require(bool(story), "SCENARIO_REFERENCE", text)
        result.append(f"{story}-AS{match['number']}")
    return result


def _test_references(text: str) -> set[str]:
    tokens = re.split(r"\s*,\s*", text.strip())
    require(all(CASE.fullmatch(token) is not None for token in tokens), "TEST_REFERENCE", text)
    return set(tokens)


def _case_traces(row: list[str], distribution: bool) -> tuple[set[str], set[str]]:
    if not distribution:
        return _requirements(row[1]) | _requirements(row[2]), set()
    # The established column is "Level / env; traces". Preconditions and
    # expected-result prose can mention malformed IDs and are never parsed.
    _, separator, trace_list = row[1].partition(";")
    require(bool(separator) and bool(trace_list.strip()), "TEST_ORPHAN", row[0])
    requirements: set[str] = set()
    scenarios: set[str] = set()
    for token in re.split(r"\s*,\s*", trace_list.strip()):
        if re.match(r"(?:[A-Z]+-)?(?:FR|SC)-", token):
            requirements.update(_requirements(token))
        else:
            scenarios.update(_scenarios(token))
    return requirements, scenarios


def feature_requirements(text: str) -> tuple[set[str], set[str]]:
    requirements: set[str] = set()
    scenarios: set[str] = set()
    found: set[str] = set()
    for table in tables(text):
        if table.heading in {"Functional requirements", "Success criteria"}:
            found.add(table.heading)
            require(table.headers[0] == "ID" and bool(table.rows), "REQUIREMENT_TABLE", table.heading)
            for row in table.rows:
                identifier = row[0]
                require(REQUIREMENT.fullmatch(identifier) is not None, "REQUIREMENT_ID", identifier)
                require(identifier not in requirements, "REQUIREMENT_DUPLICATE", identifier)
                require(len(row) > 1 and bool(row[1].strip()), "REQUIREMENT_EMPTY", identifier)
                requirements.add(identifier)
        elif table.headers[0] == "Story":
            for row in table.rows:
                story = re.match(r"(?:[A-Z]+-)?US\d+", row[0])
                require(story is not None, "SCENARIO_ID", row[0])
                assert story is not None
                numbers = re.findall(r"\bAS(\d+):", " ".join(row[1:]))
                require(bool(numbers), "SCENARIO_ID", row[0])
                for number in numbers:
                    identifier = f"{story[0]}-AS{number}"
                    require(identifier not in scenarios, "SCENARIO_DUPLICATE", identifier)
                    scenarios.add(identifier)
    require(found == {"Functional requirements", "Success criteria"} and bool(scenarios),
            "REQUIREMENT_TABLE", "missing requirements, criteria, or scenarios")
    return requirements, scenarios


def validate_coverage(spec: str, tests: str) -> set[str]:
    requirements, scenarios = feature_requirements(spec)
    parsed = tables(tests)
    definitions = [table for table in parsed if table.headers[0] in {"ID", "Case"}]
    require(len(definitions) == 1 and bool(definitions[0].rows), "TEST_TABLE", "expected one independent test table")
    cases: dict[str, set[str]] = {}
    case_scenarios: dict[str, set[str]] = {}
    for row in definitions[0].rows:
        identifier = row[0]
        require(CASE.fullmatch(identifier) is not None, "TEST_ID", identifier)
        require(identifier not in cases, "TEST_DUPLICATE", identifier)
        refs, scenario_refs = _case_traces(row, definitions[0].headers[0] == "Case")
        require(bool(refs), "TEST_ORPHAN", identifier)
        require(refs <= requirements, "REQUIREMENT_REFERENCE", str(sorted(refs - requirements)))
        cases[identifier] = refs
        if definitions[0].headers[0] == "Case":
            require(bool(scenario_refs) and scenario_refs <= scenarios, "SCENARIO_REFERENCE", row[1])
            case_scenarios[identifier] = scenario_refs
    covered = set().union(*cases.values())
    require(covered == requirements, "REQUIREMENT_UNCOVERED", str(sorted(requirements - covered)))
    scenario_coverage: dict[str, set[str]] = {}
    matrices: set[str] = set()
    for table in parsed:
        category = table.headers[0]
        if category not in {"Requirement", "Success criterion", "Scenario", "Acceptance scenario"}:
            continue
        matrices.add(category)
        seen: set[str] = set()
        for row in table.rows:
            if category in {"Scenario", "Acceptance scenario"}:
                listed_scenarios = _scenarios(row[0])
                groups = re.split(r"\s*/\s*", row[1])
                require(len(listed_scenarios) == len(groups), "SCENARIO_MATRIX", row[0])
                for ref, group in zip(listed_scenarios, groups, strict=True):
                    require(ref in scenarios and ref not in scenario_coverage, "SCENARIO_REFERENCE", ref)
                    targets = _test_references(group)
                    require(bool(targets) and targets <= cases.keys(), "TEST_REFERENCE", group)
                    if case_scenarios:
                        expected = {case for case, refs in case_scenarios.items() if ref in refs}
                        require(targets == expected, "COVERAGE_MATRIX_DRIFT", ref)
                    scenario_coverage[ref] = targets
            else:
                ref = row[0]
                require(ref in requirements and ref not in seen, "REQUIREMENT_REFERENCE", ref)
                seen.add(ref)
                targets = _test_references(row[1])
                require(bool(targets) and targets <= cases.keys(), "TEST_REFERENCE", row[1])
                expected = {case for case, refs in cases.items() if ref in refs}
                require(targets == expected, "COVERAGE_MATRIX_DRIFT", ref)
        if category in {"Requirement", "Success criterion"}:
            kind = "FR" if category == "Requirement" else "SC"
            expected_ids = {ref for ref in requirements if f"{kind}-" in ref}
            require(seen == expected_ids, "COVERAGE_MATRIX_MISSING", str(sorted(expected_ids - seen)))
    if definitions[0].headers[0] == "Case":
        require({"Requirement", "Success criterion", "Scenario"} <= matrices,
                "COVERAGE_MATRIX_MISSING", "distribution coverage matrices are required")
    require(set(scenario_coverage) == scenarios, "SCENARIO_UNCOVERED", str(sorted(scenarios - scenario_coverage.keys())))
    return requirements | scenarios


def validate_repository(root: Path) -> dict[str, Any]:
    manifest_file = confined_file(root, MANIFEST_PATH)
    manifest = read_json(manifest_file)
    review = read_json(confined_file(root, REVIEW_PATH))
    _schema(root, "spec-review-v1", review, "SPEC_REVIEW_SCHEMA")
    require(hashlib.sha256(manifest_file.read_bytes()).hexdigest() == review["base_manifest_sha256"],
            "SPEC_MANIFEST_STALE", MANIFEST_PATH)
    overrides = review["current_documents"]
    require(overrides.keys() <= manifest["documents"].keys(), "SPEC_SUCCESSOR_UNKNOWN", "successor is not a registered document")
    documents: dict[str, str] = {}
    normalized: dict[str, Any] = {}
    for identifier, record in manifest["documents"].items():
        original_path = "spec/" + record["path"]
        original_raw = confined_file(root, original_path).read_bytes()
        original = original_raw.decode("utf-8")
        original_meta, _ = frontmatter(original)
        validate_metadata(root, original_meta, identifier, record["role"])
        path = overrides.get(identifier, original_path)
        content = confined_file(root, path).read_bytes().decode("utf-8")
        metadata, body = frontmatter(content)
        normalized[identifier] = validate_metadata(root, metadata, identifier, record["role"])
        if path != original_path:
            predecessor = metadata.get("supersedes", {})
            require(predecessor.get("path") == original_path and predecessor.get("sha256") == hashlib.sha256(original_raw).hexdigest(),
                    "SPEC_SUCCESSOR_SOURCE", identifier)
            require(predecessor.get("revision") == original_meta.get("revision", 1), "SPEC_SUCCESSOR_SOURCE", identifier)
            require(metadata["revision"] > original_meta.get("revision", 1), "SPEC_SUCCESSOR_REVISION", identifier)
        documents[identifier] = body
    identifiers: set[str] = set()
    for feature, record in manifest["features"].items():
        document_id = record["root"]
        require(normalized[document_id].get("feature_id") == feature, "FRONTMATTER_FEATURE", feature)
        tests = confined_file(root, f"build/{feature}/tests.md").read_text(encoding="utf-8")
        identifiers.update(f"{document_id}#{ref}" for ref in validate_coverage(documents[document_id], tests))
    actual_sections = {(document_id, heading): value for document_id, body in documents.items()
                       for heading, value in sections(body).items()}
    seen: set[tuple[str, str]] = set()
    for trace in review["section_traces"]:
        key = (trace["document_id"], trace["heading"])
        require(key in actual_sections and key not in seen, "SPEC_SECTION_REFERENCE", str(key))
        seen.add(key)
        require(hashlib.sha256(actual_sections[key].encode()).hexdigest() == trace["sha256"],
                "SPEC_SECTION_STALE", str(key))
        refs = set(trace["requirements"])
        require(refs <= identifiers, "SPEC_TRACE_REFERENCE", str(sorted(refs - identifiers)))
        require(trace["kind"] != "normative" or bool(refs), "SPEC_OBLIGATION_UNCOVERED", str(key))
        require(trace["kind"] == "normative" or not refs, "SPEC_TRACE_KIND", str(key))
    require(seen == actual_sections.keys(), "SPEC_SECTION_UNCLASSIFIED", str(sorted(actual_sections.keys() - seen)))
    return {"documents": len(documents), "requirement_and_scenario_ids": len(identifiers),
            "sections": len(seen), "status": "independent-test-contract-coverage-only"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        result = validate_repository(args.root)
        print(f"Specification review passed: {result}. Product execution and acceptance are not claimed.")
        return 0
    except (ValidationError, OSError) as exc:
        print(f"SPEC invalid: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
