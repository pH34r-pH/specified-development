---
schema_version: 1
document_id: specified-development/distribution
role: feature
feature_id: distribution
revision: 2
target_status: mature-complete-product
approval_status: architecture-approved
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
qualifiers: [delegated-user-directive, living-spec-paradigm]
---

# Reusable repository specification lifecycle

## Product description

The distribution gives pH34r-pH's repositories one reusable specification lifecycle. Research and ideas remain free-form Markdown; minimal POCs answer only recorded questions that could invalidate a design decision. Once a product is mature, its specification describes the complete product in present tense and remains living, enduring documentation that is revised in place as the product changes. Approval, intended target, implemented source, passing tests, deployment and regeneration evidence have distinct fields and provenance.

The lifecycle advances through `spec → plan → tests → tasks` using accepted immutable inputs. Specifications, contracts, fixtures, dependency locks and generation instructions are authoritative; code is retained as a regenerable artifact. Each executable leaf is a bounded compilation action with a qualified stable identity, frozen inputs, output scope, acceptance, and one model fixed for the task and its admitted retries. Native hard dependencies govern dispatch in the selected existing execution system. Deterministic scripts handle mechanical work and cost reporting after semantic decomposition.

## Actors and acceptance scenarios

| Story | Actor and outcome | Independent acceptance scenarios |
| --- | --- | --- |
| US1 | A designer records mature intent as living documentation | AS1: given an accepted idea/research package, the specification describes the complete product with measurable behavior and explicit exclusions; no MVP reduction is introduced. AS2: given present-tense specified behavior without test or deployment receipts, delivery remains designed-only. |
| US2 | A maintainer installs and upgrades a consistent distribution | AS1: a clean initialized repository receives the approved pinned components and effective agent assets. AS2: an existing installation with wrong-version components, conflicting local overrides or generated-asset drift fails verification before use. AS3: a failed staged upgrade or recovery preserves prior accepted assets and history. |
| US3 | A planner/test designer produces accepted artifacts | AS1: tasks authoring is rejected if accepted fresh tests or an upstream revision is absent. AS2: a changed spec invalidates affected downstream artifacts while preserving prior revisions and receipts. AS3: tests have independent expected behavior, acceptance/requirement traceability and test-before-production dependencies. |
| US4 | An operator projects and dispatches bounded work | AS1: each executable leaf maps to exactly one stable issue identity and native prerequisites; epics group leaves without becoming scheduler gates. AS2: a repeated or partial projection converges without duplicates or premature readiness. AS3: a rejected or missing selected-model admission, required unsupported hard capability, missing permission, stale input or ambiguous design blocks dispatch and produces a bounded repair/handoff. |
| US5 | A worker completes a fixed-input compilation action | AS1: out-of-scope edits, changed input hashes, undeclared commands, missing acceptance evidence or a model switch prevent accepted completion. AS2: a missing behavioral decision produces a separate spec-repair task and invalidates affected descendants after an approved revision. |
| US6 | A maintainer proves scoped regeneration and reports cost | AS1: code regeneration in independent clean workspaces passes the independent behavioral contract before any scoped disposability claim. AS2: all attempts, cached input, output including reasoning, dated prices and missing fields are reported without double counting or invented billing. AS3: an exact valid cache hit avoids repeated semantic/model work and still revalidates acceptance. |
| US7 | A maintainer onboards an existing project into the living-spec lifecycle | AS1: given a repository with code and no specification, one bounded area is characterized into a reviewed present-tense specification while every other path stays explicitly unspecified and produces no gaps. AS2: a known defect found during characterization is recorded either as specified actual behavior with a follow-up change or as specified intended behavior in the initial gap list; an unrecorded defect blocks acceptance. AS3: after acceptance, an independent case whose expected value is derived from implementation output is rejected, and requirements without passing evidence form the initial gap list. AS4: an existing Spec Kit layout maps into the canonical tree with feature history and constitutions preserved. |

## Functional requirements

| ID | Required observable behavior |
| --- | --- |
| FR-001 | Research and ideas stay free-form until mature design; each optional POC names the decision, invalidating outcome, minimum experiment and stopping condition. |
| FR-002 | Specs describe the complete product directly in present tense as living documentation revised in place, preserve enduring behavioral documentation, and keep target/approval status separate from implementation, test, deployment and regeneration evidence. Prose tense never advances delivery status. |
| FR-003 | Artifact progression enforces accepted fresh `spec → plan → tests → tasks` revisions; contradictions return to their earliest authority. |
| FR-004 | Immutable artifact revisions identify upstream input hashes; changes retain history and invalidate only changed task contracts and their dependency descendants. |
| FR-005 | Installation identifies exact upstream/component versions, source/asset digests, active integration, effective overrides and generated assets; wrong versions or unapproved drift prevent use. |
| FR-006 | Upgrades are staged, reviewed as a concrete diff, and recoverable from verified rollback artifacts after interrupted promotion or failure. Local domain rules and retained history survive. |
| FR-007 | All acceptance scenarios, requirements and buildable success criteria have independent test cases or a spec-approved exclusion; existing behavior changes have expected RED evidence before production changes. |
| FR-008 | Semantic decomposition emits prose and complete structured leaf metadata in one authoring pass. Subsequent projection and validation do not call a model or derive new behavior. |
| FR-009 | Qualified stable IDs survive retries and projection and avoid cross-feature/repository `T001` collisions; each executable leaf has exactly one issue identity; groups remain non-executable. |
| FR-010 | Existing execution-contract dependency/test/path/command/evidence meanings are preserved; one existing execution owner schedules a run, with native hard dependencies and no parallel queue or ledger. |
| FR-011 | Issue projection is default-dry, idempotent, bounded to the verified target and authorized immutable creator, and does not mark tasks ready before all bindings, native edges, inputs and execution-policy checks are complete. |
| FR-012 | Each leaf freezes authoritative inputs and prerequisite outputs, exact editable/protected scope, permitted commands, acceptance predicates, reasoning class, typed requested/advisory or required-hard budgets, and an execution/model evidence profile before dispatch. |
| FR-013 | A task retains one approved exact model selection and parent/service admission across its initial attempt and admitted retries. Selection is distinct from nullable effective runtime telemetry; actual permissions and required correctness/hard capabilities are enforced. Rejected request options block; unexposed effective values are recorded honestly under the selected capability profile. A different model requires a separately reviewed repair/task identity; it is not a retry of the original task. |
| FR-014 | Missing design assumptions produce a separate upstream repair task with a durable bounded failure packet. Completion or retry cannot silently change behavior, scope, model or input revisions. |
| FR-015 | Accepted completion requires current artifact/contract hashes, allowed changed paths, declared command evidence, targeted/regression results and any prescribed review verdict. RED-only test leaves require an expected missing-behavior failure. |
| FR-016 | The retained authoritative package includes contracts, fixtures, dependency locks, generation instructions and provenance sufficient for isolated regeneration; source code is never deleted automatically. |
| FR-017 | Scoped behavioral regeneration uses clean isolated workspaces without reading retained production implementation, and passes independent tests with model/tool/dependency/environment fingerprints and all attempt evidence. Claims name only the proven scope. |
| FR-018 | Cache keys cover semantic inputs, prerequisite outputs, commands/test oracle, policy, tool/dependency locks and environment compatibility. Stale, failed, unauthorized or unknown entries are rejected; valid hits retain provenance and recheck current acceptance. |
| FR-019 | Cost reports use observed token-price equivalent with dated source-backed rate cards, keep cached tokens as a subset of input and reasoning as a subset of output, and count retries and failed attempts. Missing usage or pricing stays explicit and never implies zero. |
| FR-020 | Subscription allowance, API-equivalent comparison cost and actual invoiced charges are separate. No credential creation, API-billing fallback, automatic model router or new infrastructure is introduced. |
| FR-021 | Compatibility gates cover existing first legacy installation/existing native-contract installations and the existing executor/GitHub and Kanban boundaries, preserving local constitutions, feature naming, historical artifacts and selected execution ownership. |
| FR-022 | Rollout requires source/manifest verification, positive component resolution, full compatibility/recovery checks, a coherent isolated pilot, scoped regeneration evidence and repository-specific acceptance before activation. |
| FR-023 | Brownfield onboarding characterizes one bounded area at a time into a present-tense specification and plan with recorded sources per requirement. Characterization mode is the only permitted derivation of specification from implementation; it ends when a human reviewer accepts the specification, after which code is evidence rather than authority. Paths outside onboarded areas are explicitly unspecified and produce no gaps. |
| FR-024 | Each onboarded area has an onboarding record with repository, exact baseline revision, area paths, characterization sources for every accepted requirement, an explicit specify-actual or specify-intended decision for every known defect, independent oracle sources, acceptance actor and time, initial gaps and any existing Spec Kit layout mapping. Validation rejects untraced requirements, undecided defects, intended-behavior decisions missing from the gap list, oracle values derived from implementation output, and layout mappings that do not preserve history and constitutions. |

## Success criteria

| ID | Observable measure |
| --- | --- |
| SC-001 | Every valid package traverses all four artifact gates; all missing/stale/unaccepted upstream and delivery-status-confusion fixtures are rejected. |
| SC-002 | Every supported installation matches its approved versions and effective/generated asset digests; every injected interrupted upgrade restores the exact prior accepted scoped files without losing unrelated files or history. |
| SC-003 | 100% of acceptance scenarios, FRs and buildable SCs trace to independently defined tests; orphan tests and implementation leaves lacking test prerequisites are rejected. |
| SC-004 | The projection produces one identity per executable leaf, exactly the native hard-dependency edge set, and no runnable issues after an incomplete failed projection. Reprojection is byte-stable locally and duplicate-free remotely. |
| SC-005 | Model change, unavailable required capability, missing permission, input drift, scope violation and incomplete receipt fixtures all fail closed; repair reopens only affected authority descendants. |
| SC-006 | Two independent clean-workspace regenerations of the declared pilot scope pass the same independent behavioral/regression contract; all attempts and environment/input fingerprints are retained. |
| SC-007 | Golden cost cases match exact decimal results; input/cache and output/reasoning overlap are counted once; unknown or incomplete cases remain visibly incomplete. Validation, projection, accounting and cache-hit processing invoke zero models. |
| SC-008 | Pilot and migration fixtures preserve domain instructions and history, and make no repository/external writes or billing-route changes without the relevant authorization. |
| SC-009 | A synthetic brownfield example onboards one area with an accepted record, an initial gap list and an unspecified remainder; every named invalid onboarding record fixture is rejected with a stable diagnostic. |

## Boundaries and assumptions

The distribution owns common workflow assets and deterministic artifact tooling. Domain requirements, technical stacks, constitutions, existing code, scheduling/claiming/retries, permissions and infrastructure stay with their established owners. Complete product scope does not mean concurrent rollout to every repository.

No code deletion, repository/fork creation, GitHub publication, deployment, credentials, charges, worker/model switch, routing service or generic agent framework is authorized by this specification alone. A scoped implementation directive authorizes its concrete implementation; publication and execution-system activation remain separately observable gates. The user-approved architecture supplies design intent; candidate artifact approval does not become human acceptance merely because a script validates it.
