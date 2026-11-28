"""Check a consumer repository's Specified Development layout.

The check is deterministic and offline. It validates the canonical spec tree,
schema version 1 frontmatter, feature requirement tables, each feature's plan
implementation-targets section and its independent test contract references.
Untested requirements are reported as gaps, not errors.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING or __package__:
    from .bundle_common import ValidationError, confined_file, read_json, require
    from .spec_validation import (
        MANIFEST_PATH,
        feature_requirements,
        frontmatter,
        sections,
        tables,
        validate_metadata,
    )
    from .validate_foundation import validate_spec
else:
    from bundle_common import ValidationError, confined_file, read_json, require
    from spec_validation import (
        MANIFEST_PATH,
        feature_requirements,
        frontmatter,
        sections,
        tables,
        validate_metadata,
    )
    from validate_foundation import validate_spec

TARGETS_HEADING = "Implementation targets and direct path"
INTERFACE_HEADING = "Public interface"
CASE_TABLE_HEADERS = ("Case", "Requirements")
REQUIREMENT_TOKEN = re.compile(r"(?:[A-Z]+-)?(?:FR|SC)-\d{3}")


def _plan(root: Path, feature: str) -> None:
    relative = f"build/{feature}/plan.md"
    path = confined_file(root, relative)
    require(path.is_file(), "LAYOUT_PLAN_MISSING", relative)
    text = path.read_text(encoding="utf-8")
    body = frontmatter(text)[1] if text.startswith("---") else text
    headings = sections(body)
    require(TARGETS_HEADING in headings, "LAYOUT_PLAN_TARGETS",
            f"{relative} needs a '{TARGETS_HEADING}' section")
    require(INTERFACE_HEADING in headings, "LAYOUT_PLAN_INTERFACE",
            f"{relative} needs a '{INTERFACE_HEADING}' section listing what code outside the area relies on")


def _not_ignored(root: Path, relatives: list[str]) -> None:
    """Feature records must be tracked; a broad `build/` ignore rule silently drops them."""
    if not (root / ".git").exists():
        return
    result = subprocess.run(["git", "-C", str(root), "check-ignore", "--no-index", "--", *relatives],
                            capture_output=True, text=True, check=False)
    ignored = sorted(line.strip() for line in result.stdout.splitlines() if line.strip())
    require(not ignored, "LAYOUT_RECORDS_IGNORED",
            f"feature records are ignored by version control: {ignored}; replace a 'build/' rule with '/build/*' "
            "and '!/build/<feature>/'")


def _test_contract(root: Path, feature: str, requirements: set[str]) -> dict[str, set[str]]:
    relative = f"build/{feature}/tests.md"
    path = confined_file(root, relative)
    require(path.is_file(), "LAYOUT_TESTS_MISSING", relative)
    text = path.read_text(encoding="utf-8")
    body = frontmatter(text)[1] if text.startswith("---") else text
    contracts = [table for table in tables(body) if tuple(table.headers[:2]) == CASE_TABLE_HEADERS]
    require(len(contracts) == 1, "LAYOUT_TESTS_TABLE", f"{relative} needs one table starting with | Case | Requirements |")
    cases: dict[str, set[str]] = {}
    for row in contracts[0].rows:
        name = row[0].strip()
        require(bool(name) and name not in cases, "LAYOUT_TESTS_TABLE", f"{relative}: empty or duplicate case {name!r}")
        traced = set(REQUIREMENT_TOKEN.findall(row[1]))
        require(bool(traced), "LAYOUT_TEST_ORPHAN", f"{relative}: case {name} traces no requirement")
        unknown = sorted(traced - requirements)
        require(not unknown, "LAYOUT_TEST_REFERENCE", f"{relative}: case {name} traces unknown requirements {unknown}")
        cases[name] = traced
    return cases


def check_layout(root: Path) -> dict[str, Any]:
    validate_spec(root)
    manifest = read_json(confined_file(root, MANIFEST_PATH))
    for identifier, record in manifest["documents"].items():
        text = confined_file(root, "spec/" + record["path"]).read_text(encoding="utf-8")
        metadata, _ = frontmatter(text)
        require(metadata.get("schema_version") == 1, "LAYOUT_FRONTMATTER",
                f"{record['path']} needs schema version 1 frontmatter")
        validate_metadata(root, metadata, identifier, record["role"])
    features: dict[str, Any] = {}
    for feature, record in sorted(manifest["features"].items()):
        root_doc = manifest["documents"][record["root"]]
        _, body = frontmatter(confined_file(root, "spec/" + root_doc["path"]).read_text(encoding="utf-8"))
        requirements, scenarios = feature_requirements(body)
        _plan(root, feature)
        _not_ignored(root, [f"build/{feature}/plan.md", f"build/{feature}/tests.md"])
        cases = _test_contract(root, feature, requirements)
        covered = set().union(*cases.values()) if cases else set()
        features[feature] = {"requirements": len(requirements), "scenarios": len(scenarios), "cases": len(cases),
                             "untested": sorted(f"{feature}#{item}" for item in requirements - covered)}
    return {"documents": len(manifest["documents"]), "features": features}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="consumer repository root")
    args = parser.parse_args()
    try:
        print(json.dumps(check_layout(args.root), indent=2, sort_keys=True))
        return 0
    except (ValidationError, OSError) as exc:
        print(f"LAYOUT invalid: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
