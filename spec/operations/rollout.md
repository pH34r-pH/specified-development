---
schema_version: 1
document_id: specified-development/rollout
role: operation
revision: 2
target_status: mature-complete-product
approval_status: architecture-approved
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: []
---

# Ownership, pilot, and rollout gates

`pH34r-pH/specified-development` owns common original tooling, documentation, fixtures and releases under Apache-2.0. Consumer constitutions and domain rules, and the existing execution owner's infrastructure, remain with their owners. GitHub Releases are the planned archive/checksum/lock distribution channel; no hosted service, credentials or new infrastructure charges are needed for the foundation.

Adoption has two tracks. **Core adoption** brings a repository onto the living-spec paradigm with the [adoption kit](https://github.com/pH34r-pH/specified-development/blob/main/kit/README.md), the brownfield onboarding procedure and the requirement gap report, installed from a pinned reviewed commit; it does not wait for component releases, staged recovery, cost accounting or publication. **Distribution adoption** installs the packaged preset, extension and bundle and keeps the full G1–G4 path. Both tracks adopt one repository at a time through its own scoped, consumer-owned PR.

The brownfield pilot qualifies core adoption. It onboards one bounded area of a real existing codebase in an isolated copy: an accepted present-tense specification and plan, a valid onboarding record, independent tests, an initial gap list, one spec-first change propagated end to end through the gap report, and one scoped regeneration trial of the onboarded area. The pilot records each of these as evidence and makes no change to the original repository.

The smallest coherent distribution pilot uses a synthetic complete mature product with two features and a shared contract/asset, plus isolated sanitized copies of two existing Spec Kit installations. It tests the whole lifecycle, source directory, replacement commands, native execution/issue dry projection, receipts, cache/cost, staged upgrade/recovery and scoped behavioral regeneration. The product specification stays complete; only the pilot's environmental scope is small.

| Gate | Evidence and permitted boundary |
| --- | --- |
| G0 Foundation | Confirmed destination/license; allowlisted generic payload; exact-head CI; draft PR. No release, consumer mutation or deployment. |
| G1 Distribution | Pinned upstream/toolchain/dependencies/components, digests, licenses and clean source build; staged inventory and effective integration assets. |
| G2 Directory | Independent discovery/closure/link/asset/source-map/freshness/retention tests; repository and optional renderer parity; no undocumented adapter behavior. |
| G3 Recovery | Wrong version/tamper/interrupted promotion/rollback and concurrent edit tests with exact restoration proof. |
| G4 Complete pilot | Complete isolated synthetic lifecycle and existing-installation compatibility; independent source-excluded regeneration proof restricted to the declared module. |
| GB Brownfield pilot | Isolated copy of one real codebase: accepted onboarding record, independent tests and initial gaps; one spec-first change whose gap report lists exactly the changed requirements and their stale descendants; one scoped regeneration trial of the onboarded area. No write to the original repository. |
| G5a Core adoption | Requires G0, the pinned adoption kit, the brownfield onboarding procedure, the gap report and GB evidence. Does not require G1 archives or releases, G3 staged recovery, cost accounting or publication. A separate consumer-owned scoped PR onboards one area; no automatic broad rollout. |
| G5b Distribution adoption | Requires G1–G4. A separate consumer-owned scoped PR reconciles authority/history, existing features, active agent assets, accepted build retention and permissions. No automatic broad rollout. |
| G6 Activation | The existing owner positively enforces exact model/settings/permissions, native parents, RED-only/no-code leaves, pagination and completion predicates. Unsupported cases remain blocked; no second scheduler. |
| G7 Publication | Exact reviewed release/site/wiki destination and source/public inventory, qualified renderer/lock, auth, before-hash drift check and rollback; independent authorization per requested publication. |

Every consumer adoption is separate from application implementation and separately coordinated with its current owner. Onboarding many repositories is a sequence of individually reviewed adoptions. For onboarded areas, scoped regeneration trials recur as a specification-completeness health check: a trial that cannot reproduce compatible behavior from the artifacts identifies a specification or plan gap, not a reason to read retained code. Public evidence excludes private project research, credentials, infrastructure topology and raw logs. Successful rendering does not prove behavioral regeneration or deployment. Code remains retained throughout.
