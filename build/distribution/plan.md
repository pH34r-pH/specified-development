---
artifact: implementation-plan
revision: 1
inputs: [spec/features/distribution/index.md, spec/operations/upstream.md]
acceptance: candidate-review
implementation_status: not-started
---

# Implementation plan

## Ownership and layout

Confirmed central repository: `pH34r-pH/specified-development`; Apache-2.0 for original work. Keep common policy/tooling there; repository-specific authority stays in the consuming repository. The selected existing executor remains execution/infrastructure owner, and portable application behavior stays in its existing repository. Only the approved central foundation handoff was in scope; consumer changes stayed separate.

```text
presets/ph34r-lifecycle/preset.yml
presets/ph34r-lifecycle/templates/{spec,plan,tests,tasks}-template.md
presets/ph34r-lifecycle/commands/speckit.{specify,plan,tasks,analyze,implement,taskstoissues}.md
presets/ph34r-lifecycle/commands/speckit.github.taskstoissues.md
presets/ph34r-lifecycle/scripts/{bash/setup-tasks.sh,powershell/setup-tasks.ps1}
extensions/ph34r-contracts/extension.yml
extensions/ph34r-contracts/commands/speckit.ph34r.{tests,validate,project,verify,cost,regenerate}.md
extensions/ph34r-contracts/scripts/ph34r_contracts/{cli,gate,metadata,projection,issues,receipts,cache,cost,regeneration,installation,compatibility}.py
bundles/ph34r-standard/{bundle.yml,README.md}
catalogs/{presets,extensions,bundles}.json
schemas/{artifact,task,receipt,installation,rate-card,usage,issue-binding,regeneration}.schema.json
tools/{bootstrap,stage_upgrade,promote_upgrade,rollback_upgrade,build_release}.py
policies/{execution,compatibility,rollout}.json
generation/{instructions.md,packet.schema.json}
fixtures/{mature-feature,legacy-installation-a,legacy-native-contract,kanban-v1,native-contract-v1,github,usage,regeneration}/
tests/test_{templates,gates,metadata,projection,issues,receipts,cache,cost,installation,upgrade,compatibility,regeneration,pilot,release,cli}.py
spec/operations/{ownership,migration,release,operator,regeneration}.md # future canonical docs must be explicitly registered
pyproject.toml / uv.lock / release-lock.json / assets-manifest.json
```

Use Python 3.12, `unittest`, standard-library JSON/hash/path/Decimal/process utilities, and the locked upstream YAML parser at the YAML boundary. Resolve upstream `specify-cli` from peeled commit `f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9` (1.0.13). Generate `uv.lock`, record Python/uv/runtime observations and dependency artifact hashes, then use `uv sync --frozen`; no upstream lock was supplied. The project CLI entry point is `ph34r-spec`; it is a deterministic artifact utility, never a worker runner or scheduler.

## Component boundaries

Preset `ph34r-lifecycle@1.0.0`: replace spec/plan/tasks templates and all affected commands, add tests-template, and supply both task-setup wrappers with fresh accepted-tests prerequisites. Declare distinct script names `ph34r-setup-tasks-sh` and `ph34r-setup-tasks-ps` with explicit shell-specific file paths: upstream rejects duplicate `(name,type)` pairs and its generic script fallback favors `.sh`. The replacement tasks command explicitly selects wrappers in frontmatter `scripts.sh` and `scripts.ps`, using installed `.specify/presets/ph34r-lifecycle/scripts/...` paths so PowerShell never silently receives the Bash wrapper. Each wrapper invokes the extension's gate and then the pinned core prerequisites without recursion. Command replacements cover specify, plan, tasks, analyze, implement, legacy taskstoissues, and bundled `speckit.github.taskstoissues` if present. Replace strategy eliminates conflicting MVP/tests-optional text. Avoid broad constitution replacement. Plan points to the namespaced tests command before tasks; implement requires a validated contract. Generated commands reference installed extension/preset script paths, as resolved and verified through upstream registration, rather than source-tree paths.

Extension `ph34r-contracts@1.0.0`: adds namespaced commands and scripts. `speckit.ph34r.tests` performs semantic tests authoring from accepted spec/plan; its independent expected outcomes come from those inputs. Tasks authoring performs semantic decomposition once and emits complete records alongside prose. All deterministic verbs invoke Python directly and never launch a model. Stock authoring workflows cannot bypass missing-test gates; they remain non-qualified until their selected sequence includes the mandatory tests gate. No new authoring workflow component or task scheduler is necessary.

Bundle `ph34r-standard@1.0.0`: integration-agnostic, exact upstream requirement, preset at priority **10** with replace strategy, extension pinned 1.0.0. Core `github@1.0.0` is observed upstream but **not a required dependency**: the central deterministic issue projector replaces both command entry points when installed. `agent-context@1.0.2` and `git` are not mandatory; no automatic branch/commit hook is added. Catalogs point at separately versioned component archives; the outer bundle does not substitute for those payloads. Validate positive component resolution using actual sources, not offline warnings.

The manifest field shapes, component/version meanings, catalog/install APIs, and active-integration materialization follow the pinned upstream sources in spec/operations/upstream.md. See [distribution contract](../../spec/contracts/distribution.md) for exact native manifest examples and project data fields. Proposed archive URLs remain unset until approved archives exist at the confirmed destination; release tooling rejects null URLs/digests.

## Authoritative package and revision gates

Canonical `spec/` holds source behavior; `build/<feature>/` holds derived spec.md and retained plan.md, tests.md, tasks.md plus declared contract adapters/fixtures/locks/generation instructions. The directory and authority contracts govern source inventory and accepted retention. Sidecar `artifact-state.json` records revision IDs, byte hashes, upstream sets, acceptance actor/time/directive reference, target status, and delivery receipts. It contains no task state. Human design approval must be explicit; validation cannot manufacture it. New authoring outputs remain candidates until their gate's permitted acceptance is recorded.

Hash exact UTF-8 file bytes with SHA-256. Canonical record hashes use sorted-key UTF-8 JSON with compact separators and no timestamp or path-location entropy. Input-set hashes include normalized logical paths and content hashes; roots are recorded separately. Accepted revisions are retained. Prose and embedded task records are accepted together; a mismatch rejects the package. Every task record freezes source inputs, then adds prerequisite output digests at claim; this is materialization, not semantic decomposition. A receipt/input set is never accepted with unresolved digest placeholders.

Earliest-authority repair is explicit: discovery packet identifies conflicting claim/test, frozen hashes, bounded evidence, and affected IDs; the existing execution owner registers one deduplicated spec/plan/test repair leaf for the relevant authority revision. The original attempt stops. Approve a new upstream revision, regenerate affected downstream artifacts, compare task-contract hashes, preserve identical receipts, and mark changed descendants stale. The repair uses its own fixed model. No automatic model switch, second retry loop, or semantic repair by the projector is permitted.

## Execution contract and issue projection

Use the existing native-contract normal-dispatch profile: `schema_version: 1`, `authority`, `execution`, named commands with `cwd/argv/expect`, and `tasks.<TID>.parents/tests/paths/commands/expected`. Add metadata under **`x_distribution`** so native fields keep their meanings. Fail when the selected consumer cannot tolerate or validate this namespaced extension. Existing Kanban version-1 workstream contracts are imported read-only, preserving aggregate/test/implementation/review binding and successor-on-aggregate semantics. Never interpret a legacy aggregate as an executable leaf or flatten it silently. Import ambiguity creates a repair, not a new DAG.

Global identity is `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T###` for this package; local `T###` remains compatible with existing features. IDs are immutable logical namespaces even if the eventual hosting repository is renamed. The single task graph is projected from embedded accepted task metadata into `execution-contract.yaml`. Issue bindings map qualified ID and contract hash to target repo + numeric issue ID/number + immutable creator; they contain no dependency or scheduler state.

Dry projection writes exact issue bodies and native-edge operations. Apply, when independently authorized, verifies the authenticated user, remote/explicit target, accepted artifact hashes, selected execution owner, and permission scopes. Find existing issues by exact stable marker, fetch full paginated records, reject duplicates and semantic drift, create missing leaves without `agent-ready`, bind IDs, add native `blocked by` dependencies using **numeric issue IDs**, and add sub-issue relationships only for grouping. Read back all IDs and edges. Only then add `agent-ready` to eligible approved-author leaves. A crash leaves incomplete/uncertain leaves without ready labels; restart reconciles remote truth from markers. Prior tasks are not deleted. Extra edges, prior-ready stale leaves, and unexpected remote edits fail readiness until reviewed; ready labels are withdrawn only for affected owned issues under authorized repair operations.

The selected existing executor scheduled tasks; this tool projected and verified. Before activation, the consumer positively qualified creator/allowlist, complete native-edge pagination, task kinds, observed model/settings and completion predicates. Missing capability blocked activation and stayed with the existing owner's separately scoped change. fixed-model-v3 used the approved low-cost gpt-6-luna role default for bounded/integration leaves, with observed exact binding; architectural leaves required a preapproved capability-qualified binding. No alias, runtime guess or unsupported reasoning flag was permitted.

## Receipts, cache, and accounting

Commands are trusted named argv records; no shell interpolation or caller-defined command strings enter a receipt. Path checks reject absolute/traversal/symlink escapes and undeclared/protected modifications, including rename destinations. Parallel execution requires closed prerequisites and disjoint writable paths; repository/feature publication artifacts are serialized. A RED leaf closes only with its expected missing-behavior failure, never syntax/runtime/fixture failure. GREEN leaves use the already-defined independent tests plus focused regressions. Review gates protect public release and mutation/cost boundaries.

Cache eligibility covers accepted semantic input hashes, dependency-output hashes, command/test-oracle hashes, exact lock/tool fingerprints, fixed-model policy, and compatible environment. A hit means reuse of scoped output and provenance after acceptance revalidation, not automatic task closure. Revalidate changed scope and required commands; never cache credentials, model authority, deployment approval, or remote task state. An unknown environment/permission or failed artifact blocks reuse. No reuse of earlier source code is permitted inside a regeneration trial whose purpose requires source exclusion.

Cost records are append-only evidence attached to existing attempts, not a parallel execution ledger. Normalize observed token fields to inclusive input and inclusive output; adapters declare whether provider fields exclude cache or reasoning before conversion. Record totals only once. Formula: `((input-cached)*input_rate + cached*cached_input_rate + output*output_rate)/1_000_000`. Reasoning contributes only through inclusive output. A rate card identifies currency, source URL/digest, effective/retrieval dates, model/provider, context/service/tier applicability and normalization policy. Missing rate/usage gives null total with known subtotal and explicit missing fields. Sum all failed/retried attempts; report cost per accepted leaf only for comparable complete cohorts. Subscription usage may have API-equivalent cost but never a fabricated invoice. The included numeric rate card is deliberately a synthetic arithmetic fixture; current prices are not guessed.

## Installation and safe upgrades

Bootstrap obtains a pinned CLI build/environment and approved component payloads, verifies archive hashes before extraction, checks manifest IDs/versions, records catalogs, invokes existing primitive machinery, and verifies effective template/script/command resolution plus materialized active-integration assets. A wrong-version independent install produces a conflict; explicit staged replacement is required rather than force-adopting ownership. Unexpected overrides or tampered generated assets block use; approved domain rules remain separate and included in compatibility checks.

Upgrade operates on an isolated copied/worktree installation with no credentials. Snapshot exact managed-path bytes/modes plus known-unrelated file sentinels, current component records and active integration. Record managed paths newly introduced by the candidate. Verify the old snapshot and retain it outside paths being replaced. Install/refresh in staging, inspect generated assets and complete compatibility/recovery tests, then emit a concrete changed-path plan. Promotion requires the appropriate authorization and exact before-hash compare-and-swap. A journal records planned/applied file operations; interrupted promotion rolls back prior files and only removes newly introduced managed installation files listed in that journal. It never deletes application source or historical artifacts. Recovery verifies exact prior bytes/modes and unrelated sentinels. If restoration cannot be proved, fail closed and retain evidence; do not claim success. This compensates for, rather than exaggerates, upstream rollback behavior.

## Pilot, qualification, and rollout

The pilot exercises the **complete distribution** in a synthetic mature feature and an isolated copy of the first sanitized legacy installation: candidate/accepted states, spec→plan→tests→tasks, metadata/projection, rejected stale input, dry issue export/native-dependency fake, fixed-model policy, cache/cost, staged failure recovery, and retained-source regeneration evidence. Its scope is small because it validates the common workflow, not because it describes an MVP product.

Regeneration qualification targets only `extensions/ph34r-contracts/scripts/ph34r_contracts/gate.py` and its declared interface. Freeze its mature specification/plan, independent gate tests/fixtures, package lock, generator instructions and approved fixed-model/runtime binding. Start two independent empty workspaces and fresh generation contexts under the **same exact model binding for the entire T032 attempt**; the second receives neither the original implementation nor the first trial's generated source. Retain the original implementation outside them, deny it from read/attachment/context paths, and log the allowlisted input inventory. Generate/build the scoped module, run the identical independent behavioral + regression oracle in each workspace, retain every failed and successful attempt/cost, and compare normalized observable outputs. Do not require byte-identical implementation. A passing deterministic rendering test is not behavioral regeneration proof. No regeneration inference is executed or paid for in this design pass.

| Gate | Required evidence | Repository boundary |
| --- | --- | --- |
| G0 Authority | Latest accepted user directive and package review recorded; snapshot provenance explicit; dated provenance and current authority acceptance; destination/license before publication | Local package only |
| G1 Build | Actual pinned CLI/lock/component/archive/generated-asset digests, clean-source build and positive refs | Confirmed central repo after accepted foundation |
| G2 Compatibility | Claude/Codex active-asset tests; local override/constitution/history preservation; both existing contract profiles | Disposable copies/fixtures |
| G3 Recovery | Wrong-version/tamper/interrupted stage/promotion/rollback tests | Disposable installations |
| G4 Pilot | Complete lifecycle, projection, receipt, cache/cost, two scoped regeneration trials | Synthetic feature + isolated first legacy installation copy |
| G5 Repository adoption | Repo owner reconciles local scope, model binding, CI, permissions and current feature history | Separate explicitly scoped per-repo change |
| G6 Activation | Existing execution owner can enforce contract/observed model; creator/allowlist/native edges verified | existing executor owner or existing Kanban owner; no overlap separately owned infrastructure changes |

After the pilot, each consumer qualified adoption in its own owner-approved PR after coordinating with active work. Broad rollout and application implementation remained outside this distribution change.


## Directory and native-contract binding

Canonical source lived in spec/, while plan/tests/tasks and generated adapters lived under build/<feature>/. Accepted snapshot retention followed the authority contract. This central program's foundation, distribution and directory leaves used one build/execution-contract.yaml. build/native-bindings.json froze each qualified leaf's native local ID without changing its stable issue identity. Foundation preceded distribution; accepted distribution qualification preceded the directory implementation. These cross-feature prerequisites were native hard parents, not a second scheduler or informal gate. The foundation did not release/install the distribution.
