"""Validate a native task bundle without executing its commands or accepting work."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
from pathlib import Path
from typing import Any

try:
    from .bundle_common import (
        ValidationError,
        confined_file,
        read_json,
        require,
        safe_relative_path,
        sha256_file,
    )
except ImportError:
    from bundle_common import (
        ValidationError,
        confined_file,
        read_json,
        require,
        safe_relative_path,
        sha256_file,
    )

PROFILE = "native-bundle-v1"
GENERATOR_VERSION = "1.0.0"
SCHEMA_VERSION = 1
SHA256 = re.compile(r"^[a-f0-9]{64}$")
SOURCE_KINDS = {"spec", "plan", "tests", "tasks", "policy", "input"}
CAPABILITIES = {"read", "edit", "test"}
EVIDENCE = {"candidate_identity", "command_results", "independent_review"}


def authority_fingerprint(authority: dict[str, Any]) -> str:
    """Fingerprint a reviewed control projection; callers supply its trusted pin."""
    raw = json.dumps(authority, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def runtime_identity() -> str:
    return platform.python_implementation() + "-" + platform.python_version()


def strings(value: Any, field: str, *, empty: bool = False, unique: bool = True) -> list[str]:
    require(isinstance(value, list) and (empty or bool(value)), "FIELD_LIST", field)
    require(all(isinstance(v, str) and v.strip() for v in value), "FIELD_STRING", field)
    require(not unique or len(set(value)) == len(value), "FIELD_DUPLICATE", field)
    return value


def mapping(value: Any, field: str) -> dict[str, Any]:
    require(isinstance(value, dict) and bool(value), "FIELD_OBJECT", field)
    return value


def path_pattern(value: str) -> tuple[str, ...]:
    parts = safe_relative_path(value).parts
    require(not any(ch in value for ch in "?[]"), "PATH_PATTERN", value)
    require(all("*" not in p or p in {"*", "**"} for p in parts), "PATH_PATTERN", value)
    require("**" not in parts[:-1], "PATH_PATTERN", value)
    return parts


def contained(child: str, parent: str) -> bool:
    child_parts, parent_parts = path_pattern(child), path_pattern(parent)
    for index, part in enumerate(parent_parts):
        if part == "**":
            return True
        if index >= len(child_parts) or (part != "*" and child_parts[index] != part):
            return False
        if part == "*" and child_parts[index] == "**":
            return False
    return len(child_parts) == len(parent_parts)


def overlaps(first: str, second: str) -> bool:
    a, b = path_pattern(first), path_pattern(second)
    for left, right in zip(a, b):
        if "**" in {left, right}:
            return True
        if left != right and "*" not in {left, right}:
            return False
    return len(a) == len(b) or (len(a) < len(b) and a[-1] == "**") or (len(b) < len(a) and b[-1] == "**")


def _source_record(root: Path, record: Any, reads: list[str]) -> None:
    record = mapping(record, "source")
    require(set(record) == {"path", "sha256", "kind"}, "SOURCE_FIELDS", "source requires path, sha256, kind")
    require(record["kind"] in SOURCE_KINDS, "SOURCE_KIND", str(record["kind"]))
    path = record["path"]
    require(any(contained(path, scope) for scope in reads), "READ_SCOPE", str(path))
    require(isinstance(record["sha256"], str) and SHA256.fullmatch(record["sha256"]), "SOURCE_DIGEST", str(path))
    file = confined_file(root, path)
    require(file.is_file() and sha256_file(file) == record["sha256"], "SOURCE_STALE", str(path))


def _source(sources: dict[str, Any], name: Any, kind: str) -> None:
    require(isinstance(name, str) and name in sources, "SOURCE_UNKNOWN", str(name))
    require(sources[name]["kind"] == kind, "SOURCE_TRACE_KIND", f"{name}: expected {kind}")


def _refs(value: Any, known: dict[str, Any], field: str) -> set[str]:
    refs = set(strings(value, field))
    require(refs <= known.keys(), "TRACE_UNKNOWN", field + ": " + str(sorted(refs - known.keys())))
    return refs


def _validate_authority(bundle: dict[str, Any], sources: dict[str, Any]) -> dict[str, Any]:
    authority = mapping(bundle.get("authority"), "authority")
    require(set(authority) == {"read_paths", "write_paths", "protected_paths", "capabilities", "acceptance_source", "promotion"}, "AUTHORITY_FIELDS", "unknown or missing authority fields")
    for key in ("read_paths", "write_paths", "protected_paths"):
        for path in strings(authority[key], key, empty=key == "protected_paths"):
            path_pattern(path)
    require(set(strings(authority["capabilities"], "capabilities")) <= CAPABILITIES, "AUTHORITY_CAPABILITY", "only read/edit/test declarations are supported")
    require(authority["promotion"] == "target-repository-only", "AUTHORITY_PROMOTION", "validation cannot grant acceptance or promotion")
    _source(sources, authority["acceptance_source"], "policy")
    return authority


def _validate_trace(profile: dict[str, Any], sources: dict[str, Any], commands: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    requirements = mapping(profile.get("requirements"), "requirements")
    plans = mapping(profile.get("plans"), "plans")
    tests = mapping(profile.get("tests"), "tests")
    for record in requirements.values():
        require(isinstance(record, dict) and set(record) == {"source", "observable"}, "REQUIREMENT_FIELDS", "source and observable required")
        _source(sources, record.get("source"), "spec")
        require(isinstance(record.get("observable"), str) and record["observable"].strip(), "ACCEPTANCE_OBSERVABLE", "requirement needs observable behavior")
    for record in plans.values():
        require(isinstance(record, dict) and set(record) == {"source", "requirements"}, "PLAN_FIELDS", "source and requirements required")
        _source(sources, record.get("source"), "plan")
        _refs(record.get("requirements"), requirements, "plan requirements")
    for record in tests.values():
        require(isinstance(record, dict) and set(record) == {"source", "requirements", "command", "expected_exit", "observable"}, "TEST_FIELDS", "unknown or missing test fields")
        _source(sources, record.get("source"), "tests")
        _refs(record.get("requirements"), requirements, "test requirements")
        require(record.get("command") in commands, "TEST_COMMAND", "unknown test command")
        require(type(record.get("expected_exit")) is int, "TEST_EXIT", "test must declare expected exit")
        require(isinstance(record.get("observable"), str) and record["observable"].strip(), "TEST_OBSERVABLE", "test must declare independent expected behavior")
    return requirements, plans, tests


def _validate_commands(root: Path, commands: dict[str, Any], authority: dict[str, Any]) -> None:
    for name, command in commands.items():
        require(isinstance(command, dict), "COMMAND_RECORD", name)
        require(set(command) == {"argv", "cwd", "capability"}, "COMMAND_FIELDS", name)
        strings(command.get("argv"), name + " argv", unique=False)
        cwd = command.get("cwd")
        if cwd != ".":
            confined_file(root, cwd)
        require(command.get("capability") in authority["capabilities"], "COMMAND_CAPABILITY", name)


def _validate_task(task_id: str, task: Any, trace: Any, state: dict[str, Any]) -> None:
    require(isinstance(task, dict) and isinstance(trace, dict), "TASK_RECORD", task_id)
    require(set(trace) == {"source", "plan", "requirements", "evidence"}, "TRACE_FIELDS", task_id)
    require(set(task) == {"parents", "tests", "paths", "commands", "expected"}, "TASK_FIELDS", task_id)
    strings(task["parents"], "parents", empty=True)
    require(set(task["parents"]) <= state["tasks"].keys(), "PARENT_UNKNOWN", task_id)
    _refs(task["commands"], state["commands"], task_id + " commands")
    traced_tests = _refs(task["tests"], state["tests"], task_id + " tests")
    reqs = _refs(trace.get("requirements"), state["requirements"], task_id + " requirements")
    require(trace.get("plan") in state["plans"], "PLAN_UNKNOWN", task_id)
    require(reqs <= set(state["plans"][trace["plan"]]["requirements"]), "PLAN_TRACE", task_id)
    test_reqs = set().union(*(set(state["tests"][t]["requirements"]) for t in traced_tests))
    require(reqs <= test_reqs, "TEST_TRACE", task_id)
    require(all(state["tests"][t]["command"] in task["commands"] for t in traced_tests), "TASK_TEST_COMMAND", task_id)
    _source(state["sources"], trace.get("source"), "tasks")
    require(set(strings(trace.get("evidence"), "evidence")) >= EVIDENCE, "EVIDENCE_REQUIRED", task_id)
    require(isinstance(task["expected"], str) and task["expected"].strip(), "TASK_EXPECTED", task_id)
    authority = state["authority"]
    for path in strings(task["paths"], task_id + " paths"):
        require(any(contained(path, scope) for scope in authority["write_paths"]), "WRITE_SCOPE", task_id + ": " + path)
        require(not any(overlaps(path, scope) for scope in authority["protected_paths"]), "PROTECTED_SCOPE", task_id + ": " + path)
        frozen = [s["path"] for s in state["sources"].values() if s["kind"] != "input"]
        require(not any(overlaps(path, source) for source in frozen), "FROZEN_SOURCE_WRITE", task_id + ": " + path)


def _acyclic(tasks: dict[str, Any]) -> None:
    remaining = set(tasks)
    completed: set[str] = set()
    while remaining:
        ready = {name for name in remaining if set(tasks[name]["parents"]) <= completed}
        require(bool(ready), "TASK_CYCLE", ", ".join(sorted(remaining)))
        remaining -= ready
        completed |= ready


def validate_bundle(root: Path, path: str, *, expected_authority_sha256: str | None = None) -> dict[str, Any]:
    bundle = mapping(read_json(confined_file(root, path)), "bundle")
    require(type(bundle.get("schema_version")) is int and bundle["schema_version"] == SCHEMA_VERSION, "SCHEMA_UNSUPPORTED", "explicit migration is required")
    require("x_bundle" in bundle, "MIGRATION_REQUIRED", "legacy native contracts require reviewed concrete bundle metadata; no automatic authority migration")
    require(set(bundle) == {"schema_version", "feature", "status", "authority", "commands", "tasks", "x_bundle"}, "BUNDLE_FIELDS", "unknown or missing bundle fields")
    profile = mapping(bundle["x_bundle"], "x_bundle")
    require(set(profile) == {"profile", "versions", "sources", "requirements", "plans", "tests", "task_traces"}, "PROFILE_FIELDS", "unknown or missing profile fields")
    require(profile.get("profile") == PROFILE, "PROFILE_UNSUPPORTED", "explicit migration is required")
    require(profile.get("versions") == {"schema": SCHEMA_VERSION, "generator": GENERATOR_VERSION, "runtime": runtime_identity()}, "VERSION_UNSUPPORTED", "generator/schema/runtime identity must match exactly")
    require(bundle.get("status") == "candidate", "ACCEPTANCE_AUTHORITY", "a bundle validator cannot declare target acceptance")
    sources = mapping(profile.get("sources"), "sources")
    require(len(sources) <= 256, "SOURCE_BUDGET", "maximum source count is 256")
    require(all(isinstance(v, dict) for v in sources.values()), "SOURCE_FIELDS", "source records must be objects")
    authority = _validate_authority(bundle, sources)
    require(expected_authority_sha256 is not None, "AUTHORITY_PIN_REQUIRED", "supply an independently reviewed authority fingerprint")
    require(authority_fingerprint(authority) == expected_authority_sha256, "AUTHORITY_PIN_MISMATCH", "bundle authority differs from the caller's reviewed control state")
    paths = [v.get("path") for v in sources.values()]
    require(len(set(paths)) == len(paths) and path not in paths, "SOURCE_DUPLICATE", "sources must be unique and cannot recursively hash the bundle")
    for record in sources.values():
        _source_record(root, record, authority["read_paths"])
    commands = mapping(bundle.get("commands"), "commands")
    _validate_commands(root, commands, authority)
    requirements, plans, tests = _validate_trace(profile, sources, commands)
    tasks = mapping(bundle.get("tasks"), "tasks")
    traces = mapping(profile.get("task_traces"), "task_traces")
    require(tasks.keys() == traces.keys(), "TASK_TRACE_COVERAGE", "native tasks and traces must match exactly")
    state = {"tasks": tasks, "commands": commands, "requirements": requirements, "plans": plans, "tests": tests, "sources": sources, "authority": authority}
    for name, task in tasks.items():
        _validate_task(name, task, traces[name], state)
    _acyclic(tasks)
    for records, label in ((plans, "plans"), (tests, "tests"), (traces, "tasks")):
        covered = set().union(*(set(record["requirements"]) for record in records.values()))
        require(covered == requirements.keys(), "REQUIREMENT_COVERAGE", label)
    require(set().union(*(set(task["tests"]) for task in tasks.values())) == tests.keys(), "TEST_COVERAGE", "unreferenced tests")
    return bundle


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--authority-sha256", required=True, help="independently reviewed authority projection fingerprint")
    args = parser.parse_args()
    try:
        bundle = validate_bundle(args.root, args.bundle, expected_authority_sha256=args.authority_sha256)
        print(json.dumps({"valid": True, "tasks": len(bundle["tasks"]), "target_acceptance": "not-granted"}, sort_keys=True))
        return 0
    except (ValidationError, KeyError, TypeError, AttributeError) as exc:
        print("BUNDLE invalid: " + str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
