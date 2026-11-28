"""Shared command-line options for archive read policy budgets."""
from __future__ import annotations

import argparse

from experiment_compiler.archive_policy import PackageReadPolicy

_FIELDS = ("max_member_bytes", "max_total_bytes", "max_members", "max_compression_ratio")

ARCHIVE_POLICY_OPTIONS: frozenset[str] = frozenset(name.replace("_", "-") for name in _FIELDS)

_HELP = {
    "max_member_bytes": "maximum expanded bytes of one archive member",
    "max_total_bytes": "maximum expanded bytes across all archive members",
    "max_members": "maximum number of archive members, including the manifest",
    "max_compression_ratio": "maximum expanded-to-compressed ratio of one member",
}


def _positive_int(text: str) -> int:
    try:
        value = int(text, 10)
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {text!r}") from None
    if value <= 0:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {text!r}")
    return value


def add_archive_policy_options(parser: argparse.ArgumentParser) -> None:
    group = parser.add_argument_group("archive read policy")
    for name in _FIELDS:
        group.add_argument(
            "--" + name.replace("_", "-"),
            dest=name,
            type=_positive_int,
            default=None,
            metavar="N",
            help=_HELP[name],
        )


def archive_policy_from_args(args: argparse.Namespace) -> PackageReadPolicy | None:
    budgets = {name: getattr(args, name, None) for name in _FIELDS}
    given = {name: value for name, value in budgets.items() if value is not None}
    if not given:
        return None
    return PackageReadPolicy(**given)
