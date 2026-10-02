---
document_id: specified-development/distribution
feature_id: distribution
artifact: specification
revision: 1
target_status: mature-complete-product
architecture_approval: delegated-user-directive
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
---

# Reusable repository specification lifecycle

## Completed-product description

The distribution gave pH34r-pH's repositories one reusable specification lifecycle. Research and ideas remained free-form Markdown; minimal POCs answered only recorded questions that could invalidate a design decision. Once the intended product was mature, its specification described that complete product in past tense and remained enduring documentation. Approval, intended target, implemented source, passing tests, deployment, and regeneration evidence had distinct fields and provenance.

The lifecycle advanced through `spec → plan → tests → tasks` using accepted immutable inputs. Specifications, contracts, fixtures, dependency locks, and generation instructions were authoritative; code was retained as a regenerable artifact. Each executable leaf was a bounded compilation action with a qualified stable identity, frozen inputs, output scope, acceptance, and one model fixed for the task and its admitted retries. Native hard dependencies governed dispatch in the selected existing execution system. Deterministic scripts handled mechanical work and cost reporting after semantic decomposition.

## Actors and acceptance scenarios

| Story | Actor and completed outcome | Independent acceptance scenarios |
| --- | --- | --- |
| US1 | A designer recorded mature intent and enduring documentation | AS1: given an accepted idea/research package, specification described the complete intended product with measurable behavior and explicit exclusions; no MVP reduction was introduced. AS2: given past-tense target prose without test/deployment receipts, delivery remained designed-only. |
| US2 | A maintainer installed and upgraded a consistent distribution | AS1: a clean initialized repository received the approved pinned components and effective agent assets. AS2: an existing installation with wrong-version components, conflicting local overrides, or generated-asset drift failed verification before use. AS3: failed staged upgrade or recovery preserved prior accepted assets and history. |
| US3 | A planner/test designer produced accepted artifacts | AS1: tasks authoring was rejected if accepted fresh tests or an upstream revision was absent. AS2: a changed spec invalidated affected downstream artifacts while preserving prior revisions and receipts. AS3: tests had independent expected behavior, acceptance/requirement traceability, and test-before-production dependencies. |
| US4 | An operator projected and dispatched bounded work | AS1: each executable leaf mapped to exactly one stable issue identity and native prerequisites; epics grouped leaves without becoming scheduler gates. AS2: a repeated/partial projection converged without duplicates or premature readiness. AS3: a rejected/missing selected-model admission, required unsupported hard capability, missing permission, stale input, or ambiguous design blocked dispatch and produced a bounded repair/handoff. |
| US5 | A worker completed a fixed-input compilation action | AS1: out-of-scope edits, changed input hashes, undeclared commands, missing acceptance evidence, or a model switch prevented accepted completion. AS2: a missing behavioral decision produced a separate spec-repair task and invalidated affected descendants after approved revision. |
| US6 | A maintainer proved scoped regeneration and reported cost | AS1: code regeneration in independent clean workspaces passed the independent behavioral contract before any scoped disposability claim. AS2: all attempts, cached input, output including reasoning, dated prices, and missing fields were reported without double counting or invented billing. AS3: an exact valid cache hit avoided repeated semantic/model work and still revalidated acceptance. |

## Functional requirements

| ID | Required observable behavior (completed-product semantics) |
| --- | --- |
| FR-001 | Research/ideas stayed free-form until mature design; each optional POC named the decision, invalidating outcome, minimum experiment, and stopping condition. |
| FR-002 | Specs described the complete intended product directly in past tense, preserved enduring behavioral documentation, and kept target/approval status separate from implementation/test/deployment/regeneration evidence. |
| FR-003 | Artifact progression enforced accepted fresh `spec → plan → tests → tasks` revisions; contradictions returned to their earliest authority. |
| FR-004 | Immutable artifact revisions identified upstream input hashes; changes retained history and invalidated only changed task contracts and their dependency descendants. |
| FR-005 | Installation identified exact upstream/component versions, source/asset digests, active integration, effective overrides, and generated assets; wrong versions or unapproved drift prevented use. |
| FR-006 | Upgrades were staged, reviewed as a concrete diff, and recoverable from verified rollback artifacts after interrupted promotion or failure. Local domain rules and retained history survived. |
| FR-007 | All acceptance scenarios, requirements, and buildable success criteria had independent test cases or a spec-approved exclusion; existing behavior changes had expected RED evidence before production changes. |
| FR-008 | Semantic decomposition emitted prose and complete structured leaf metadata in one authoring pass. Subsequent projection/validation did not call a model or derive new behavior. |
| FR-009 | Qualified stable IDs survived retries/projection and avoided cross-feature/repository `T001` collisions; each executable leaf had exactly one issue identity; groups remained non-executable. |
| FR-010 | Existing execution-contract dependency/test/path/command/evidence meanings were preserved; one existing execution owner scheduled a run, with native hard dependencies and no parallel queue or ledger. |
| FR-011 | Issue projection was default-dry, idempotent, bounded to the verified target and authorized immutable creator, and did not mark tasks ready before all bindings, native edges, inputs, and execution-policy checks were complete. |
| FR-012 | Each leaf froze authoritative inputs and prerequisite outputs, exact editable/protected scope, permitted commands, acceptance predicates, reasoning class, typed requested/advisory or required-hard budgets, and an execution/model evidence profile before dispatch. |
| FR-013 | A task retained one approved exact model selection and parent/service admission across its initial attempt and admitted retries. Selection was distinct from nullable effective runtime telemetry; actual permissions and required correctness/hard capabilities were enforced. Rejected request options blocked; unexposed effective values were recorded honestly under the selected capability profile. A different model required a separately reviewed repair/task identity; it was not a retry of the original task. |
| FR-014 | Missing design assumptions produced a separate upstream repair task with a durable bounded failure packet. Completion or retry could not silently change behavior, scope, model, or input revisions. |
| FR-015 | Accepted completion required current artifact/contract hashes, allowed changed paths, declared command evidence, targeted/regression results, and any prescribed review verdict. RED-only test leaves required an expected missing-behavior failure. |
| FR-016 | The retained authoritative package included contracts, fixtures, dependency locks, generation instructions, and provenance sufficient for isolated regeneration; source code was never deleted automatically. |
| FR-017 | Scoped behavioral regeneration used clean isolated workspaces without reading retained production implementation, and passed independent tests with model/tool/dependency/environment fingerprints and all attempt evidence. Claims named only the proven scope. |
| FR-018 | Cache keys covered semantic inputs, prerequisite outputs, commands/test oracle, policy, tool/dependency locks, and environment compatibility. Stale/failed/unauthorized/unknown entries were rejected; valid hits retained provenance and rechecked current acceptance. |
| FR-019 | Cost reports used observed token-price equivalent with dated source-backed rate cards, kept cached tokens as a subset of input and reasoning as a subset of output, and counted retries/failed attempts. Missing usage/pricing stayed explicit and never implied zero. |
| FR-020 | Subscription allowance, API-equivalent comparison cost, and actual invoiced charges were separate. No credential creation, API-billing fallback, automatic model router, or new infrastructure was introduced. |
| FR-021 | Compatibility gates covered existing first legacy installation/existing native-contract installations and the existing executor/GitHub and Kanban boundaries, preserving local constitutions, feature naming, historical artifacts, and selected execution ownership. |
| FR-022 | Rollout required source/manifest verification, positive component resolution, full compatibility/recovery checks, a coherent isolated pilot, scoped regeneration evidence, and repository-specific acceptance before activation. |

## Success criteria

| ID | Observable measure |
| --- | --- |
| SC-001 | Every valid package traversed all four artifact gates; all missing/stale/unaccepted upstream and delivery-status-confusion fixtures were rejected. |
| SC-002 | Every supported installation matched its approved versions and effective/generated asset digests; every injected interrupted upgrade restored the exact prior accepted scoped files without losing unrelated files/history. |
| SC-003 | 100% of acceptance scenarios and FRs and buildable SCs traced to independently defined tests; orphan tests and implementation leaves lacking test prerequisites were rejected. |
| SC-004 | The projection produced one identity per executable leaf, exactly the native hard-dependency edge set, and no runnable issues after an incomplete failed projection. Reprojection was byte-stable locally and duplicate-free remotely. |
| SC-005 | Model change, unavailable required capability, missing permission, input drift, scope violation, and incomplete receipt fixtures all failed closed; repair reopened only affected authority descendants. |
| SC-006 | Two independent clean-workspace regenerations of the declared pilot scope passed the same independent behavioral/regression contract; all attempts and environment/input fingerprints were retained. |
| SC-007 | Golden cost cases matched exact decimal results; input/cache and output/reasoning overlap were counted once; unknown/incomplete cases remained visibly incomplete. Validation/projection/accounting/cache-hit processing invoked zero models. |
| SC-008 | Pilot and migration fixtures preserved domain instructions and history, and made no repository/external writes or billing-route changes without the relevant authorization. |

## Boundaries and assumptions

The distribution owned common workflow assets and deterministic artifact tooling. Domain requirements, technical stacks, constitutions, existing code, scheduling/claiming/retries, permissions, and infrastructure stayed with their established owners. Complete product scope did not mean concurrent rollout to every repository.

No code deletion, repository/fork creation, GitHub publication, deployment, credentials, charges, worker/model switch, routing service, or generic agent framework was authorized by this design pass. A later scoped implementation directive could authorize its concrete implementation; publication and execution-system activation remained separately observable gates. The user-approved architecture supplied design intent; candidate artifact approval did not become human acceptance merely because a script validated it.
