"""Opt-in clean-wheel check: SPECIFIED_TEST_WHEEL=/absolute/package.whl."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import unittest
import venv
import zipfile
from pathlib import Path

from tools import bundle_validation as validator

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.environ.get("SPECIFIED_TEST_WHEEL"), "set SPECIFIED_TEST_WHEEL for the clean installed-package gate")
class InstalledPackageTests(unittest.TestCase):
    def test_wheel_carries_exact_project_license(self):
        wheel = Path(os.environ["SPECIFIED_TEST_WHEEL"]).resolve(strict=True)
        with zipfile.ZipFile(wheel) as archive:
            license_paths = [
                name for name in archive.namelist() if name.endswith(".dist-info/licenses/LICENSE")
            ]
            self.assertEqual(len(license_paths), 1)
            self.assertEqual(archive.read(license_paths[0]), (ROOT / "LICENSE").read_bytes())

    def test_wheel_module_and_portable_copy_have_same_round_trip(self):
        wheel = Path(os.environ["SPECIFIED_TEST_WHEEL"]).resolve(strict=True)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            env_root = root / "environment"
            venv.EnvBuilder(with_pip=True).create(env_root)
            binary = env_root / ("Scripts" if os.name == "nt" else "bin")
            python = binary / ("python.exe" if os.name == "nt" else "python")
            environment = os.environ.copy()
            environment.pop("PYTHONPATH", None)

            def run(command):
                result = subprocess.run(command, cwd=root, env=environment, capture_output=True,
                                        text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout

            run([str(python), "-m", "pip", "install", "--no-index", "--no-deps", str(wheel)])
            fixture = ROOT / "tests/fixtures/bundle-v2"
            if not fixture.exists():
                fixture = ROOT / "tests/fixtures/bundle"
            inputs = root / "inputs"
            shutil.copytree(fixture, inputs)
            bundle = json.loads((inputs / "bundle.json").read_text())
            pin = (validator.reviewed_fingerprint(bundle) if bundle["schema_version"] == 2
                   else validator.authority_fingerprint(bundle["authority"]))
            copied = root / "portable"
            copied.mkdir()
            for name in ("bundle_common.py", "bundle_validation.py", "bundle_review.py"):
                shutil.copy2(ROOT / "tools" / name, copied / name)

            extension = ".exe" if os.name == "nt" else ""
            invocations = [
                ([str(binary / ("specified-validate-bundle" + extension))],
                 [str(binary / ("specified-bundle-review" + extension))]),
                ([str(python), "-m", "tools.bundle_validation"], [str(python), "-m", "tools.bundle_review"]),
                ([str(python), "-S", str(copied / "bundle_validation.py")],
                 [str(python), "-S", str(copied / "bundle_review.py")]),
            ]
            outputs = []
            for index, (validate, review) in enumerate(invocations):
                arguments = ["bundle.json", "--root", str(inputs), "--authority-sha256", pin]
                result = json.loads(run(validate + arguments))
                self.assertTrue(result["valid"])
                self.assertEqual(result["target_acceptance"], "not-granted")
                output = root / f"review-{index}"
                run(review + ["render", *arguments, "--output", str(output)])
                run(review + ["render", *arguments, "--output", str(output), "--check"])
                details = list((output / "objects").glob("*.json"))
                self.assertEqual(len(details), 1)
                detail = details[0]
                expanded = root / f"expanded-{index}"
                run(review + ["expand", str(detail), "--sha256", hashlib.sha256(detail.read_bytes()).hexdigest(),
                              "--output", str(expanded)])
                run(validate + ["bundle.json", "--root", str(expanded), "--authority-sha256", pin])
                self.assertEqual((expanded / "bundle.json").read_bytes(), (inputs / "bundle.json").read_bytes())
                outputs.append({str(p.relative_to(output)): p.read_bytes() for p in output.rglob("*") if p.is_file()})
            self.assertEqual(outputs[0], outputs[1])
            self.assertEqual(outputs[0], outputs[2])
            run([str(binary / ("specified-validate-foundation" + extension)), "--help"])
            run([str(binary / ("specified-task-review" + extension)), "--help"])
            run([str(binary / ("specified-onboarding" + extension)), "--help"])
            run([str(python), "-m", "tools.release_attribution", "--help"])


if __name__ == "__main__":
    unittest.main()
