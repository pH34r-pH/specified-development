"""Independent malformed-package checks; not fresh-agent behavioral trials."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_foundation import ValidationError, allowed_public_path
from tools.validate_skills import validate_package

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "deabstract-stablecode"


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name) / "deabstract-stablecode"
        shutil.copytree(SOURCE, self.root)

    def change(self, relative, old, new):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def rejects(self, code):
        with self.assertRaisesRegex(ValidationError, "^" + code + ":"):
            validate_package(self.root)

    def test_complete_copy_without_repository_or_upstream_passes(self):
        # The copied folder has neither a .git directory nor sibling skills.
        self.assertEqual(validate_package(self.root), 11)

    def test_missing_entry_is_rejected(self):
        (self.root / "SKILL.md").unlink()
        self.rejects("SKILL_FILES")

    def test_missing_reference_is_rejected(self):
        (self.root / "references/audit-tests.md").unlink()
        self.rejects("SKILL_FILES")

    def test_missing_license_is_rejected(self):
        (self.root / "LICENSE.dzhng-skills").unlink()
        self.rejects("SKILL_FILES")

    def test_unregistered_file_is_rejected(self):
        (self.root / "extra.md").write_text("unexpected\n")
        self.rejects("SKILL_FILES")

    def test_symlink_resource_is_rejected(self):
        target = self.root / "references/audit-tests.md"
        target.unlink()
        target.symlink_to(self.root / "README.md")
        self.rejects("SKILL_SYMLINK")

    def test_symlink_package_root_is_rejected(self):
        alias = Path(self.workspace.name) / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValidationError, "^SKILL_SYMLINK:"):
            validate_package(alias)

    def test_parent_escape_is_rejected_even_when_target_exists(self):
        (self.root.parent / "outside.md").write_text("# Exists\n")
        self.change("SKILL.md", "[usage guide](README.md)", "[usage guide](../outside.md)")
        self.rejects("LINK_ESCAPE")

    def test_dangling_local_link_is_rejected(self):
        self.change("SKILL.md", "[usage guide](README.md)", "[usage guide](absent.md)")
        self.rejects("LINK_MISSING")

    def test_missing_anchor_is_rejected(self):
        self.change("SKILL.md", "[usage guide](README.md)", "[usage guide](README.md#absent)")
        self.rejects("LINK_FRAGMENT_MISSING")

    def test_invalid_frontmatter_is_rejected(self):
        self.change("SKILL.md", "---\nname:", "name:")
        self.rejects("SKILL_FRONTMATTER")

    def test_duplicate_frontmatter_is_rejected(self):
        self.change("SKILL.md", "name: deabstract-stablecode", "name: deabstract-stablecode\nname: duplicate")
        self.rejects("SKILL_FRONTMATTER")

    def test_name_mismatch_is_rejected(self):
        self.change("SKILL.md", "name: deabstract-stablecode", "name: unrelated")
        self.rejects("SKILL_NAME")

    def test_empty_description_is_rejected(self):
        path = self.root / "SKILL.md"
        lines = path.read_text().splitlines()
        path.write_text("\n".join("description: " if line.startswith("description:") else line for line in lines) + "\n")
        self.rejects("SKILL_DESCRIPTION")

    def test_altered_license_bytes_are_rejected(self):
        self.change("LICENSE.dzhng-skills", "2026 David Zhang", "2025 Someone Else")
        self.rejects("SKILL_LICENSE")

    def test_moving_upstream_reference_is_rejected(self):
        self.change("NOTICE.md", "/blob/d51322866ffa298838346960414d18a221b52588/", "/blob/main/")
        self.rejects("SKILL_PROVENANCE")

    def test_external_procedure_dependency_is_rejected(self):
        self.change("SKILL.md", "[usage guide](README.md)", "[usage guide](https://example.org/required-skill)")
        self.rejects("SKILL_EXTERNAL_PROCEDURE")

    def test_non_utf8_file_is_rejected(self):
        (self.root / "README.md").write_bytes(b"\xff\n")
        self.rejects("SKILL_ENCODING")

    def test_cli_rejects_malformed_copy(self):
        (self.root / "README.md").unlink()
        result = subprocess.run([sys.executable, str(ROOT / "tools/validate_skills.py"), str(self.root)], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("SKILL_FILES:", result.stderr)
        self.assertNotIn("checks passed", result.stdout)

    def test_cli_accepts_portable_copy(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/validate_skills.py"), str(self.root)], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("behavioral qualification not claimed", result.stdout)

    def test_public_scope_accepts_only_explicit_new_paths(self):
        self.assertTrue(allowed_public_path("skills/deabstract-stablecode/SKILL.md"))
        self.assertTrue(allowed_public_path("tools/validate_skills.py"))
        for path in ("skills/unreviewed/SKILL.md", "skills/deabstract-stablecode/.env", "skills/deabstract-stablecode/extra.py", "skills/deabstract-stablecode/secrets/key.md", "skills/../README.md"):
            with self.subTest(path=path):
                self.assertFalse(allowed_public_path(path))


if __name__ == "__main__":
    unittest.main()
