---
artifact: independent-test-contract
revision: 1
acceptance: candidate-review
implementation_tests_run: false
---

# Independent directory test contract

Expected behavior came from the canonical directory feature and document/authority contracts. This contract preceded leaf decomposition. Tests had no implementation-derived goldens. Positive and negative cases used disposable workspaces/fake remotes and never published or changed consumer repositories. Expected RED meant missing intended behavior; parser/syntax/fixture/environment errors did not qualify.

Each suite recorded test-author RED then unchanged-oracle GREEN and focused regressions from its implementation successor. Integration qualification required the actual pinned upstream/component/renderer locks; unknown versions/capabilities blocked rather than skipping required assertions. Live external-link availability was separate dated evidence, not deterministic CI success.

| ID | Requirements | Success criteria | Suite | Independent input | Oracle |
| --- | --- | --- | --- | --- | --- |
| DIR-001 | DS-FR-001/002/003 | DS-SC-002 | inventory | Registered two-feature tree, roles, unknown file, missing doc, duplicate IDs and case-fold collisions | Exact handwritten inventory; every invalid variant rejects before writes |
| DIR-002 | DS-FR-002 | DS-SC-005 | inventory | Rename feature source while retaining stable doc/requirement IDs; invalid slugs and reused IDs | Logical identity retained, path/hash changed, invalid/reused identities rejected |
| DIR-003 | DS-FR-003/004 | DS-SC-001 | closure | Feature A/B, shared contract C, unrelated D, shuffled input enumeration and dependency cycle | Selected dependency-first C,A only; navigation to B does not select B; cycle fails |
| DIR-004 | DS-FR-003/004/005 | DS-SC-002 | links | Requirement/schema citation missing normative-ref, undeclared closure target, missing schema ref | No hidden normative omission; explicit stable diagnostics |
| DIR-005 | DS-FR-005 | DS-SC-002 | links | Relative links/assets/fragments, traversal, symlink, absolute local path, unsafe scheme | All valid targets resolve; hostile/unknown target rejects with zero mutations |
| DIR-006 | DS-FR-005/013/014 | DS-SC-004 | links | Duplicate/Unicode headings, escaped destinations, image refs and reference-style Markdown links | Pinned renderer-derived anchors and all references validate; ambiguity/collision rejects |
| DIR-007 | DS-FR-004/006 | DS-SC-001 | compile | Hand-authored exact adapter bytes/order; source LF/CRLF/UTF-8 cases and invalid encoding | Two clean runs byte-identical; source slices exactly original bytes; invalid UTF-8 fails |
| DIR-008 | DS-FR-006/009 | DS-SC-001 | compile | Source-map byte ranges and canonical JSON/hash fixture independent of compiler | Ranges recover exact source; canonical lock root matches handwritten oracle; no hash self-cycle |
| DIR-009 | DS-FR-009/010 | DS-SC-003/005 | freshness | Change each source/asset/manifest/lock/template/projector/renderer/consumer-authority fingerprint | Freshness rejects affected change/unknown; accepted history remains unchanged |
| DIR-010 | DS-FR-004/010 | DS-SC-005 | freshness | Edit unrelated feature with unchanged closure; add shared dependency; alter prose seemingly cosmetic | Full revalidation precedes preservation; changed closure/contract native descendants stale only |
| DIR-011 | DS-FR-007 | DS-SC-003 | commands | Disposable upstream scripts using build feature env/no-persist and sibling contracts | All paths in build; no feature.json write; no canonical symlink; guarded read-only adapter |
| DIR-012 | DS-FR-007/008 | DS-SC-003 | commands | Specify/clarify canonical edits; plan/tests/tasks/analyze/implement stale/missing adapter; unsupported stock invocation | Edits hit source atomically; every supported entrypoint and CI rejects drift without prompt dependency |
| DIR-013 | DS-FR-008/015 | DS-SC-003 | commands | Two active integrations; tampered/old materialized commands and local domain constitution | Verified overrides resolve correctly; tamper blocks, local authority retained |
| DIR-014 | DS-FR-011 | DS-SC-002 | retention | Failure injection at every stage/promotion boundary plus concurrent before-hash change | Prior adapter bytes/modes/sentinels intact or proven restored; partial failure never claimed accepted |
| DIR-015 | DS-FR-011/012 | DS-SC-005 | retention | Accepted snapshots/tasks/issue IDs/receipts vs explicit candidate clean inventory | Snapshots append-only; dry/apply cleanup never deletes accepted/code/unknown/symlink paths |
| DIR-016 | DS-FR-012 | DS-SC-005 | retention | git check-ignore for every retained/disposable path and accepted revision receipt | No blanket build ignore; retained paths visible; generated paths disposable explicitly |
| DIR-017 | DS-FR-013 | DS-SC-004 | views | Optional pinned MkDocs config on two-feature source with real links/assets | docs_dir spec/site_dir build/site; normalized source prose/assets match; all renderer links pass |
| DIR-018 | DS-FR-014 | DS-SC-004 | views | Wiki Home/sidebar/reserved-name mapping, collisions, page links/Unicode anchors/assets | Injective deterministic map; exact parity; collision fails before remote calls |
| DIR-019 | DS-FR-014 | DS-SC-004 | views | Fake wiki separate Git remote, unauthorized/missing capability/base drift/direct edits | Dry makes no writes; apply requires authorization/access/current base; drift repair is one-way |
| DIR-020 | DS-FR-015 | DS-SC-002/003 | upgrade | Pinned preset+extension fresh install/existing wrong version; stage upgrade tamper/failure | Active generated assets verified; retained rollback proof; consumer source/authority untouched |
| DIR-021 | DS-FR-016 | DS-SC-006 | pilot | Complete two-feature synthetic product and frozen isolated legacy installation fixtures | Full spec-plan-tests-tasks/native identity/cache/cost compatibility; no extra scheduler/consumer write |
| DIR-022 | DS-FR-010/012/016 | DS-SC-005/006 | pilot | Native contract/qualified ID fixture with same T001 in distinct features; grouping/navigation deps | Exactly one issue per leaf, native hard parents only; no doc/nav scheduling edges |
| DIR-023 | DS-FR-013/014/016 | DS-SC-004/006 | pilot | Public allowlist vs private-path/credential sentinel, source-map audit and dry export | Private/secret sentinel rejects; no original private evidence copied; no automatic publish |
| DIR-024 | DS-FR-001/006/016 | DS-SC-006 | pilot | Compare entire source manifest with acceptance traces and retained-code/regeneration claims | Every requirement covered; rendering not behavioral regeneration proof; no deletion/false delivery claim |

Renderer output expectations were captured from primary documented behavior and the pinned renderer in isolation, reviewed before implementation. They included repository/site/wiki fragment differences; no invented universal anchor rule passed by construction. Source-byte equality and output link behavior were both required. Wiki remote fixtures explicitly exercised complete inventory and compare-and-swap drift checks.

The baseline distribution test contract remained required for native execution, accounting, installations, model guards and behavioral regeneration. The directory feature extended its inputs; passing these 24 directory cases alone could not claim full distribution delivery or regeneration.

| Acceptance scenario | Independent cases |
| --- | --- |
| DS-US1-AS1 | DIR-011, DIR-012 |
| DS-US1-AS2 | DIR-002 |
| DS-US1-AS3 | DIR-001, DIR-004 |
| DS-US2-AS1 | DIR-003, DIR-007, DIR-008 |
| DS-US2-AS2 | DIR-009, DIR-011, DIR-012 |
| DS-US2-AS3 | DIR-009, DIR-010 |
| DS-US3-AS1 | DIR-005, DIR-006, DIR-017, DIR-018 |
| DS-US3-AS2 | DIR-007, DIR-017, DIR-018, DIR-023 |
| DS-US3-AS3 | DIR-019 |
| DS-US4-AS1 | DIR-015, DIR-016 |
| DS-US4-AS2 | DIR-014, DIR-020 |
| DS-US4-AS3 | DIR-020, DIR-021, DIR-023 |

Suite test leaves and unchanged-oracle successors were inventory T002→T003, links T004→T005, compile T006→T007, freshness T008→T009, commands T010→T011, retention T012→T013, views T014→T015, upgrade T016→T017 and pilot T018→T019. Required review/handoff was T020→T021→T022 with native dependencies retained in the execution contract. Product test execution remained pending.
