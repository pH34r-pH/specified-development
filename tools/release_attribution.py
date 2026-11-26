"""Read-only verification of reviewed attribution in candidate component ZIPs."""
from __future__ import annotations

import argparse
import hashlib
import re
import stat
import zipfile
from pathlib import Path
from typing import Any

from .bundle_common import (
    ValidationError,
    cli_error,
    confined_file,
    parse_json,
    reject_path_aliases,
    require,
    safe_relative_path,
    sha256_file,
)

SHA256 = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
RELATIONSHIPS = {"original", "copied", "adapted", "generated", "dependency", "reference-only"}
LOCK_LIMIT = 8 * 1024 * 1024


def _digest(value: object, expression: re.Pattern[str], field: str) -> str:
    require(isinstance(value, str) and expression.fullmatch(value) is not None,
            "RELEASE_DIGEST", f"{field} requires an exact lowercase digest")
    assert isinstance(value, str)
    return value


def _index(rows: Any, key: str) -> dict[str, dict[str, Any]]:
    require(isinstance(rows, list), "RELEASE_INVENTORY", f"{key} inventory must be a list")
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        require(isinstance(row, dict) and isinstance(row.get(key), str) and bool(row[key]),
                "RELEASE_INVENTORY", f"entry needs {key}")
        identity = row[key].casefold()
        require(identity not in result, "RELEASE_DUPLICATE", f"duplicate {key}")
        result[identity] = row
    return result


def _inventory(component: dict[str, Any], upstream_commit: str) -> dict[str, str]:
    files = _index(component.get("files"), "path")
    sources = _index(component.get("attribution_sources"), "id")
    require(files and sources, "RELEASE_INVENTORY", "files and reviewed attribution are required")
    contents: dict[str, str] = {}
    used: set[str] = set()
    for item in files.values():
        path = safe_relative_path(item["path"]).as_posix()
        contents[path] = _digest(item.get("sha256"), SHA256, "member SHA-256")
        ids = item.get("source_ids")
        if not isinstance(ids, list) or not ids or not all(isinstance(value, str) for value in ids):
            raise ValidationError("RELEASE_ATTRIBUTION: each member needs source attribution")
        for source_id in ids:
            source = sources.get(source_id.casefold())
            require(source is not None and source["id"] == source_id
                    and source.get("relationship") != "reference-only",
                    "RELEASE_ATTRIBUTION", "archive member requires a shipped source")
            used.add(source_id.casefold())
    reject_path_aliases(list(contents), code="RELEASE_ARCHIVE_MEMBERS")

    for folded_id, source in sources.items():
        relationship = source.get("relationship")
        require(isinstance(relationship, str) and relationship in RELATIONSHIPS,
                "RELEASE_ATTRIBUTION", "source relationship is unsupported")
        require(isinstance(source.get("locator"), str) and source["locator"].strip(),
                "RELEASE_ATTRIBUTION", "source locator is required")
        identity = source.get("revision_or_sha256")
        require(isinstance(identity, str) and (COMMIT.fullmatch(identity) or SHA256.fullmatch(identity)),
                "RELEASE_ATTRIBUTION", "source revision or dependency digest is required")
        if source["locator"] == "github/spec-kit":
            require(identity == upstream_commit, "RELEASE_UPSTREAM", "stale Spec Kit attribution source")
        legal_files = _index(source.get("required_legal_files"), "path")
        if relationship == "reference-only":
            require(folded_id not in used and not legal_files,
                    "RELEASE_ATTRIBUTION", "references cannot supply shipped bytes")
            continue
        license_id = source.get("spdx")
        require(isinstance(license_id, str) and license_id.strip() and source.get("disposition") == "approved",
                "RELEASE_RIGHTS", "unresolved or incompatible shipped-source disposition")
        require(folded_id in used and legal_files, "RELEASE_ATTRIBUTION",
                "shipped source needs attributed members and reviewed legal files")
        for member in legal_files.values():
            path = safe_relative_path(member["path"]).as_posix()
            digest = _digest(member.get("sha256"), SHA256, "legal file SHA-256")
            require(contents.get(path) == digest, "RELEASE_NOTICE", f"required legal file missing or stale: {path}")
    return contents


def _verify_zip(archive: Path, expected: dict[str, str]) -> None:
    try:
        with zipfile.ZipFile(archive) as package:
            observed: dict[str, zipfile.ZipInfo] = {}
            seen: set[str] = set()
            for member in package.infolist():
                path = safe_relative_path(member.orig_filename.removesuffix("/") if member.is_dir()
                                          else member.orig_filename).as_posix()
                file_type = stat.S_IFDIR if member.is_dir() else stat.S_IFREG
                require(stat.S_IFMT(member.external_attr >> 16) in (0, file_type),
                        "RELEASE_ARCHIVE_MEMBER", f"member type differs from its path: {path}")
                require(path not in seen, "RELEASE_DUPLICATE", f"duplicate archive member: {path}")
                seen.add(path)
                if member.is_dir():
                    require(any(file.startswith(path + "/") for file in expected),
                            "RELEASE_ARCHIVE_MEMBERS", f"unreviewed directory: {path}")
                else:
                    observed[path] = member
            reject_path_aliases(list(seen), code="RELEASE_ARCHIVE_MEMBERS")
            require(observed.keys() == expected.keys(), "RELEASE_ARCHIVE_MEMBERS",
                    "candidate membership differs from the reviewed lock")
            for path, digest in expected.items():
                with package.open(observed[path]) as stream:
                    actual = hashlib.sha256()
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        actual.update(chunk)
                require(actual.hexdigest() == digest, "RELEASE_MEMBER_DIGEST", f"reviewed member changed: {path}")
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError, OSError) as exc:
        raise ValidationError("RELEASE_ARCHIVE: cannot read candidate ZIP") from exc


def verify(lock: Path, archive_root: Path, *, lock_sha256: str, upstream_commit: str) -> tuple[str, ...]:
    expected = _digest(lock_sha256, SHA256, "reviewed lock SHA-256")
    commit = _digest(upstream_commit, COMMIT, "pinned upstream commit")
    with lock.open("rb") as stream:
        raw = stream.read(LOCK_LIMIT + 1)
    require(len(raw) <= LOCK_LIMIT and hashlib.sha256(raw).hexdigest() == expected,
            "RELEASE_LOCK_DIGEST", "candidate lock must match the reviewed bytes")
    release = parse_json(raw, source="candidate release lock")
    require(isinstance(release, dict) and type(release.get("schema_version")) is int
            and release["schema_version"] == 1, "RELEASE_LOCK", "expected release lock version 1")
    upstream = release.get("upstream")
    require(isinstance(upstream, dict) and upstream.get("repository") == "github/spec-kit"
            and upstream.get("commit") == commit, "RELEASE_UPSTREAM", "stale or missing reviewed upstream source")
    components = _index(release.get("components"), "id")
    require(components, "RELEASE_LOCK", "candidate component inventory is empty")
    verified: list[str] = []
    for item in components.values():
        require(isinstance(item.get("version"), str) and item["version"].strip(),
                "RELEASE_LOCK", "component version is required")
        archive = item.get("archive")
        if not isinstance(archive, dict):
            raise ValidationError("RELEASE_LOCK: component archive is required")
        expected_files = _inventory(item, commit)
        path = confined_file(archive_root, safe_relative_path(archive.get("path")).as_posix())
        archive_digest = _digest(archive.get("sha256"), SHA256, "archive SHA-256")
        require(path.is_file() and sha256_file(path) == archive_digest,
                "RELEASE_ARCHIVE_DIGEST", "candidate archive is missing or differs from reviewed bytes")
        _verify_zip(path, expected_files)
        verified.append(f"{item['id']}@{item['version']}")
    return tuple(verified)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lock", type=Path)
    parser.add_argument("--archive-root", type=Path, required=True)
    parser.add_argument("--lock-sha256", required=True)
    parser.add_argument("--upstream-commit", required=True)
    args = parser.parse_args()
    try:
        for component in verify(args.lock, args.archive_root, lock_sha256=args.lock_sha256,
                                upstream_commit=args.upstream_commit):
            print(f"Verified candidate attribution for {component}")
    except (OSError, ValidationError) as exc:
        return cli_error(exc, context="Release attribution")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
