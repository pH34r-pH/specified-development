---
artifact: executable-decomposition
revision: 4
acceptance: candidate-review
dispatch_status: planned-not-dispatched
---

# foundation dependency-ordered leaves

Semantic decomposition was completed in this fixed-model design pass. Each unchecked leaf mapped 1:1 to one issue. build/execution-contract.yaml parents were the sole execution graph. build/native-bindings.json retained stable qualified-to-native ID bindings. Feature/epic grouping and source document dependencies were not scheduling edges. Missing model/runtime/budget/permission/input bindings blocked claim; no model switched mid-attempt.

- [ ] T001 Establish minimal empty-repository PR base
  Parents: none. Kind: bootstrap. Reasoning: mechanical. Tests: FND-001.
  Outputs: README.md, LICENSE, build/foundation/accepted/receipts/T001/*/bootstrap.json, build/foundation/runtime/T001/*/**.
  Acceptance: Verify/preserve observed main seed with exactly README/LICENSE, or minimally seed only a truly empty approved target; retain actual repository/base/seed/file/permission/disclosure/issue/creator facts and actual accepted bootstrap verdict in immutable sanitized durable receipt; publication facts alone do not close the leaf; no ready label or history reset.
- [ ] T002 Publish sanitized specification foundation as draft PR
  Parents: T001. Kind: foundation. Reasoning: bounded. Tests: FND-002, FND-003, FND-004, FND-005, FND-006, FND-007, FND-008, FND-009.
  Outputs: spec/**, build/distribution/plan.md, build/distribution/tests.md, build/distribution/tasks.md, build/directory-specs/plan.md, build/directory-specs/tests.md, build/directory-specs/tasks.md, build/foundation/plan.md, build/foundation/tests.md, build/foundation/tasks.md, README.md, .gitignore, tools/validate_foundation.py, tests/test_foundation.py, tests/fixtures/foundation/**, .github/workflows/foundation.yml, build/execution-contract.yaml, build/native-bindings.json, payload-inventory.json, build/foundation/accepted/receipts/T002/*/completion.json, build/foundation/runtime/T002/*/**.
  Acceptance: Bounded stdlib validator, independent fixtures and read-only officially pinned CI pass in isolated branch at exact accepted design inputs using only available published interfaces; one issue/native accepted T001 parent, draft PR and exact-head checks verified; sanitized durable completion receipt retains parent/service exact selected gpt-6-luna/requested-xhigh evidence, nullable effective observations, requested/advisory budgets/parent stop plan and actual permissions/input/scope/issue/parent/PR/check evidence and authorized verdict on separate append-only evidence ref. Candidate/source/parent/permission/selection/correctness or required hard-cap/missing acceptance/stale gates block; optional unexposed telemetry alone does not; no invented acceptance, merge, release, deployment or consumer change.

## Structured semantic metadata

```task-metadata
{
  "metadata_schema": "ph34r-task-authoring-v1",
  "namespace": "pH34r-pH/specified-development/foundation",
  "artifact_acceptance": "candidate-review",
  "dispatchable": false,
  "execution_owner": "unbound-existing-owner",
  "model_policy_revision": "fixed-model-v3",
  "external_native_parents": {},
  "commands": {
    "C_BOOTSTRAP": {
      "cwd": ".",
      "argv": [
        "gh",
        "api",
        "repos/pH34r-pH/specified-development",
        "--jq",
        "{full_name: .full_name, default_branch: .default_branch, private: .private, size: .size, permissions: .permissions}"
      ],
      "expect": "exact target/empty-or-current-base/permissions observed before minimal seed; remote authorization observed"
    },
    "C_SEED": {
      "cwd": ".",
      "argv": [
        "git",
        "push",
        "origin",
        "HEAD:refs/heads/main"
      ],
      "expect": "only empty-main seed README/LICENSE; never force; skip if main exists and preserve actual base"
    },
    "C_FOUNDATION": {
      "cwd": ".",
      "argv": [
        "python",
        "tools/validate_foundation.py"
      ],
      "expect": "bounded scaffold structural/privacy validation GREEN; product behavior not claimed"
    },
    "C_FOUNDATION_TESTS": {
      "cwd": ".",
      "argv": [
        "python",
        "-m",
        "unittest",
        "tests.test_foundation",
        "-v"
      ],
      "expect": "independent malformed fixtures rejected and valid fixture passes"
    },
    "C_CI_HEAD": {
      "cwd": ".",
      "argv": [
        "gh",
        "pr",
        "view",
        "--repo",
        "pH34r-pH/specified-development",
        "--json",
        "number,headRefOid,isDraft,statusCheckRollup"
      ],
      "expect": "actual current branch draft PR head equals recorded passing check-run head; issue/parent/model receipt"
    },
    "C_CI_CHECKS": {
      "cwd": ".",
      "argv": [
        "gh",
        "pr",
        "checks",
        "--repo",
        "pH34r-pH/specified-development",
        "--watch",
        "--fail-fast"
      ],
      "expect": "expected foundation CI succeeded at the exact separately observed PR head; empty or stale checks cannot qualify"
    }
  },
  "tasks": [
    {
      "local_id": "T001",
      "qualified_id": "pH34r-pH/specified-development/foundation/T001",
      "title": "Establish minimal empty-repository PR base",
      "kind": "bootstrap",
      "parents": [],
      "tests": [
        "FND-001"
      ],
      "reasoning_class": "mechanical",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "README.md",
            "sha256": "244626aa20284126d38f5ea3bab243f961860bb24fea8f935d979e15b53c7c7c"
          },
          {
            "path": "LICENSE",
            "sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"
          },
          {
            "path": ".gitignore",
            "sha256": "4b84a5015c78fe37f105132d44b3a94c664907568fa3aeb83711afd0172081ee"
          },
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/index.md",
            "sha256": "043041fcc2071a7f25fbe5dde3da218a85b5a8a03edea1c7e6d9cdfb158b6f9d"
          },
          {
            "path": "spec/usage/lifecycle.md",
            "sha256": "373f4408d944482a7028b9bd09987f7516a2f5650e65de0a8cf4bd95c0847d75"
          },
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
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
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
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
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "build/foundation/plan.md",
            "sha256": "aefa2faab79bbb7bd9e6e7e8b02da8c90bf6d63a291b215337f072959cc48a74"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "ef9184d73607b4d7e0a934a9976b7403480e27fa0324135912a1701e245ee8ee"
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
            "path": "build/distribution/tasks.md",
            "sha256": "48baea57dce561116b0997727d4f52850b9dd2f5d58bd242ed02820817f9e686"
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
            "path": "build/directory-specs/tasks.md",
            "sha256": "497c4fe17515054c6d8b24910551d7a91432ff7b438c76e7c9db20c377abd4d8"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "e5eaf761213b740fd5912eb1292e87b70542c182585d238314bb360ece1970e0"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "2c1e700a165e1c329cd7f6d43d02e2f854c2aff94ade8515a23226ac0012d651"
          },
          {
            "path": "build/native-bindings.json",
            "sha256": "fc5ebccdbe838079d3b9355aeb3194a265576544b618924b846d661b4e0fe368"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact accepted reviewed design commit/tree and isolated worktree; observed main seed is publication evidence only, not an accepted task verdict",
        "prerequisite_outputs": "T001: no executable native parent. T002: only T001 accepted sanitized durable bootstrap receipt with immutable store ref/hash and native issue/parent evidence; missing/stale/unaccepted blocks. No later distribution interface prerequisite.",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata",
        "claim_time_hash_bindings": [
          {
            "path": "build/execution-contract.yaml",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          },
          {
            "path": "payload-inventory.json",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          },
          {
            "path": "build/foundation/tasks.md",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          }
        ]
      },
      "output_scope": [
        "README.md",
        "LICENSE",
        "build/foundation/accepted/receipts/T001/*/bootstrap.json",
        "build/foundation/runtime/T001/*/**"
      ],
      "read_scope": [
        "README.md",
        "LICENSE",
        ".gitignore",
        "spec/**",
        "build/foundation/**",
        "build/distribution/plan.md",
        "build/distribution/tests.md",
        "build/distribution/tasks.md",
        "build/directory-specs/plan.md",
        "build/directory-specs/tests.md",
        "build/directory-specs/tasks.md",
        "build/execution-contract.yaml",
        "build/native-bindings.json",
        "payload-inventory.json",
        "tools/validate_foundation.py",
        "tests/test_foundation.py",
        "tests/fixtures/foundation/**",
        ".github/workflows/foundation.yml",
        "all confined files explicitly listed in the sanitized public inventory at the frozen source revision",
        "declared native-parent receipt immutable store object",
        "observed Python 3.12 stdlib/git/gh and official action pin provenance",
        "readonly refs/status/objects and authorized metadata for exact target repo/assigned issues/PR"
      ],
      "commands": [
        "C_BOOTSTRAP",
        "C_SEED"
      ],
      "acceptance": "Verify/preserve observed main seed with exactly README/LICENSE, or minimally seed only a truly empty approved target; retain actual repository/base/seed/file/permission/disclosure/issue/creator facts and actual accepted bootstrap verdict in immutable sanitized durable receipt; publication facts alone do not close the leaf; no ready label or history reset.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "observed_runtime_and_fixed_model_if_required",
        "permissions",
        "review_verdict",
        "sanitized_durable_receipt_commit_blob_hash",
        "actual_authorized_verdict_not_publication_inference"
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
        "Observed Python 3.12 stdlib for published JSON/Markdown design interfaces",
        "observed git/gh versions, isolated worktree and target authorization",
        "official first-party CI action SHA/provenance before authoring",
        "observed exact model/settings/context/output budget if model leaf; no required unreleased distribution module/component/lock/renderer"
      ],
      "permission_requirements": [
        "Approved central foundation task outputs and assigned issue/draft-PR operations only",
        "Explicit read allowlist and frozen source/control hashes; authoritative design immutable within attempt",
        "Observed existing-owner-approved append-only receipt-ref read/write permission before claim",
        "No merge/release/deploy/wiki/consumer changes/credentials/infra charges; raw private logs never published"
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
        "marker": "<!-- spec-task:pH34r-pH/specified-development/foundation/T001 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "read_authorization": {
        "precedence": "Explicit read allowlist and actual permission required for every frozen input/control file; hash entry alone grants no additional read or write",
        "deterministic_full_inventory": true,
        "model_context": "assigned leaf authority/semantics and bounded diagnostics only; no all-60-record model context or new decomposition",
        "frozen_authority_writable": false,
        "inventory_paths": "confinement and symlink validation; no implicit private/unregistered files"
      },
      "receipt_policy": {
        "public_output_path": "build/foundation/accepted/receipts/T001/*/bootstrap.json",
        "attempt_path_binding": "Before work bind * to exactly one safe attempt slug and canonical real path; reject dot/traversal/symlink/other-leaf paths",
        "durable_store": {
          "kind": "existing-repository-append-only-git-ref",
          "repository": "pH34r-pH/specified-development",
          "ref": "refs/heads/evidence/foundation-receipts",
          "permission_and_owner_approval": "observe before claim; unavailable blocks; no new credentials",
          "immutable_ref": "receipt commit/blob and sha256 retained in existing task owner"
        },
        "overwrite_existing": false,
        "cleanup_permitted": false,
        "acceptance": "actual verdict/actor/time and exact accepted source/native/input/parent evidence; never inferred from path or publication",
        "private_raw_logs": "build/foundation/runtime/T001/*/**",
        "private_logs_public": false,
        "tested_head_preservation": "Completion receipt stored on declared separate evidence ref after exact-head checks; tested implementation head unchanged; source change needs fresh checks/new receipt"
      }
    },
    {
      "local_id": "T002",
      "qualified_id": "pH34r-pH/specified-development/foundation/T002",
      "title": "Publish sanitized specification foundation as draft PR",
      "kind": "foundation",
      "parents": [
        "T001"
      ],
      "tests": [
        "FND-002",
        "FND-003",
        "FND-004",
        "FND-005",
        "FND-006",
        "FND-007",
        "FND-008",
        "FND-009"
      ],
      "reasoning_class": "bounded",
      "frozen_inputs": {
        "authoritative": [
          {
            "path": "README.md",
            "sha256": "244626aa20284126d38f5ea3bab243f961860bb24fea8f935d979e15b53c7c7c"
          },
          {
            "path": "LICENSE",
            "sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"
          },
          {
            "path": ".gitignore",
            "sha256": "4b84a5015c78fe37f105132d44b3a94c664907568fa3aeb83711afd0172081ee"
          },
          {
            "path": "spec/manifest.json",
            "sha256": "fd6a67a708845644727970467cc2f589cb3276d738c61331609087265e92bdd9"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "be382df71bd0346216028b65f94632bcb996f73f3ef7f67440c67de7fe07cb74"
          },
          {
            "path": "spec/index.md",
            "sha256": "043041fcc2071a7f25fbe5dde3da218a85b5a8a03edea1c7e6d9cdfb158b6f9d"
          },
          {
            "path": "spec/usage/lifecycle.md",
            "sha256": "373f4408d944482a7028b9bd09987f7516a2f5650e65de0a8cf4bd95c0847d75"
          },
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "d2a7b9e3243e161066258f2ccf57a1c8dadccb240a4080c5f247c1cccb813c39"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
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
            "path": "spec/contracts/distribution.md",
            "sha256": "7405ac0f16ea918c890b33845258a0b633082de3d6e3c122e32e3046636a4f29"
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
            "path": "spec/assets/rate-card.fixture.json",
            "sha256": "e6e6e6db42971c8f14a577296f2d6b43f28b97f8d687da936d0e99c8c75222f6"
          },
          {
            "path": "build/foundation/plan.md",
            "sha256": "aefa2faab79bbb7bd9e6e7e8b02da8c90bf6d63a291b215337f072959cc48a74"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "ef9184d73607b4d7e0a934a9976b7403480e27fa0324135912a1701e245ee8ee"
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
            "path": "build/distribution/tasks.md",
            "sha256": "48baea57dce561116b0997727d4f52850b9dd2f5d58bd242ed02820817f9e686"
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
            "path": "build/directory-specs/tasks.md",
            "sha256": "497c4fe17515054c6d8b24910551d7a91432ff7b438c76e7c9db20c377abd4d8"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "e5eaf761213b740fd5912eb1292e87b70542c182585d238314bb360ece1970e0"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "2c1e700a165e1c329cd7f6d43d02e2f854c2aff94ade8515a23226ac0012d651"
          },
          {
            "path": "build/native-bindings.json",
            "sha256": "fc5ebccdbe838079d3b9355aeb3194a265576544b618924b846d661b4e0fe368"
          },
          {
            "path": "spec/contracts/execution-capabilities.md",
            "sha256": "0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e"
          }
        ],
        "repository_baseline": "Freeze exact accepted reviewed design commit/tree and isolated worktree; observed main seed is publication evidence only, not an accepted task verdict",
        "prerequisite_outputs": "T001: no executable native parent. T002: only T001 accepted sanitized durable bootstrap receipt with immutable store ref/hash and native issue/parent evidence; missing/stale/unaccepted blocks. No later distribution interface prerequisite.",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata",
        "claim_time_hash_bindings": [
          {
            "path": "build/execution-contract.yaml",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          },
          {
            "path": "payload-inventory.json",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          },
          {
            "path": "build/foundation/tasks.md",
            "rule": "freeze exact accepted bytes digest in external claim packet; no recursive self-hash in task metadata"
          }
        ],
        "accepted_parent_compatibility": {
          "qualified_id": "pH34r-pH/specified-development/foundation/T001",
          "issue_number": 2,
          "receipt_commit": "8b26481704e0483bb94c41c2c93407f234c9e0ae",
          "receipt_path": "build/foundation/accepted/receipts/T001/bootstrap-20261001T232906Z/bootstrap.json",
          "receipt_sha256": "ed807b05cdce8bc7d8b9bbf86dd0a7a60824374f357c4ceee79c92f37ffb411e",
          "rule": "preserve existing accepted receipt; unchanged bootstrap semantics; reviewed compatibility and native readiness checked before new T002 admission; historical T002 hashes refreshed separately"
        }
      },
      "output_scope": [
        "spec/**",
        "build/distribution/plan.md",
        "build/distribution/tests.md",
        "build/distribution/tasks.md",
        "build/directory-specs/plan.md",
        "build/directory-specs/tests.md",
        "build/directory-specs/tasks.md",
        "build/foundation/plan.md",
        "build/foundation/tests.md",
        "build/foundation/tasks.md",
        "README.md",
        ".gitignore",
        "tools/validate_foundation.py",
        "tests/test_foundation.py",
        "tests/fixtures/foundation/**",
        ".github/workflows/foundation.yml",
        "build/execution-contract.yaml",
        "build/native-bindings.json",
        "payload-inventory.json",
        "build/foundation/accepted/receipts/T002/*/completion.json",
        "build/foundation/runtime/T002/*/**"
      ],
      "read_scope": [
        "README.md",
        "LICENSE",
        ".gitignore",
        "spec/**",
        "build/foundation/**",
        "build/distribution/plan.md",
        "build/distribution/tests.md",
        "build/distribution/tasks.md",
        "build/directory-specs/plan.md",
        "build/directory-specs/tests.md",
        "build/directory-specs/tasks.md",
        "build/execution-contract.yaml",
        "build/native-bindings.json",
        "payload-inventory.json",
        "tools/validate_foundation.py",
        "tests/test_foundation.py",
        "tests/fixtures/foundation/**",
        ".github/workflows/foundation.yml",
        "all confined files explicitly listed in the sanitized public inventory at the frozen source revision",
        "declared native-parent receipt immutable store object",
        "observed Python 3.12 stdlib/git/gh and official action pin provenance",
        "readonly refs/status/objects and authorized metadata for exact target repo/assigned issues/PR"
      ],
      "commands": [
        "C_FOUNDATION",
        "C_FOUNDATION_TESTS",
        "C_CI_HEAD",
        "C_CI_CHECKS"
      ],
      "acceptance": "Bounded stdlib validator, independent fixtures and read-only officially pinned CI pass in isolated branch at exact accepted design inputs using only available published interfaces; one issue/native accepted T001 parent, draft PR and exact-head checks verified; sanitized durable completion receipt retains parent/service exact selected gpt-6-luna/requested-xhigh evidence, nullable effective observations, requested/advisory budgets/parent stop plan and actual permissions/input/scope/issue/parent/PR/check evidence and authorized verdict on separate append-only evidence ref. Candidate/source/parent/permission/selection/correctness or required hard-cap/missing acceptance/stale gates block; optional unexposed telemetry alone does not; no invented acceptance, merge, release, deployment or consumer change.",
      "expected_outcome": "GREEN-and-focused-regression-or-declared-deterministic-receipt",
      "evidence_predicates": [
        "accepted_input_hashes",
        "actual_parent_output_hashes",
        "changed_paths",
        "declared_commands",
        "expected_oracle_result",
        "fixed_model_selection_admission_and_profile_required_evidence",
        "permissions",
        "review_verdict",
        "sanitized_durable_receipt_commit_blob_hash",
        "actual_authorized_verdict_not_publication_inference"
      ],
      "fixed_model_policy": {
        "policy_id": "fixed-model-v3",
        "mode": "one-selected-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "xhigh",
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
        "Observed Python 3.12 stdlib for published JSON/Markdown design interfaces",
        "observed git/gh versions, isolated worktree and target authorization",
        "official first-party CI action SHA/provenance before authoring",
        "Parent/service admission selected exact gpt-6-luna and requested xhigh; effective identity/reasoning/speed/context/usage/token/timer fields may be unexposed for ordinary foundation work"
      ],
      "permission_requirements": [
        "Approved central foundation task outputs and assigned issue/draft-PR operations only",
        "Explicit read allowlist and frozen source/control hashes; authoritative design immutable within attempt",
        "Observed existing-owner-approved append-only receipt-ref read/write permission before claim",
        "No merge/release/deploy/wiki/consumer changes/credentials/infra charges; raw private logs never published"
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
        "marker": "<!-- spec-task:pH34r-pH/specified-development/foundation/T002 -->",
        "repository": "pH34r-pH/specified-development",
        "remote_repository_confirmed": true,
        "issue_id": null,
        "issue_number": null,
        "creator": "observe-authorized-existing-owner-policy",
        "agent_ready": false
      },
      "state": "planned-not-dispatched",
      "read_authorization": {
        "precedence": "Explicit read allowlist and actual permission required for every frozen input/control file; hash entry alone grants no additional read or write",
        "deterministic_full_inventory": true,
        "model_context": "assigned leaf authority/semantics and bounded diagnostics only; no all-60-record model context or new decomposition",
        "frozen_authority_writable": false,
        "inventory_paths": "confinement and symlink validation; no implicit private/unregistered files"
      },
      "receipt_policy": {
        "public_output_path": "build/foundation/accepted/receipts/T002/*/completion.json",
        "attempt_path_binding": "Before work bind * to exactly one safe attempt slug and canonical real path; reject dot/traversal/symlink/other-leaf paths",
        "durable_store": {
          "kind": "existing-repository-append-only-git-ref",
          "repository": "pH34r-pH/specified-development",
          "ref": "refs/heads/evidence/foundation-receipts",
          "permission_and_owner_approval": "observe before claim; unavailable blocks; no new credentials",
          "immutable_ref": "receipt commit/blob and sha256 retained in existing task owner"
        },
        "overwrite_existing": false,
        "cleanup_permitted": false,
        "acceptance": "actual verdict/actor/time and exact accepted source/native/input/parent evidence; never inferred from path or publication",
        "private_raw_logs": "build/foundation/runtime/T002/*/**",
        "private_logs_public": false,
        "tested_head_preservation": "Completion receipt stored on declared separate evidence ref after exact-head checks; tested implementation head unchanged; source change needs fresh checks/new receipt"
      },
      "execution_capability_profile": "ordinary-implementation-v1"
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
