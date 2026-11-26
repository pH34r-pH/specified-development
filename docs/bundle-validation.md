# Executable bundle validation and review

See the [delivery status and qualification evidence](../REVIEW.md#delivery-status) for the scope of these tools and the remaining distribution gates.

The three portable files `tools/bundle_common.py`, `tools/bundle_validation.py`, and `tools/bundle_review.py` validate and review a native task bundle using Python's standard library. Copy them together; target repositories need no repository-specific validator, Long-Haul Python dependency, model, service, or network access.

The current profile is `native-bundle-v2`, schema `2`, generator `2.0.0`. It binds reviewed commands and their exact declared source bytes and validates on supported CPython 3.12 patch releases. The generation runtime recorded in a bundle is provenance, separate from the compatible runtime performing validation. Exact regeneration remains an additional check in the pinned CI environment. Tool source SHA-256 values are retained, so changing code without changing its display version remains observable. The original version 1 fixture and pin remain unchanged under the explicit legacy contract below.

```sh
export BUNDLE_AUTHORITY_SHA256=9713363e11ede97f43b5faee72ad86ae8692e3a14f7a7a8d90edf8eb58aaaf7a
python tools/bundle_validation.py bundle.json --root tests/fixtures/bundle-v2 --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
python tools/bundle_review.py render bundle.json --root tests/fixtures/bundle-v2 --output /tmp/bundle-review --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
python tools/bundle_review.py render bundle.json --root tests/fixtures/bundle-v2 --output /tmp/bundle-review --authority-sha256 "$BUNDLE_AUTHORITY_SHA256" --check
```

The pin comes from independently reviewed caller/control state, never from a field supplied by the candidate bundle. For version 2, `reviewed_fingerprint(bundle)` hashes a projection with exactly six keys: `profile`, `schema_version`, `versions`, `authority`, `commands`, and `sources`. `profile` is `native-bundle-v2`; `versions` and `sources` are the corresponding `x_bundle` records. The other values are the exact native bundle fields. This covers command IDs, ordered argv, cwd, capability, explicit script-source associations, all declared source identities/digests, acceptance-policy identity and generation provenance. Every source digest is also verified against actual confined file bytes.

The serialization remains the existing authority-pin byte contract: Python JSON with sorted keys, compact separators, `ensure_ascii=True`, `allow_nan=False`, UTF-8 encoding and no trailing newline. It is not advertised as RFC 8785. A target owner reviews the exact projection and supplies its SHA-256. Changing a command, script bytes plus their declared hash, or an authority field requires a new caller-reviewed pin. Computing a pin from unreviewed candidate data does not establish approval. This comparison boundary is not a digital signature or authentication service.

Exit 0 means structural conformance or exact regeneration. Exit 2 means invalid, stale, incompatible, or unsafe input. Validation does not run declared commands, accept task results, change native scheduling, or grant deployment/publication authority. The target repository retains its independent acceptance and runtime sandbox boundaries.

## Version 2 command and path contract

The [version 2 fixture](../tests/fixtures/bundle-v2/bundle.json) uses the existing native graph and trace records. Its `schema_version` and `x_bundle.versions.schema` are `2`; `x_bundle.profile` is `native-bundle-v2`; `x_bundle.versions.generator` is `2.0.0`. A supported generation runtime has the form `CPython-3.12.<patch>`. Validation requires a CPython 3.12 host, independently of that recorded patch identity. Unknown profile/schema/generator combinations remain errors.

Each command has exactly `argv`, `cwd`, `capability`, and `script_source`. The initial restricted form is `python <script> [arguments]` or `python3 <script> [arguments]`. `script_source` identifies a declared `tests` or `input` source record, and the script path resolved relative to the confined working directory must exactly equal that record's path. Inline `-c`, module `-m`, shell interpreters and interpreter options before the script are unsupported. Script arguments after its path are ordinary data covered by the pin. Other command forms need an explicit profile extension.

The executor resolves the logical Python command to its admitted interpreter. Validation never executes a command, inspects runtime effects, discovers dynamic imports, or proves that a capability declaration is truthful. A reviewer includes required helper scripts in the declared source closure; any reviewed script, including one classified as ordinary input, is protected from task outputs. The existing executor still owns actual filesystem/network containment and target acceptance. `reviewed_commands: true` means the declared identities match the supplied pin; it does not mean the task is ready, executed or accepted.

Version 2 uses `NFC(NFC(component).casefold())` only as a conservative rejection key. It rejects source/inventory/output aliases, including differently spelled shared directory components, and checks protected paths and frozen sources with those keys. Protection also rejects an output naming a protected/frozen path's ancestor, because replacing or deleting that directory could remove the protected content. Thus protecting `src/credentials/**` rejects `src/credentials`, its case aliases, and `src`, while a distinct sibling such as `src/credentials-sibling/key` remains available. Terminal `**` includes zero or more components. Exact source names and bytes are retained. Read/write allowlist containment still compares exact components: `SRC` cannot gain access through permission for `src`. Safe Unicode names remain valid. Whole-component `*` and terminal `**` retain their existing grammar; the original version 1 comparison behavior is preserved separately.

These checks establish logical rejection of the named case/normalization aliases. They do not claim that all filesystem-specific aliases are modeled, or that a case-insensitive operating system has been qualified. Lossless expansion applies collision and file/directory-prefix safety before writing, including when materializing a legacy object.

## Preserved version 1 record contract

`native-bundle-v1`, schema `1`, generator `1.0.0` retains its original authority-only pin and exact CPython runtime comparison. The frozen fixture records `CPython-3.12.14`, with authority pin `5d10341e61568ce6795fe194ffc4d0188863b7e32f46864c00dfb118e8f034ec`. The legacy validator result explicitly reports `reviewed_commands: false`; the rendered review says command review is not granted. Version 1 remains a structural compatibility reader and does not acquire version 2 command binding or portable path guarantees by implication.

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

Rendering produces `README.md`, `regeneration.json`, and one `objects/<sha256>.json` file. The review lists intent, parents, observable acceptance, tests, and write boundaries, and names the risks requiring target review. Long text is shortened visibly; the object preserves every declared input path and exact byte string. Its input identity covers the native task contract, sources, and their digests. The receipt separately records the bundle's declared generation provenance and the actual renderer's generator, CPython patch, OS family, architecture, Unicode database and source-file identities. It also binds review/detail fingerprints. These observations are not an immutable hosted-image identifier. There are no timestamps or workspace paths in deterministic outputs.

A supported-runtime validation success does not promise identical rendering receipts on another runtime: differing actual provenance produces `REGENERATION_DRIFT` under `--check`. Use the pinned regeneration lane for exact readback; use the compatibility test lane to validate the unchanged version 2 fixture on supported patch releases.

Expansion requires the expected object SHA-256 and an empty destination. It verifies all bytes and path relationships before writing, refuses traversal/symlink output roots and existing nonempty directories, and never overwrites source or accepted records.

```sh
python tools/bundle_review.py expand /tmp/bundle-review/objects/EXACT_SHA256.json --sha256 EXACT_SHA256 --output /tmp/bundle-expanded
python tools/bundle_validation.py bundle.json --root /tmp/bundle-expanded --authority-sha256 "$BUNDLE_AUTHORITY_SHA256"
```

The example oracle independently demonstrates missing/wrong code failing and correct code passing in disposable test workspaces. This qualifies the validator and fixture; it does not claim an actual agent produced or independently accepted a target implementation.

## Legacy compatibility and migration

The scaffold validator checks the legacy authoring records at their current
candidate stage. The native bundle validator distinguishes legacy version 1
structure from version 2 reviewed command identities. The existing executor and target owner supply the
evidence required for later stages.

| Requirement | Candidate and frozen contract | Existing owner at admission or completion |
| --- | --- | --- |
| Frozen inputs | Require a nonempty exact-byte input list and verify each declared hash. | Recheck approved source and accepted parent receipts for the assigned attempt. |
| Fixed model | Require a fixed policy with switching and implicit resolution disabled. A pending binding remains reviewable. Deterministic leaves declare no model. | Bind one admitted selection to the attempt. Validate a supplied selection history against that selection. Keep optional effective observations separate. |
| Issue identity | Require one stable marker, a single target repository, and either a complete issue binding or an explicit pending binding. Reject cross-task duplicates. | Require exactly one independently observed issue matching the assigned repository, number, immutable ID, state, and marker at the foundation evidence check. |
| Output and acceptance | Require a bounded relative output scope, observable acceptance and declared commands. Executable model leaves reference their test cases. | Verify actual scope, command and independent target evidence before accepting the result. |

The checked-in authoring records and native graph remain candidates. Pending
model and issue bindings grant no readiness or acceptance. The read-only
validator consumes observations supplied by the existing owner and never
dispatches a task.

The existing 60-task execution contract and its accepted historical receipts remain byte-identical. [Its compact review](../build/bundle-review/README.md) is the human entry point; the lossless object retains its machine detail and frozen source closure. Rendering it requires `--legacy-review-only`. Its unresolved symbolic read scopes and old candidate semantics are explicitly unqualified for the new generic profile.

```sh
python tools/bundle_review.py render build/execution-contract.yaml --legacy-review-only --output build/bundle-review --check
```

Calling the generic validator on this legacy contract returns `MIGRATION_REQUIRED`; it never invents concrete permissions or promotes a historical candidate. A target owner must review concrete source records, trace coverage, scope/capability limits, command forms and source associations, version provenance, and independent acceptance authority to author a version 2 bundle. Retain the predecessor by immutable Git identity, supply the newly reviewed version 2 pin, regenerate the new review, and rerun target checks. No version 1 pin is reinterpreted as a version 2 pin. Unsupported profile/schema/generator combinations and host runtimes fail explicitly. This release performs no silent migration, model dispatch, installation, publication, or deployment.

The repository reuses its existing native contract format, confined-file/hash helpers, and read-only GitHub CI. No second task graph, workflow engine, scheduler, database, or source-of-truth service is introduced.

## Existing implementation review

The implementation search included the repository's scaffold validator and [Spec Kit's pinned bundle validator](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/bundles/validator.py) and [manifest model](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/bundles/manifest.py). Those upstream bundles compose installable extensions/presets/workflows; their validation covers manifest structure and component references. Spec-plan-test-task acceptance and frozen target scopes need this repository's native task profile. The new code extends existing confined reads and hashes, follows explicit versioned validation, and leaves upstream installation machinery unchanged. No upstream code was copied.

The path-alias repair reuses Python's standard-library [Unicode normalization](https://docs.python.org/3.12/library/unicodedata.html) and [case-folding guidance](https://docs.python.org/3.12/howto/unicode.html). [PathSpec](https://python-path-specification.readthedocs.io/en/stable/api.html) was considered; its Git ignore matching language is broader and different from this profile's deliberately bounded component grammar. Retaining the existing matcher and adding standard Unicode comparison keys avoids changing permissions or adding a mandatory runtime dependency.

Both profiles bound JSON inputs to 8 MiB, qualified source inventories to 256 entries, and combined rendered input bytes to 16 MiB. Larger bundles require an explicit profile change or a smaller independently reviewable unit.
