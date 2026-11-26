# Shared strict-reader and path-safety decision

**Decision:** share adversarial conformance vectors and retain each consumer's
existing implementation and policy boundary. No new safety package or mandatory
cross-repository release dependency is introduced. This implements the bounded
reuse evaluation in [issue #31](https://github.com/pH34r-pH/specified-development/issues/31).

## Existing solutions and the smallest useful reuse

Python's [JSON parser](https://docs.python.org/3.12/library/json.html) already
provides object-pair, numeric-constant and floating-point hooks. Specified
Development and Experiment Compiler use those hooks to reject duplicate keys
and nonfinite inputs. The local `bundle_common.parse_json` extends that same
parser with a finite-number check for exponent overflow and typed parse errors;
it is not a second JSON parser.

[PathSpec](https://python-path-specification.readthedocs.io/en/latest/readme.html)
implements gitignore matching. [Wildcard Match](https://facelessuser.github.io/wcmatch/)
implements richer Bash-like matching and filesystem globbing. Those are useful
when a consumer needs their syntax, but neither is a drop-in replacement for a
reviewed restricted authority language that permits only whole-component `*`
and terminal `**`. They also do not replace archive inventory checks or frozen
Git object-mode checks. Preserve the current restricted language and test its
security semantics instead of widening it incidentally during library adoption.

[rfc8785](https://pypi.org/project/rfc8785/) supplies established JSON
canonicalization for a future consumer requiring JCS. The separate
[fingerprint decision](fingerprint-serialization.md) preserves established pin
bytes with fixed vectors. None of these libraries is copied or bundled here;
their documentation informed the comparison.

## Why the boundaries remain separate

| Consumer and source | Shared semantics | Consumer-owned policy |
| --- | --- | --- |
| [Specified Development helpers](../tools/bundle_common.py) | Strict UTF-8 JSON, duplicate/nonfinite rejection, lexical relative paths and exact-byte hashes. | Working-tree confinement and symlink checks, declared read/write/protected scope, portable materialization collisions, limited authority globs, and the bundle profile's JSON/source budgets. |
| [Experiment Compiler core](https://github.com/pH34r-pH/experiment-compiler/blob/ca76cca015d1bc8c4ffbace2bfafca2ef8ebab90/experiment_compiler/core.py) | Strict JSON hooks, relative member paths, identity and collision checks. | Portable archive names, Windows device-name exclusions, exact inventory/size/digest checks, and caller-owned archive resource policy. |
| [Long-Haul repository identities](https://github.com/pH34r-pH/long-haul/blob/660d0258da03950682a37a23d39a2a2b910372c1/src/long_haul/work/repository_models.py) and [Git reader](https://github.com/pH34r-pH/long-haul/blob/660d0258da03950682a37a23d39a2a2b910372c1/src/long_haul/work/repository_git.py) | Validated relative identifiers and exact content identity. | Frozen Git objects, denied `.git` context paths, object-mode rejection for links and submodules, disabled acquisition/filters, and Git-context resource limits. |

An archive can legitimately forbid a Windows device name while a frozen Git
object keeps that exact name as an identity. A lexical path helper accepting
`.git/config` does not grant write authority; Specified Development's admitted
scope still decides that. Long-Haul denies it at its repository-context path
boundary. The corpus records these differences explicitly.

Resource limits remain with their actual consumers. Experiment Compiler's
[completed operational-policy decision](https://github.com/pH34r-pH/experiment-compiler/issues/134)
must not acquire the bundle validator's 8 MiB input cap as an artifact-format
restriction. Replacing the Git object reader with a shared working-tree reader
would also remove a material isolation boundary.

## Executable common vectors

[`conformance.json`](../tests/fixtures/safety/conformance.json) is a small,
language-neutral corpus of JSON, path and path-collection cases. The normal
stdlib suite runs its local tests through the actual parser and expansion
preflight. It includes nested duplicate JSON keys, literal nonfinite values,
numeric overflow, malformed JSON, traversal, case and Unicode-normalization
collisions, file/directory conflicts and safe non-ASCII positive controls.
Malformed bundle/detail shapes have separate tests in
[`test_tooling.py`](../tests/test_tooling.py); syntactically valid JSON arrays
are not intrinsically invalid until a domain record requires an object.

The optional cross-repository tests import the real helpers from exact supplied
local checkouts. They check both the commit identity and tracked-file cleanliness
before importing, perform no downloads or installations, and leave the source
trees unchanged. Long-Haul's model module needs its existing Pydantic dependency
in the test environment; that dependency is not added to the portable tools.

```sh
SPECIFIED_EXPERIMENT_COMPILER_ROOT=/path/to/experiment-compiler \
SPECIFIED_LONG_HAUL_ROOT=/path/to/long-haul \
python -m unittest discover -s tests -p test_safety_conformance.py -v
```

The corpus pins the inspected revisions. Update those pins, reviewed expectations
and observation record together when evaluating a newer consumer; a mutable
checkout is not interchangeable evidence. Without supplied checkouts, the local
cases still run and the optional cross-repository class is visibly skipped.

## Observed results and remaining external gaps

The retained [conformance observation](../build/shared-safety-conformance.json)
records a 26 November 2026 helper-level run with CPython 3.12.14 and Pydantic
2.13.4 against the exact revisions above. Four cross-repository tests passed.
Two deliberately separate probes produced expected failures:

- Experiment Compiler's `json_value` accepts exponent overflow such as `1e999`
  as a nonfinite float.
- Its `unique_paths` rejects case collisions but accepts a pair of NFC/NFD
  spellings of the same name.

These are known gaps owned by
[Experiment Compiler #155](https://github.com/pH34r-pH/experiment-compiler/issues/155),
not intentional policy differences or passing safety guarantees. The expected-
failure probes preserve the desired rejection assertion; when that consumer is
fixed, the unexpected success forces the observation and expectation to be
reviewed. This work does not modify that repository or reopen its completed
resource-policy issue.

The link tests check Specified Development's confinement, the compiler's actual
regular-file reader, and Long-Haul's rejection of symlink/submodule Git modes.
They are helper-level conformance evidence, not a complete hostile archive,
filesystem-race, runtime-sandbox or product qualification. Existing owners remain
[Long-Haul #245](https://github.com/pH34r-pH/long-haul/issues/245), the completed
[repository-context foundation #242](https://github.com/pH34r-pH/long-haul/issues/242),
and [candidate-capacity follow-up #293](https://github.com/pH34r-pH/long-haul/issues/293).

## Extraction threshold

A future shared package is justified only when at least two consumers can use
the same semantics without importing each other's application, weakening their
trust boundaries, or inheriting another consumer's resource policy. Establish
consumer parity with these vectors and existing exact historical fixtures
before deleting duplicated implementation. Shared fixtures are the useful
common component now; no new package lifecycle is required to close a local
safety repair.
