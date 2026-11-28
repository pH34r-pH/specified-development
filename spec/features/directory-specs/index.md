---
schema_version: 1
document_id: specified-development/directory-specs
role: feature
feature_id: directory-specs
revision: 2
target_status: mature-complete-product
approval_status: proposed
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: [user-requested-enhancement-design-candidate, living-spec-paradigm]
---

# Canonical specification directory

The distribution keeps complete product intent in a formatted, navigable `spec/` directory. Usage, feature behavior, contracts and operations are editable living source documents; documentation uses those same documents. Spec Kit-compatible build adapters and downstream plans, tests and tasks live under `build/<stable-feature-id>/`. The directory replaces a canonical single-file convention without forking upstream Spec Kit.

## Actors and scenarios

| Story | Outcome and acceptance scenarios |
| --- | --- |
| DS-US1 Author | AS1: authors edit canonical pages through specify/clarify, and no generated file is accepted as source. AS2: stable feature/document/requirement identities survive a file rename. AS3: an unregistered normative file or undeclared normative dependency fails rather than being omitted. |
| DS-US2 Planner | AS1: choosing one feature assembles its complete normative closure, shared contracts/assets and consumer authority without unrelated feature prose. AS2: plan/tests/tasks run only on fresh accepted source and adapter hashes. AS3: changed content, locks, renderers, templates or projectors invalidate affected contracts and descendants. |
| DS-US3 Reader | AS1: source links, relative assets, duplicate headings and cross-page anchors work in repository, site and optional wiki views. AS2: documentation contains the canonical prose with no model rewrite. AS3: unauthorized or divergent wiki publication fails closed and does not reverse-sync into source. |
| DS-US4 Maintainer | AS1: accepted build revisions and issue identities survive cleaning temporary output. AS2: an interrupted generation or upgrade preserves prior accepted artifacts and consumer code. AS3: a consumer with legacy layout remains read-only until an explicitly scoped adoption change is approved. |

## Functional requirements

| ID | Required observable behavior |
| --- | --- |
| DS-FR-001 | Canonical source uses `spec/index.md`, `usage/`, `features/<stable-id>/`, `contracts/`, `operations/` and `assets/`; every source and asset has an explicit role and inventory entry. |
| DS-FR-002 | Stable document, feature and requirement identities are independent of paths, titles and local task numbers. Duplicate IDs, case-fold path collisions and invalid feature slugs are rejected. |
| DS-FR-003 | A manifest selects normative document dependencies and feature roots; navigation only defines reading order. Whole-tree validation rejects unregistered files, missing dependencies and normative cross-references outside declared closure. |
| DS-FR-004 | Selection includes feature roots, transitive normative dependencies, referenced assets and explicit consumer authority/locks. Closure and order are deterministic, cycles are rejected, and unrelated features are excluded from selected semantic inputs. Whole-tree discovery still detects additions and deletions and revalidates selection. |
| DS-FR-005 | File and link validation rejects traversal, absolute local paths, symlink escapes, unsafe schemes, unresolved links/assets/anchors, duplicate/ambiguous anchors, schema references and wiki-name collisions. External links require allowed schemes; availability checks remain separately recorded. |
| DS-FR-006 | A compiled read-only `build/<feature>/spec.md` adapter preserves source prose exactly, with deterministic headings/separators, byte-range source mapping, manifest/closure hashes and generated provenance; it has no independent authority. |
| DS-FR-007 | Wrappers set `SPECIFY_FEATURE_DIRECTORY` to the generated build feature directory and `SPECIFY_FEATURE_NO_PERSIST=1`; upstream scripts see compatible sibling files. No canonical source symlink is placed in build. Unsupported stock commands and stale or missing adapters are blocked at deterministic entrypoints and CI. |
| DS-FR-008 | Replacement specify/clarify edits canonical `spec/` atomically and reruns discovery and validation; plan/tests/tasks/analyze/implement resolve source maps and current acceptance. Hooks alone do not enforce freshness. |
| DS-FR-009 | Input locks include full discovery inventory, selected document/asset hashes, manifest dependency/order hash, relevant consumer authority, and dependency/template/projector/renderer versions and digests. Semantic closure and discovery fingerprints are distinct; unknown fields prevent freshness claims. |
| DS-FR-010 | Source, content, asset, configuration and tool changes cause conservative revalidation and comparison of affected contract hashes. No prose edit is presumed cosmetic. Unrelated-feature edits with unchanged validated closure preserve unaffected accepted receipts; changes to selection or shared contracts invalidate affected artifacts and native descendants. |
| DS-FR-011 | Candidate generation uses staging and atomic promotion with before-hash checks. Failed compilation or validation leaves prior views intact and retains diagnostics; accepted snapshots are never overwritten. |
| DS-FR-012 | Accepted plans, tests, task metadata, execution contracts, issue bindings, input snapshots and receipts under build are immutable retained authority/evidence. Cleaning uses an explicit disposable allowlist and cannot delete accepted records or code. |
| DS-FR-013 | Repository Markdown and optional pinned static-site rendering consume `spec/` directly; prose and asset byte provenance is recorded. Static-site configuration uses `docs_dir: spec` and `site_dir: build/site`; it requires a qualified renderer lock before activation. |
| DS-FR-014 | Optional GitHub wiki export is a deterministic one-way view with checked page-name/link/anchor/asset maps and complete managed inventory. Direct wiki drift blocks publication; no LLM rewrite or automatic reverse synchronization occurs. |
| DS-FR-015 | Preset/extension command and generated-asset overrides provide the directory behavior against a pinned compatible upstream version; installation and upgrade verify all active assets and retain rollback artifacts. Unsupported integrations remain blocked. |
| DS-FR-016 | Pilot and rollout gates test a complete mature two-feature product, shared contracts, independent oracles, native leaf identity and compatibility before any consumer adoption or publication. No new scheduler, task DAG or generic agent framework is introduced. |

## Success criteria

| ID | Observable oracle |
| --- | --- |
| DS-SC-001 | Two clean assemblies from the same frozen inputs produce identical adapter, lock and source-map bytes, and select all and only the declared closure. |
| DS-SC-002 | Every named invalid fixture fails with a stable diagnostic before source/build/publication mutation; an interrupted promotion restores the exact prior managed state. |
| DS-SC-003 | Every supported command rejects stale or missing adapters and edits the intended authority; both tested active integrations resolve verified replacement assets. |
| DS-SC-004 | Repository/site/wiki link and content parity tests pass against pinned renderers; wiki publication stays pending until destination, access and authorization are verified. |
| DS-SC-005 | Accepted snapshots and issue identities survive cleanup, path rename and unrelated-feature change; changed-contract descendants alone become stale. |
| DS-SC-006 | A complete isolated pilot passes this independent contract and baseline lifecycle compatibility gates with no consumer mutation or new scheduler. |

## Boundaries

The feature does not create a documentation CMS, bidirectional wiki editor, inference router, deployment service or language for specifying arbitrary application behavior. Research is not automatically normative. Renderer support is qualified explicitly; preserving Markdown bytes does not by itself prove equivalent rendering. Source renames change hashes while preserving logical identity. Public export is allowlisted and never includes private research, credentials or runtime logs.
