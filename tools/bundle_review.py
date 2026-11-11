"""Deterministic compact review and lossless local bundle expansion."""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
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
    from .bundle_validation import GENERATOR_VERSION, runtime_identity, validate_bundle
except ImportError:
    from bundle_common import (
        ValidationError,
        confined_file,
        read_json,
        require,
        safe_relative_path,
        sha256_file,
    )
    from bundle_validation import GENERATOR_VERSION, runtime_identity, validate_bundle


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
    return {"generator": GENERATOR_VERSION, "runtime": runtime_identity(), "source_sha256": {p.name: sha256_file(p) for p in tools}}


def _summary(bundle: dict[str, Any], identity: str, native_sha: str, legacy: bool) -> bytes:
    state = "legacy view; migration and generic validation required" if legacy else "structurally validated candidate; target acceptance not granted"
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
        expected = bundle.get("authority", {}).get("sha256", {})
        require(isinstance(expected, dict) and bool(expected), "LEGACY_SOURCES", "frozen source hashes required")
        for source, sha in expected.items():
            require(sha256_file(confined_file(root, source)) == sha, "SOURCE_STALE", source)
    paths = sorted({path, *_source_paths(bundle, legacy)})
    require(sum(confined_file(root, source).stat().st_size for source in paths) <= 16 * 1024 * 1024, "INPUT_BUDGET", "maximum combined input size is 16 MiB")
    detail = {"schema_version": 1, "kind": "lossless-bundle-inputs", "entrypoint": path,
              "mode": "legacy-review-only" if legacy else "validated-candidate", "authority_sha256": expected_authority_sha256,
              "inputs": [_input(root, source) for source in paths]}
    raw = canonical(detail)
    identity = digest(raw)
    summary = _summary(bundle, identity, sha256_file(confined_file(root, path)), legacy)
    receipt = {"schema_version": 1, "detail_sha256": identity, "review_sha256": digest(summary), "toolchain": tool_identity(),
               "input_sha256": {record["path"]: record["sha256"] for record in detail["inputs"]},
               "state": detail["mode"], "target_acceptance": "not-granted", "publication": "not-performed"}
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
    payload = json.loads(raw)
    require(payload.get("schema_version") == 1 and payload.get("kind") == "lossless-bundle-inputs", "DETAIL_VERSION", "explicit migration required")
    records = payload.get("inputs")
    require(isinstance(records, list) and bool(records), "DETAIL_INPUTS", "missing input inventory")
    files: dict[str, bytes] = {}
    for record in records:
        path = record["path"]
        safe_relative_path(path)
        require(path not in files, "DETAIL_DUPLICATE", path)
        data = base64.b64decode(record["base64"], validate=True)
        require(digest(data) == record["sha256"], "INPUT_TAMPERED", path)
        files[path] = data
    paths = [safe_relative_path(path) for path in files]
    require(not any(left in right.parents for left in paths for right in paths), "DETAIL_PATH_CONFLICT", "file/directory prefix collision")
    require(not output.is_symlink(), "OUTPUT_SYMLINK", str(output))
    require(not output.exists() or not any(output.iterdir()), "OUTPUT_NOT_EMPTY", str(output))
    write_or_check(output, files, check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    render = sub.add_parser("render")
    render.add_argument("bundle")
    render.add_argument("--root", type=Path, default=Path.cwd())
    render.add_argument("--output", type=Path, required=True)
    render.add_argument("--check", action="store_true")
    render.add_argument("--legacy-review-only", action="store_true")
    render.add_argument("--authority-sha256", help="independently reviewed authority projection fingerprint")
    restore = sub.add_parser("expand")
    restore.add_argument("detail", type=Path)
    restore.add_argument("--sha256", required=True)
    restore.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.operation == "render":
            write_or_check(args.output, generate(args.root, args.bundle, legacy=args.legacy_review_only, expected_authority_sha256=args.authority_sha256), check=args.check)
        else:
            expand(args.detail, args.sha256, args.output)
        print("Bundle review operation passed; target acceptance not granted.")
        return 0
    except (ValidationError, OSError, ValueError, KeyError, TypeError) as exc:
        print("BUNDLE review failed: " + str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
