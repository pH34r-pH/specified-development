# Validation and quality checks

The portable bundle tools have no third-party runtime dependencies. Canonical
specification authoring uses the optional `authoring` dependencies in
`pyproject.toml`. CI installs the exact authoring, packaging and quality-tool
versions and transitive hashes in `requirements-dev.txt`.

## Local commands

Use CPython 3.12 in an isolated environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install --require-hashes -r requirements-dev.txt
python tools/validate_foundation.py
python -m tools.spec_validation
python -m tools.task_review --check
python -m unittest discover -s tests -v
ruff check --no-cache tools tests
mypy --cache-dir /tmp/specified-development-mypy tools
zizmor --offline .github/workflows .github/dependabot.yml
pip-audit --requirement requirements-dev.txt --no-deps --disable-pip --strict
```

Ruff checks maintained tools and tests. Frozen fixture code and generated review
objects are data, excluded from mechanical style changes. Mypy checks all
maintained tools; shape validation remains necessary for untrusted JSON/YAML.
The tests separately demonstrate typed malformed-input errors and internal-fault
diagnostics, so a passing type check is not treated as input validation.

CI also builds a wheel from a temporary archive of its exact Git revision, then
installs it into a clean environment without resolving dependencies. Its required
packaging gate compares the installed commands, module invocation and portable
three-file copy through validation, rendering, exact regeneration, expansion and
revalidation. To run this gate locally after building a wheel outside the checkout:

```sh
SPECIFIED_TEST_WHEEL=/absolute/path/to/package.whl python -m unittest discover -s tests -p test_packaging.py -v
```

Zizmor audits local workflow definitions without a GitHub token. Offline audits
cannot establish current upstream repository or action vulnerability state.
`pip-audit` queries the public vulnerability feed for the fully pinned development
and authoring dependency set. It does not execute bundle commands, prove the
absence of unknown vulnerabilities, or claim coverage of a nonexistent portable
runtime dependency graph. Feed failures fail the audit rather than report a
clean result.

## Compatibility and exact regeneration

The validation suite runs on actual CPython 3.12.12 and 3.12.14. Version 2 bundles
declare supported CPython 3.12 compatibility separately from the actual runtime
recorded in regeneration evidence. Historical version 1 bundles retain their
exact-runtime compatibility contract.

The foundation CI job retains CPython 3.12.14 for exact checked-in regeneration.
It checks the legacy native review, the historical version 1 example and the
version 2 example. The compatibility job runs the same tests on 3.12.12 without
rewriting fixtures or claiming an exact match to 3.12.14 regeneration receipts.
Both jobs use `ubuntu-24.04`. That is an explicit OS release label, not an
immutable hosted-image digest; the hosted image can receive updates. Bundle
receipts retain the observed runtime, OS family, machine and relevant tool
identities within the declared qualification scope.

## Updates

Dependabot checks GitHub Actions and Python dependencies weekly. External actions
are pinned to verified full commit IDs; local action references do not need a
remote commit suffix. The shared governance action has its own reviewed
[update procedure](governance-maintenance.md).

Direct development pins live in `requirements-dev.in`. Regenerate the standard
pip-compatible lock with `uv pip compile requirements-dev.in --generate-hashes
--python-version 3.12 --output-file requirements-dev.txt` (initial qualification:
uv 0.13.9), inspect the dependency and hash diff, and rerun the same checks.
Current generated review receipts and inventory digests are updated after tool
changes; frozen native sources and accepted historical evidence retain their
original identities.

Implementation follows the existing tools' documentation:
[Ruff configuration](https://docs.astral.sh/ruff/configuration/),
[Mypy configuration](https://mypy.readthedocs.io/en/stable/config_file.html),
[Zizmor usage](https://docs.zizmor.sh/usage/), and
[Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
