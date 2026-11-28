"""Shared command-line options for archive read policy budgets."""
from __future__ import annotations

import argparse

from experiment_compiler.archive_policy import PackageReadPolicy

_OPTIONS = (
    ("--max-member-bytes", "max_member_bytes", "maximum expanded bytes of one archive member"),
    ("--max-total-bytes", "max_total_bytes", "maximum expanded bytes across all archive members"),
    ("--max-members", "max_members", "maximum number of archive members, including the manifest"),
    ("--max-compression-ratio", "max_compression_ratio", "maximum expanded-to-compressed ratio of one member"),
)


def _positive_integer(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {text!r}") from None
    if value <= 0:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {text!r}")
    return value


def add_archive_policy_options(parser: argparse.ArgumentParser) -> None:
    for flag, dest, help_text in _OPTIONS:
        parser.add_argument(flag, dest=dest, type=_positive_integer, default=None, metavar="N", help=help_text)


def archive_policy_from_args(args: argparse.Namespace) -> PackageReadPolicy | None:
    budgets = {dest: getattr(args, dest, None) for _, dest, _ in _OPTIONS}
    given = {name: value for name, value in budgets.items() if value is not None}
    if not given:
        return None
    return PackageReadPolicy(**given)
