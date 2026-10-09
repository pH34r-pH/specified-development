---
artifact: executable-decomposition
revision: 4
acceptance: candidate-review
dispatch_status: planned-not-dispatched
---

# directory-specs dependency-ordered leaves

Semantic decomposition was completed in this fixed-model design pass. Each unchecked leaf mapped 1:1 to one issue. build/execution-contract.yaml parents were the sole execution graph. build/native-bindings.json retained stable qualified-to-native ID bindings. Feature/epic grouping and source document dependencies were not scheduling edges. Missing model/runtime/budget/permission/input bindings blocked claim; no model switched mid-attempt.

Cross-feature native prerequisites (authoring input, projected into the sole native contract): {"T001": ["pH34r-pH/spec-kit-distribution/001-reusable-distribution/T036"]}

- [ ] T001 Freeze directory toolchain and baseline interfaces
  Parents: none. Kind: qualification. Reasoning: mechanical. Tests: declared deterministic receipt.
  Outputs: locks/directory.lock.json.
  Acceptance: Exact upstream/tool/dependency/approved baseline interface hashes frozen; renderer unknown stays blocked; zero inference.
- [ ] T002 Author inventory and stable-ID oracles
  Parents: T001. Kind: test. Reasoning: bounded. Tests: DIR-001, DIR-002.
  Outputs: tests/test_document_inventory.py, tests/fixtures/documents/inventory/**.
  Acceptance: Independent valid/invalid inventory/rename goldens have expected missing-behavior RED; no harness-error substitution.
- [ ] T003 Implement inventory and schema validation
  Parents: T002. Kind: implementation. Reasoning: integration. Tests: DIR-001, DIR-002.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_inventory.py, schemas/document-manifest.schema.json.
  Acceptance: Complete whole-tree inventory/schema/identity/role validation and stable rename behavior pass unchanged T002 oracle.
- [ ] T004 Author closure and reference validation oracles
  Parents: T003. Kind: test. Reasoning: integration. Tests: DIR-003, DIR-004, DIR-005, DIR-006.
  Outputs: tests/test_document_links.py, tests/fixtures/documents/links/**.
  Acceptance: Handwritten normative closure/link/asset/anchor cases and pinned parser/renderer observations are reviewed before production implementation; expected RED retained.
- [ ] T005 Implement closure and parsed references
  Parents: T004. Kind: implementation. Reasoning: architectural. Tests: DIR-003, DIR-004, DIR-005, DIR-006.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_links.py.
  Acceptance: Dependency closure/parsed link/anchor/schema/asset validation preserves navigation boundary, confines paths and passes unchanged oracle without model calls.
- [ ] T006 Author adapter source-map and hash goldens
  Parents: T005. Kind: test. Reasoning: integration. Tests: DIR-007, DIR-008.
  Outputs: tests/test_document_compile.py, tests/fixtures/documents/compile/**.
  Acceptance: Exact bytes/order/ranges/canonical hash independently fixed, invalid encoding and unknown fingerprint cases RED for contractual cause.
- [ ] T007 Implement deterministic adapter assembly
  Parents: T006. Kind: implementation. Reasoning: integration. Tests: DIR-007, DIR-008.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_compile.py.
  Acceptance: Two isolated runs byte-identical; every source range exactly matches original; lock root has no self-cycle and selected closure only.
- [ ] T008 Author freshness and change-effect tests
  Parents: T007. Kind: test. Reasoning: integration. Tests: DIR-009, DIR-010.
  Outputs: tests/test_document_freshness.py, tests/fixtures/documents/freshness/**.
  Acceptance: Each required hash/version/input change blocks stale use; unrelated change preservation requires full revalidation; native changed-descendant expectations independently fixed.
- [ ] T009 Implement freshness and artifact invalidation
  Parents: T008. Kind: implementation. Reasoning: architectural. Tests: DIR-009, DIR-010.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_freshness.py.
  Acceptance: Every entrypoint verifies accepted closure/tool/source-map hashes; changed contracts and native descendants stale; historical receipts/unaffected validated contracts retained.
- [ ] T010 Author command and active-asset compatibility tests
  Parents: T009. Kind: test. Reasoning: integration. Tests: DIR-011, DIR-012, DIR-013.
  Outputs: tests/test_directory_commands.py, tests/fixtures/documents/commands/**.
  Acceptance: Disposable upstream path/no-persist and every canonical/adapter semantic command independently exercised for both integrations; tamper/stale direct writes RED.
- [ ] T011 Implement wrappers and replacement command assets
  Parents: T010. Kind: implementation. Reasoning: integration. Tests: DIR-011, DIR-012, DIR-013.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_commands.py, presets/ph34r-lifecycle/commands/**, extensions/ph34r-contracts/extension.yml.
  Acceptance: Canonical-edit and guarded build commands resolve verified overrides/no-persist/sibling paths; no source symlinks, hooks-only freshness or invented flags.
- [ ] T012 Author stage recovery and retention tests
  Parents: T007. Kind: test. Reasoning: integration. Tests: DIR-014, DIR-015, DIR-016.
  Outputs: tests/test_document_retention.py, tests/fixtures/documents/retention/**.
  Acceptance: Independent byte/mode/sentinel/accepted-history inventory and every interruption/cleanup/cas fixture show contractual RED; code and accepted records protected.
- [ ] T013 Implement staged promotion snapshots and bounded cleanup
  Parents: T009, T012. Kind: implementation. Reasoning: architectural. Tests: DIR-014, DIR-015, DIR-016.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_retention.py, .gitignore.
  Acceptance: Journal/before-hash recovery proves exact prior state; accepted snapshots append-only; only declared disposable managed paths cleanable; no deletion of code/history.
- [ ] T014 Author optional site/wiki parity and drift tests
  Parents: T005, T007. Kind: test. Reasoning: integration. Tests: DIR-017, DIR-018, DIR-019.
  Outputs: tests/test_document_views.py, tests/fixtures/documents/views/**.
  Acceptance: Exact pinned renderer evidence fixes repository/site/wiki maps/prose/assets; fake remote exercises unauthorized/missing/drift; no live publish.
- [ ] T015 Implement optional documentation projections
  Parents: T013, T014. Kind: implementation. Reasoning: integration. Tests: DIR-017, DIR-018, DIR-019.
  Outputs: extensions/ph34r-contracts/scripts/ph34r_contracts/document_views.py, templates/mkdocs.yml, templates/wiki/**.
  Acceptance: Optional locked site source config and deterministic injective one-way wiki mapping pass parity/drift oracles; dry default and authorization/access/current-base gates; no rewrite/reverse sync.
- [ ] T016 Author directory install/upgrade compatibility tests
  Parents: T011, T013. Kind: test. Reasoning: integration. Tests: DIR-020.
  Outputs: tests/test_directory_upgrade.py, tests/fixtures/documents/upgrade/**.
  Acceptance: Wrong-version/active-asset/tamper/interruption cases use baseline verified installer with unchanged consumer/domain authority; absent support yields explicit RED/block.
- [ ] T017 Integrate directory assets into verified releases
  Parents: T015, T016. Kind: implementation. Reasoning: integration. Tests: DIR-020.
  Outputs: presets/ph34r-lifecycle/preset.yml, extensions/ph34r-contracts/extension.yml, bundles/ph34r-standard/bundle.yml, tools/verify_directory_assets.py.
  Acceptance: Pinned component identities/digests/effective generated assets and rollback inventory include directory guards/views; compatibility verified, no release publication.
- [ ] T018 Author complete pilot native-identity and public-boundary tests
  Parents: T017. Kind: test. Reasoning: architectural. Tests: DIR-021, DIR-022, DIR-023, DIR-024.
  Outputs: tests/test_directory_pilot.py, tests/fixtures/documents/pilot/**.
  Acceptance: Complete two-feature lifecycle and native-only edges, private sentinel/content provenance/status boundaries independently fixed; no projection-derived oracle or consumer writes.
- [ ] T019 Run isolated complete directory compatibility pilot
  Parents: T018. Kind: qualification. Reasoning: mechanical. Tests: DIR-021, DIR-022, DIR-023, DIR-024.
  Outputs: build/directory-specs/accepted/pilot-candidate/qualification.json.
  Acceptance: All deterministic cases pass in clean synthetic/isolated installation fixtures with exact lock; optional unqualified target explicitly blocked; no inference/publication/consumer mutation.
- [ ] T020 Review directory authority and command correctness independently
  Parents: T019. Kind: review. Reasoning: architectural. Tests: DIR-001, DIR-002, DIR-003, DIR-004, DIR-005, DIR-006, DIR-007, DIR-008, DIR-009, DIR-010, DIR-011, DIR-012, DIR-013, DIR-014, DIR-015, DIR-016, DIR-017, DIR-018, DIR-019, DIR-020, DIR-021, DIR-022, DIR-023, DIR-024.
  Outputs: build/directory-specs/accepted/review-candidate/review.json.
  Acceptance: Independent reviewer checks full traces/closures/source parity/native semantics/retention/recovery/settings and reports remaining blockers; findings create separate repair, not silent behavior change.
- [ ] T021 Prepare scoped consumer adoption and publication handoff
  Parents: T020. Kind: documentation. Reasoning: bounded. Tests: DIR-020, DIR-021, DIR-023.
  Outputs: build/directory-specs/accepted/adoption-candidate/handoff.json.
  Acceptance: Existing canonical rollout/authority contracts compiled into concrete owner-scoped migration, rollback/history/public destination checks and remaining gates; no new semantics, application changes or external activation.
- [ ] T022 Assemble reviewed directory compatibility evidence
  Parents: T020, T021. Kind: qualification. Reasoning: mechanical. Tests: DIR-001, DIR-002, DIR-003, DIR-004, DIR-005, DIR-006, DIR-007, DIR-008, DIR-009, DIR-010, DIR-011, DIR-012, DIR-013, DIR-014, DIR-015, DIR-016, DIR-017, DIR-018, DIR-019, DIR-020, DIR-021, DIR-022, DIR-023, DIR-024.
  Outputs: build/directory-specs/accepted/release-candidate/evidence.json.
  Acceptance: Exact artifact/test/source/lock/model history inventory and pending release/adoption/renderers evidence accurate; zero missing-field substitution and no universal disposability claim.

## Structured semantic metadata

```task-metadata
{
  "metadata_schema": "ph34r-task-authoring-v1",
  "namespace": "pH34r-pH/specified-development/directory-specs",
  "artifact_acceptance": "candidate-review",
  "dispatchable": false,
  "execution_owner": "unbound-existing-owner",
  "model_policy_revision": "fixed-model-v3",
  "external_native_parents": {
    "T001": [
      "pH34r-pH/spec-kit-distribution/001-reusable-distribution/T036"
    ]
  },
  "commands": {
    "C_INVENTORY": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_inventory",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_LINKS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_links",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_COMPILE": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_compile",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_FRESHNESS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_freshness",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_COMMANDS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_directory_commands",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_RETENTION": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_retention",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_VIEWS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_document_views",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_UPGRADE": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_directory_upgrade",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_PILOT": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_directory_pilot",
        "-v"
      ],
      "expect": "declared contractual RED for independent test leaf; GREEN and focused regressions for successor"
    },
    "C_LOCK": {
      "cwd": ".",
      "argv": [
        "python",
        "tools/verify_directory_lock.py",
        "--check"
      ],
      "expect": "exact required fingerprints or explicit compatibility block"
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
      "expect": "all required baseline/directory product tests GREEN with exact environment"
    }
  },
  "tasks": [
    {
      "local_id": "T001",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T001",
      "title": "Freeze directory toolchain and baseline interfaces",
      "kind": "qualification",
      "parents": [],
      "tests": [],
      "reasoning_class": "mechanical",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "locks/directory.lock.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_LOCK"
      ],
      "acceptance": "Exact upstream/tool/dependency/approved baseline interface hashes frozen; renderer unknown stays blocked; zero inference.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "observed_runtime_and_fixed_model_if_required",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-runtime-settings-rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Observe supported effective settings; unsupported requirements block; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "actual supported model/settings/context and permissions if inference required"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "output_token_budget_state": "not-applicable",
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T001 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched"
    },
    {
      "local_id": "T002",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T002",
      "title": "Author inventory and stable-ID oracles",
      "kind": "test",
      "parents": [
        "T001"
      ],
      "tests": [
        "DIR-001",
        "DIR-002"
      ],
      "reasoning_class": "bounded",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_inventory.py",
        "tests/fixtures/documents/inventory/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_INVENTORY"
      ],
      "acceptance": "Independent valid/invalid inventory/rename goldens have expected missing-behavior RED; no harness-error substitution.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T002 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T003",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T003",
      "title": "Implement inventory and schema validation",
      "kind": "implementation",
      "parents": [
        "T002"
      ],
      "tests": [
        "DIR-001",
        "DIR-002"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_inventory.py",
        "schemas/document-manifest.schema.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_INVENTORY"
      ],
      "acceptance": "Complete whole-tree inventory/schema/identity/role validation and stable rename behavior pass unchanged T002 oracle.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T003 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T004",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T004",
      "title": "Author closure and reference validation oracles",
      "kind": "test",
      "parents": [
        "T003"
      ],
      "tests": [
        "DIR-003",
        "DIR-004",
        "DIR-005",
        "DIR-006"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_links.py",
        "tests/fixtures/documents/links/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_LINKS"
      ],
      "acceptance": "Handwritten normative closure/link/asset/anchor cases and pinned parser/renderer observations are reviewed before production implementation; expected RED retained.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T004 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T005",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T005",
      "title": "Implement closure and parsed references",
      "kind": "implementation",
      "parents": [
        "T004"
      ],
      "tests": [
        "DIR-003",
        "DIR-004",
        "DIR-005",
        "DIR-006"
      ],
      "reasoning_class": "architectural",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_links.py"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_LINKS",
        "C_INVENTORY"
      ],
      "acceptance": "Dependency closure/parsed link/anchor/schema/asset validation preserves navigation boundary, confines paths and passes unchanged oracle without model calls.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "capability-qualified-approved",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T005 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T006",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T006",
      "title": "Author adapter source-map and hash goldens",
      "kind": "test",
      "parents": [
        "T005"
      ],
      "tests": [
        "DIR-007",
        "DIR-008"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_compile.py",
        "tests/fixtures/documents/compile/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_COMPILE"
      ],
      "acceptance": "Exact bytes/order/ranges/canonical hash independently fixed, invalid encoding and unknown fingerprint cases RED for contractual cause.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T006 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T007",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T007",
      "title": "Implement deterministic adapter assembly",
      "kind": "implementation",
      "parents": [
        "T006"
      ],
      "tests": [
        "DIR-007",
        "DIR-008"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_compile.py"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_COMPILE",
        "C_LINKS"
      ],
      "acceptance": "Two isolated runs byte-identical; every source range exactly matches original; lock root has no self-cycle and selected closure only.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T007 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T008",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T008",
      "title": "Author freshness and change-effect tests",
      "kind": "test",
      "parents": [
        "T007"
      ],
      "tests": [
        "DIR-009",
        "DIR-010"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_freshness.py",
        "tests/fixtures/documents/freshness/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_FRESHNESS"
      ],
      "acceptance": "Each required hash/version/input change blocks stale use; unrelated change preservation requires full revalidation; native changed-descendant expectations independently fixed.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T008 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T009",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T009",
      "title": "Implement freshness and artifact invalidation",
      "kind": "implementation",
      "parents": [
        "T008"
      ],
      "tests": [
        "DIR-009",
        "DIR-010"
      ],
      "reasoning_class": "architectural",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_freshness.py"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_FRESHNESS",
        "C_COMPILE"
      ],
      "acceptance": "Every entrypoint verifies accepted closure/tool/source-map hashes; changed contracts and native descendants stale; historical receipts/unaffected validated contracts retained.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "capability-qualified-approved",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T009 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T010",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T010",
      "title": "Author command and active-asset compatibility tests",
      "kind": "test",
      "parents": [
        "T009"
      ],
      "tests": [
        "DIR-011",
        "DIR-012",
        "DIR-013"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_directory_commands.py",
        "tests/fixtures/documents/commands/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_COMMANDS"
      ],
      "acceptance": "Disposable upstream path/no-persist and every canonical/adapter semantic command independently exercised for both integrations; tamper/stale direct writes RED.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T010 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T011",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T011",
      "title": "Implement wrappers and replacement command assets",
      "kind": "implementation",
      "parents": [
        "T010"
      ],
      "tests": [
        "DIR-011",
        "DIR-012",
        "DIR-013"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_commands.py",
        "presets/ph34r-lifecycle/commands/**",
        "extensions/ph34r-contracts/extension.yml"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_COMMANDS",
        "C_FRESHNESS"
      ],
      "acceptance": "Canonical-edit and guarded build commands resolve verified overrides/no-persist/sibling paths; no source symlinks, hooks-only freshness or invented flags.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T011 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T012",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T012",
      "title": "Author stage recovery and retention tests",
      "kind": "test",
      "parents": [
        "T007"
      ],
      "tests": [
        "DIR-014",
        "DIR-015",
        "DIR-016"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_retention.py",
        "tests/fixtures/documents/retention/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_RETENTION"
      ],
      "acceptance": "Independent byte/mode/sentinel/accepted-history inventory and every interruption/cleanup/cas fixture show contractual RED; code and accepted records protected.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T012 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T013",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T013",
      "title": "Implement staged promotion snapshots and bounded cleanup",
      "kind": "implementation",
      "parents": [
        "T009",
        "T012"
      ],
      "tests": [
        "DIR-014",
        "DIR-015",
        "DIR-016"
      ],
      "reasoning_class": "architectural",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_retention.py",
        ".gitignore"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_RETENTION",
        "C_FRESHNESS"
      ],
      "acceptance": "Journal/before-hash recovery proves exact prior state; accepted snapshots append-only; only declared disposable managed paths cleanable; no deletion of code/history.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "capability-qualified-approved",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T013 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T014",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T014",
      "title": "Author optional site/wiki parity and drift tests",
      "kind": "test",
      "parents": [
        "T005",
        "T007"
      ],
      "tests": [
        "DIR-017",
        "DIR-018",
        "DIR-019"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_document_views.py",
        "tests/fixtures/documents/views/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_VIEWS"
      ],
      "acceptance": "Exact pinned renderer evidence fixes repository/site/wiki maps/prose/assets; fake remote exercises unauthorized/missing/drift; no live publish.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T014 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T015",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T015",
      "title": "Implement optional documentation projections",
      "kind": "implementation",
      "parents": [
        "T013",
        "T014"
      ],
      "tests": [
        "DIR-017",
        "DIR-018",
        "DIR-019"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "extensions/ph34r-contracts/scripts/ph34r_contracts/document_views.py",
        "templates/mkdocs.yml",
        "templates/wiki/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_VIEWS",
        "C_RETENTION"
      ],
      "acceptance": "Optional locked site source config and deterministic injective one-way wiki mapping pass parity/drift oracles; dry default and authorization/access/current-base gates; no rewrite/reverse sync.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T015 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T016",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T016",
      "title": "Author directory install/upgrade compatibility tests",
      "kind": "test",
      "parents": [
        "T011",
        "T013"
      ],
      "tests": [
        "DIR-020"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_directory_upgrade.py",
        "tests/fixtures/documents/upgrade/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_UPGRADE"
      ],
      "acceptance": "Wrong-version/active-asset/tamper/interruption cases use baseline verified installer with unchanged consumer/domain authority; absent support yields explicit RED/block.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T016 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T017",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T017",
      "title": "Integrate directory assets into verified releases",
      "kind": "implementation",
      "parents": [
        "T015",
        "T016"
      ],
      "tests": [
        "DIR-020"
      ],
      "reasoning_class": "integration",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "presets/ph34r-lifecycle/preset.yml",
        "extensions/ph34r-contracts/extension.yml",
        "bundles/ph34r-standard/bundle.yml",
        "tools/verify_directory_assets.py"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_UPGRADE",
        "C_COMMANDS"
      ],
      "acceptance": "Pinned component identities/digests/effective generated assets and rollback inventory include directory guards/views; compatibility verified, no release publication.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T017 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T018",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T018",
      "title": "Author complete pilot native-identity and public-boundary tests",
      "kind": "test",
      "parents": [
        "T017"
      ],
      "tests": [
        "DIR-021",
        "DIR-022",
        "DIR-023",
        "DIR-024"
      ],
      "reasoning_class": "architectural",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "tests/test_directory_pilot.py",
        "tests/fixtures/documents/pilot/**"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_PILOT"
      ],
      "acceptance": "Complete two-feature lifecycle and native-only edges, private sentinel/content provenance/status boundaries independently fixed; no projection-derived oracle or consumer writes.",
      "expected_outcome": "expected-contractual-RED",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "capability-qualified-approved",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T018 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T019",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T019",
      "title": "Run isolated complete directory compatibility pilot",
      "kind": "qualification",
      "parents": [
        "T018"
      ],
      "tests": [
        "DIR-021",
        "DIR-022",
        "DIR-023",
        "DIR-024"
      ],
      "reasoning_class": "mechanical",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "build/directory-specs/accepted/pilot-candidate/qualification.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_PILOT",
        "C_ALL"
      ],
      "acceptance": "All deterministic cases pass in clean synthetic/isolated installation fixtures with exact lock; optional unqualified target explicitly blocked; no inference/publication/consumer mutation.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "observed_runtime_and_fixed_model_if_required",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-runtime-settings-rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Observe supported effective settings; unsupported requirements block; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "actual supported model/settings/context and permissions if inference required"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "output_token_budget_state": "not-applicable",
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T019 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched"
    },
    {
      "local_id": "T020",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T020",
      "title": "Review directory authority and command correctness independently",
      "kind": "review",
      "parents": [
        "T019"
      ],
      "tests": [
        "DIR-001",
        "DIR-002",
        "DIR-003",
        "DIR-004",
        "DIR-005",
        "DIR-006",
        "DIR-007",
        "DIR-008",
        "DIR-009",
        "DIR-010",
        "DIR-011",
        "DIR-012",
        "DIR-013",
        "DIR-014",
        "DIR-015",
        "DIR-016",
        "DIR-017",
        "DIR-018",
        "DIR-019",
        "DIR-020",
        "DIR-021",
        "DIR-022",
        "DIR-023",
        "DIR-024"
      ],
      "reasoning_class": "architectural",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "build/directory-specs/accepted/review-candidate/review.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Independent reviewer checks full traces/closures/source parity/native semantics/retention/recovery/settings and reports remaining blockers; findings create separate repair, not silent behavior change.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "capability-qualified-approved",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T020 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T021",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T021",
      "title": "Prepare scoped consumer adoption and publication handoff",
      "kind": "documentation",
      "parents": [
        "T020"
      ],
      "tests": [
        "DIR-020",
        "DIR-021",
        "DIR-023"
      ],
      "reasoning_class": "bounded",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "build/directory-specs/accepted/adoption-candidate/handoff.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Existing canonical rollout/authority contracts compiled into concrete owner-scoped migration, rollback/history/public destination checks and remaining gates; no new semantics, application changes or external activation.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-selection-admission-provenance-and-separate-available-effective-observations/rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Preserve parent/service requested options and admission; record unexposed effective settings explicitly; rejected requests/hard requirements block; no invented flags",
        "selection_evidence_required": true,
        "effective_telemetry": "nullable by profile; selection never copied into effective fields",
        "retry_selection": "same exact model for this task; different model requires separately reviewed repair/task identity"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "selected-model admission, actual permissions/correctness requirements and nullable effective telemetry"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": null,
        "output_token_budget_state": "advisory-request-or-explicitly-unavailable",
        "actual_context_preflight_required": false,
        "wall_budget_kind": "requested-advisory",
        "output_budget_kind": "requested-advisory; unexposed capacity/control may remain null",
        "parent_stop_conditions": "best-effort elapsed/progress/scope checks at existing owner checkpoints; pause/cancel when observed; no enforced timer or token cap claimed"
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T021 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "execution_capability_profile": "ordinary-implementation-v1"
    },
    {
      "local_id": "T022",
      "qualified_id": "pH34r-pH/specified-development/directory-specs/T022",
      "title": "Assemble reviewed directory compatibility evidence",
      "kind": "qualification",
      "parents": [
        "T020",
        "T021"
      ],
      "tests": [
        "DIR-001",
        "DIR-002",
        "DIR-003",
        "DIR-004",
        "DIR-005",
        "DIR-006",
        "DIR-007",
        "DIR-008",
        "DIR-009",
        "DIR-010",
        "DIR-011",
        "DIR-012",
        "DIR-013",
        "DIR-014",
        "DIR-015",
        "DIR-016",
        "DIR-017",
        "DIR-018",
        "DIR-019",
        "DIR-020",
        "DIR-021",
        "DIR-022",
        "DIR-023",
        "DIR-024"
      ],
      "reasoning_class": "mechanical",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "782874a6eb0d3bf006594aa6b7b12fa21cec2a4f2b4d78ca19f1643cb376d9e2"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "b91ed36cdbfc806923cb015ca096dc9e3312d2d76a9a2e0cbdd6009627a12224"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
          },
          {
            "path": "spec/operations/upstream.md",
            "sha256": "b6c49f416da521c2df5bae0c188e322424c366213cf01b8007cebeb80ed9833b"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "15747e10d73b23023f8a2f153ce927fd6bd2333476165b8dc157a34c6d960a6b"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact isolated worktree HEAD, selected accepted input revision and scoped readable inventory before claim",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "build/directory-specs/accepted/release-candidate/evidence.json"
      ],
      "read_scope": [
        "spec/**",
        "build/directory-specs/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_ALL"
      ],
      "acceptance": "Exact artifact/test/source/lock/model history inventory and pending release/adoption/renderers evidence accurate; zero missing-field substitution and no universal disposability claim.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "observed_runtime_and_fixed_model_if_required",
        "permissions",
        "review_verdict"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "deterministic-no-model",
        "role": "deterministic",
        "role_default_model": null,
        "exact_model": null,
        "binding_state": "not-applicable",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-runtime-settings-rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": false,
        "reasoning_configuration": "Observe supported effective settings; unsupported requirements block; no invented adapter flags"
      },
      "runtime_requirements": [
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "actual supported model/settings/context and permissions if inference required"
      ],
      "permission_requirements": [
        "task-scoped outputs only",
        "no consumer mutation, merge, deployment, credentials or new infrastructure charges",
        "remote issue/draft-PR operations only for expressly authorized foundation handoff; later product publication needs explicit authorization"
      ],
      "budget": {
        "wall_minutes": 90,
        "initial_attempts": 1,
        "retry_owner": "existing execution system",
        "max_output_tokens": 0,
        "output_token_budget_state": "not-applicable",
        "actual_context_preflight_required": false
      },
      "issue_identity": {
        "marker": "<!-- spec-task:pH34r-pH/specified-development/directory-specs/T022 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched"
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
