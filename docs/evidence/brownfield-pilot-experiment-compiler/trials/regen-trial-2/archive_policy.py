"""Archive read policy: caller-owned operational budgets for reading ZIP archives."""
from __future__ import annotations

import hashlib
import math
import zipfile
from dataclasses import dataclass, fields

_CHUNK_SIZE = 1024 * 1024


class PackageError(ValueError):
    """Malformed, unsafe or mismatched package input."""


class ResourcePolicyError(PackageError):
    """A local resource policy refused the package (not a validity judgement)."""

    def __init__(
        self,
        budget: str,
        limit: int,
        *,
        member: str | None = None,
        observed: int | None = None,
    ) -> None:
        self.budget = budget
        self.limit = limit
        self.member = member
        self.observed = observed
        message = "Local resource policy refused package"
        if member is not None:
            message += f" for member {member!r}"
        message += f": {budget} exceeds {limit}"
        if observed is not None:
            message += f" (observed {observed})"
        super().__init__(message)


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


def _ratio_exceeded(expanded: int, compressed: int, budget: int) -> bool:
    return expanded > compressed * budget


def _observed_ratio(expanded: int, compressed: int) -> int:
    # Integer report of the ratio that exceeded the budget: ceil(expanded / compressed).
    # A zero compressed size makes the ratio unbounded; report the expanded size then.
    if compressed <= 0:
        return expanded
    return math.ceil(expanded / compressed)


class ArchiveMemberReader:
    """Single-pass member hashing with optional capture under a read policy."""

    def __init__(self, archive: zipfile.ZipFile, policy: PackageReadPolicy | None) -> None:
        self.archive = archive
        self.policy = policy
        self.total_bytes = 0
        self._check_inventory()

    def _check_inventory(self) -> None:
        policy = self.policy
        if policy is None:
            return
        infos = self.archive.infolist()
        if policy.max_members is not None and len(infos) > policy.max_members:
            raise ResourcePolicyError("max_members", policy.max_members, observed=len(infos))
        declared_total = 0
        for info in infos:
            declared_total += info.file_size
            self._check_member(info.filename, info.file_size, declared_total, info.compress_size)

    def _check_member(self, name: str, member_bytes: int, total: int, compressed: int) -> None:
        policy = self.policy
        if policy is None:
            return
        if policy.max_member_bytes is not None and member_bytes > policy.max_member_bytes:
            raise ResourcePolicyError(
                "max_member_bytes", policy.max_member_bytes, member=name, observed=member_bytes
            )
        if policy.max_total_bytes is not None and total > policy.max_total_bytes:
            raise ResourcePolicyError(
                "max_total_bytes", policy.max_total_bytes, member=name, observed=total
            )
        if policy.max_compression_ratio is not None and _ratio_exceeded(
            member_bytes, compressed, policy.max_compression_ratio
        ):
            raise ResourcePolicyError(
                "max_compression_ratio",
                policy.max_compression_ratio,
                member=name,
                observed=_observed_ratio(member_bytes, compressed),
            )

    def read(self, info: zipfile.ZipInfo, *, capture: bool = False) -> tuple[str, int, bytearray]:
        digest = hashlib.sha256()
        captured = bytearray()
        size = 0
        name = info.filename
        try:
            with self.archive.open(info) as stream:
                while True:
                    chunk = stream.read(_CHUNK_SIZE)
                    if not chunk:
                        break
                    size += len(chunk)
                    self.total_bytes += len(chunk)
                    self._check_member(name, size, self.total_bytes, info.compress_size)
                    digest.update(chunk)
                    if capture:
                        captured.extend(chunk)
        except ResourcePolicyError:
            raise
        except (zipfile.BadZipFile, EOFError, OSError, RuntimeError, NotImplementedError) as error:
            raise PackageError(f"Package member {name!r} could not be read: {error}") from error
        if size != info.file_size:
            raise PackageError(
                f"Package member {name!r} expanded to {size} bytes but declares {info.file_size}"
            )
        return digest.hexdigest(), size, captured
