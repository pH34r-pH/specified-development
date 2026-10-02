---
artifact: executable-decomposition
revision: 3
acceptance: candidate-review
dispatch_status: planned-not-dispatched
---

# distribution dependency-ordered leaves

Semantic decomposition was completed in this fixed-model design pass. Each unchecked leaf mapped 1:1 to one issue. build/execution-contract.yaml parents were the sole execution graph. build/native-bindings.json retained stable qualified-to-native ID bindings. Feature/epic grouping and source document dependencies were not scheduling edges. Missing model/runtime/budget/permission/input bindings blocked claim; no model switched mid-attempt.

Cross-feature native prerequisites (authoring input, projected into the sole native contract): {"T001": ["pH34r-pH/specified-development/foundation/T002"]}

- [ ] T001 Freeze the toolchain and execution policy
  Parents: none. Kind: setup. Reasoning: mechanical. Tests: declared deterministic receipt.
  Outputs: pyproject.toml, uv.lock, policies/execution.json, extensions/ph34r-contracts/scripts/ph34r_contracts/__init__.py.
  Acceptance: Pinned upstream commit/version and resolved dependency artifact hashes are recorded; Python/uv are observed; fixed-model-v3 records approved low-cost gpt-6-luna default, preserved reasoning/speed tiers and immutable historical attribution; future dispatch requires exact selected-model admission, declared capability evidence and authority acceptance.
- [ ] T002 Author independent mature-workflow template tests
  Parents: T001. Kind: test. Reasoning: bounded. Tests: TST-001, TST-002.
  Outputs: tests/test_templates.py, fixtures/mature-feature/spec.md, fixtures/mature-feature/plan.md, fixtures/mature-feature/tests.md, fixtures/mature-feature/tasks.md, fixtures/mature-feature/artifact-state.json.
  Acceptance: Golden complete-product/status fixtures are independently authored from spec/contract; stock instructions exhibit the expected MVP/tests/status mismatch; RED cause is contractual, not a broken harness.
- [ ] T003 Implement the mature lifecycle preset
  Parents: T002. Kind: implementation. Reasoning: integration. Tests: TST-001, TST-002.
  Outputs: presets/ph34r-lifecycle/preset.yml, presets/ph34r-lifecycle/templates/spec-template.md, presets/ph34r-lifecycle/templates/plan-template.md, presets/ph34r-lifecycle/templates/tests-template.md, presets/ph34r-lifecycle/templates/tasks-template.md, presets/ph34r-lifecycle/commands/speckit.specify.md, presets/ph34r-lifecycle/commands/speckit.plan.md, presets/ph34r-lifecycle/commands/speckit.tasks.md, presets/ph34r-lifecycle/commands/speckit.analyze.md, presets/ph34r-lifecycle/commands/speckit.implement.md, presets/ph34r-lifecycle/commands/speckit.taskstoissues.md, presets/ph34r-lifecycle/commands/speckit.github.taskstoissues.md, presets/ph34r-lifecycle/scripts/bash/setup-tasks.sh, presets/ph34r-lifecycle/scripts/powershell/setup-tasks.ps1.
  Acceptance: Replacement instructions describe complete mature products in past tense with separate evidence status, mandate independent tests before tasks and complete structured records, redirect both GitHub issue commands, and preserve domain constitutions; targeted GREEN uses T002 oracle unchanged.
- [ ] T004 Author artifact gate, revision and repair tests
  Parents: T001. Kind: test. Reasoning: integration. Tests: TST-003, TST-004, TST-017.
  Outputs: tests/test_gates.py, fixtures/mature-feature/revisions.json, fixtures/mature-feature/repair-packets.json.
  Acceptance: Independent missing/candidate/stale tests, changed-descendant and deduplicated repair fixtures have expected RED against absent behavior; preserved unrelated receipts are asserted.
- [ ] T005 Implement immutable authority gates and repair handoff
  Parents: T004. Kind: implementation. Reasoning: architectural. Tests: TST-003, TST-004, TST-017.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/gate.py, schemas/artifact.schema.json.
  Acceptance: Exact hash/acceptance prerequisites gate progression; history is retained, only changed contracts and descendants stale, repair packets hand off one bounded leaf to the existing owner without scheduling or model switches; targeted GREEN/regression passes.
- [ ] T006 Author metadata and traceability tests
  Parents: T001. Kind: test. Reasoning: bounded. Tests: TST-009, TST-010.
  Outputs: tests/test_metadata.py, fixtures/mature-feature/invalid-metadata.json.
  Acceptance: Every required field, missing trace, unknown parent, cycle, ambiguous scope and parallel overlap fixture has an independently specified rejection; no semantic field is synthesized by validation.
- [ ] T007 Implement structured task parsing and validation
  Parents: T005, T006. Kind: implementation. Reasoning: integration. Tests: TST-009, TST-010.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/metadata.py, schemas/task.schema.json.
  Acceptance: Single embedded metadata block matches checklist prose; full traces, command/path/budget/policy requirements and acyclic native dependencies validate; missing semantics returns earliest-authority error; no model calls.
- [ ] T008 Author native-contract projection tests
  Parents: T007. Kind: test. Reasoning: integration. Tests: TST-011, TST-012.
  Outputs: tests/test_projection.py, fixtures/native-contract-v1/execution-contract.yaml, fixtures/native-contract-v1/expected-edges.json, fixtures/kanban-v1/execution-contract.yaml, fixtures/kanban-v1/aggregate-bindings.json.
  Acceptance: Handwritten native-edge/qualified-ID goldens distinguish local T001 collisions, non-executable groups and legacy aggregate gates; missing projector has expected RED.
- [ ] T009 Implement the deterministic execution-contract projector
  Parents: T008. Kind: implementation. Reasoning: integration. Tests: TST-011, TST-012.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/projection.py.
  Acceptance: existing native-contract native fields retain meanings, extensions are namespaced, legacy aggregate bindings remain intact and ambiguous imports reject; two projections are byte-stable and have exactly the golden native edge set.
- [ ] T010 Author scope, fixed-model and receipt tests
  Parents: T007. Kind: test. Reasoning: integration. Tests: TST-015, TST-016, TST-018.
  Outputs: tests/test_receipts.py, fixtures/mature-feature/receipts.json, fixtures/mature-feature/model-observations.json.
  Acceptance: Independent selection/admission-vs-effective telemetry, advisory-vs-required-hard limits, measurement qualification, no-fallback, RED/GREEN/regression, changed hash/scope/commands and permission fixtures distinguish contractual rejection from harness error.
- [ ] T011 Implement preflight and completion receipt guards
  Parents: T010. Kind: implementation. Reasoning: architectural. Tests: TST-015, TST-016, TST-018.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/receipts.py, schemas/receipt.schema.json.
  Acceptance: One exact selected model/service admission per task, profile-specific required capability and actual permission/input/scope gates, nullable effective observations and requested/advisory parent stop plan validate; explicit hard limits fail closed without verified controls; actual acceptance predicates and unchanged-oracle regression pass; no silent fallback, false enforcement or completion side effect.
- [ ] T012 Author cache eligibility and revalidation tests
  Parents: T007. Kind: test. Reasoning: bounded. Tests: TST-020.
  Outputs: tests/test_cache.py, fixtures/mature-feature/cache-cases.json.
  Acceptance: Each authoritative/prerequisite/oracle/tool/policy/environment difference or unknown is a miss/block; the exact hit requires provenance and current acceptance rather than treating a hash as completion.
- [ ] T013 Implement scoped artifact cache validation
  Parents: T011, T012. Kind: implementation. Reasoning: bounded. Tests: TST-020.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/cache.py.
  Acceptance: Canonical key covers all contract inputs and compatibility fingerprints; valid output reuse retains origin and reruns required validation with no inference; failed/stale/secret/permission entries cannot be reused.
- [ ] T014 Author independent token-price accounting goldens
  Parents: T001. Kind: test. Reasoning: bounded. Tests: TST-021, TST-022, TST-023.
  Outputs: tests/test_cost.py, fixtures/usage/inclusive.json, fixtures/usage/exclusive-native.json, fixtures/usage/missing.json, fixtures/usage/attempts.json, fixtures/usage/rate-card.fixture.json.
  Acceptance: Exact Decimal goldens include 0.0057, incomplete 0.0056 subtotal, C0 vs unknown, exclusive-to-inclusive adapters, duplicate attempts/retries and subscription distinctions; rates are labeled synthetic and not live prices.
- [ ] T015 Implement observed token-price equivalent accounting
  Parents: T014. Kind: implementation. Reasoning: integration. Tests: TST-021, TST-022, TST-023.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/cost.py, schemas/rate-card.schema.json, schemas/usage.schema.json.
  Acceptance: Inclusive counts avoid overlap double counting, source/date/tier applicability is enforced, all unique attempts count, missing fields remain null with explicit subtotal, comparable cohorts only; no billing route or model calls.
- [ ] T016 Author pinned installation and hostile-input tests
  Parents: T003. Kind: test. Reasoning: integration. Tests: TST-006, TST-026.
  Outputs: tests/test_installation.py, fixtures/legacy-installation-a/installation-inventory.json, fixtures/legacy-native-contract/installation-inventory.json, fixtures/mature-feature/hostile-archives.json.
  Acceptance: Disposable fixtures prove stock wrong-version skipping, tamper/unknown digest, unsafe archive/catalog/path inputs and secret-sentinel rejection independently of the wrapper; expected missing-guard RED is retained.
- [ ] T017 Implement verified bootstrap and executable extension packaging
  Parents: T005, T009, T011, T013, T015, T016. Kind: implementation. Reasoning: architectural. Tests: TST-006, TST-026.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/installation.py, schemas/installation.schema.json, tools/bootstrap.py, extensions/ph34r-contracts/extension.yml, extensions/ph34r-contracts/commands/speckit.ph34r.tests.md, extensions/ph34r-contracts/commands/speckit.ph34r.validate.md, extensions/ph34r-contracts/commands/speckit.ph34r.project.md, extensions/ph34r-contracts/commands/speckit.ph34r.verify.md, extensions/ph34r-contracts/commands/speckit.ph34r.cost.md, extensions/ph34r-contracts/commands/speckit.ph34r.regenerate.md.
  Acceptance: Approved source digests and manifest identities are verified before extraction/mutation; upstream primitive install is reused, independent ownership conflicts reject, active generated assets are checked; six namespaced command paths resolve; no credential/model inference from deterministic verbs.
- [ ] T018 Author staged upgrade and interruption recovery tests
  Parents: T017. Kind: test. Reasoning: integration. Tests: TST-008.
  Outputs: tests/test_upgrade.py, fixtures/mature-feature/upgrade-journal.json.
  Acceptance: Failure injection covers every declared stage/promotion boundary; independent before-byte/mode/sentinel inventory defines recovery; failed replacement cannot be reported as rollback success.
- [ ] T019 Implement staged upgrade, journaled promotion and rollback
  Parents: T018. Kind: implementation. Reasoning: architectural. Tests: TST-008, TST-026.
  Outputs: tools/stage_upgrade.py, tools/promote_upgrade.py, tools/rollback_upgrade.py.
  Acceptance: Stage operates outside consumer root, before-hash compare-and-swap detects concurrent edits, verified rollback artifacts/journal restore exact prior managed bytes/modes and sentinels; newly introduced installation files only reconciled from journal; application code/history preserved.
- [ ] T020 Author issue projection authorization and crash tests
  Parents: T009. Kind: test. Reasoning: integration. Tests: TST-013, TST-014.
  Outputs: tests/test_issues.py, fixtures/github/pages.json, fixtures/github/partial-projection.json, fixtures/github/creator-policy.json.
  Acceptance: Fake paginated issue/native-edge API covers >100 items, numeric IDs, duplicate markers/extra edges, user vs App creator, permissions/wrong target and partial replay; default dry plan makes zero mutations.
- [ ] T021 Implement idempotent native GitHub issue operations
  Parents: T011, T020. Kind: implementation. Reasoning: architectural. Tests: TST-013, TST-014.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/issues.py, schemas/issue-binding.schema.json.
  Acceptance: Plan/apply preserves 1:1 leaf identity and exact native edges; complete remote readback precedes readiness, creator/target/permission/drift gates fail closed, partial replay converges without duplicates, grouping creates no scheduler dependency; no existing executor workflow change.
- [ ] T022 Author existing-installation and execution-owner compatibility tests
  Parents: T017. Kind: test. Reasoning: integration. Tests: TST-007, TST-024.
  Outputs: tests/test_compatibility.py, fixtures/legacy-installation-a/local-authority.json, fixtures/legacy-native-contract/local-authority.json, fixtures/github/existing-executor-capability.json.
  Acceptance: Sanitized observed installations/authority histories, Claude/Codex active/inactive assets, existing executor creator/allowlist/selected-model admission and capability profiles alongside native execution semantics are exercised; incompatibility is an explicit block rather than synthetic support.
- [ ] T023 Implement compatibility policy and checks
  Parents: T019, T021, T022. Kind: implementation. Reasoning: integration. Tests: TST-007, TST-024.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/compatibility.py, policies/compatibility.json.
  Acceptance: Both materialized installations and active integration transitions preserve local domain constitutions/history; existing owner contracts are supported only at positively qualified versions; existing executor limitations and existing infrastructure ownership ownership remain unchanged.
- [ ] T024 Author regeneration oracle and frozen generation instructions
  Parents: T005, T011. Kind: test. Reasoning: architectural. Tests: TST-005, TST-019.
  Outputs: tests/test_regeneration.py, fixtures/regeneration/input-inventory.json, fixtures/regeneration/expected-behavior.json, generation/instructions.md, generation/packet.schema.json.
  Acceptance: Independent gate behavior oracle covers the declared gate.py interface; retained implementation exclusion, missing input inventory, two trial identity and failed-trial retention rules are defined; generation instructions freeze approved inputs/model/runtime and no new agent runner.
- [ ] T025 Implement scoped regeneration evidence verification
  Parents: T024. Kind: implementation. Reasoning: integration. Tests: TST-005, TST-019.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/regeneration.py, schemas/regeneration.schema.json.
  Acceptance: Verifier accepts only the complete allowlisted-input evidence, two independent clean workspaces, fixed exact selection/admission and profile-required evidence, with any missing measurements explicitly unqualified and passing independent behavior/regression receipts; all attempts retained and claims limited to gate.py; it launches no model and deletes no code.
- [ ] T026 Author upstream manifest, packaging and release-lock tests
  Parents: T017. Kind: test. Reasoning: integration. Tests: TST-027.
  Outputs: tests/test_release.py, fixtures/mature-feature/release-cases.json.
  Acceptance: Actual upstream-native validators and source fixtures test exact component versions/IDs, supplied-file paths, source digests, positive reference resolution and identical-source packaging; offline/unreachable warning is insufficient for release.
- [ ] T027 Implement local bundle build and release integrity tooling
  Parents: T023, T025, T026. Kind: implementation. Reasoning: integration. Tests: TST-027.
  Outputs: bundles/ph34r-standard/bundle.yml, bundles/ph34r-standard/README.md, catalogs/presets.json, catalogs/extensions.json, catalogs/bundles.json, tools/build_release.py, release-lock.json, assets-manifest.json.
  Acceptance: Candidate-local build pins actual component/dependency/upstream/archive/asset digests and positively resolves local sources; deterministic package output is reproducible; unpublished destination URLs cannot be fabricated or marked release-ready; full online publication remains gated.
- [ ] T028 Author documented CLI behavior and no-model tests
  Parents: T007, T009, T011, T013, T015, T017, T021, T023, T025. Kind: test. Reasoning: bounded. Tests: TST-028.
  Outputs: tests/test_cli.py, fixtures/mature-feature/cli-cases.json.
  Acceptance: Every documented verb/exit class rejects missing/stale authority and shell-like untrusted command input; instrumented model/mutation adapter proves deterministic verbs do not invoke inference or unintended writes.
- [ ] T029 Integrate the deterministic CLI entry point
  Parents: T027, T028. Kind: implementation. Reasoning: integration. Tests: TST-028.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/cli.py.
  Acceptance: All contract verbs delegate to approved guards/projectors, emit bounded typed results, preserve default-dry semantics and shell-free named argv execution; CLI suite and full focused regression pass with no model calls.
- [ ] T030 Author complete isolated pilot test
  Parents: T029. Kind: test. Reasoning: integration. Tests: TST-025.
  Outputs: tests/test_pilot.py, fixtures/mature-feature/pilot-expectations.json.
  Acceptance: Oracle exercises complete mature chain, revision rejection, dry issue plan, missing selected-model admission/profile policy, cache/cost, staged failure recovery and adoption gate states in an isolated first legacy installation installation; absent proof never becomes delivery.
- [ ] T031 Qualify the complete deterministic pilot in disposable copies
  Parents: T030. Kind: qualification. Reasoning: mechanical. Tests: TST-007, TST-023, TST-024, TST-025.
  Outputs: evidence/pilot/receipts.json, evidence/pilot/input-inventory.json, evidence/pilot/compatibility.json.
  Acceptance: Synthetic feature and isolated sanitized first legacy installation copy pass all deterministic compatibility/recovery/lifecycle checks with zero model/external writes; E3 regeneration and publication/model activation remain accurately pending until separate prerequisites pass.
- [ ] T032 Prove two scoped behavioral regeneration trials
  Parents: T025, T031. Kind: qualification. Reasoning: architectural. Tests: TST-019.
  Outputs: evidence/regeneration/trials.json, evidence/regeneration/run-1/gate.py, evidence/regeneration/run-2/gate.py, evidence/regeneration/receipts.json.
  Acceptance: After confirmed available model binding and authorized inference, two independent clean source-excluded generation trials pass the unchanged gate behavior/regression oracle; observations, all failures/costs/input fingerprints retained; no deletion or broader disposability claim.
- [ ] T033 Review independent oracle and cross-artifact boundaries
  Parents: T031, T032. Kind: review. Reasoning: architectural. Tests: TST-001, TST-002, TST-009, TST-012, TST-014, TST-016, TST-019, TST-022, TST-026.
  Outputs: evidence/review.json.
  Acceptance: Independent review validates complete-product intent, oracle provenance, contract/identity/native edges, fixed-model/permission enforcement, rollback and billing/regeneration claim limits; verdict cites current inputs and actual receipts rather than substituting for human artifact acceptance.
- [ ] T034 Write repository adoption and operator handoff documentation
  Parents: T023, T031. Kind: documentation. Reasoning: integration. Tests: TST-024, TST-025.
  Outputs: build/distribution/accepted/operator-handoff/ownership.md, build/distribution/accepted/operator-handoff/migration.md, build/distribution/accepted/operator-handoff/operator.md, build/distribution/accepted/operator-handoff/regeneration.md, build/distribution/accepted/operator-handoff/release.md.
  Acceptance: Existing canonical ownership/rollout/generation contracts compiled into owner-scoped adoption/operator handoff; local authority/model/runtime/upgrade/rollback/cost/regeneration/publication gates remained explicit. Missing behavior created a separate spec repair, never invented documentation authority; no consumer/executor change.
- [ ] T035 Assemble verified local release-candidate evidence
  Parents: T027, T029, T033, T034. Kind: qualification. Reasoning: mechanical. Tests: TST-025, TST-027.
  Outputs: evidence/release-candidate.json, evidence/release-manifest.sha256.
  Acceptance: Clean-source candidate build and exact component/generated-asset/digest/reference matrix, complete pilot/two regeneration/review receipts and rollback proof are present; public destination/license and mutation authorization are separate explicit states, never invented or bypassed.
- [ ] T036 Emit gated rollout handoff and identity bindings
  Parents: T035. Kind: handoff. Reasoning: mechanical. Tests: TST-014, TST-024, TST-025.
  Outputs: policies/rollout.json, evidence/rollout-handoff.json, evidence/issue-bindings.json.
  Acceptance: Every repository and execution owner has explicit candidate/accepted/blocked adoption state and proof refs; dry identities preserve 1:1 leaves with null remote IDs; all actual repository/issue/publication/deployment mutations wait for their authorized owner and qualified runtime policy.

## Structured semantic metadata

```task-metadata
{
  "metadata_schema": "ph34r-task-authoring-v1",
  "namespace": "pH34r-pH/spec-kit-distribution/001-reusable-distribution",
  "artifact_acceptance": "candidate-review",
  "dispatchable": false,
  "execution_owner": "unbound-existing-owner",
  "model_policy_revision": "fixed-model-v3",
  "external_native_parents": {
    "T001": [
      "pH34r-pH/specified-development/foundation/T002"
    ]
  },
  "commands": {
    "C_TEMPLATES": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_templates",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_GATES": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_gates",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_METADATA": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_metadata",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_PROJECTION": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_projection",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_RECEIPTS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_receipts",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_CACHE": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_cache",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_COST": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_cost",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_INSTALL": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_installation",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_UPGRADE": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_upgrade",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_ISSUES": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_issues",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_COMPAT": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_compatibility",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_REGEN_CONTRACT": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_regeneration",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_RELEASE": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_release",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_CLI": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_cli",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_PILOT": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_pilot",
        "-v"
      ],
      "expect": "declared expected RED for test-authoring; GREEN for implementation/qualification"
    },
    "C_ENV": {
      "cwd": ".",
      "argv": [
        "python",
        "--version"
      ],
      "expect": "observed Python 3.12 and separately recorded uv/runtime/upstream fingerprint"
    },
    "C_LOCK": {
      "cwd": ".",
      "argv": [
        "uv",
        "sync",
        "--frozen"
      ],
      "expect": "exact resolved lock; no runtime/model/provider fallback"
    },
    "C_ALL": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-v"
      ],
      "expect": "all required behavioral/regression tests pass; E3 gate explicitly accounted"
    },
    "C_BUILD": {
      "cwd": ".",
      "argv": [
        "python",
        "tools/build_release.py",
        "--mode",
        "candidate-local"
      ],
      "expect": "local verified candidate only; no publish/install into consumers"
    },
    "C_REGEN_VERIFY": {
      "cwd": ".",
      "argv": [
        "ph34r-spec",
        "regeneration",
        "verify",
        "--trial",
        "evidence/regeneration/trials.json",
        "--contract",
        "specs/001-reusable-distribution/execution-contract.yaml"
      ],
      "expect": "two real independently isolated fixed-model trials satisfy unchanged behavioral oracle"
    }
  },
  "tasks": [
    {
      "local_id": "T001",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T001",
      "title": "Freeze the toolchain and execution policy",
      "kind": "setup",
      "story": "US2",
      "goal": "Pinned upstream commit/version and resolved dependency artifact hashes are recorded; Python/uv are observed; fixed-model-v3 records approved low-cost gpt-6-luna default, preserved reasoning/speed tiers and immutable historical attribution; future dispatch requires exact selected-model admission, declared capability evidence and authority acceptance.",
      "parents": [],
      "tests": [],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "pyproject.toml",
        "uv.lock",
        "policies/execution.json",
        "extensions/ph34r-contracts/scripts/ph34r_contracts/__init__.py"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ENV",
        "C_LOCK"
      ],
      "acceptance": "Pinned upstream commit/version and resolved dependency artifact hashes are recorded; Python/uv are observed; fixed-model-v3 records approved low-cost gpt-6-luna default, preserved reasoning/speed tiers and immutable historical attribution; future dispatch requires exact selected-model admission, declared capability evidence and authority acceptance.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "mechanical",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-reasoning-tier-and-rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "record supported effective runtime setting; unsupported requirement blocks; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "zero inference calls"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T001 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt"
    },
    {
      "local_id": "T002",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T002",
      "title": "Author independent mature-workflow template tests",
      "kind": "test",
      "story": "US1",
      "goal": "Golden complete-product/status fixtures are independently authored from spec/contract; stock instructions exhibit the expected MVP/tests/status mismatch; RED cause is contractual, not a broken harness.",
      "parents": [
        "T001"
      ],
      "tests": [
        "TST-001",
        "TST-002"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_templates.py",
        "fixtures/mature-feature/spec.md",
        "fixtures/mature-feature/plan.md",
        "fixtures/mature-feature/tests.md",
        "fixtures/mature-feature/tasks.md",
        "fixtures/mature-feature/artifact-state.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_TEMPLATES"
      ],
      "acceptance": "Golden complete-product/status fixtures are independently authored from spec/contract; stock instructions exhibit the expected MVP/tests/status mismatch; RED cause is contractual, not a broken harness.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T002 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T003",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T003",
      "title": "Implement the mature lifecycle preset",
      "kind": "implementation",
      "story": "US1",
      "goal": "Replacement instructions describe complete mature products in past tense with separate evidence status, mandate independent tests before tasks and complete structured records, redirect both GitHub issue commands, and preserve domain constitutions; targeted GREEN uses T002 oracle unchanged.",
      "parents": [
        "T002"
      ],
      "tests": [
        "TST-001",
        "TST-002"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "presets/ph34r-lifecycle/preset.yml",
        "presets/ph34r-lifecycle/templates/spec-template.md",
        "presets/ph34r-lifecycle/templates/plan-template.md",
        "presets/ph34r-lifecycle/templates/tests-template.md",
        "presets/ph34r-lifecycle/templates/tasks-template.md",
        "presets/ph34r-lifecycle/commands/speckit.specify.md",
        "presets/ph34r-lifecycle/commands/speckit.plan.md",
        "presets/ph34r-lifecycle/commands/speckit.tasks.md",
        "presets/ph34r-lifecycle/commands/speckit.analyze.md",
        "presets/ph34r-lifecycle/commands/speckit.implement.md",
        "presets/ph34r-lifecycle/commands/speckit.taskstoissues.md",
        "presets/ph34r-lifecycle/commands/speckit.github.taskstoissues.md",
        "presets/ph34r-lifecycle/scripts/bash/setup-tasks.sh",
        "presets/ph34r-lifecycle/scripts/powershell/setup-tasks.ps1"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_TEMPLATES"
      ],
      "acceptance": "Replacement instructions describe complete mature products in past tense with separate evidence status, mandate independent tests before tasks and complete structured records, redirect both GitHub issue commands, and preserve domain constitutions; targeted GREEN uses T002 oracle unchanged.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T003 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T004",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T004",
      "title": "Author artifact gate, revision and repair tests",
      "kind": "test",
      "story": "US3",
      "goal": "Independent missing/candidate/stale tests, changed-descendant and deduplicated repair fixtures have expected RED against absent behavior; preserved unrelated receipts are asserted.",
      "parents": [
        "T001"
      ],
      "tests": [
        "TST-003",
        "TST-004",
        "TST-017"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_gates.py",
        "fixtures/mature-feature/revisions.json",
        "fixtures/mature-feature/repair-packets.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_GATES"
      ],
      "acceptance": "Independent missing/candidate/stale tests, changed-descendant and deduplicated repair fixtures have expected RED against absent behavior; preserved unrelated receipts are asserted.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T004 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T005",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T005",
      "title": "Implement immutable authority gates and repair handoff",
      "kind": "implementation",
      "story": "US3",
      "goal": "Exact hash/acceptance prerequisites gate progression; history is retained, only changed contracts and descendants stale, repair packets hand off one bounded leaf to the existing owner without scheduling or model switches; targeted GREEN/regression passes.",
      "parents": [
        "T004"
      ],
      "tests": [
        "TST-003",
        "TST-004",
        "TST-017"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/gate.py",
        "schemas/artifact.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_GATES"
      ],
      "acceptance": "Exact hash/acceptance prerequisites gate progression; history is retained, only changed contracts and descendants stale, repair packets hand off one bounded leaf to the existing owner without scheduling or model switches; targeted GREEN/regression passes.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T005 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T006",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T006",
      "title": "Author metadata and traceability tests",
      "kind": "test",
      "story": "US3",
      "goal": "Every required field, missing trace, unknown parent, cycle, ambiguous scope and parallel overlap fixture has an independently specified rejection; no semantic field is synthesized by validation.",
      "parents": [
        "T001"
      ],
      "tests": [
        "TST-009",
        "TST-010"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_metadata.py",
        "fixtures/mature-feature/invalid-metadata.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_METADATA"
      ],
      "acceptance": "Every required field, missing trace, unknown parent, cycle, ambiguous scope and parallel overlap fixture has an independently specified rejection; no semantic field is synthesized by validation.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T006 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T007",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T007",
      "title": "Implement structured task parsing and validation",
      "kind": "implementation",
      "story": "US3",
      "goal": "Single embedded metadata block matches checklist prose; full traces, command/path/budget/policy requirements and acyclic native dependencies validate; missing semantics returns earliest-authority error; no model calls.",
      "parents": [
        "T005",
        "T006"
      ],
      "tests": [
        "TST-009",
        "TST-010"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/metadata.py",
        "schemas/task.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_METADATA",
        "C_GATES"
      ],
      "acceptance": "Single embedded metadata block matches checklist prose; full traces, command/path/budget/policy requirements and acyclic native dependencies validate; missing semantics returns earliest-authority error; no model calls.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T007 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T008",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T008",
      "title": "Author native-contract projection tests",
      "kind": "test",
      "story": "US4",
      "goal": "Handwritten native-edge/qualified-ID goldens distinguish local T001 collisions, non-executable groups and legacy aggregate gates; missing projector has expected RED.",
      "parents": [
        "T007"
      ],
      "tests": [
        "TST-011",
        "TST-012"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_projection.py",
        "fixtures/native-contract-v1/execution-contract.yaml",
        "fixtures/native-contract-v1/expected-edges.json",
        "fixtures/kanban-v1/execution-contract.yaml",
        "fixtures/kanban-v1/aggregate-bindings.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_PROJECTION"
      ],
      "acceptance": "Handwritten native-edge/qualified-ID goldens distinguish local T001 collisions, non-executable groups and legacy aggregate gates; missing projector has expected RED.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T008 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T009",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T009",
      "title": "Implement the deterministic execution-contract projector",
      "kind": "implementation",
      "story": "US4",
      "goal": "existing native-contract native fields retain meanings, extensions are namespaced, legacy aggregate bindings remain intact and ambiguous imports reject; two projections are byte-stable and have exactly the golden native edge set.",
      "parents": [
        "T008"
      ],
      "tests": [
        "TST-011",
        "TST-012"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/projection.py"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_PROJECTION",
        "C_METADATA"
      ],
      "acceptance": "existing native-contract native fields retain meanings, extensions are namespaced, legacy aggregate bindings remain intact and ambiguous imports reject; two projections are byte-stable and have exactly the golden native edge set.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T009 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T010",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T010",
      "title": "Author scope, fixed-model and receipt tests",
      "kind": "test",
      "story": "US5",
      "goal": "Independent selection/admission-vs-effective telemetry, advisory-vs-required-hard limits, measurement qualification, no-fallback, RED/GREEN/regression, changed hash/scope/commands and permission fixtures distinguish contractual rejection from harness error.",
      "parents": [
        "T007"
      ],
      "tests": [
        "TST-015",
        "TST-016",
        "TST-018"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_receipts.py",
        "fixtures/mature-feature/receipts.json",
        "fixtures/mature-feature/model-observations.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_RECEIPTS"
      ],
      "acceptance": "Independent selection/admission-vs-effective telemetry, advisory-vs-required-hard limits, measurement qualification, no-fallback, RED/GREEN/regression, changed hash/scope/commands and permission fixtures distinguish contractual rejection from harness error.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T010 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T011",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T011",
      "title": "Implement preflight and completion receipt guards",
      "kind": "implementation",
      "story": "US5",
      "goal": "One exact selected model/service admission per task, profile-specific required capability and actual permission/input/scope gates, nullable effective observations and requested/advisory parent stop plan validate; explicit hard limits fail closed without verified controls; actual acceptance predicates and unchanged-oracle regression pass; no silent fallback, false enforcement or completion side effect.",
      "parents": [
        "T010"
      ],
      "tests": [
        "TST-015",
        "TST-016",
        "TST-018"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/receipts.py",
        "schemas/receipt.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_RECEIPTS",
        "C_GATES"
      ],
      "acceptance": "One exact selected model/service admission per task, profile-specific required capability and actual permission/input/scope gates, nullable effective observations and requested/advisory parent stop plan validate; explicit hard limits fail closed without verified controls; actual acceptance predicates and unchanged-oracle regression pass; no silent fallback, false enforcement or completion side effect.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T011 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T012",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T012",
      "title": "Author cache eligibility and revalidation tests",
      "kind": "test",
      "story": "US6",
      "goal": "Each authoritative/prerequisite/oracle/tool/policy/environment difference or unknown is a miss/block; the exact hit requires provenance and current acceptance rather than treating a hash as completion.",
      "parents": [
        "T007"
      ],
      "tests": [
        "TST-020"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_cache.py",
        "fixtures/mature-feature/cache-cases.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_CACHE"
      ],
      "acceptance": "Each authoritative/prerequisite/oracle/tool/policy/environment difference or unknown is a miss/block; the exact hit requires provenance and current acceptance rather than treating a hash as completion.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T012 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T013",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T013",
      "title": "Implement scoped artifact cache validation",
      "kind": "implementation",
      "story": "US6",
      "goal": "Canonical key covers all contract inputs and compatibility fingerprints; valid output reuse retains origin and reruns required validation with no inference; failed/stale/secret/permission entries cannot be reused.",
      "parents": [
        "T011",
        "T012"
      ],
      "tests": [
        "TST-020"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/cache.py"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_CACHE",
        "C_RECEIPTS"
      ],
      "acceptance": "Canonical key covers all contract inputs and compatibility fingerprints; valid output reuse retains origin and reruns required validation with no inference; failed/stale/secret/permission entries cannot be reused.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T013 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T014",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T014",
      "title": "Author independent token-price accounting goldens",
      "kind": "test",
      "story": "US6",
      "goal": "Exact Decimal goldens include 0.0057, incomplete 0.0056 subtotal, C0 vs unknown, exclusive-to-inclusive adapters, duplicate attempts/retries and subscription distinctions; rates are labeled synthetic and not live prices.",
      "parents": [
        "T001"
      ],
      "tests": [
        "TST-021",
        "TST-022",
        "TST-023"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_cost.py",
        "fixtures/usage/inclusive.json",
        "fixtures/usage/exclusive-native.json",
        "fixtures/usage/missing.json",
        "fixtures/usage/attempts.json",
        "fixtures/usage/rate-card.fixture.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_COST"
      ],
      "acceptance": "Exact Decimal goldens include 0.0057, incomplete 0.0056 subtotal, C0 vs unknown, exclusive-to-inclusive adapters, duplicate attempts/retries and subscription distinctions; rates are labeled synthetic and not live prices.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T014 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T015",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T015",
      "title": "Implement observed token-price equivalent accounting",
      "kind": "implementation",
      "story": "US6",
      "goal": "Inclusive counts avoid overlap double counting, source/date/tier applicability is enforced, all unique attempts count, missing fields remain null with explicit subtotal, comparable cohorts only; no billing route or model calls.",
      "parents": [
        "T014"
      ],
      "tests": [
        "TST-021",
        "TST-022",
        "TST-023"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/cost.py",
        "schemas/rate-card.schema.json",
        "schemas/usage.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_COST"
      ],
      "acceptance": "Inclusive counts avoid overlap double counting, source/date/tier applicability is enforced, all unique attempts count, missing fields remain null with explicit subtotal, comparable cohorts only; no billing route or model calls.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T015 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T016",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T016",
      "title": "Author pinned installation and hostile-input tests",
      "kind": "test",
      "story": "US2",
      "goal": "Disposable fixtures prove stock wrong-version skipping, tamper/unknown digest, unsafe archive/catalog/path inputs and secret-sentinel rejection independently of the wrapper; expected missing-guard RED is retained.",
      "parents": [
        "T003"
      ],
      "tests": [
        "TST-006",
        "TST-026"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_installation.py",
        "fixtures/legacy-installation-a/installation-inventory.json",
        "fixtures/legacy-native-contract/installation-inventory.json",
        "fixtures/mature-feature/hostile-archives.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_INSTALL"
      ],
      "acceptance": "Disposable fixtures prove stock wrong-version skipping, tamper/unknown digest, unsafe archive/catalog/path inputs and secret-sentinel rejection independently of the wrapper; expected missing-guard RED is retained.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T016 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T017",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T017",
      "title": "Implement verified bootstrap and executable extension packaging",
      "kind": "implementation",
      "story": "US2",
      "goal": "Approved source digests and manifest identities are verified before extraction/mutation; upstream primitive install is reused, independent ownership conflicts reject, active generated assets are checked; six namespaced command paths resolve; no credential/model inference from deterministic verbs.",
      "parents": [
        "T005",
        "T009",
        "T011",
        "T013",
        "T015",
        "T016"
      ],
      "tests": [
        "TST-006",
        "TST-026"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/installation.py",
        "schemas/installation.schema.json",
        "tools/bootstrap.py",
        "extensions/ph34r-contracts/extension.yml",
        "extensions/ph34r-contracts/commands/speckit.ph34r.tests.md",
        "extensions/ph34r-contracts/commands/speckit.ph34r.validate.md",
        "extensions/ph34r-contracts/commands/speckit.ph34r.project.md",
        "extensions/ph34r-contracts/commands/speckit.ph34r.verify.md",
        "extensions/ph34r-contracts/commands/speckit.ph34r.cost.md",
        "extensions/ph34r-contracts/commands/speckit.ph34r.regenerate.md"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_INSTALL",
        "C_TEMPLATES"
      ],
      "acceptance": "Approved source digests and manifest identities are verified before extraction/mutation; upstream primitive install is reused, independent ownership conflicts reject, active generated assets are checked; six namespaced command paths resolve; no credential/model inference from deterministic verbs.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T017 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T018",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T018",
      "title": "Author staged upgrade and interruption recovery tests",
      "kind": "test",
      "story": "US2",
      "goal": "Failure injection covers every declared stage/promotion boundary; independent before-byte/mode/sentinel inventory defines recovery; failed replacement cannot be reported as rollback success.",
      "parents": [
        "T017"
      ],
      "tests": [
        "TST-008"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_upgrade.py",
        "fixtures/mature-feature/upgrade-journal.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_UPGRADE"
      ],
      "acceptance": "Failure injection covers every declared stage/promotion boundary; independent before-byte/mode/sentinel inventory defines recovery; failed replacement cannot be reported as rollback success.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T018 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T019",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T019",
      "title": "Implement staged upgrade, journaled promotion and rollback",
      "kind": "implementation",
      "story": "US2",
      "goal": "Stage operates outside consumer root, before-hash compare-and-swap detects concurrent edits, verified rollback artifacts/journal restore exact prior managed bytes/modes and sentinels; newly introduced installation files only reconciled from journal; application code/history preserved.",
      "parents": [
        "T018"
      ],
      "tests": [
        "TST-008",
        "TST-026"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tools/stage_upgrade.py",
        "tools/promote_upgrade.py",
        "tools/rollback_upgrade.py"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_UPGRADE",
        "C_INSTALL"
      ],
      "acceptance": "Stage operates outside consumer root, before-hash compare-and-swap detects concurrent edits, verified rollback artifacts/journal restore exact prior managed bytes/modes and sentinels; newly introduced installation files only reconciled from journal; application code/history preserved.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T019 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T020",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T020",
      "title": "Author issue projection authorization and crash tests",
      "kind": "test",
      "story": "US4",
      "goal": "Fake paginated issue/native-edge API covers >100 items, numeric IDs, duplicate markers/extra edges, user vs App creator, permissions/wrong target and partial replay; default dry plan makes zero mutations.",
      "parents": [
        "T009"
      ],
      "tests": [
        "TST-013",
        "TST-014"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_issues.py",
        "fixtures/github/pages.json",
        "fixtures/github/partial-projection.json",
        "fixtures/github/creator-policy.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ISSUES"
      ],
      "acceptance": "Fake paginated issue/native-edge API covers >100 items, numeric IDs, duplicate markers/extra edges, user vs App creator, permissions/wrong target and partial replay; default dry plan makes zero mutations.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T020 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T021",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T021",
      "title": "Implement idempotent native GitHub issue operations",
      "kind": "implementation",
      "story": "US4",
      "goal": "Plan/apply preserves 1:1 leaf identity and exact native edges; complete remote readback precedes readiness, creator/target/permission/drift gates fail closed, partial replay converges without duplicates, grouping creates no scheduler dependency; no existing executor workflow change.",
      "parents": [
        "T011",
        "T020"
      ],
      "tests": [
        "TST-013",
        "TST-014"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/issues.py",
        "schemas/issue-binding.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ISSUES",
        "C_PROJECTION",
        "C_RECEIPTS"
      ],
      "acceptance": "Plan/apply preserves 1:1 leaf identity and exact native edges; complete remote readback precedes readiness, creator/target/permission/drift gates fail closed, partial replay converges without duplicates, grouping creates no scheduler dependency; no existing executor workflow change.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T021 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T022",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T022",
      "title": "Author existing-installation and execution-owner compatibility tests",
      "kind": "test",
      "story": "US2",
      "goal": "Sanitized observed installations/authority histories, Claude/Codex active/inactive assets, existing executor creator/allowlist/selected-model admission and capability profiles alongside native execution semantics are exercised; incompatibility is an explicit block rather than synthetic support.",
      "parents": [
        "T017"
      ],
      "tests": [
        "TST-007",
        "TST-024"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_compatibility.py",
        "fixtures/legacy-installation-a/local-authority.json",
        "fixtures/legacy-native-contract/local-authority.json",
        "fixtures/github/existing-executor-capability.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_COMPAT"
      ],
      "acceptance": "Sanitized observed installations/authority histories, Claude/Codex active/inactive assets, existing executor creator/allowlist/selected-model admission and capability profiles alongside native execution semantics are exercised; incompatibility is an explicit block rather than synthetic support.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T022 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T023",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T023",
      "title": "Implement compatibility policy and checks",
      "kind": "implementation",
      "story": "US2",
      "goal": "Both materialized installations and active integration transitions preserve local domain constitutions/history; existing owner contracts are supported only at positively qualified versions; existing executor limitations and separately owned infrastructure changes ownership remain unchanged.",
      "parents": [
        "T019",
        "T021",
        "T022"
      ],
      "tests": [
        "TST-007",
        "TST-024"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/compatibility.py",
        "policies/compatibility.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_COMPAT",
        "C_INSTALL",
        "C_PROJECTION"
      ],
      "acceptance": "Both materialized installations and active integration transitions preserve local domain constitutions/history; existing owner contracts are supported only at positively qualified versions; existing executor limitations and existing infrastructure ownership ownership remain unchanged.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T023 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T024",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T024",
      "title": "Author regeneration oracle and frozen generation instructions",
      "kind": "test",
      "story": "US6",
      "goal": "Independent gate behavior oracle covers the declared gate.py interface; retained implementation exclusion, missing input inventory, two trial identity and failed-trial retention rules are defined; generation instructions freeze approved inputs/model/runtime and no new agent runner.",
      "parents": [
        "T005",
        "T011"
      ],
      "tests": [
        "TST-005",
        "TST-019"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_regeneration.py",
        "fixtures/regeneration/input-inventory.json",
        "fixtures/regeneration/expected-behavior.json",
        "generation/instructions.md",
        "generation/packet.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_REGEN_CONTRACT"
      ],
      "acceptance": "Independent gate behavior oracle covers the declared gate.py interface; retained implementation exclusion, missing input inventory, two trial identity and failed-trial retention rules are defined; generation instructions freeze approved inputs/model/runtime and no new agent runner.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T024 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T025",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T025",
      "title": "Implement scoped regeneration evidence verification",
      "kind": "implementation",
      "story": "US6",
      "goal": "Verifier accepts only the complete allowlisted-input evidence, two independent clean workspaces, fixed exact selection/admission and profile-required evidence, with any missing measurements explicitly unqualified and passing independent behavior/regression receipts; all attempts retained and claims limited to gate.py; it launches no model and deletes no code.",
      "parents": [
        "T024"
      ],
      "tests": [
        "TST-005",
        "TST-019"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/regeneration.py",
        "schemas/regeneration.schema.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_REGEN_CONTRACT",
        "C_GATES",
        "C_RECEIPTS"
      ],
      "acceptance": "Verifier accepts only the complete allowlisted-input evidence, two independent clean workspaces, fixed exact selection/admission and profile-required evidence, with any missing measurements explicitly unqualified and passing independent behavior/regression receipts; all attempts retained and claims limited to gate.py; it launches no model and deletes no code.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T025 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T026",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T026",
      "title": "Author upstream manifest, packaging and release-lock tests",
      "kind": "test",
      "story": "US2",
      "goal": "Actual upstream-native validators and source fixtures test exact component versions/IDs, supplied-file paths, source digests, positive reference resolution and identical-source packaging; offline/unreachable warning is insufficient for release.",
      "parents": [
        "T017"
      ],
      "tests": [
        "TST-027"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_release.py",
        "fixtures/mature-feature/release-cases.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_RELEASE"
      ],
      "acceptance": "Actual upstream-native validators and source fixtures test exact component versions/IDs, supplied-file paths, source digests, positive reference resolution and identical-source packaging; offline/unreachable warning is insufficient for release.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T026 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T027",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T027",
      "title": "Implement local bundle build and release integrity tooling",
      "kind": "implementation",
      "story": "US2",
      "goal": "Candidate-local build pins actual component/dependency/upstream/archive/asset digests and positively resolves local sources; deterministic package output is reproducible; unpublished destination URLs cannot be fabricated or marked release-ready; full online publication remains gated.",
      "parents": [
        "T023",
        "T025",
        "T026"
      ],
      "tests": [
        "TST-027"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "bundles/ph34r-standard/bundle.yml",
        "bundles/ph34r-standard/README.md",
        "catalogs/presets.json",
        "catalogs/extensions.json",
        "catalogs/bundles.json",
        "tools/build_release.py",
        "release-lock.json",
        "assets-manifest.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_RELEASE",
        "C_BUILD"
      ],
      "acceptance": "Candidate-local build pins actual component/dependency/upstream/archive/asset digests and positively resolves local sources; deterministic package output is reproducible; unpublished destination URLs cannot be fabricated or marked release-ready; full online publication remains gated.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T027 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T028",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T028",
      "title": "Author documented CLI behavior and no-model tests",
      "kind": "test",
      "story": "US4",
      "goal": "Every documented verb/exit class rejects missing/stale authority and shell-like untrusted command input; instrumented model/mutation adapter proves deterministic verbs do not invoke inference or unintended writes.",
      "parents": [
        "T007",
        "T009",
        "T011",
        "T013",
        "T015",
        "T017",
        "T021",
        "T023",
        "T025"
      ],
      "tests": [
        "TST-028"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_cli.py",
        "fixtures/mature-feature/cli-cases.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_CLI"
      ],
      "acceptance": "Every documented verb/exit class rejects missing/stale authority and shell-like untrusted command input; instrumented model/mutation adapter proves deterministic verbs do not invoke inference or unintended writes.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "bounded",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 8192,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T028 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T029",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T029",
      "title": "Integrate the deterministic CLI entry point",
      "kind": "implementation",
      "story": "US4",
      "goal": "All contract verbs delegate to approved guards/projectors, emit bounded typed results, preserve default-dry semantics and shell-free named argv execution; CLI suite and full focused regression pass with no model calls.",
      "parents": [
        "T027",
        "T028"
      ],
      "tests": [
        "TST-028"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/cli.py"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_CLI",
        "C_ALL"
      ],
      "acceptance": "All contract verbs delegate to approved guards/projectors, emit bounded typed results, preserve default-dry semantics and shell-free named argv execution; CLI suite and full focused regression pass with no model calls.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "GREEN",
        "focused_regression"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T029 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T030",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T030",
      "title": "Author complete isolated pilot test",
      "kind": "test",
      "story": "US6",
      "goal": "Oracle exercises complete mature chain, revision rejection, dry issue plan, missing selected-model admission/profile policy, cache/cost, staged failure recovery and adoption gate states in an isolated first legacy installation installation; absent proof never becomes delivery.",
      "parents": [
        "T029"
      ],
      "tests": [
        "TST-025"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_pilot.py",
        "fixtures/mature-feature/pilot-expectations.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_PILOT"
      ],
      "acceptance": "Oracle exercises complete mature chain, revision rejection, dry issue plan, missing selected-model admission/profile policy, cache/cost, staged failure recovery and adoption gate states in an isolated first legacy installation installation; absent proof never becomes delivery.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "expected_missing_behavior_RED"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T030 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "expected-contractual-RED",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T031",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T031",
      "title": "Qualify the complete deterministic pilot in disposable copies",
      "kind": "qualification",
      "story": "US6",
      "goal": "Synthetic feature and isolated sanitized first legacy installation copy pass all deterministic compatibility/recovery/lifecycle checks with zero model/external writes; E3 regeneration and publication/model activation remain accurately pending until separate prerequisites pass.",
      "parents": [
        "T030"
      ],
      "tests": [
        "TST-007",
        "TST-023",
        "TST-024",
        "TST-025"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "evidence/pilot/receipts.json",
        "evidence/pilot/input-inventory.json",
        "evidence/pilot/compatibility.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_PILOT",
        "C_ALL"
      ],
      "acceptance": "Synthetic feature and isolated sanitized first legacy installation copy pass all deterministic compatibility/recovery/lifecycle checks with zero model/external writes; E3 regeneration and publication/model activation remain accurately pending until separate prerequisites pass.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "mechanical",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-reasoning-tier-and-rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "record supported effective runtime setting; unsupported requirement blocks; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "zero inference calls"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T031 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt"
    },
    {
      "local_id": "T032",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T032",
      "title": "Prove two scoped behavioral regeneration trials",
      "kind": "qualification",
      "story": "US6",
      "goal": "After confirmed available model binding and authorized inference, two independent clean source-excluded generation trials pass the unchanged gate behavior/regression oracle; observations, all failures/costs/input fingerprints retained; no deletion or broader disposability claim.",
      "parents": [
        "T025",
        "T031"
      ],
      "tests": [
        "TST-019"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "evidence/regeneration/trials.json",
        "evidence/regeneration/run-1/gate.py",
        "evidence/regeneration/run-2/gate.py",
        "evidence/regeneration/receipts.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "independent gate behavioral tests/fixtures",
        "frozen dependency lock and generation instructions",
        "native parent evidence and regeneration verifier only"
      ],
      "commands": [
        "C_REGEN_VERIFY",
        "C_ALL"
      ],
      "acceptance": "After confirmed available model binding and authorized inference, two independent clean source-excluded generation trials pass the unchanged gate behavior/regression oracle; observations, all failures/costs/input fingerprints retained; no deletion or broader disposability claim.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T032 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "denied_read_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/gate.py",
        "retained production gate implementation and every copy/context/attachment of its contents",
        "first-trial generated source and transcripts during the second fresh generation context"
      ],
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1",
      "measurement_qualification": {
        "behavioral_claim": "scoped gate.py source-excluded behavioral/regression proof",
        "fully_measured_claim": "requires measurement-qualified-experiment-v1 and actual declared fields/rates",
        "unexposed_fields": "retain null/reasons and unqualified measurement status; no cost/effective-settings comparison claim"
      }
    },
    {
      "local_id": "T033",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T033",
      "title": "Review independent oracle and cross-artifact boundaries",
      "kind": "review",
      "story": "US3",
      "goal": "Independent review validates complete-product intent, oracle provenance, contract/identity/native edges, fixed-model/permission enforcement, rollback and billing/regeneration claim limits; verdict cites current inputs and actual receipts rather than substituting for human artifact acceptance.",
      "parents": [
        "T031",
        "T032"
      ],
      "tests": [
        "TST-001",
        "TST-002",
        "TST-009",
        "TST-012",
        "TST-014",
        "TST-016",
        "TST-019",
        "TST-022",
        "TST-026"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "evidence/review.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Independent review validates complete-product intent, oracle provenance, contract/identity/native edges, fixed-model/permission enforcement, rollback and billing/regeneration claim limits; verdict cites current inputs and actual receipts rather than substituting for human artifact acceptance.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "architectural",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "capability-qualified-authoring-or-review",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "requires-existing-approved-capability-binding",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 24576,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T033 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T034",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T034",
      "title": "Write repository adoption and operator handoff documentation",
      "kind": "documentation",
      "story": "US2",
      "goal": "Candidate central ownership, first legacy installation pilot/existing native-contract second and owner-coordinated later rollout, local authority preservation, execution-owner compatibility blockers, safe upgrade/recovery, exact cost/disposability limits and publication gates are reviewable; no consumer/existing executor changes.",
      "parents": [
        "T023",
        "T031"
      ],
      "tests": [
        "TST-024",
        "TST-025"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "build/distribution/accepted/operator-handoff/ownership.md",
        "build/distribution/accepted/operator-handoff/migration.md",
        "build/distribution/accepted/operator-handoff/operator.md",
        "build/distribution/accepted/operator-handoff/regeneration.md",
        "build/distribution/accepted/operator-handoff/release.md"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Existing canonical ownership/rollout/generation contracts compiled into owner-scoped adoption/operator handoff; local authority/model/runtime/upgrade/rollback/cost/regeneration/publication gates remained explicit. Missing behavior created a separate spec repair, never invented documentation authority; no consumer/executor change.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "integration",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "fixed-once-per-attempt",
        "role": "low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "requested_alias": null,
        "exact_model": "gpt-6-luna",
        "binding_state": "approved-default-awaiting-parent-service-admission",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "approved exact selected-model parent/service admission",
        "approved existing inference route",
        "profile-specific correctness/hard requirements; advisory budgets and nullable observations"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 16384,
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T034 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T035",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T035",
      "title": "Assemble verified local release-candidate evidence",
      "kind": "qualification",
      "story": "US2",
      "goal": "Clean-source candidate build and exact component/generated-asset/digest/reference matrix, complete pilot/two regeneration/review receipts and rollback proof are present; public destination/license and mutation authorization are separate explicit states, never invented or bypassed.",
      "parents": [
        "T027",
        "T029",
        "T033",
        "T034"
      ],
      "tests": [
        "TST-025",
        "TST-027"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "evidence/release-candidate.json",
        "evidence/release-manifest.sha256"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_BUILD",
        "C_RELEASE",
        "C_ALL"
      ],
      "acceptance": "Clean-source candidate build and exact component/generated-asset/digest/reference matrix, complete pilot/two regeneration/review receipts and rollback proof are present; public destination/license and mutation authorization are separate explicit states, never invented or bypassed.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "mechanical",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-reasoning-tier-and-rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "record supported effective runtime setting; unsupported requirement blocks; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "zero inference calls"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T035 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt"
    },
    {
      "local_id": "T036",
      "qualified_id": "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T036",
      "title": "Emit gated rollout handoff and identity bindings",
      "kind": "handoff",
      "story": "US4",
      "goal": "Every repository and execution owner has explicit candidate/accepted/blocked adoption state and proof refs; dry identities preserve 1:1 leaves with null remote IDs; all actual repository/issue/publication/deployment mutations wait for their authorized owner and qualified runtime policy.",
      "parents": [
        "T035"
      ],
      "tests": [
        "TST-014",
        "TST-024",
        "TST-025"
      ],
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "spec/operations/rollout.md",
            "sha256": "080d0b180e3bb6d2edd8072dd575ae19b39ae27f8b4523f10349be503e3b86bd"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "6d6cc562a3988436a954c9594ab82836000bfe58c6dac7f95d2e4486f03b1437"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "dab8584bbfd4a096e46144efdcf5ff255c919690240ef4beac7f60ec6f8f5a60"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated central repository HEAD and scoped readable inventory before claim; retained code is evidence",
        "prerequisite_outputs": "freeze actual output digests of every native parent before claim; missing or stale output blocks claim",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "policies/rollout.json",
        "evidence/rollout-handoff.json",
        "evidence/issue-bindings.json"
      ],
      "protected_paths": [
        ".git/",
        ".codex/",
        ".aws/",
        "spec/",
        "build/distribution/accepted/"
      ],
      "read_scope": [
        "accepted feature package",
        "declared authoritative inputs",
        "current scoped source/test baseline",
        "native parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Every repository and execution owner has explicit candidate/accepted/blocked adoption state and proof refs; dry identities preserve 1:1 leaves with null remote IDs; all actual repository/issue/publication/deployment mutations wait for their authorized owner and qualified runtime policy.",
      "evidence_predicates": [
        "artifact_hash",
        "contract_hash",
        "frozen_input_set_hash",
        "changed_paths",
        "diff_hash",
        "fixed_commands",
        "declared_validation_predicate",
        "review_or_operator_verdict"
      ],
      "reasoning_class": "mechanical",
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "requested_alias": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-reasoning-tier-and-rate-card",
        "silent_alias_resolution": false,
        "mid_attempt_switch": false,
        "observed_identity_required": false,
        "reasoning_configuration": "record supported effective runtime setting; unsupported requirement blocks; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "frozen dependency/toolchain lock",
        "isolated workspace",
        "no credentials in artifacts",
        "zero inference calls"
      ],
      "permission_requirements": [
        "Task-scoped isolated central worktree only",
        "No consumer modification or existing executor infrastructure change",
        "Remote release/adoption/publication requires separate explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/spec-kit-distribution/001-reusable-distribution/T036 -->",
        "candidate_repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "required_immutable_creator": "pH34r-pH",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt"
    }
  ],
  "artifact_revision": 3,
  "execution_capability_contract": {
    "id": "execution-capability-v1",
    "path": "spec/contracts/execution-capabilities.md",
    "default_model_profile": "ordinary-implementation-v1",
    "hard_requirements": "explicit task security/financial/technical or correctness requirements never downgraded",
    "measurement_profile": "measurement-qualified-experiment-v1 only for declared fully measured claim"
  }
}
```
