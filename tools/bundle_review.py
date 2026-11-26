"""Deterministic compact review and lossless local bundle expansion."""
from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import html
import json
import platform
import unicodedata
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING or __package__:
    from .bundle_common import (
        ValidationError,
        cli_error,
        confined_file,
        parse_json,
        path_alias_key,
        read_json,
        reject_path_aliases,
        require,
        safe_relative_path,
        sha256_file,
    )
    from .bundle_validation import (
        GENERATOR_VERSION,
        REVIEWED_PROFILE,
        runtime_identity,
        validate_bundle,
    )
else:  # Direct invocation, including the portable three-file bundle tools.
    from bundle_common import (
        ValidationError,
        cli_error,
        confined_file,
        parse_json,
        path_alias_key,
        read_json,
        reject_path_aliases,
        require,
        safe_relative_path,
        sha256_file,
    )
    from bundle_validation import (
        GENERATOR_VERSION,
        REVIEWED_PROFILE,
        runtime_identity,
        validate_bundle,
    )


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False) + "\n").encode()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _cell(value: Any, limit: int = 110) -> str:
    text = " ".join(str(value).split())
    text = text if len(text) <= limit else text[:limit - 1] + "…"
    for char in "\\|[]`*_:!":
        text = text.replace(char, "\\" + char)
    return html.escape(text)


def _source_paths(bundle: dict[str, Any], legacy: bool) -> list[str]:
    if legacy:
        return sorted(bundle.get("authority", {}).get("sha256", {}))
    return sorted(record["path"] for record in bundle["x_bundle"]["sources"].values())


def _input(root: Path, path: str) -> dict[str, str]:
    raw = confined_file(root, path).read_bytes()
    require(len(raw) <= 8 * 1024 * 1024, "INPUT_TOO_LARGE", path)
    return {"path": path, "sha256": digest(raw), "base64": base64.b64encode(raw).decode("ascii")}


def tool_identity() -> dict[str, Any]:
    tools = [Path(__file__).with_name(name) for name in ("bundle_common.py", "bundle_validation.py", "bundle_review.py")]
    return {"generator": GENERATOR_VERSION, "runtime": runtime_identity(),
            "platform": {"system": platform.system(), "machine": platform.machine(), "unicode": unicodedata.unidata_version},
            "source_sha256": {p.name: sha256_file(p) for p in tools}}


def _summary(bundle: dict[str, Any], identity: str, native_sha: str, legacy: bool) -> bytes:
    if legacy:
        state = "legacy view; migration and generic validation required"
    elif bundle["x_bundle"]["profile"] == REVIEWED_PROFILE:
        state = "structurally validated candidate with reviewed command identities; target acceptance not granted"
    else:
        state = "legacy v1 structural validation; command review and target acceptance not granted"
    lines = ["# Bundle review", "", f"State: **{state}**.", "", f"Feature: {_cell(bundle.get('feature', 'unknown'))}.", "", f"Native bytes: `{native_sha}`. Machine detail: [lossless object](objects/{identity}.json).", "", "The native task contract remains the sole dependency graph. This view executes no command, accepts no result, and grants no publication or deployment authority. Long descriptions are shortened here; the object retains every input byte.", "", "Risks to review: commands are unexecuted declarations; broad write scopes need target sandbox enforcement; frozen or accepted inputs cannot be silently replaced; structural conformance cannot establish source rights or independent target acceptance.", "", "| Task / intent | Parents | Observable acceptance | Tests | Write boundary |", "| --- | --- | --- | --- | --- |"]
    for name, task in sorted(bundle.get("tasks", {}).items()):
        title = bundle.get("x_distribution", {}).get("task_metadata", {}).get(name, {}).get("title", "")
        row = [name + (": " + title if title else ""), ", ".join(task.get("parents", [])) or "none", task.get("expected", "missing"), ", ".join(task.get("tests", [])), ", ".join(task.get("paths", []))]
        lines.append("| " + " | ".join(_cell(value) for value in row) + " |")
    lines += ["", "Source and authority review remains required. Structural conformance does not prove that prose is correct, tests are sufficient, commands obey their declared scope, or a legacy task is ready to execute.", ""]
    return "\n".join(lines).encode()


def generate(root: Path, path: str, *, legacy: bool = False, expected_authority_sha256: str | None = None) -> dict[str, bytes]:
    bundle = read_json(confined_file(root, path)) if legacy else validate_bundle(root, path, expected_authority_sha256=expected_authority_sha256)
    require(isinstance(bundle, dict) and isinstance(bundle.get("tasks"), dict), "NATIVE_SHAPE", path)
    if legacy:
        require("x_bundle" not in bundle, "LEGACY_MODE", "profiled bundles must use ordinary validation")
        authority = bundle.get("authority")
        require(isinstance(authority, dict), "LEGACY_SOURCES", "authority must be an object")
        authority = cast(dict[str, Any], authority)
        expected = authority.get("sha256", {})
        require(isinstance(expected, dict) and bool(expected), "LEGACY_SOURCES", "frozen source hashes required")
        distribution = bundle.get("x_distribution", {})
        require(isinstance(distribution, dict), "LEGACY_METADATA", "distribution metadata must be an object")
        metadata = distribution.get("task_metadata", {})
        require(isinstance(metadata, dict), "LEGACY_METADATA", "task metadata must be an object")
        for name, task in bundle["tasks"].items():
            require(isinstance(task, dict), "LEGACY_TASK", name)
            for field in ("parents", "tests", "paths"):
                items = task.get(field, [])
                require(isinstance(items, list) and all(isinstance(item, str) for item in items), "LEGACY_TASK", name + ": " + field)
            display = metadata.get(name, {})
            require(isinstance(display, dict) and isinstance(display.get("title", ""), str), "LEGACY_METADATA", name)
        for source, sha in expected.items():
            require(sha256_file(confined_file(root, source)) == sha, "SOURCE_STALE", source)
    paths = sorted({path, *_source_paths(bundle, legacy)})
    require(sum(confined_file(root, source).stat().st_size for source in paths) <= 16 * 1024 * 1024, "INPUT_BUDGET", "maximum combined input size is 16 MiB")
    reviewed = not legacy and bundle["x_bundle"]["profile"] == REVIEWED_PROFILE
    detail: dict[str, Any] = {"schema_version": 1, "kind": "lossless-bundle-inputs", "entrypoint": path,
              "mode": "legacy-review-only" if legacy else ("validated-v2-candidate" if reviewed else "legacy-v1-structural"),
              "authority_sha256": expected_authority_sha256,
              "inputs": [_input(root, source) for source in paths]}
    raw = canonical(detail)
    identity = digest(raw)
    summary = _summary(bundle, identity, sha256_file(confined_file(root, path)), legacy)
    receipt = {"schema_version": 1, "detail_sha256": identity, "review_sha256": digest(summary), "toolchain": tool_identity(),
               "input_sha256": {record["path"]: record["sha256"] for record in detail["inputs"]},
               "state": detail["mode"], "reviewed_commands": reviewed,
               "bundle_generation": bundle.get("x_bundle", {}).get("versions"),
               "target_acceptance": "not-granted", "publication": "not-performed"}
    return {"README.md": summary, "regeneration.json": canonical(receipt), f"objects/{identity}.json": raw}


def write_or_check(output: Path, files: dict[str, bytes], *, check: bool) -> None:
    require(not any(p.is_symlink() for p in (output, *output.parents)), "OUTPUT_SYMLINK", str(output))
    for relative, raw in files.items():
        path = confined_file(output, relative)
        if check:
            require(path.is_file() and path.read_bytes() == raw, "REGENERATION_DRIFT", relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists():
                require(path.read_bytes() == raw or not relative.startswith("objects/"), "OBJECT_IMMUTABLE", relative)
            path.write_bytes(raw)


def expand(detail: Path, expected_sha: str, output: Path) -> None:
    raw = detail.read_bytes()
    require(digest(raw) == expected_sha, "DETAIL_TAMPERED", "detail fingerprint mismatch")
    payload = parse_json(raw, source=str(detail))
    require(isinstance(payload, dict), "DETAIL_SHAPE", "detail must be an object")
    require(type(payload.get("schema_version")) is int and payload["schema_version"] == 1
            and payload.get("kind") == "lossless-bundle-inputs", "DETAIL_VERSION", "explicit migration required")
    records = payload.get("inputs")
    require(isinstance(records, list) and bool(records), "DETAIL_INPUTS", "missing input inventory")
    files: dict[str, bytes] = {}
    for record in records:
        require(isinstance(record, dict) and set(record) == {"path", "sha256", "base64"},
                "DETAIL_RECORD", "each input requires path, sha256 and base64")
        path = record["path"]
        safe_relative_path(path)
        require(path not in files, "DETAIL_DUPLICATE", path)
        require(isinstance(record["base64"], str), "DETAIL_BASE64", path)
        require(isinstance(record["sha256"], str), "DETAIL_DIGEST", path)
        try:
            data = base64.b64decode(record["base64"], validate=True)
        except (binascii.Error, ValueError) as exc:
            raise ValidationError(f"DETAIL_BASE64: {path}") from exc
        require(digest(data) == record["sha256"], "INPUT_TAMPERED", path)
        files[path] = data
    reject_path_aliases(list(files), code="DETAIL_PATH_ALIAS")
    paths = [path_alias_key(path) for path in files]
    require(not any(len(left) < len(right) and left == right[:len(left)] for left in paths for right in paths),
            "DETAIL_PATH_CONFLICT", "file/directory prefix collision")
    require(not output.is_symlink(), "OUTPUT_SYMLINK", str(output))
    require(not output.exists() or not any(output.iterdir()), "OUTPUT_NOT_EMPTY", str(output))
    write_or_check(output, files, check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--debug", action="store_true", help="show a traceback for an unexpected internal fault")
    sub = parser.add_subparsers(dest="operation", required=True)
    render = sub.add_parser("render")
    render.add_argument("bundle")
    render.add_argument("--root", type=Path, default=Path.cwd())
    render.add_argument("--output", type=Path, required=True)
    render.add_argument("--check", action="store_true")
    render.add_argument("--legacy-review-only", action="store_true")
    render.add_argument("--authority-sha256", help="independently reviewed authority projection fingerprint")
    render.add_argument("--debug", action="store_true", default=argparse.SUPPRESS,
                        help="show a traceback for an unexpected internal fault")
    restore = sub.add_parser("expand")
    restore.add_argument("detail", type=Path)
    restore.add_argument("--sha256", required=True)
    restore.add_argument("--output", type=Path, required=True)
    restore.add_argument("--debug", action="store_true", default=argparse.SUPPRESS,
                         help="show a traceback for an unexpected internal fault")
    args = parser.parse_args()
    try:
        if args.operation == "render":
            write_or_check(args.output, generate(args.root, args.bundle, legacy=args.legacy_review_only, expected_authority_sha256=args.authority_sha256), check=args.check)
        else:
            expand(args.detail, args.sha256, args.output)
        print("Bundle review operation passed; target acceptance not granted.")
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI boundary reports internal faults with a distinct exit.
        return cli_error(exc, context="BUNDLE review failed", debug=args.debug)


if __name__ == "__main__":
    raise SystemExit(main())
