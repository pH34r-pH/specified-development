# Executable bundle validation and review

The three portable files `tools/bundle_common.py`, `tools/bundle_validation.py`, and `tools/bundle_review.py` validate and review a native task bundle using Python's standard library. Copy them together; target repositories need no repository-specific validator, Long-Haul Python dependency, model, service, or network access.

The qualified version is `native-bundle-v1`, generator `1.0.0`, with the exact CPython runtime recorded in the bundle and regeneration receipt. The hermetic example pins `CPython-3.12.14`; CI runs that version. Tool source SHA-256 values are also retained, so changing code without changing its display version remains observable.

```sh
export BUNDLE_AUTHORITY_SHA256=5d10341e61568ce6795fe194ffc4d0188863b7e32f46864c00dfb118e8f034ec
python tools/bundle_validation.py bundle.json --root tests/fixtures/bundle --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
python tools/bundle_review.py render bundle.json --root tests/fixtures/bundle --output /tmp/bundle-review --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
python tools/bundle_review.py render bundle.json --root tests/fixtures/bundle --output /tmp/bundle-review --authority-sha256 "$BUNDLE_AUTHORITY_SHA256" --check
```

The authority pin comes from independently reviewed caller/control state, never from a field supplied by the candidate bundle. The example value above freezes the public fixture's exact authority projection, including `acceptance_source: {id, sha256}`. That digest must match the independently frozen policy source record and bytes. A target owner reviews its own projection and supplies its canonical sorted-JSON SHA-256; changing allowed paths, capabilities, or acceptance-policy bytes then requires a new caller-reviewed pin. This fingerprint is a comparison boundary, not a digital signature or authentication service.

Exit 0 means structural conformance or exact regeneration. Exit 2 means invalid, stale, incompatible, or unsafe input. Validation does not run declared commands, accept task results, change native scheduling, or grant deployment/publication authority. The target repository retains its independent acceptance and runtime sandbox boundaries.

## Version 1 record contract

The native JSON contract carries the sole DAG at `tasks.<id>.parents`. Its required top-level fields are `schema_version`, `feature`, `status`, `authority`, `commands`, `tasks`, and `x_bundle`. The complete worked record is [the fixture](../tests/fixtures/bundle/bundle.json); fields outside this profile fail rather than acquiring inferred semantics.

| Record | Required behavior |
| --- | --- |
| `authority` | Concrete read/write/protected path patterns, declared read/edit/test capabilities, a frozen policy source, and `promotion: target-repository-only`. Exact paths, whole-component `*`, and terminal `**` are supported. Absolute paths, traversal, empty components, control characters, and ambiguous glob forms fail. |
| `x_bundle.versions` | Exact schema, generator, and runtime identity. Unknown versions block with an explicit compatibility diagnostic. |
| `x_bundle.sources` | Unique confined path, SHA-256 of exact bytes, and one source kind: spec, plan, tests, tasks, policy, or ordinary input. Frozen semantic sources cannot be task outputs. Symlink traversal and stale bytes fail. |
| `requirements`, `plans`, `tests` | Stable IDs, source-kind checks, observable requirement/oracle expectations, complete foreign-key traces, fixed command references, and expected exit status. Every requirement reaches a plan, test, and task. |
| `tasks` | Known acyclic parents, nonempty test/command/output lists, observable acceptance, output scope within authority and outside protected paths. Commands are explicit argv/cwd/capability declarations. Validation cannot prove arbitrary code's effects or that its asserted capability is truthful. |
| `x_bundle.task_traces` | Exactly one trace per native task, a frozen tasks source, plan/requirement links, and required evidence for exact candidate identity, command results, and independent review. A worker's success statement cannot replace these fields. |

Repository-work references can remain ordinary exact inputs or policy/source records. The upstream identity boundary is [Long-Haul #242 at its accepted revision](https://github.com/pH34r-pH/long-haul/tree/5cab6749e65090b16d0b28970fe4edc81379d646/contracts/repository-work). This tool does not reinterpret that extension or import Long-Haul runtime classes. Resource rights, privacy admission, credentials, and actual caller authority must be checked by the target's existing policy boundary before generating or exposing a bundle.

## Compact review and exact expansion

Rendering produces `README.md`, `regeneration.json`, and one `objects/<sha256>.json` file. The review lists intent, parents, observable acceptance, tests, and write boundaries, and names the risks requiring target review. Long text is shortened visibly; the object preserves every declared input path and exact byte string. Its input identity covers the native task contract, sources, and their digests. The receipt separately binds generator/runtime/source identities and the review/detail fingerprints. There are no timestamps or workspace paths in deterministic outputs.

Expansion requires the expected object SHA-256 and an empty destination. It verifies all bytes and path relationships before writing, refuses traversal/symlink output roots and existing nonempty directories, and never overwrites source or accepted records.

```sh
python tools/bundle_review.py expand /tmp/bundle-review/objects/EXACT_SHA256.json --sha256 EXACT_SHA256 --output /tmp/bundle-expanded
python tools/bundle_validation.py bundle.json --root /tmp/bundle-expanded --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
```

The example oracle independently demonstrates missing/wrong code failing and correct code passing in disposable test workspaces. This qualifies the validator and fixture; it does not claim an actual agent produced or independently accepted a target implementation.

## Legacy compatibility and migration

The existing 60-task execution contract and its accepted historical receipts remain byte-identical. [Its compact review](../build/bundle-review/README.md) is the human entry point; the lossless object retains its machine detail and frozen source closure. Rendering it requires `--legacy-review-only`. Its unresolved symbolic read scopes and old candidate semantics are explicitly unqualified for the new generic profile.

```sh
python tools/bundle_review.py render build/execution-contract.yaml --legacy-review-only --output build/bundle-review --check
```

Calling the generic validator on this legacy contract returns `MIGRATION_REQUIRED`; it never invents concrete permissions or promotes a historical candidate. A target owner must review concrete source records, trace coverage, scope/capability limits, exact versions, and independent acceptance authority to author a new version-1 bundle. Retain the predecessor by immutable Git identity, regenerate the new review, and rerun target checks. Unsupported past/future schema, generator, or runtime versions fail explicitly. This release performs no silent migration, model dispatch, installation, publication, or deployment.

The repository reuses its existing native contract format, confined-file/hash helpers, and read-only GitHub CI. No second task graph, workflow engine, scheduler, database, or source-of-truth service is introduced.

## Existing implementation review

The implementation search included the repository's scaffold validator and [Spec Kit's pinned bundle validator](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/bundles/validator.py) and [manifest model](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/bundles/manifest.py). Those upstream bundles compose installable extensions/presets/workflows; their validation covers manifest structure and component references. Spec-plan-test-task acceptance and frozen target scopes need this repository's native task profile. The new code extends existing confined reads and hashes, follows explicit versioned validation, and leaves upstream installation machinery unchanged. No upstream code was copied.

Version 1 bounds JSON inputs to 8 MiB, qualified source inventories to 256 entries, and combined rendered input bytes to 16 MiB. Larger bundles require an explicit profile change or a smaller independently reviewable unit.
