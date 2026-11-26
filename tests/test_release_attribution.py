from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.bundle_common import ValidationError
from tools.release_attribution import verify

UPSTREAM = "b" * 40


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class ReleaseAttributionTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.archive = self.root / "candidate.zip"
        self.lock = self.root / "release-lock.json"
        self.content = {
            "LICENSE": b"synthetic project license",
            "legal/spec-kit.txt": b"synthetic upstream notice",
            "preset.yml": b"synthetic original preset",
            "templates/input.md": b"synthetic adapted template",
        }
        self.component = {
            "id": "fixture-preset",
            "version": "1.0.0",
            "archive": {"path": self.archive.name},
            "files": [
                {
                    "path": name, "sha256": digest(data),
                    "source_ids": ["project"] if name in {"LICENSE", "preset.yml"} else ["upstream"],
                }
                for name, data in self.content.items()
            ],
            "attribution_sources": [
                self.source("project", "original", "fixture/project", "a" * 40, "Apache-2.0", "LICENSE"),
                self.source("upstream", "adapted", "github/spec-kit", UPSTREAM, "MIT", "legal/spec-kit.txt"),
                self.source("citation", "reference-only", "fixture/reference", "c" * 64, None, None),
            ],
        }
        self.release = {
            "schema_version": 1,
            "upstream": {"repository": "github/spec-kit", "commit": UPSTREAM},
            "components": [self.component],
        }

    def source(self, identity, relationship, locator, revision, spdx, path):
        return {
            "id": identity, "relationship": relationship, "locator": locator,
            "revision_or_sha256": revision, "spdx": spdx,
            "disposition": "approved" if path is not None else "reference-only",
            "required_legal_files": [] if path is None else [
                {"path": path, "sha256": digest(self.content[path])},
            ],
        }

    def candidate(self) -> str:
        with zipfile.ZipFile(self.archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for path, data in self.content.items():
                bundle.writestr(path, data)
        self.component["archive"]["sha256"] = digest(self.archive.read_bytes())
        raw = json.dumps(self.release).encode()
        self.lock.write_bytes(raw)
        return digest(raw)

    def verify(self, expected: str | None = None) -> tuple[str, ...]:
        actual = self.candidate()
        return verify(self.lock, self.root, lock_sha256=actual if expected is None else expected,
                      upstream_commit=UPSTREAM)

    def test_candidate_matches_independently_pinned_release_lock(self):
        self.assertEqual(self.verify(), ("fixture-preset@1.0.0",))
        with self.assertRaisesRegex(ValidationError, "RELEASE_LOCK_DIGEST"):
            self.verify("0" * 64)

    def test_rejects_stale_upstream_revision_in_lock_or_attribution(self):
        for record, key in (
            (self.release["upstream"], "commit"),
            (self.component["attribution_sources"][1], "revision_or_sha256"),
        ):
            with self.subTest(key=key):
                record[key] = "d" * 40
                with self.assertRaisesRegex(ValidationError, "RELEASE_UPSTREAM"):
                    self.verify()
                record[key] = UPSTREAM

    def test_rejects_unreviewed_and_incompatible_shipped_sources(self):
        for disposition in ("unresolved", "incompatible"):
            with self.subTest(disposition=disposition):
                self.component["attribution_sources"][1]["disposition"] = disposition
                with self.assertRaisesRegex(ValidationError, "RELEASE_RIGHTS"):
                    self.verify()

    def test_rejects_missing_or_stale_required_legal_file(self):
        legal = self.component["attribution_sources"][1]["required_legal_files"][0]
        for reviewed in ("no-such-notice", "legal/spec-kit.txt"):
            with self.subTest(file=reviewed):
                legal.update(path=reviewed, sha256="d" * 64)
                with self.assertRaisesRegex(ValidationError, "RELEASE_NOTICE"):
                    self.verify()

    def test_rejects_new_member_even_when_archive_digest_matches(self):
        self.content["unreviewed.md"] = b"synthetic added bytes"
        with self.assertRaisesRegex(ValidationError, "RELEASE_ARCHIVE_MEMBERS"):
            self.verify()

    def test_rejects_changed_member_digest_even_when_archive_digest_matches(self):
        self.content["LICENSE"] = b"different synthetic project license"
        with self.assertRaisesRegex(ValidationError, "RELEASE_MEMBER_DIGEST"):
            self.verify()

    def test_reference_only_citation_cannot_supply_payload(self):
        self.component["files"][0]["source_ids"] = ["citation"]
        with self.assertRaisesRegex(ValidationError, "RELEASE_ATTRIBUTION"):
            self.verify()


if __name__ == "__main__":
    unittest.main()
