"""Shared confined reads and exact-byte identities; no repository-specific policy."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


class ValidationError(ValueError):
    """A stable, user-facing validation failure."""


def require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise ValidationError(f"{code}: {message}")


def read_json(path: Path) -> Any:
    try:
        require(path.stat().st_size <= 8 * 1024 * 1024, "JSON_TOO_LARGE", "maximum JSON input is 8 MiB")
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=_invalid_constant)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"JSON_INVALID: {path}: {exc}") from exc


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, "JSON_DUPLICATE", key)
        result[key] = value
    return result


def _invalid_constant(value: str) -> None:
    raise ValidationError("JSON_NONFINITE: " + value)


def safe_relative_path(value: Any, *, code: str = "PATH_INVALID") -> PurePosixPath:
    require(isinstance(value, str) and value != "", code, "path must be a nonempty string")
    require("\\" not in value and not any(ord(c) < 32 for c in value), code, f"unsafe path {value!r}")
    require(not value.startswith("/") and not re.match(r"^[A-Za-z]:", value), code, f"absolute path {value!r}")
    parts = value.split("/")
    require(all(part not in {"", ".", ".."} for part in parts), code, f"traversal or empty component in {value!r}")
    return PurePosixPath(value)


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

