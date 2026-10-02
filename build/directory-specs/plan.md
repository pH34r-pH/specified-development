---
artifact: implementation-plan
revision: 1
acceptance: candidate-review
delivery_status: designed-only
---

# Directory implementation plan

The implementation reused upstream v1.0.13 primitives through the existing distribution's preset and extension. It added a small documents module to `extensions/ph34r-contracts/scripts/ph34r_contracts/`, rather than a fork, new scheduler or generic agent framework. `spec/manifest.json` was the explicit inventory/dependency source and navigation.json only reading order. Directory requirements and contracts were the earliest behavioral authority.

Python 3.12 and the same resolved distribution lock provided deterministic compilation/validation. The first implementation leaf froze actual approved tool/dependency/renderer digests; optional site/wiki support could not claim qualification with missing versions. Stdlib path/JSON/hash operations handled deterministic control data; existing approved Markdown tooling supplied parse/render rules. A parser dependency needed a pinned primary-source compatibility test before lock acceptance. No freehand regex parser was accepted as complete Markdown link/anchor validation.

Independent fixtures preceded implementation: two feature trees, shared contracts/assets, normative vs navigation links, Unicode/duplicate headings, malformed references and locks, symlink/case collisions, accepted histories and interrupted promotions. Test authors fixed expected closure/output slices/diagnostics from the source contract; implementation did not generate its own goldens.

Modules were `document_inventory.py` (full discovery/schema/IDs), `document_links.py` (parsed references/assets/anchors), `document_compile.py` (selection/order/assembly/map/lock), `document_freshness.py` (entrypoint accepted inputs/change effects), `document_retention.py` (snapshots/clean/staged promotion), and `document_views.py` (optional pinned renderer/wiki mapping). Small module boundaries described scopes; they did not require a general plugin framework. Existing gates/receipt/cache/projection helpers were reused through declared interfaces after their baseline qualification; absent required interfaces were a compatibility block or separate repair.

Wrappers and preset replacements handled every specified semantic command. specify/clarify edited source; plan/tests/tasks/analyze/implement required fresh accepted inputs and compiled adapters. `SPECIFY_FEATURE_NO_PERSIST=1` applied throughout subprocess trees. The adapter included exact source bytes and source map, never symlinked source; tests verified upstream sibling resolution in disposable roots. CI repeated the deterministic guards independently of agent prompts/hooks.

Changes promoted from a stage with managed inventory, before-hash comparison and retained journal/rollback state. Accepted build revisions stored exact source snapshots and downstream artifacts. Cleanup only targeted explicit disposable outputs. Changing an unrelated feature revalidated full discovery/closure before preserving unchanged receipts; changing shared inputs conservatively staled affected contracts and native descendants. No immutable history was overwritten.

Static documentation used source directly. Wiki export was optional, one-way and dry by default; page/link/anchor/asset maps were deterministic and collision-tested against pinned renderers. Drift or missing wiki access blocked apply. Content parity was source-token/asset evidence plus renderer behavior, not a prose rewrite. No publication occurred in implementation tests.

The ordered native leaf graph separated independent test authorship, implementations, integration qualification, recovery and review. Each leaf had one issue identity and one fixed model binding; metadata below was the complete semantic decomposition. Mechanical checks used scripts; no decomposition model or routing service was needed. Baseline installation/gate/projection behavior was a frozen external input requirement, not a copied second DAG. Both features required qualification before consumer rollout.
