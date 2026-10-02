---
document_id: specified-development/directory-specs
feature_id: directory-specs
revision: 1
target_status: mature-complete-product
approval_status: user-requested-enhancement-design-candidate
delivery_status: designed-only
delivery_evidence: []
---

# Canonical specification directory

The distribution kept complete product intent in a formatted, navigable `spec/` directory. Usage, feature behavior, contracts, and operations were editable source documents; documentation used those same documents. Spec Kit-compatible build adapters and downstream plans, tests, and tasks lived under `build/<stable-feature-id>/`. The directory replaced a canonical single-file convention without forking upstream Spec Kit.

## Actors and scenarios

| Story | Completed outcome and acceptance scenarios |
| --- | --- |
| DS-US1 Author | AS1: authors edited canonical pages through specify/clarify, and no generated file was accepted as source. AS2: stable feature/document/requirement identities survived a file rename. AS3: an unregistered normative file or undeclared normative dependency failed rather than being omitted. |
| DS-US2 Planner | AS1: choosing one feature assembled its complete normative closure, shared contracts/assets and consumer authority without unrelated feature prose. AS2: plan/tests/tasks ran only on fresh accepted source and adapter hashes. AS3: changed content, locks, renderers, templates or projectors invalidated affected contracts and descendants. |
| DS-US3 Reader | AS1: source links, relative assets, duplicate headings and cross-page anchors worked in repository, site and optional wiki views. AS2: documentation contained the canonical prose with no model rewrite. AS3: unauthorized or divergent wiki publication failed closed and did not reverse-sync into source. |
| DS-US4 Maintainer | AS1: accepted build revisions and issue identities survived cleaning temporary output. AS2: an interrupted generation or upgrade preserved prior accepted artifacts and consumer code. AS3: a consumer with legacy layout remained read-only until an explicitly scoped adoption change was approved. |

## Functional requirements

| ID | Completed-product semantics |
| --- | --- |
| DS-FR-001 | Canonical source used `spec/index.md`, `usage/`, `features/<stable-id>/`, `contracts/`, `operations/`, and `assets/`; every source/asset had an explicit role and inventory entry. |
| DS-FR-002 | Stable document, feature and requirement identities were independent of paths, titles and local task numbers. Duplicate IDs, case-fold path collisions and invalid feature slugs were rejected. |
| DS-FR-003 | A manifest selected normative document dependencies and feature roots; navigation only defined reading order. Whole-tree validation rejected unregistered files, missing dependencies and normative cross-references outside declared closure. |
| DS-FR-004 | Selection included feature roots, transitive normative dependencies, referenced assets and explicit consumer authority/locks. Closure/order were deterministic, cycles rejected, and unrelated features were excluded from selected semantic inputs. Whole-tree discovery still detected additions/deletions and revalidated selection. |
| DS-FR-005 | File/link validation rejected traversal, absolute local paths, symlink escapes, unsafe schemes, unresolved links/assets/anchors, duplicate/ambiguous anchors, schema references and wiki-name collisions. External links required allowed schemes; availability checks remained separately recorded. |
| DS-FR-006 | A compiled read-only `build/<feature>/spec.md` adapter preserved source prose exactly, with deterministic headings/separators, byte-range source mapping, manifest/closure hashes and generated provenance; it had no independent authority. |
| DS-FR-007 | Wrappers set `SPECIFY_FEATURE_DIRECTORY` to the generated build feature directory and `SPECIFY_FEATURE_NO_PERSIST=1`; upstream scripts saw compatible sibling files. No canonical source symlink was placed in build. Unsupported stock commands and stale/missing adapters were blocked at deterministic entrypoints and CI. |
| DS-FR-008 | Replacement specify/clarify edited canonical `spec/` atomically and reran discovery/validation; plan/tests/tasks/analyze/implement resolved source maps and current acceptance. Hooks alone did not enforce freshness. |
| DS-FR-009 | Input locks included full discovery inventory, selected document/assets hashes, manifest dependency/order hash, relevant consumer authority, dependency/template/projector/renderer versions and digests. Semantic closure and discovery fingerprints were distinct; unknown fields prevented freshness claims. |
| DS-FR-010 | Source/content/assets/config/tool changes caused conservative revalidation and comparison of affected contract hashes. No prose edit was presumed cosmetic. Unrelated-feature edits with unchanged validated closure preserved unaffected accepted receipts; changes to selection or shared contracts invalidated affected artifacts and native descendants. |
| DS-FR-011 | Candidate generation used staging and atomic promotion with before-hash checks. Failed compilation/validation left prior views intact and retained diagnostics; accepted snapshots were never overwritten. |
| DS-FR-012 | Accepted plans, tests, task metadata, execution contracts, issue bindings, input snapshots and receipts under build were immutable retained authority/evidence. Cleaning used an explicit disposable allowlist and could not delete accepted records or code. |
| DS-FR-013 | Repository Markdown and optional pinned static-site rendering consumed `spec/` directly; prose/asset byte provenance was recorded. Static-site configuration used `docs_dir: spec`, `site_dir: build/site`; it required a qualified renderer lock before activation. |
| DS-FR-014 | Optional GitHub wiki export was a deterministic one-way view with checked page-name/link/anchor/asset maps and complete managed inventory. Direct wiki drift blocked publication; no LLM rewrite or automatic reverse synchronization occurred. |
| DS-FR-015 | Preset/extension command and generated-asset overrides provided the directory behavior against a pinned compatible upstream version; installation/upgrade verified all active assets and retained rollback artifacts. Unsupported integrations remained blocked. |
| DS-FR-016 | Pilot/rollout gates tested a complete mature two-feature product, shared contracts, independent oracles, native leaf identity and compatibility before any consumer adoption/publication. No new scheduler, task DAG or generic agent framework was introduced. |

## Success criteria

| ID | Observable oracle |
| --- | --- |
| DS-SC-001 | Two clean assemblies from the same frozen inputs produced identical adapter, lock and source-map bytes, and selected all and only the declared closure. |
| DS-SC-002 | Every named invalid fixture failed with a stable diagnostic before source/build/publication mutation; an interrupted promotion restored the exact prior managed state. |
| DS-SC-003 | Every supported command rejected stale/missing adapters and edited the intended authority; both tested active integrations resolved verified replacement assets. |
| DS-SC-004 | Repository/site/wiki link and content parity tests passed against pinned renderers; wiki publication stayed pending until destination/access/authorization were verified. |
| DS-SC-005 | Accepted snapshots and issue identities survived cleanup, path rename and unrelated-feature change; changed-contract descendants alone became stale. |
| DS-SC-006 | A complete isolated pilot passed this independent contract and baseline lifecycle compatibility gates with no consumer mutation or new scheduler. |

## Boundaries

The feature did not create a documentation CMS, bidirectional wiki editor, inference router, deployment service, or language for specifying arbitrary application behavior. Research was not automatically normative. Renderer support was qualified explicitly; preserving Markdown bytes did not by itself prove equivalent rendering. Source renames changed hashes while preserving logical identity. Public export was allowlisted and never included private research, credentials or runtime logs.
