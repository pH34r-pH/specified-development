# Installing and invoking the tools

The portable bundle validator and reviewer use Python's standard library. Copy
`tools/bundle_common.py`, `tools/bundle_validation.py`, and
`tools/bundle_review.py` together when a target only needs bundle operations.
There is no Long-Haul runtime dependency. The same functions are available through
standard Python package entry points; installing this tooling does not install
or qualify the planned Spec Kit distribution.

## Local installation

Use a Python 3.12 environment and the repository's reviewed development/build
dependency pins when building the local wheel. From an environment that already
has the build backend, a local install can remain offline:

```sh
python -m pip install --no-index --no-deps --no-build-isolation .
```

The base package has no runtime dependencies. The optional `authoring` extra
provides PyYAML, JSON Schema and Markdown parsers for the current specification
authoring checks. Install those dependencies from a reviewed environment or
wheelhouse before using `specified-validate-spec`; they are not imported by the
portable bundle tools. CI locks its development dependencies separately from
the package's supported dependency ranges.

| Installed command | Equivalent module |
| --- | --- |
| `specified-validate-bundle` | `python -m tools.bundle_validation` |
| `specified-bundle-review` | `python -m tools.bundle_review` |
| `specified-validate-foundation` | `python -m tools.validate_foundation` |
| `specified-validate-spec` | `python -m tools.spec_validation` |
| `specified-task-review` | `python -m tools.task_review` |
| `specified-onboarding` | `python -m tools.onboarding` |
| `specified-gaps` | `python -m tools.gaps` |

The existing `python tools/bundle_validation.py ...` and
`python tools/bundle_review.py ...` commands continue to work, including in the
three-file copy. The foundation command validates a repository checkout; pass
its path as the positional argument, or run it from the checkout root. Package
installation does not copy the repository's specification and evidence tree
into site-packages.

Import selection depends on the invocation's `__package__` value. An import
failure inside a module propagates normally; it is never retried as an import
of an unrelated top-level module.

## Brownfield onboarding records

`specified-onboarding` validates one [onboarding record](../spec/usage/onboarding.md)
against the onboarded repository's accepted specification. It needs the
`authoring` extra. Run it from the onboarded repository root, or pass `--root`:

```sh
specified-onboarding onboarding.json --root /path/to/project
specified-onboarding onboarding.json --root /path/to/project --results results.json
```

The record names the onboarded areas, characterization sources for every
accepted requirement, a decision for each known defect, the independent oracle
and the initial gaps. With `--results` (independent case outcomes at the exact
baseline revision), the declared gaps must equal the requirements without
passing evidence. The validator never runs project code and never derives
expected values from implementation output. A worked example lives in
[tests/fixtures/onboarding/tally](../tests/fixtures/onboarding/tally/onboarding.json).
The command exits 0 when the record is valid and 2 for an invalid record or I/O failure.

## Requirement status and gaps

`specified-gaps` reports requirement status, gaps and stale descendants from
independent evidence, following the
[gap propagation contract](../spec/contracts/documents.md#requirement-status-and-gap-propagation).
It needs the `authoring` extra:

```sh
specified-gaps evidence.json --root /path/to/project --output status.json
specified-gaps evidence.json --root /path/to/project --previous status.json --output next.json
```

The evidence file names the exact revision, the features, the independent cases
with the requirements each traces, optional tasks with the cases each depends
on, and optional case outcomes recorded at that revision against the
requirement hashes in force when they ran. Each requirement is untested, stale,
failing, regressed or satisfied, and every requirement that is not satisfied is
a gap. With `--previous`, requirements that were added or whose text changed
are listed as changed, together with exactly the cases, tasks and plan sections
that trace them. The report is canonical JSON. It exits 0 on success and 2 for
invalid evidence or an I/O failure; prose and document fields never mark a
requirement satisfied.

## Diagnostics

Bundle validation and review return exit 0 on success, exit 2 for invalid input
or an I/O failure, and exit 3 for an unexpected internal fault. The foundation
command preserves exit 1 for its ordinary validation errors. Every error is
reported on stderr; a successful JSON response stays on stdout.

Unexpected exceptions have the `INTERNAL_ERROR` classification, rather than
claiming the bundle was malformed. Add `--debug` to expose their traceback:

```sh
specified-validate-bundle bundle.json --root /path/to/input --authority-sha256 REVIEWED_PIN --debug
specified-bundle-review render bundle.json --root /path/to/input --output /path/to/review --authority-sha256 REVIEWED_PIN --debug
specified-validate-foundation /path/to/checkout --debug
```

The underlying library functions still raise their original exceptions, which
lets callers and tests distinguish input validation from implementation faults.
Tracebacks are a diagnostic aid and do not change the result or bypass checks.

## Serialization and reuse

The [fingerprint byte contract](fingerprint-serialization.md) specifies existing
pin bytes and fixed conformance vectors. The [shared safety decision](shared-safety.md)
records which strict-reader and path checks can share vectors across repositories
and which policies remain consumer-owned.
The [governance maintenance guide](governance-maintenance.md) explains the
shared profile category and the reviewed action-pin update process.

Packaging follows the [PyPA project metadata specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
and [setuptools pyproject support](https://setuptools.pypa.io/en/stable/userguide/pyproject_config.html).
No custom installer or command launcher is required.
