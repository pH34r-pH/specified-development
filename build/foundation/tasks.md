---
artifact: executable-decomposition
revision: 1
acceptance: candidate-review
dispatch_status: planned-not-dispatched
---

# foundation dependency-ordered leaves

Semantic decomposition was completed in this fixed-model design pass. Each unchecked leaf mapped 1:1 to one issue. build/execution-contract.yaml parents were the sole execution graph. build/native-bindings.json retained stable qualified-to-native ID bindings. Feature/epic grouping and source document dependencies were not scheduling edges. Missing model/runtime/budget/permission/input bindings blocked claim; no model switched mid-attempt.

- [ ] T001 Establish minimal empty-repository PR base
  Parents: none. Kind: bootstrap. Reasoning: mechanical. Tests: FND-001.
  Outputs: README.md, LICENSE, build/foundation/runtime/bootstrap-receipt.json.
  Acceptance: Observed confirmed empty repo seeded with exactly README/LICENSE once; existing main preserved; base SHA/disclosure recorded; one leaf identity bound without ready label.
- [ ] T002 Publish sanitized specification foundation as draft PR
  Parents: T001. Kind: foundation. Reasoning: bounded. Tests: FND-002, FND-003, FND-004, FND-005, FND-006.
  Outputs: spec/**, build/distribution/plan.md, build/distribution/tests.md, build/distribution/tasks.md, build/directory-specs/plan.md, build/directory-specs/tests.md, build/directory-specs/tasks.md, build/foundation/plan.md, build/foundation/tests.md, build/foundation/tasks.md, README.md, .gitignore, tools/validate_foundation.py, tests/test_foundation.py, tests/fixtures/foundation/**, .github/workflows/foundation.yml, build/execution-contract.yaml, build/native-bindings.json, payload-inventory.json.
  Acceptance: Allowlisted payload plus bounded validator/independent fixtures/read-only pinned-action CI committed in isolated branch; exactly one leaf issue and native seed parent, draft PR; exact-head checks pass and actual fixed gpt-6-luna receipt retained; no merge/release/deploy/consumer edit.

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
            "sha256": "ab16cd4fb54849580879155cfa872287471889085d5165bc97077af7cf6d377d"
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
            "sha256": "b5562a1348d4d4ce520905bf8d191276c4e8b5d61a4a0e20134fdbef52a3fd14"
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
            "sha256": "3d1690753ab2aecc686e9bb65c9824f2871937d9fc3b899b55fbfddebf4f5d3c"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "5c3ee9629d2a14cf0c1eb695f6ee87030b246f2485af2793693fb5e763e7a8b7"
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
            "sha256": "2abb40d134ef95f8a7492ccda1f2f589f6698a77b9c65618937ada595adfc56f"
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
            "sha256": "90f845521d980d9b52287fc6113cefb285f5385e0497aeb4a20766fd2b7aff55"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "6a1096a19c022defafacfa9e44404dc12283b8d668809efd7734336cd6ef3fc0"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "4ad389ca096ec75feadfff2411d14e38a2f38aa8fabee8a0e7057fdbda7cd44b"
          }
        ],
        "repository_baseline": "Observe confirmed public repo; bootstrap records actual base HEAD; foundation starts isolated branch at that exact HEAD",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
      },
      "output_scope": [
        "README.md",
        "LICENSE",
        "build/foundation/runtime/bootstrap-receipt.json"
      ],
      "read_scope": [
        "spec/**",
        "build/foundation/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_BOOTSTRAP",
        "C_SEED"
      ],
      "acceptance": "Observed confirmed empty repo seeded with exactly README/LICENSE once; existing main preserved; base SHA/disclosure recorded; one leaf identity bound without ready label.",
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
        "Explicitly approved central scaffold/issue/draft-PR only",
        "bootstrap direct-main exception exactly README/LICENSE if repo empty",
        "no merge/release/deploy/wiki/consumer edits/credentials/infra charges"
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
      "state": "planned-not-dispatched"
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
            "sha256": "ab16cd4fb54849580879155cfa872287471889085d5165bc97077af7cf6d377d"
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
            "sha256": "b5562a1348d4d4ce520905bf8d191276c4e8b5d61a4a0e20134fdbef52a3fd14"
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
            "sha256": "3d1690753ab2aecc686e9bb65c9824f2871937d9fc3b899b55fbfddebf4f5d3c"
          },
          {
            "path": "build/foundation/tests.md",
            "sha256": "5c3ee9629d2a14cf0c1eb695f6ee87030b246f2485af2793693fb5e763e7a8b7"
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
            "sha256": "2abb40d134ef95f8a7492ccda1f2f589f6698a77b9c65618937ada595adfc56f"
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
            "sha256": "90f845521d980d9b52287fc6113cefb285f5385e0497aeb4a20766fd2b7aff55"
          },
          {
            "path": "build/foundation/handoff.md",
            "sha256": "6a1096a19c022defafacfa9e44404dc12283b8d668809efd7734336cd6ef3fc0"
          },
          {
            "path": "build/foundation/design-validation.json",
            "sha256": "4ad389ca096ec75feadfff2411d14e38a2f38aa8fabee8a0e7057fdbda7cd44b"
          }
        ],
        "repository_baseline": "Observe confirmed public repo; bootstrap records actual base HEAD; foundation starts isolated branch at that exact HEAD",
        "prerequisite_outputs": "Freeze actual native-parent output/oracle digests; missing/stale blocks; baseline distribution interfaces are separately frozen accepted prerequisites",
        "native_contract": "Freeze accepted sole native-contract bytes digest and stable identity table before claim; no self-hash embedded in authoring metadata"
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
        "payload-inventory.json"
      ],
      "read_scope": [
        "spec/**",
        "build/foundation/**",
        "tests/fixtures/**",
        "locked tool/dependency sources",
        "declared native-parent outputs"
      ],
      "commands": [
        "C_FOUNDATION",
        "C_FOUNDATION_TESTS",
        "C_CI_HEAD",
        "C_CI_CHECKS"
      ],
      "acceptance": "Allowlisted payload plus bounded validator/independent fixtures/read-only pinned-action CI committed in isolated branch; exactly one leaf issue and native seed parent, draft PR; exact-head checks pass and actual fixed gpt-6-luna receipt retained; no merge/release/deploy/consumer edit.",
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
        "Python 3.12",
        "isolated worktree",
        "resolved lock/tool fingerprints",
        "actual supported model/settings/context and permissions if inference required"
      ],
      "permission_requirements": [
        "Explicitly approved central scaffold/issue/draft-PR only",
        "bootstrap direct-main exception exactly README/LICENSE if repo empty",
        "no merge/release/deploy/wiki/consumer edits/credentials/infra charges"
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
      "state": "planned-not-dispatched"
    }
  ]
}
```
