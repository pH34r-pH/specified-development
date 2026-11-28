---
artifact: implementation-plan
revision: 2
acceptance: candidate-review
delivery_status: designed-only
---

# Directory implementation plan

The implementation reuses upstream v1.0.13 primitives through the existing distribution's preset and extension. It adds a small documents module to `extensions/ph34r-contracts/scripts/ph34r_contracts/`, rather than a fork, new scheduler or generic agent framework. `spec/manifest.json` is the explicit inventory/dependency source and navigation.json only reading order. Directory requirements and contracts are the earliest behavioral authority.

## Implementation targets and direct path

**Component and consumers.** The documents module of `ph34r-contracts` implements DS-FR-001 through DS-FR-016. Its real consumers are the replacement specify/clarify/plan/tests/tasks/analyze/implement commands, the freshness entrypoints, CI guards and the optional site/wiki views. The specification owns all observable behavior; this section owns only technical choices.

**Current and target implementation.** There is no current implementation. The accepted implementation decision is Python 3.12 with the standard library plus the distribution's locked Markdown and YAML parsers, running inside the existing extension. There is no candidate port: a different language or runtime would be a plan revision against the same specification and DIR test contract, and it would need comparative evidence under the same oracle.

**Reuse.** Upstream Spec Kit v1.0.13 primitives through the preset/extension, `graphlib` and `heapq` for closure order (see the decision record below), the existing gate/receipt/cache/projection helpers through declared interfaces, and the approved Markdown tooling for link and anchor parsing. All are pinned through the distribution lock.

**Direct path and state.** Each command call reads one immutable manifest snapshot, validates, selects closure, assembles bytes and a source map in memory, and promotes from a stage with before-hash checks. All state is per-call except the managed build outputs, whose ownership belongs to the staged-promotion journal. Feature selection, renderer choice and wiki export are runtime inputs; the closure algorithm, tie rule and lock schema are fixed at build time.

**Layer dispositions.**

| Layer | Disposition | Duty |
| --- | --- | --- |
| Six document modules (inventory, links, compile, freshness, retention, views) | Retain | Separate scopes with independent fixtures; no plugin framework. |
| Read-only `build/<feature>/spec.md` adapter | Preserve as external compatibility boundary | Upstream scripts need sibling files. Exit condition: upstream supports a canonical source directory directly. |
| Wiki/site projection | Retain, optional at runtime | Users choose whether to publish views. |
| Generic rendering or agent abstraction | Remove | No consumer requires it. |

**Objective and preserved acceptance.** The objective is correct, deterministic closure and freshness, not speed. Every DIR case remains the acceptance bar. A simplification that drops a validation duty is not acceptable, and no performance claim is made.

**Unresolved decisions and local discretion.** DIR-003 now carries an explicit ready-set tie witness with an executable property oracle (directory test contract, composition decision oracles). Implementation tasks may choose private function boundaries, internal names and error-message wording within the declared module scopes and stable diagnostic codes.

## Prior-art decision record: normative dependency closure and order

**Status:** plan-level design candidate; no compiler implementation, task dispatch, new test, or product qualification is claimed.

The T005 dogfood pilot has not run: T005 remains `planned-not-dispatched` behind T004. The composition oracle review for this decision is complete (#7). The closeout checklist is guidance only until a task-owner-authorized implementation slice is ready.

**Requirement and constraints.** This choice supports DS-FR-003/004 and the existing document contract: select a feature root and its transitive `normative_dependencies`, exclude presentation-only navigation edges and unrelated documents, emit each selected document once with dependencies before dependents, use stable document-ID tie-breaking, and reject cycles. The full discovered manifest remains the authority for reference and cycle validation; its graph is not a task-execution graph.

**Candidate composition.** After validating every manifest dependency reference against the complete registered document set, compute the selected closure with an iterative worklist and visited set. Use Python 3.12's standard-library `graphlib.TopologicalSorter` for dependency-first readiness and cycle detection, registering document IDs and predecessor IDs in sorted order. Use `heapq` to choose the smallest currently ready ID; after marking one ID done, add newly ready IDs to the heap. Filter the resulting order to the selected closure. This makes the documented ID tie-break explicit instead of relying on `TopologicalSorter.static_order()`, whose result the Python documentation says depends on insertion order. Validate references before graph construction because the API automatically adds an unregistered predecessor as a node. If `prepare()` raises `CycleError`, abort before producing or promoting output, even though the API can still expose acyclic partial progress. Report the repository's stable cycle diagnostic rather than an arbitrary cycle path.

**Assumptions and invariants.** Manifest shape/reference validation has already succeeded; document IDs are stable ASCII strings; dependency edges mean input selection only; the whole manifest graph is acyclic; and assembly owns a single immutable manifest snapshot. The selected result is exactly the root's transitive dependency closure, has no duplicate IDs, places every dependency before its dependent, and is independent of JSON/map enumeration and navigation order. The graph and heap are per-call state; this design uses no shared mutable state or parallel execution. Graph discovery/order is in-memory and side-effect free; the existing staged-promotion contract still owns filesystem writes.

**Alternatives.** An iterative sorted depth-first traversal with active/visited sets can produce a dependency-first order in O(V+E) time, with less heap overhead, but the compiler would own cycle detection, tie policy, and stable diagnostics. `TopologicalSorter.static_order()` is simpler; sorted insertion would make it repeatable, but it does not express the contract's smallest-currently-ready ID rule as directly. A repeated full scan for ready nodes avoids a heap but can spend O(V²+E) time. The composed standard-library candidate keeps established graph bookkeeping and makes the tie rule explicit.

**Costs and compatibility.** For V manifest documents and E dependency edges, closure discovery is O(V+E); ordering the full manifest with a priority queue is O(V+E+V log V) time and O(V+E) space. These are analytical bounds for adjacency-list graph processing plus heap operations, not measured latency or a claim that this small manifest needs optimization. Python 3.12 is already the planned runtime; `graphlib` has been available since Python 3.9, and neither module adds a third-party package. The direct API contract is documented in [Python 3.12 `graphlib`](https://docs.python.org/3.12/library/graphlib.html) and [Python 3.12 `heapq`](https://docs.python.org/3.12/library/heapq.html); the insertion-order caveat is material to this design. The API docs link to their source, but this plan copies no Python implementation code. Python's distribution license is the PSF License Version 2 ([license terms](https://docs.python.org/3.12/license.html)); ordinary use of the standard-library API is not a separate package dependency.

**Oracle trace and remaining gap.** Existing DIR-003 already specifies transitive closure, navigation-only exclusion, shuffled input enumeration, dependency-first ordering, and cycle rejection. DIR-003 also carries a hand-authored multi-node ready-set tie witness whose expected order was fixed from the invariants before implementation; an executable property oracle rejects a sorted depth-first postorder and an insertion-order topological order, so the tie policy is independently covered. No performance test is warranted for this deterministic design choice; empirical performance remains unclaimed.

**Sources and attribution.** The algorithm/data-structure reasoning is consistent with Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, *Fundamental Algorithms*, 3rd ed. (1997), whose author page verifies the work and edition ([TAOCP bibliography](https://cs.stanford.edu/~knuth/taocp.html)); no TAOCP section is claimed for this particular operation. For a directly relevant algorithm treatment, see Cormen, Leiserson, Rivest, and Stein, *Introduction to Algorithms*, 4th ed. (2022), §§6.5 “Priority queues” and 20.4 “Topological sort” ([MIT Press edition metadata](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/), [official table of contents](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/4e_toc.pdf)). These references support algorithm and cost reasoning; TAOCP is not used as a design-pattern catalog. Book citations are not code licenses, and no book prose, code, figure, or exercise is reproduced.

Python 3.12 and the same resolved distribution lock provide deterministic compilation/validation. The first implementation leaf freezes actual approved tool/dependency/renderer digests; optional site/wiki support cannot claim qualification with missing versions. Stdlib path/JSON/hash operations handle deterministic control data; existing approved Markdown tooling supplies parse/render rules. A parser dependency needs a pinned primary-source compatibility test before lock acceptance. No freehand regex parser is accepted as complete Markdown link/anchor validation.

Independent fixtures precede implementation: two feature trees, shared contracts/assets, normative vs navigation links, Unicode/duplicate headings, malformed references and locks, symlink/case collisions, accepted histories and interrupted promotions. Test authors fix expected closure/output slices/diagnostics from the source contract; implementation does not generate its own goldens.

Modules are `document_inventory.py` (full discovery/schema/IDs), `document_links.py` (parsed references/assets/anchors), `document_compile.py` (selection/order/assembly/map/lock), `document_freshness.py` (entrypoint accepted inputs/change effects), `document_retention.py` (snapshots/clean/staged promotion), and `document_views.py` (optional pinned renderer/wiki mapping). Small module boundaries describe scopes; they do not require a general plugin framework. Existing gates/receipt/cache/projection helpers are reused through declared interfaces after their baseline qualification; absent required interfaces are a compatibility block or separate repair.

Wrappers and preset replacements handle every specified semantic command. specify/clarify edit source; plan/tests/tasks/analyze/implement require fresh accepted inputs and compiled adapters. `SPECIFY_FEATURE_NO_PERSIST=1` applies throughout subprocess trees. The adapter includes exact source bytes and source map, never symlinked source; tests verify upstream sibling resolution in disposable roots. CI repeats the deterministic guards independently of agent prompts/hooks.

Changes promote from a stage with managed inventory, before-hash comparison and retained journal/rollback state. Accepted build revisions store exact source snapshots and downstream artifacts. Cleanup only targets explicit disposable outputs. Changing an unrelated feature revalidates full discovery/closure before preserving unchanged receipts; changing shared inputs conservatively stales affected contracts and native descendants. No immutable history is overwritten.

Static documentation uses source directly. Wiki export is optional, one-way and dry by default; page/link/anchor/asset maps are deterministic and collision-tested against pinned renderers. Drift or missing wiki access blocks apply. Content parity is source-token/asset evidence plus renderer behavior, not a prose rewrite. No publication occurs in implementation tests.

The ordered native leaf graph separates independent test authorship, implementations, integration qualification, recovery and review. Each leaf has one issue identity and one fixed model binding; the task metadata is the complete semantic decomposition. Mechanical checks use scripts; no decomposition model or routing service is needed. Baseline installation/gate/projection behavior is a frozen external input requirement, not a copied second DAG. Both features require qualification before consumer rollout.
