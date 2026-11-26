"""Shared confined reads and exact-byte identities; no repository-specific policy."""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import traceback
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any


class ValidationError(ValueError):
    """A stable, user-facing validation failure."""


def require(condition: object, code: str, message: str) -> None:
    if not condition:
        raise ValidationError(f"{code}: {message}")


def read_json(path: Path) -> Any:
    try:
        require(path.stat().st_size <= 8 * 1024 * 1024, "JSON_TOO_LARGE", "maximum JSON input is 8 MiB")
        return parse_json(path.read_bytes(), source=str(path))
    except OSError as exc:
        raise ValidationError(f"JSON_INVALID: {path}: {exc}") from exc


def parse_json(data: str | bytes, *, source: str = "JSON input") -> Any:
    """Decode UTF-8 JSON without accepting duplicate keys or nonfinite numbers."""
    try:
        text = data.decode("utf-8") if isinstance(data, bytes) else data
        value = json.loads(text, object_pairs_hook=_unique_object,
                           parse_constant=_invalid_constant, parse_float=_finite_float)
        pending = [value]
        while pending:
            item = pending.pop()
            if isinstance(item, str):
                require(not any(0xD800 <= ord(char) <= 0xDFFF for char in item),
                        "JSON_UNICODE", "unpaired surrogate in JSON string")
            elif isinstance(item, dict):
                pending.extend(item.keys())
                pending.extend(item.values())
            elif isinstance(item, list):
                pending.extend(item)
        return value
    except ValidationError:
        raise
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise ValidationError(f"JSON_INVALID: {source}: {exc}") from exc


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, "JSON_DUPLICATE", key)
        result[key] = value
    return result


def _invalid_constant(value: str) -> None:
    raise ValidationError("JSON_NONFINITE: " + value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    require(math.isfinite(parsed), "JSON_NONFINITE", value)
    return parsed


def safe_relative_path(value: Any, *, code: str = "PATH_INVALID") -> PurePosixPath:
    require(isinstance(value, str) and value != "", code, "path must be a nonempty string")
    require(not any(0xD800 <= ord(char) <= 0xDFFF for char in value), code, "unpaired surrogate in path")
    require("\\" not in value and not any(ord(c) < 32 for c in value), code, f"unsafe path {value!r}")
    require(not value.startswith("/") and not re.match(r"^[A-Za-z]:", value), code, f"absolute path {value!r}")
    parts = value.split("/")
    require(all(part not in {"", ".", ".."} for part in parts), code, f"traversal or empty component in {value!r}")
    return PurePosixPath(value)


def path_alias_key(value: str) -> tuple[str, ...]:
    """Conservative comparison key; never use it to grant access or rename a path."""
    return tuple(unicodedata.normalize("NFC", unicodedata.normalize("NFC", part).casefold())
                 for part in safe_relative_path(value).parts)


def reject_path_aliases(paths: list[str], *, code: str = "PATH_ALIAS") -> None:
    """Reject conflicting spellings of files or shared directory components."""
    prefixes: dict[tuple[str, ...], tuple[str, ...]] = {}
    for path in paths:
        exact, folded = safe_relative_path(path).parts, path_alias_key(path)
        for count in range(1, len(exact) + 1):
            key, spelling = folded[:count], exact[:count]
            require(key not in prefixes or prefixes[key] == spelling, code, f"ambiguous path spelling: {path!r}")
            prefixes[key] = spelling


def confined_file(root: Path, relative: str, *, code: str = "PATH_ESCAPE") -> Path:
    rel = safe_relative_path(relative)
    candidate = root.joinpath(*rel.parts)
    cursor = root
    for part in rel.parts:
        cursor = cursor / part
        require(not cursor.is_symlink(), code, f"symlink is not allowed: {relative}")
    resolved_root = root.resolve()
    resolved = candidate.resolve(strict=False)
    require(resolved == resolved_root or resolved_root in resolved.parents, code, f"path escaped root: {relative}")
    return candidate


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cli_error(exc: Exception, *, context: str, debug: bool = False) -> int:
    """Keep invalid inputs separate from bugs, without hiding a failing exit."""
    if isinstance(exc, ValidationError):
        print(f"{context}: {exc}", file=sys.stderr)
        return 2
    if isinstance(exc, OSError):
        print(f"{context}: IO_ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"{context}: INTERNAL_ERROR: {type(exc).__name__}; rerun with --debug", file=sys.stderr)
    if debug:
        traceback.print_exception(exc)
    return 3

