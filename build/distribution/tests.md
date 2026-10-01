---
artifact: independent-test-contract
revision: 1
inputs: [spec.md, plan.md, contracts/distribution.md]
acceptance: candidate-review
execution_evidence: none-product-not-built
---

# Independent test contract

The oracle below was derived from accepted-intent behavior and the declared interfaces, before production implementation. Expected outcomes must not be computed by calling the production implementation or copied from its output. Golden artifact/edge/cost fixtures are authored independently and reviewed with this contract. Test fixtures are synthetic or sanitized installation assets; no private application data, cloud credentials, live deployment, or paid inference belongs in the default suite.

Default environment E1: Python 3.12, locked dependencies, `unittest`, temporary isolated filesystem, fake GitHub/process/worker responses, no network/model calls. E2: pinned upstream CLI in a disposable initialized checkout, active Claude then Codex integration, no authentication store or external mutation. E3: approved existing model/runtime in two independent clean regeneration workspaces, retained source denied, real observed identity and all attempt receipts. E3 is a gated qualification, not part of this design pass or ordinary unit tests.

Each row defines its complete stable case: level/environment, traces, preconditions/fixtures, stimulus, independent observable result, exact planned test path and test-authoring → implementation/qualification leaf. CLI outcomes use the exit/error classifications in contracts/distribution.md. All rows include boundary/negative cases rather than implementation-mirroring assertions.

| Case | Level / env; traces | Preconditions and stimulus | Expected observable result | Planned path; leaf mapping |
| --- | --- | --- | --- | --- |
| TST-001 | static/contract E1; US1-AS1, FR-001/002, SC-001 | Mature full-product fixture plus idea/POC record. Author/render through installed instructions; inject automatic MVP reduction or unbounded POC. | Full intended behavior and explicit exclusions retained; POC has named invalidating outcome/minimum scope/stop. Semantic review rejects scope reduction; deterministic lint flags contrary instruction text but does not claim it proves maturity. | `tests/test_templates.py`; T002 → T003; review/handoff T033 |
| TST-002 | contract E1; US1-AS2, FR-002, SC-001 | Past-tense spec, approved target, empty delivery receipts; then inject unverified deployment/implementation status. | Designed-only remains visible; no accepted delivery claim without matching observed receipts. Prose tense never advances delivery. | `tests/test_templates.py`; T002 → T003; review/handoff T033 |
| TST-003 | contract E1; US3-AS1, FR-003, SC-001 | Accepted spec/plan; tests missing, candidate, or hash-stale. Invoke tasks preflight, direct CLI and stock workflow route. | All routes reject with upstream repair reference before task authoring or execution; fresh accepted tests permit next gate. | `tests/test_gates.py`; T004 → T005 |
| TST-004 | integration E1; US3-AS2, FR-004, SC-001/005 | Three-leaf graph, retained revisions/receipts. Change one task's spec input and then an unrelated artifact. | Only changed contract and transitive dependents stale; independent receipt/revision remains queryable; stale descendant cannot complete. | `tests/test_gates.py`; T004 → T005 |
| TST-005 | contract E1; US6-AS1, FR-016, SC-006 | Regeneration input inventory missing each contract/fixture/lock/instruction in turn; then complete inventory. | Missing authoritative input blocks qualification with exact missing field; complete package is usable without retained implementation as an input. No source deletion occurs. | `tests/test_regeneration.py`; T024 → T025 |
| TST-006 | integration E2; US2-AS1/AS2, FR-005, SC-002 | Pinned CLI and independently installed wrong-version component; corrupt archive or remove advertised version/digest. | Verifier rejects each mismatch/unknown even if stock bundle install reports skip/success; exact approved install matches component and asset inventory. | `tests/test_installation.py`; T016 → T017 |
| TST-007 | integration E2; US2-AS1/AS2, FR-005/021, SC-002 | Approved preset, conflicting local override, altered materialized Claude/Codex skill, inactive integration switch. | Effective stack and active generated assets match approved hashes; drift/conflict blocks; switching verifies newly materialized assets and preserves local domain instructions. | `tests/test_compatibility.py`; T022 → T023/T031 |
| TST-008 | recovery E2; US2-AS3, FR-006, SC-002 | Exact old snapshot plus unrelated sentinel. Inject failure at every staged/promotion journal operation and failed preset replacement. | Prior managed files/bytes/modes, records, and sentinels restored; introduced installation assets only reconciled per journal; application source/history preserved. Unproved rollback fails closed with retained evidence. | `tests/test_upgrade.py`; T018 → T019 |
| TST-009 | static/contract E1; US3-AS3, FR-007, SC-003 | Hand-authored full coverage matrix; remove a scenario/FR/SC trace, introduce orphan test, or copy oracle from implementation. | Complete traces pass; missing/orphan rows reject; independent-oracle review detects production-derived expectation. No exclusion exists in this release target. | `tests/test_metadata.py`; T006 → T007; review/handoff T033 |
| TST-010 | contract E1; US4-AS3, FR-008/012, SC-003/005 | Structured leaf missing each required semantic field, ambiguous output, cycle, undeclared parent/command, writable overlap. | Reject before projection/claim; complete prose+metadata agrees. Deterministic validation/projecting invokes zero models and never supplies missing semantics. | `tests/test_metadata.py`; T006 → T007 |
| TST-011 | contract E1; US4-AS1, FR-009, SC-004 | Two repositories/features each with local T001, retry/rename fixture, group record. Project twice. | Qualified identities distinct and stable, one marker/issue plan per executable leaf, no executable issue for groups; namespace unaffected by host rename. | `tests/test_projection.py`; T008 → T009 |
| TST-012 | integration E1; US4-AS1, FR-010, SC-004 | existing native-contract-v1 handwritten edge golden and Kanban-v1 aggregate binding fixture; parent closure/sub-issue-only grouping. | Exact native parent edge set; sub-issues supply no readiness; legacy successor still waits on aggregate. One execution owner chosen, unsupported/ambiguous profile rejects. | `tests/test_projection.py`; T008 → T009; review/handoff T033 |
| TST-013 | contract E1; US4-AS2, FR-011, SC-004 | Fake >100 issues/dependencies, duplicate marker, partial creates/edge writes, replay after crash. | Complete pagination; numeric issue IDs used for API edges; readback exact; no duplicates, drift rejected, deterministic local export byte-stable; incomplete leaves never made ready. | `tests/test_issues.py`; T020 → T021 |
| TST-014 | security E1; US4-AS2/AS3, FR-011/021/022, SC-004/008 | App-created issue versus authorized user; wrong remote, absent Issues permission, early ready label, stale remote edit or extra edge. | Dry mode makes zero mutations. Apply blocks unauthorized immutable creator/target/permission/staleness; owned affected readiness withheld/withdrawn under authorized repair; no blocked/runnable labels or scheduler side effects. | `tests/test_issues.py`; T020 → T021; review/handoff T033, T036 |
| TST-015 | security/contract E1; US5-AS1, FR-012/015, SC-005 | Frozen inputs plus parent outputs. Alter hash, add command, modify protected path/rename destination, or escape root. | Receipt/preflight rejects each before accepted completion; declared exact scope and current command receipts pass. No receipt can expand authority. | `tests/test_receipts.py`; T010 → T011 |
| TST-016 | runtime-contract E1; US4-AS3, FR-013/020, SC-005/008 | Configured default without observed model; unavailable `gpt-6.1-luna`; then explicitly approved `gpt-6-luna` binding, reasoning/speed tier request, changed model mid-attempt, unsupported settings. | Unavailable alias rejects; fixed-model-v3 low-cost default is explicitly approved gpt-6-luna, with no future 5.6 assignment or historical rewrite. Only observed available exact binding admits an attempt; reasoning/speed requests are preserved, model switch rejects receipt, unsupported settings block instead of generating flags; deterministic leaves forbid inference. | `tests/test_receipts.py`; T010 → T011; review/handoff T033 |
| TST-017 | integration E1; US5-AS2, FR-014/004, SC-005 | Two repeated bounded missing-behavior packets under same task/contract; accept a separate earliest-authority repair. | Existing owner receives one repair identity, original attempt stops without model change; approved revision invalidates affected descendants and preserves unrelated evidence. Distribution creates no retry/resume loop. | `tests/test_gates.py`; T004 → T005 |
| TST-018 | contract E1; US3-AS3/US5-AS1, FR-007/015, SC-003/005 | RED leaf with expected missing behavior vs syntax/fixture/permission error; GREEN without regression/review. | Only intended RED can close test leaf; production requires its closed test prerequisite and prescribed GREEN/regression/review receipts. Missing evidence never terminalizes acceptance. | `tests/test_receipts.py`; T010 → T011 |
| TST-019 | behavioral E3; US6-AS1, FR-016/017, SC-006 | Complete frozen packet; two empty independent workspaces and fresh contexts; original gate.py retained outside denied scope. Generate both trials under one approved exact model binding for the entire T032 attempt, excluding first-trial source from the second. | Both independently pass same gate behavioral/regression oracle; allowed-read inventory proves original and prior-trial implementation excluded; normalized outputs match; every failed trial retained; claim names gate.py only. Source retained and no full-repo disposability claim. | `tests/test_regeneration.py`; T024 → T025/T032; review/handoff T033 |
| TST-020 | contract E1; US6-AS3, FR-018, SC-007 | Accepted cold attempt/cache artifact; vary inputs, parent outputs, oracle, command, lock, model policy, environment and permission; exact hit. | Every relevant change/unknown/failed artifact is miss/block with reason. Exact hit revalidates acceptance and scoped commands with zero inference, retains origin provenance, never imports secrets/task state. | `tests/test_cache.py`; T012 → T013 |
| TST-021 | arithmetic E1; US6-AS2, FR-019, SC-007 | Inclusive I1000/C200/O500/R100 and synthetic rates 2/0.5/8; provider fixture excludes cache/reasoning in base fields. | Exact string 0.0057 USD; normalization yields inclusive counts with documented transform; cached input and reasoning counted once; C>I or R>O rejects. | `tests/test_cost.py`; T014 → T015 |
| TST-022 | contract E1; US6-AS2, FR-019/020, SC-007/008 | Missing rate or token fields, dated-tier mismatch, C=0 vs unknown C, subscription vs invoice records. | Missing cache rate with C200 yields null total and known subtotal 0.0056; explicit missing fields. Observed C0 needs no cache-rate product. Tier/date mismatch rejects; API-equivalent never labeled actual charge; no API fallback. | `tests/test_cost.py`; T014 → T015; review/handoff T033 |
| TST-023 | contract/performance E1; US6-AS2/AS3, FR-008/019, SC-007 | Successful/failed/retry attempts, duplicate attempt identity, incomparable cards/cohorts; instrument model-call fake. | Unique attempts counted once; failed/retry usage included; incomplete total visibly incomplete; only comparable complete cost per accepted leaf; validation/projection/accounting/cache-hit make zero model calls. | `tests/test_cost.py`; T014 → T015/T031 |
| TST-024 | compatibility E2; US2-AS1/US4-AS3, FR-021/010, SC-008 | Sanitized first legacy installation/existing native-contract asset snapshots, local authority/feature history, existing executor creator/allowlist/model capability fixture, legacy Kanban aggregate. | Domain rules and retained artifacts unchanged; Claude/Codex active assets correct; existing executor incompatibility/unobserved binding remains explicit block; no queue or existing executor/separately owned infrastructure changes edit. | `tests/test_compatibility.py`; T022 → T023/T031; review/handoff T034, T036 |
| TST-025 | end-to-end E2; US2-AS3/US6-AS1, FR-022/006, SC-002/008 | Complete synthetic mature feature, isolated first legacy installation copy, stage failure, dry issue plan, unobserved model/public destination and per-repo adoption records. | Full product lifecycle passes deterministic gates; inference/activation/publication remain blocked where evidence/authorization absent. Complete readiness requires qualification including TST-019; no existing-repo/cloud writes. | `tests/test_pilot.py`; T030 → T031/T035/T036; review/handoff T034 |
| TST-026 | security E1/E2; US2-AS2/US5-AS1, FR-005/011/012/015/016, SC-002/005/008 | Archive traversal/symlink, absolute path, unapproved catalog/redirect, output/log secret sentinel. | Before mutation/extraction, unsafe sources/scopes reject; bounded reports omit sentinel secrets; rollback source confined. No remote input can add a shell command. | `tests/test_installation.py`; T016 → T017/T019; review/handoff T033 |
| TST-027 | native-schema/integration E2; US2-AS1, FR-005/021/022, SC-002/008 | Actual preset/extension/bundle manifests and component sources; wrong ID/version/missing file/digest, unreachable reference warning, rebuild twice. | Pinned upstream validators parse the selected field shapes; positive references resolve; wrong/unknown source fails release despite stock warnings; source-identical build reproduces declared package hashes. | `tests/test_release.py`; T026 → T027/T035 |
| TST-028 | CLI contract E1; US3-AS1/US4-AS3/US6-AS2, FR-003/008/012/019, SC-001/005/007 | Invoke all documented verbs with valid/malformed/stale inputs and shell-like strings; model/process mutation fake. | Stable typed results/exit codes, trusted argv only; deterministic verbs never launch inference. Missing options/fields do not silently default authority. | `tests/test_cli.py`; T028 → T029 |

## Coverage matrices

| Scenario | Cases |
| --- | --- |
| US1-AS1 / AS2 | TST-001 / TST-002 |
| US2-AS1 / AS2 / AS3 | TST-006, TST-007, TST-024, TST-027 / TST-006, TST-007, TST-026 / TST-008, TST-025 |
| US3-AS1 / AS2 / AS3 | TST-003, TST-028 / TST-004 / TST-009, TST-018 |
| US4-AS1 / AS2 / AS3 | TST-011, TST-012 / TST-013, TST-014 / TST-010, TST-014, TST-016, TST-024, TST-028 |
| US5-AS1 / AS2 | TST-015, TST-018, TST-026 / TST-017 |
| US6-AS1 / AS2 / AS3 | TST-005, TST-019, TST-025 / TST-021, TST-022, TST-023, TST-028 / TST-020, TST-023 |

| Requirement | Cases |
| --- | --- |
| FR-001 | TST-001 |
| FR-002 | TST-001, TST-002 |
| FR-003 | TST-003, TST-028 |
| FR-004 | TST-004, TST-017 |
| FR-005 | TST-006, TST-007, TST-026, TST-027 |
| FR-006 | TST-008, TST-025 |
| FR-007 | TST-009, TST-018 |
| FR-008 | TST-010, TST-023, TST-028 |
| FR-009 | TST-011 |
| FR-010 | TST-012, TST-024 |
| FR-011 | TST-013, TST-014, TST-026 |
| FR-012 | TST-010, TST-015, TST-026, TST-028 |
| FR-013 | TST-016 |
| FR-014 | TST-017 |
| FR-015 | TST-015, TST-018, TST-026 |
| FR-016 | TST-005, TST-019, TST-026 |
| FR-017 | TST-019 |
| FR-018 | TST-020 |
| FR-019 | TST-021, TST-022, TST-023, TST-028 |
| FR-020 | TST-016, TST-022 |
| FR-021 | TST-007, TST-014, TST-024, TST-027 |
| FR-022 | TST-014, TST-025, TST-027 |

| Success criterion | Cases |
| --- | --- |
| SC-001 | TST-001, TST-002, TST-003, TST-004, TST-028 |
| SC-002 | TST-006, TST-007, TST-008, TST-025, TST-026, TST-027 |
| SC-003 | TST-009, TST-010, TST-018 |
| SC-004 | TST-011, TST-012, TST-013, TST-014 |
| SC-005 | TST-004, TST-010, TST-015, TST-016, TST-017, TST-018, TST-026, TST-028 |
| SC-006 | TST-005, TST-019 |
| SC-007 | TST-020, TST-021, TST-022, TST-023, TST-028 |
| SC-008 | TST-014, TST-016, TST-022, TST-024, TST-025, TST-026, TST-027 |

All SCs are buildable qualification criteria. No coverage exclusion is claimed. Contract entity rules are covered as follows: artifact/revision TST-002/003/004/017; task/contract TST-009/010/011/012; installation/release TST-006/007/008/026/027; issue binding TST-013/014; model/receipt TST-015/016/018; cache TST-020; usage/rate card TST-021/022/023; regeneration TST-005/019/025. The final column above is the mandatory TST→task/file matrix.

## Evidence and independence rules

Test-authoring leaves precede their production leaves through native hard dependencies. Expected RED is a missing contractual behavior, not an unrelated import/syntax/fixture failure; the receipt names the expected failure. GREEN records the targeted command and focused regression; release qualification records the complete suite. Test edits changing the oracle return to tests/spec authority, never silently accompany a GREEN implementation leaf.

The independent review leaf T033 reviews oracle derivation, full-product maturity, scope, model enforcement, authority, native edge semantics, security/recovery and cost/regeneration claim limits. A model-assisted review remains subject to an observed capability-qualified fixed model/runtime binding; no model is invoked during deterministic package validation. Product tests above were specified, not executed in this design pass. Local design-validation evidence checks internal completeness, graph/projection equality, links/hashes, and arithmetic fixtures only.
