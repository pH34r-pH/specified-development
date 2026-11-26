"""Validate a native task bundle without executing its commands or accepting work."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING or __package__:
    from .bundle_common import (
        cli_error,
        confined_file,
        path_alias_key,
        read_json,
        reject_path_aliases,
        require,
        safe_relative_path,
        sha256_file,
    )
else:  # Direct invocation, including the portable three-file bundle tools.
    from bundle_common import (
        cli_error,
        confined_file,
        path_alias_key,
        read_json,
        reject_path_aliases,
        require,
        safe_relative_path,
        sha256_file,
    )

PROFILE = "native-bundle-v1"
REVIEWED_PROFILE = "native-bundle-v2"
GENERATOR_VERSION = "2.0.0"
SCHEMA_VERSION = 1
REVIEWED_SCHEMA_VERSION = 2
SHA256 = re.compile(r"^[a-f0-9]{64}$")
SOURCE_KINDS = {"spec", "plan", "tests", "tasks", "policy", "input"}
CAPABILITIES = {"read", "edit", "test"}
EVIDENCE = {"candidate_identity", "command_results", "independent_review"}


def authority_fingerprint(authority: dict[str, Any]) -> str:
    """Fingerprint a reviewed control projection; callers supply its trusted pin."""
    raw = json.dumps(authority, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def reviewed_fingerprint(bundle: dict[str, Any]) -> str:
    """Version 2 binds reviewed commands and source bytes, not candidate assertions."""
    profile = mapping(bundle.get("x_bundle"), "x_bundle")
    require(profile.get("profile") == REVIEWED_PROFILE, "PROFILE_UNSUPPORTED", "reviewed command pins require native-bundle-v2")
    projection = {"profile": REVIEWED_PROFILE, "schema_version": bundle.get("schema_version"),
                  "versions": profile.get("versions"), "authority": bundle.get("authority"),
                  "commands": bundle.get("commands"), "sources": profile.get("sources")}
    return authority_fingerprint(projection)


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


def path_pattern(value: str, *, portable: bool = False) -> tuple[str, ...]:
    parts = safe_relative_path(value).parts
    require(not any(ch in value for ch in "?[]"), "PATH_PATTERN", value)
    require(all("*" not in p or p in {"*", "**"} for p in parts), "PATH_PATTERN", value)
    require("**" not in parts[:-1], "PATH_PATTERN", value)
    return path_alias_key(value) if portable else parts


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


def overlaps(first: str, second: str, *, portable: bool = False) -> bool:
    """V2 also protects matching ancestors against directory replacement."""
    a, b = path_pattern(first, portable=portable), path_pattern(second, portable=portable)
    for left, right in zip(a, b):
        if "**" in {left, right}:
            return True
        if left != right and "*" not in {left, right}:
            return False
    if portable:
        # A matching prefix can name the protected root itself (terminal **
        # includes zero components), or an ancestor whose replacement removes it.
        return True
    return len(a) == len(b) or (len(a) < len(b) and a[-1] == "**") or (len(b) < len(a) and b[-1] == "**")


def _source_record(root: Path, record: Any, reads: list[str]) -> None:
    record = mapping(record, "source")
    require(set(record) == {"path", "sha256", "kind"}, "SOURCE_FIELDS", "source requires path, sha256, kind")
    require(isinstance(record["kind"], str) and record["kind"] in SOURCE_KINDS, "SOURCE_KIND", str(record["kind"]))
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
    acceptance = authority["acceptance_source"]
    require(isinstance(acceptance, dict) and set(acceptance) == {"id", "sha256"}, "ACCEPTANCE_SOURCE_FIELDS", "pin an exact policy source identity and digest")
    _source(sources, acceptance["id"], "policy")
    require(acceptance["sha256"] == sources[acceptance["id"]].get("sha256"), "ACCEPTANCE_SOURCE_DIGEST", "reviewed acceptance-source digest differs from source record")
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
        require(isinstance(record.get("command"), str) and record["command"] in commands, "TEST_COMMAND", "unknown test command")
        require(type(record.get("expected_exit")) is int, "TEST_EXIT", "test must declare expected exit")
        require(isinstance(record.get("observable"), str) and record["observable"].strip(), "TEST_OBSERVABLE", "test must declare independent expected behavior")
    return requirements, plans, tests


def _validate_commands(root: Path, commands: dict[str, Any], authority: dict[str, Any],
                       sources: dict[str, Any], *, reviewed: bool) -> None:
    for name, command in commands.items():
        require(isinstance(command, dict), "COMMAND_RECORD", name)
        fields = {"argv", "cwd", "capability"} | ({"script_source"} if reviewed else set())
        require(set(command) == fields, "COMMAND_FIELDS", name)
        argv = strings(command.get("argv"), name + " argv", unique=False)
        cwd = command.get("cwd")
        if cwd != ".":
            confined_file(root, cwd)
        require(command.get("capability") in authority["capabilities"], "COMMAND_CAPABILITY", name)
        if reviewed:
            require(len(argv) >= 2 and argv[0] in {"python", "python3"} and not argv[1].startswith("-"),
                    "COMMAND_FORM", "v2 supports only python/python3 <declared script> [arguments]")
            script_id = command.get("script_source")
            require(isinstance(script_id, str) and script_id in sources, "COMMAND_SOURCE", name)
            require(sources[script_id]["kind"] in {"tests", "input"}, "COMMAND_SOURCE_KIND", name)
            script = safe_relative_path(argv[1])
            resolved = script if cwd == "." else safe_relative_path(cwd) / script
            require(str(resolved) == sources[script_id]["path"], "COMMAND_SOURCE_PATH", name)
            require((root if cwd == "." else confined_file(root, cwd)).is_dir(), "COMMAND_CWD", name)


def _validate_task(task_id: str, task: Any, trace: Any, state: dict[str, Any]) -> None:
    require(isinstance(task, dict) and isinstance(trace, dict), "TASK_RECORD", task_id)
    require(set(trace) == {"source", "plan", "requirements", "evidence"}, "TRACE_FIELDS", task_id)
    require(set(task) == {"parents", "tests", "paths", "commands", "expected"}, "TASK_FIELDS", task_id)
    strings(task["parents"], "parents", empty=True)
    require(set(task["parents"]) <= state["tasks"].keys(), "PARENT_UNKNOWN", task_id)
    _refs(task["commands"], state["commands"], task_id + " commands")
    traced_tests = _refs(task["tests"], state["tests"], task_id + " tests")
    reqs = _refs(trace.get("requirements"), state["requirements"], task_id + " requirements")
    require(isinstance(trace.get("plan"), str) and trace["plan"] in state["plans"], "PLAN_UNKNOWN", task_id)
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
        require(not any(overlaps(path, scope, portable=state["reviewed"]) for scope in authority["protected_paths"]), "PROTECTED_SCOPE", task_id + ": " + path)
        script_ids = {c["script_source"] for c in state["commands"].values()} if state["reviewed"] else set()
        frozen = [s["path"] for name, s in state["sources"].items() if s["kind"] != "input" or name in script_ids]
        require(not any(overlaps(path, source, portable=state["reviewed"]) for source in frozen), "FROZEN_SOURCE_WRITE", task_id + ": " + path)


def _acyclic(tasks: dict[str, Any]) -> None:
    remaining = set(tasks)
    completed: set[str] = set()
    while remaining:
        ready = {name for name in remaining if set(tasks[name]["parents"]) <= completed}
        require(bool(ready), "TASK_CYCLE", ", ".join(sorted(remaining)))
        remaining -= ready
        completed |= ready


def _validate_versions(bundle: dict[str, Any], profile: dict[str, Any]) -> bool:
    """Retain v1 exactness; v2 separates compatible validation from provenance."""
    name = profile.get("profile")
    require(name in (PROFILE, REVIEWED_PROFILE), "PROFILE_UNSUPPORTED", "explicit migration is required")
    reviewed = name == REVIEWED_PROFILE
    schema = REVIEWED_SCHEMA_VERSION if reviewed else SCHEMA_VERSION
    require(type(bundle.get("schema_version")) is int and bundle["schema_version"] == schema,
            "SCHEMA_UNSUPPORTED", "profile and schema must match; explicit migration is required")
    versions = profile["versions"]
    require(isinstance(versions, dict) and set(versions) == {"schema", "generator", "runtime"},
            "VERSION_UNSUPPORTED", "schema, generator and generation runtime are required")
    require(type(versions.get("schema")) is int and versions["schema"] == schema,
            "VERSION_UNSUPPORTED", "schema version must match the profile")
    if not reviewed:
        require(versions == {"schema": SCHEMA_VERSION, "generator": "1.0.0", "runtime": runtime_identity()},
                "VERSION_UNSUPPORTED", "legacy v1 generator/schema/runtime identity must match exactly")
        return False
    require(versions.get("generator") == GENERATOR_VERSION and isinstance(versions.get("runtime"), str)
            and re.fullmatch(r"CPython-3\.12\.[0-9]+", versions["runtime"]) is not None,
            "VERSION_UNSUPPORTED", "v2 requires generator 2.0.0 and CPython 3.12 generation provenance")
    require(platform.python_implementation() == "CPython" and platform.python_version_tuple()[:2] == ("3", "12"),
            "RUNTIME_UNSUPPORTED", "v2 validation supports CPython 3.12 patch releases")
    return True


def validate_bundle(root: Path, path: str, *, expected_authority_sha256: str | None = None) -> dict[str, Any]:
    bundle = mapping(read_json(confined_file(root, path)), "bundle")
    require(type(bundle.get("schema_version")) is int and bundle["schema_version"] in {SCHEMA_VERSION, REVIEWED_SCHEMA_VERSION}, "SCHEMA_UNSUPPORTED", "explicit migration is required")
    require("x_bundle" in bundle, "MIGRATION_REQUIRED", "legacy native contracts require reviewed concrete bundle metadata; no automatic authority migration")
    require(set(bundle) == {"schema_version", "feature", "status", "authority", "commands", "tasks", "x_bundle"}, "BUNDLE_FIELDS", "unknown or missing bundle fields")
    profile = mapping(bundle["x_bundle"], "x_bundle")
    require(set(profile) == {"profile", "versions", "sources", "requirements", "plans", "tests", "task_traces"}, "PROFILE_FIELDS", "unknown or missing profile fields")
    reviewed = _validate_versions(bundle, profile)
    require(bundle.get("status") == "candidate", "ACCEPTANCE_AUTHORITY", "a bundle validator cannot declare target acceptance")
    sources = mapping(profile.get("sources"), "sources")
    require(len(sources) <= 256, "SOURCE_BUDGET", "maximum source count is 256")
    require(all(isinstance(v, dict) and set(v) == {"path", "sha256", "kind"} for v in sources.values()),
            "SOURCE_FIELDS", "source records require path, sha256 and kind")
    require(all(isinstance(v["path"], str) for v in sources.values()), "SOURCE_FIELDS", "source paths must be strings")
    require(all(isinstance(v["kind"], str) and v["kind"] in SOURCE_KINDS for v in sources.values()),
            "SOURCE_KIND", "source kinds must be supported strings")
    authority = _validate_authority(bundle, sources)
    require(expected_authority_sha256 is not None, "AUTHORITY_PIN_REQUIRED", "supply an independently reviewed authority fingerprint")
    fingerprint = reviewed_fingerprint(bundle) if reviewed else authority_fingerprint(authority)
    require(fingerprint == expected_authority_sha256, "AUTHORITY_PIN_MISMATCH", "bundle differs from the caller's reviewed control state")
    paths = [v.get("path") for v in sources.values()]
    require(len(set(paths)) == len(paths) and path not in paths, "SOURCE_DUPLICATE", "sources must be unique and cannot recursively hash the bundle")
    if reviewed:
        reject_path_aliases([path, *paths], code="SOURCE_ALIAS")
        for key in ("read_paths", "write_paths", "protected_paths"):
            reject_path_aliases(authority[key])
    for record in sources.values():
        _source_record(root, record, authority["read_paths"])
    commands = mapping(bundle.get("commands"), "commands")
    _validate_commands(root, commands, authority, sources, reviewed=reviewed)
    requirements, plans, tests = _validate_trace(profile, sources, commands)
    tasks = mapping(bundle.get("tasks"), "tasks")
    traces = mapping(profile.get("task_traces"), "task_traces")
    require(tasks.keys() == traces.keys(), "TASK_TRACE_COVERAGE", "native tasks and traces must match exactly")
    state = {"tasks": tasks, "commands": commands, "requirements": requirements, "plans": plans, "tests": tests, "sources": sources, "authority": authority, "reviewed": reviewed}
    for name, task in tasks.items():
        _validate_task(name, task, traces[name], state)
    if reviewed:
        reject_path_aliases([path for task in tasks.values() for path in task["paths"]], code="OUTPUT_ALIAS")
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
    parser.add_argument("--debug", action="store_true", help="show a traceback for an unexpected internal fault")
    args = parser.parse_args()
    try:
        bundle = validate_bundle(args.root, args.bundle, expected_authority_sha256=args.authority_sha256)
        print(json.dumps({"valid": True, "tasks": len(bundle["tasks"]), "profile": bundle["x_bundle"]["profile"],
                          "reviewed_commands": bundle["x_bundle"]["profile"] == REVIEWED_PROFILE,
                          "target_acceptance": "not-granted"}, sort_keys=True))
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI boundary reports internal faults with a distinct exit.
        return cli_error(exc, context="BUNDLE validation failed", debug=args.debug)


if __name__ == "__main__":
    raise SystemExit(main())
