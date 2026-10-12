#!/usr/bin/env python3
"""Offline structural validation for this repository's portable skill package.

This validates the package's small single-line frontmatter subset, not arbitrary
YAML, every Markdown extension, or the behavior of an agent using the skill.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.validate_foundation import (
    ValidationError, git_blob_sha, require, validate_markdown_links,
)

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "SKILL.md", "README.md", "NOTICE.md", "LICENSE", "LICENSE.dzhng-skills",
    "references/explore-unknowns.md", "references/plan-targets.md",
    "references/refactor-clean.md", "references/audit-tests.md",
    "references/qualify-change.md", "references/review-decisions.md",
}
# Independently inspected source license blobs, not generated from the candidate.
LICENSE_BLOBS = {
    "LICENSE": "d645695673349e3947e8e5ae42332d0ac3164cd7",
    "LICENSE.dzhng-skills": "c92e086f821a15b25a063f684faf3e75b3f67f56",
}
UPSTREAM_PIN = "d51322866ffa298838346960414d18a221b52588"


def validate_package(root: Path) -> int:
    root = Path(root)
    require(not root.is_symlink(), "SKILL_SYMLINK", "package root must not be a symlink")
    require(root.is_dir(), "SKILL_ROOT", "package directory is missing")
    actual = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        require(not path.is_symlink(), "SKILL_SYMLINK", relative)
        require(path.is_file() or path.is_dir(), "SKILL_ENTRY", relative)
        if path.is_file():
            actual.add(relative)
    require(actual == FILES, "SKILL_FILES", f"missing={sorted(FILES-actual)}; unexpected={sorted(actual-FILES)}")
    texts = {}
    for relative in sorted(actual):
        data = (root / relative).read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValidationError(f"SKILL_ENCODING: {relative} is not UTF-8") from None
        require(text.endswith("\n") and "\r" not in text and "\x00" not in text, "SKILL_TEXT", relative)
        texts[relative] = text
        if relative in LICENSE_BLOBS:
            require(git_blob_sha(data) == LICENSE_BLOBS[relative], "SKILL_LICENSE", relative)

    entry = texts["SKILL.md"]
    sections = entry.split("---\n", 2)
    require(len(sections) == 3 and sections[0] == "", "SKILL_FRONTMATTER", "expected opening and closing frontmatter")
    fields = {}
    for line in sections[1].splitlines():
        key, separator, value = line.partition(":")
        require(bool(separator) and key in {"name", "description", "license"} and key not in fields, "SKILL_FRONTMATTER", "only unique single-line name, description and license fields are supported")
        fields[key] = value.strip()
    require(set(fields) == {"name", "description", "license"}, "SKILL_FRONTMATTER", "required fields are missing")
    require(fields["name"] == root.name == "deabstract-stablecode", "SKILL_NAME", "name must match the package directory")
    require(1 <= len(fields["description"]) <= 1024, "SKILL_DESCRIPTION", "description must contain 1-1024 characters")
    require(fields["license"] == "Apache-2.0 AND MIT", "SKILL_LICENSE", "license declaration changed")
    # No upstream URL is needed by an executable procedure. Provenance is separate.
    for relative, text in texts.items():
        if relative == "SKILL.md" or relative.startswith("references/"):
            require(re.search(r"https?://", text) is None, "SKILL_EXTERNAL_PROCEDURE", relative)
    notice = texts["NOTICE.md"]
    refs = re.findall(r"https://github\.com/dzhng/skills/blob/([^/]+)/", notice)
    require(len(refs) == 6 and set(refs) == {UPSTREAM_PIN} and f"`{UPSTREAM_PIN}`" in notice, "SKILL_PROVENANCE", "six inspected sources must use the documented full pin")
    markdown = {relative: relative for relative in actual if relative.endswith(".md")}
    validate_markdown_links(root, markdown)
    return len(actual)


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("usage: validate_skills.py [path/to/deabstract-stablecode]", file=sys.stderr)
        return 2
    root = Path(args[0]) if args else ROOT / "skills" / "deabstract-stablecode"
    try:
        count = validate_package(root)
    except (ValidationError, OSError) as exc:
        print(f"SKILLS validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"SKILLS package checks passed ({count} files); agent behavioral qualification not claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
