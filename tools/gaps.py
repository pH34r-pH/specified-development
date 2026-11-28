"""Report requirement status, gaps and stale descendants from independent evidence.

Status comes only from independent case outcomes recorded at an exact revision
against exact requirement text hashes. Prose and document fields never mark a
requirement satisfied. The report is deterministic, offline and model-free.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING or __package__:
    from .bundle_common import ValidationError, confined_file, read_json, require
    from .spec_validation import (
        MANIFEST_PATH,
        REQUIREMENT,
        frontmatter,
        sections,
        tables,
    )
else:
    from bundle_common import ValidationError, confined_file, read_json, require
    from spec_validation import (
        MANIFEST_PATH,
        REQUIREMENT,
        frontmatter,
        sections,
        tables,
    )

EVIDENCE_KIND = "requirement-evidence"
REPORT_KIND = "requirement-status"
REVISION_RE = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
OUTCOMES = {"pass", "fail"}
REQUIREMENT_TABLES = {"Functional requirements", "Success criteria"}


def _object(value: Any, code: str, context: str, keys: set[str], optional: frozenset[str] = frozenset()) -> dict[str, Any]:
    require(isinstance(value, dict), code, f"{context} must be an object")
    value = cast(dict[str, Any], value)
    missing = keys - optional - value.keys()
    unknown = value.keys() - keys
    require(not missing and not unknown, code, f"{context}: missing={sorted(missing)} unknown={sorted(unknown)}")
    return value


def _revision(value: Any, context: str) -> str:
    require(isinstance(value, str) and REVISION_RE.fullmatch(value) is not None,
            "GAP_REVISION", f"{context} must be an exact commit identity")
    return cast(str, value)


def requirement_hash(text: str) -> str:
    return hashlib.sha256(" ".join(text.split()).encode("utf-8")).hexdigest()


def requirement_texts(root: Path, features: list[str]) -> dict[str, str]:
    """Return qualified requirement ID -> normalized description hash for each feature."""
    manifest = read_json(confined_file(root, MANIFEST_PATH))
    require(isinstance(manifest, dict) and isinstance(manifest.get("features"), dict)
            and isinstance(manifest.get("documents"), dict), "GAP_SPEC", "spec manifest is malformed")
    result: dict[str, str] = {}
    for feature in features:
        record = manifest["features"].get(feature)
        require(isinstance(record, dict), "GAP_SPEC", f"not a specified feature: {feature}")
        document = manifest["documents"].get(record.get("root"))
        require(isinstance(document, dict), "GAP_SPEC", f"feature root is not a registered document: {feature}")
        _, body = frontmatter(confined_file(root, "spec/" + document["path"]).read_text(encoding="utf-8"))
        for table in tables(body):
            if table.heading not in REQUIREMENT_TABLES:
                continue
            for row in table.rows:
                identifier = row[0]
                require(REQUIREMENT.fullmatch(identifier) is not None and len(row) > 1, "GAP_SPEC", identifier)
                qualified = f"{feature}#{identifier}"
                require(qualified not in result, "GAP_SPEC", f"duplicate requirement: {qualified}")
                result[qualified] = requirement_hash(row[1])
    return result


def plan_citations(root: Path, features: list[str], changed: set[str]) -> list[str]:
    """Return plan sections (path#heading) that cite a changed requirement ID."""
    cited: list[str] = []
    for feature in features:
        relative = f"build/{feature}/plan.md"
        path = confined_file(root, relative)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        body = frontmatter(text)[1] if text.startswith("---") else text
        identifiers = {item.split("#", 1)[1] for item in changed if item.startswith(feature + "#")}
        for heading, section in sections(body).items():
            if any(re.search(rf"(?<![\w-]){re.escape(identifier)}(?![\w-])", section) for identifier in identifiers):
                cited.append(f"{relative}#{heading}")
    return sorted(cited)


def build_report(root: Path, evidence: Any, previous: Any | None = None) -> dict[str, Any]:
    evidence = _object(evidence, "GAP_SHAPE", "evidence",
                       {"schema_version", "kind", "revision", "features", "cases", "tasks", "results"})
    require(evidence["schema_version"] == 1 and evidence["kind"] == EVIDENCE_KIND, "GAP_SHAPE",
            "evidence must be a version 1 requirement-evidence record")
    revision = _revision(evidence["revision"], "revision")
    features = evidence["features"]
    require(isinstance(features, list) and bool(features) and all(isinstance(item, str) for item in features)
            and len(set(features)) == len(features), "GAP_SHAPE", "features must be a nonempty unique list")
    hashes = requirement_texts(root, features)

    cases = evidence["cases"]
    require(isinstance(cases, dict), "GAP_SHAPE", "cases must be an object")
    traces: dict[str, set[str]] = {}
    for name, case in cases.items():
        case = _object(case, "GAP_SHAPE", f"case {name}", {"requirements"})
        requirements = case["requirements"]
        require(isinstance(requirements, list) and bool(requirements), "GAP_ORPHAN_CASE", f"case traces no requirement: {name}")
        unknown = sorted(set(requirements) - hashes.keys())
        require(not unknown, "GAP_UNKNOWN_REQUIREMENT", f"case {name} traces unknown requirements: {unknown}")
        traces[name] = set(requirements)

    tasks = evidence["tasks"]
    require(isinstance(tasks, dict), "GAP_SHAPE", "tasks must be an object")
    task_cases: dict[str, set[str]] = {}
    for name, task in tasks.items():
        task = _object(task, "GAP_SHAPE", f"task {name}", {"cases"})
        named = task["cases"]
        require(isinstance(named, list) and bool(named), "GAP_SHAPE", f"task {name} needs cases")
        unknown = sorted(set(named) - traces.keys())
        require(not unknown, "GAP_UNKNOWN_CASE", f"task {name} names unknown cases: {unknown}")
        task_cases[name] = set(named)

    outcomes: dict[str, str] = {}
    run_hashes: dict[str, str] = {}
    results = evidence["results"]
    if results is not None:
        results = _object(results, "GAP_SHAPE", "results", {"revision", "requirement_hashes", "cases"})
        require(_revision(results["revision"], "results.revision") == revision, "GAP_RESULTS_REVISION",
                "results must be recorded at the evidence revision")
        recorded = results["cases"]
        require(isinstance(recorded, dict), "GAP_SHAPE", "results.cases must be an object")
        undeclared = sorted(set(recorded) - traces.keys())
        require(not undeclared, "GAP_UNKNOWN_CASE", f"outcomes for undeclared cases: {undeclared}")
        require(all(value in OUTCOMES for value in recorded.values()), "GAP_OUTCOME", "outcomes must be pass or fail")
        outcomes = cast(dict[str, str], recorded)
        run_hashes = results["requirement_hashes"]
        require(isinstance(run_hashes, dict) and all(isinstance(value, str) for value in run_hashes.values()),
                "GAP_SHAPE", "results.requirement_hashes must map requirements to hashes")

    prior: dict[str, Any] = {}
    if previous is not None:
        require(isinstance(previous, dict) and previous.get("kind") == REPORT_KIND
                and isinstance(previous.get("requirements"), dict), "GAP_PREVIOUS", "previous must be a requirement-status report")
        prior = previous["requirements"]

    statuses: dict[str, dict[str, Any]] = {}
    for requirement, current in sorted(hashes.items()):
        tracing = sorted(name for name, traced in traces.items() if requirement in traced)
        if not tracing:
            status = "untested"
        elif run_hashes.get(requirement) != current or any(name not in outcomes for name in tracing):
            status = "stale"
        elif any(outcomes[name] == "fail" for name in tracing):
            before = prior.get(requirement, {})
            status = "regressed" if before.get("status") == "satisfied" and before.get("hash") == current else "failing"
        else:
            status = "satisfied"
        statuses[requirement] = {"hash": current, "status": status, "cases": tracing}

    changed = sorted(requirement for requirement, current in hashes.items()
                     if previous is not None and prior.get(requirement, {}).get("hash") != current)
    changed_set = set(changed)
    stale_cases = sorted(name for name, traced in traces.items() if traced & changed_set)
    stale_tasks = sorted(name for name, named in task_cases.items() if named & set(stale_cases))
    return {
        "schema_version": 1,
        "kind": REPORT_KIND,
        "revision": revision,
        "requirements": statuses,
        "gaps": sorted(requirement for requirement, entry in statuses.items() if entry["status"] != "satisfied"),
        "changed": changed,
        "stale": {"cases": stale_cases, "tasks": stale_tasks,
                  "plan_sections": plan_citations(root, features, changed_set)},
    }


def canonical(report: dict[str, Any]) -> bytes:
    return (json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="requirement-evidence JSON")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    parser.add_argument("--previous", type=Path, help="previous requirement-status report")
    parser.add_argument("--output", type=Path, help="write the report here instead of stdout")
    args = parser.parse_args()
    try:
        previous = read_json(args.previous) if args.previous else None
        raw = canonical(build_report(args.root, read_json(args.evidence), previous))
        if args.output:
            args.output.write_bytes(raw)
        else:
            sys.stdout.buffer.write(raw)
        return 0
    except (ValidationError, OSError) as exc:
        print(f"GAP report invalid: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
