---
artifact: executable-decomposition
revision: 2
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
  Parents: T001. Kind: foundation. Reasoning: bounded. Tests: FND-002, FND-003, FND-004, FND-005, FND-006.
  Outputs: spec/**, build/distribution/plan.md, build/distribution/tests.md, build/distribution/tasks.md, build/directory-specs/plan.md, build/directory-specs/tests.md, build/directory-specs/tasks.md, build/foundation/plan.md, build/foundation/tests.md, build/foundation/tasks.md, README.md, .gitignore, tools/validate_foundation.py, tests/test_foundation.py, tests/fixtures/foundation/**, .github/workflows/foundation.yml, build/execution-contract.yaml, build/native-bindings.json, payload-inventory.json, build/foundation/accepted/receipts/T002/*/completion.json, build/foundation/runtime/T002/*/**.
  Acceptance: Bounded stdlib validator, independent fixtures and read-only officially pinned CI pass in isolated branch at exact accepted design inputs using only available published interfaces; one issue/native accepted T001 parent, draft PR and exact-head checks verified; sanitized durable completion receipt retains actual fixed gpt-6-luna/runtime/settings/budget/permissions/input/scope/issue/parent/PR/check evidence and authorized verdict on separate append-only evidence ref. Candidate/unbound/missing/stale gates block; no invented acceptance, merge, release, deployment or consumer change.

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
            "sha256": "2c69c14e12b4636b1c199e8863089afe8493ac5b2c5fde8f7614f9753183f427"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "fbfec669d41612c9cad616fc275968cfbc41b16b1eaf4ea512318534c0e77312"
          },
          {
            "path": "spec/index.md",
            "sha256": "043041fcc2071a7f25fbe5dde3da218a85b5a8a03edea1c7e6d9cdfb158b6f9d"
          },
          {
            "path": "spec/usage/lifecycle.md",
            "sha256": "b527bbb338356ba26cf34459cff6f4431f7527292ebf274f24609266715a301c"
          },
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "093a140f8793294f7429fe89a12a512182befddf5bf45e4085a56c23a01aba38"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "ddfa9420e77436bcc59896ff0c644e996d0d79c3d5fc9d00b6687670c8a4c360"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "90d394fdd3cbdd69d8a7ac6610a74c443f09648ec37b1f9d6c3e84dee026922a"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "3623268099dc2335b3071e087426da61b3e4e8a6051dbf578bd1168d44a76a15"
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
            "sha256": "92ae70a9cc0ff8370511b54ae866061508d44c03ed3f522335a1527418d0de3b"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "4189b0637d8a4d813e750a1ab76e7e111857a9d3abdf3e9d1726814eaac3dea5"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "d22254900e42685a6bdd4c99522d380360d3ad390c90ccd866490c80bad6a9b4"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "10e1f7a64e531adbe93e25731c0e11c94734ddd1ad0374eb88bdc4c17890d2b4"
          },
          {
            "path": "build/distribution/tasks.md",
            "sha256": "b6c521ea087686b7d01d3c93fcc1756423954d3dda14cf0be14bd9a3a0b1549e"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "a01cab2937d6e00bf772081f8ddeaf8964ba62ab4e8d5934b4f05d7c9d9a3e18"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "build/directory-specs/tasks.md",
            "sha256": "a466fb51d1b329e4a90925ff9d5383ca3efde47bd25d03e3e6d1c36745c31bd8"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "9284ce852c8279e9dd234b210c84364c7a9777552f7493cbbc57c88f485f57a3"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "b6aae937254f8cdb39a77f83c7c78db96d20365d1bbf39edf7963969f91356fd"
          },
          {
            "path": "build/native-bindings.json",
            "sha256": "fc5ebccdbe838079d3b9355aeb3194a265576544b618924b846d661b4e0fe368"
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
        "FND-006"
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
            "sha256": "2c69c14e12b4636b1c199e8863089afe8493ac5b2c5fde8f7614f9753183f427"
          },
          {
            "path": "spec/navigation.json",
            "sha256": "fbfec669d41612c9cad616fc275968cfbc41b16b1eaf4ea512318534c0e77312"
          },
          {
            "path": "spec/index.md",
            "sha256": "043041fcc2071a7f25fbe5dde3da218a85b5a8a03edea1c7e6d9cdfb158b6f9d"
          },
          {
            "path": "spec/usage/lifecycle.md",
            "sha256": "b527bbb338356ba26cf34459cff6f4431f7527292ebf274f24609266715a301c"
          },
          {
            "path": "spec/features/distribution/index.md",
            "sha256": "093a140f8793294f7429fe89a12a512182befddf5bf45e4085a56c23a01aba38"
          },
          {
            "path": "spec/features/directory-specs/index.md",
            "sha256": "3ac2637e29205d920d9b3fd6e13f658ffef3b5cc7a38cf710f5e01335a632d4a"
          },
          {
            "path": "spec/contracts/authority.md",
            "sha256": "ddfa9420e77436bcc59896ff0c644e996d0d79c3d5fc9d00b6687670c8a4c360"
          },
          {
            "path": "spec/contracts/documents.md",
            "sha256": "90d394fdd3cbdd69d8a7ac6610a74c443f09648ec37b1f9d6c3e84dee026922a"
          },
          {
            "path": "spec/contracts/distribution.md",
            "sha256": "3623268099dc2335b3071e087426da61b3e4e8a6051dbf578bd1168d44a76a15"
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
            "sha256": "92ae70a9cc0ff8370511b54ae866061508d44c03ed3f522335a1527418d0de3b"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "4189b0637d8a4d813e750a1ab76e7e111857a9d3abdf3e9d1726814eaac3dea5"
          },
          {
            "path": "build/distribution/plan.md",
            "sha256": "d22254900e42685a6bdd4c99522d380360d3ad390c90ccd866490c80bad6a9b4"
          },
          {
            "path": "build/distribution/tests.md",
            "sha256": "10e1f7a64e531adbe93e25731c0e11c94734ddd1ad0374eb88bdc4c17890d2b4"
          },
          {
            "path": "build/distribution/tasks.md",
            "sha256": "b6c521ea087686b7d01d3c93fcc1756423954d3dda14cf0be14bd9a3a0b1549e"
          },
          {
            "path": "build/directory-specs/plan.md",
            "sha256": "a01cab2937d6e00bf772081f8ddeaf8964ba62ab4e8d5934b4f05d7c9d9a3e18"
          },
          {
            "path": "build/directory-specs/tests.md",
            "sha256": "b8e8e521cf200c803eccd459c1a6de661d55ac3dd8268c1080e996fcc8a8dac6"
          },
          {
            "path": "build/directory-specs/tasks.md",
            "sha256": "a466fb51d1b329e4a90925ff9d5383ca3efde47bd25d03e3e6d1c36745c31bd8"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "9284ce852c8279e9dd234b210c84364c7a9777552f7493cbbc57c88f485f57a3"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "b6aae937254f8cdb39a77f83c7c78db96d20365d1bbf39edf7963969f91356fd"
          },
          {
            "path": "build/native-bindings.json",
            "sha256": "fc5ebccdbe838079d3b9355aeb3194a265576544b618924b846d661b4e0fe368"
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
      "acceptance": "Bounded stdlib validator, independent fixtures and read-only officially pinned CI pass in isolated branch at exact accepted design inputs using only available published interfaces; one issue/native accepted T001 parent, draft PR and exact-head checks verified; sanitized durable completion receipt retains actual fixed gpt-6-luna/runtime/settings/budget/permissions/input/scope/issue/parent/PR/check evidence and authorized verdict on separate append-only evidence ref. Candidate/unbound/missing/stale gates block; no invented acceptance, merge, release, deployment or consumer change.",
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
        "mode": "one-observed-model-per-attempt",
        "role": "approved-low-cost-luna",
        "role_default_model": "gpt-6-luna",
        "exact_model": null,
        "binding_state": "required-before-claim",
        "requested_reasoning_effort": "preserve-existing-explicit-request",
        "requested_speed_tier": "preserve-existing-explicit-request",
        "historical_attribution": "immutable-observed-model-runtime-settings-rate-card",
        "mid_attempt_switch": false,
        "silent_alias_resolution": false,
        "observed_identity_required": true,
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
        "max_output_tokens": null,
        "output_token_budget_state": "required-before-claim",
        "actual_context_preflight_required": true
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
      }
    }
  ],
  "artifact_revision": 2
}
```
