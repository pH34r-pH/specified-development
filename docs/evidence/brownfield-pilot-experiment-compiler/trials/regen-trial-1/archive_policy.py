"""Archive read policy: caller-owned budgets for reading Compiled Experiment ZIP archives."""
from __future__ import annotations

import hashlib
import zipfile
from dataclasses import dataclass, fields

_CHUNK_SIZE = 1024 * 1024


class PackageError(Exception):
    """A package could not be read or is malformed."""


class ResourcePolicyError(PackageError):
    """Local resource policy refused a package."""

    def __init__(self, budget: str, limit: int, member: str | None = None) -> None:
        self.budget = budget
        self.limit = limit
        self.member = member
        where = f" member {member!r}" if member is not None else ""
        super().__init__(f"Local resource policy refused package{where}: {budget} exceeds {limit}")


@dataclass(frozen=True)
class PackageReadPolicy:
    max_member_bytes: int | None = None
    max_total_bytes: int | None = None
    max_members: int | None = None
    max_compression_ratio: int | None = None

    def __post_init__(self) -> None:
        for field in fields(self):
            value = getattr(self, field.name)
            if value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{field.name} must be a positive integer, got {value!r}")


def _check_member(policy: PackageReadPolicy, name: str, expanded: int, compressed: int) -> None:
    if policy.max_member_bytes is not None and expanded > policy.max_member_bytes:
        raise ResourcePolicyError("max_member_bytes", policy.max_member_bytes, name)
    ratio = policy.max_compression_ratio
    if ratio is not None and expanded > compressed * ratio:
        raise ResourcePolicyError("max_compression_ratio", ratio, name)


def _check_total(policy: PackageReadPolicy, total: int) -> None:
    if policy.max_total_bytes is not None and total > policy.max_total_bytes:
        raise ResourcePolicyError("max_total_bytes", policy.max_total_bytes)


class ArchiveMemberReader:
    """Single-pass member hashing with optional capture, under an optional policy."""

    def __init__(self, archive: zipfile.ZipFile, policy: PackageReadPolicy | None = None) -> None:
        self._archive = archive
        self._policy = policy
        self._observed_total = 0
        if policy is not None:
            self._check_inventory()

    def _check_inventory(self) -> None:
        policy = self._policy
        assert policy is not None
        infos = self._archive.infolist()
        if policy.max_members is not None and len(infos) > policy.max_members:
            raise ResourcePolicyError("max_members", policy.max_members)
        declared_total = 0
        for info in infos:
            _check_member(policy, info.filename, info.file_size, info.compress_size)
            declared_total += info.file_size
            _check_total(policy, declared_total)

    def read(self, info: zipfile.ZipInfo, capture: bool = False) -> tuple[str, int, bytes]:
        """Return (sha256 hex digest, expanded size, bytes if captured else b"")."""
        policy = self._policy
        digest = hashlib.sha256()
        captured = bytearray()
        size = 0
        try:
            with self._archive.open(info) as stream:
                while True:
                    chunk = stream.read(_CHUNK_SIZE)
                    if not chunk:
                        break
                    size += len(chunk)
                    self._observed_total += len(chunk)
                    if policy is not None:
                        _check_member(policy, info.filename, size, info.compress_size)
                        _check_total(policy, self._observed_total)
                    if size > info.file_size:
                        raise PackageError(
                            f"Package member {info.filename!r} expands beyond its declared size {info.file_size}"
                        )
                    digest.update(chunk)
                    if capture:
                        captured.extend(chunk)
        except PackageError:
            raise
        except (zipfile.BadZipFile, zipfile.LargeZipFile, EOFError, OSError) as error:
            raise PackageError(f"Package member {info.filename!r} could not be read: {error}") from error
        if size != info.file_size:
            raise PackageError(
                f"Package member {info.filename!r} expanded to {size} bytes but declares {info.file_size}"
            )
        return digest.hexdigest(), size, bytes(captured) if capture else b""
