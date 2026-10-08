---
document_id: specified-development/lifecycle
target_status: mature-complete-product
approval_status: user-requested-enhancement-design-candidate
delivery_status: designed-only
delivery_evidence: []
---

# Authoring and using the lifecycle

Research and ideas stayed in free-form Markdown outside canonical product authority until accepted into a mature design. Each optional proof of concept recorded a decision that it could invalidate, the smallest useful experiment, its stopping condition, and evidence. Spec authors described the full intended product directly in past tense. Explicit target and approval fields accompanied separate implementation, test, deployment, and regeneration evidence.

Authors edited `spec/` and chose stable feature IDs. A deterministic guard discovered the entire tree, validated every declared document/link/asset, and assembled the selected feature's normative closure. Approval froze source hashes and an accepted revision. A planner produced `build/<feature>/plan.md`; independent expected behavior became `tests.md`; semantic decomposition then produced `tasks.md` and complete structured metadata. Each step required fresh accepted upstream artifacts.

The compatibility `build/<feature>/spec.md` was labeled generated, read-only, and derived. It carried source IDs, input hashes, and a source map. Canonical edits went through replacement specify/clarify commands to `spec/`; direct edits to generated adapters were rejected. Existing domain constitutions remained consumer-owned authority and were included in frozen inputs.

The selected existing executor claimed dependency-ready leaves only after exact accepted inputs, native parent outputs, selected-model admission, capability-profile requirements, and permissions were verified; unexposed optional effective settings/usage remained explicit. A missing design assumption stopped that attempt and produced a separate bounded repair task at the earliest authority. Models never changed mid-attempt. Deterministic validation, projection, scheduling in the existing owner, and cache/cost accounting used scripts after this design's semantic decomposition.

## Prior-art review before plan authoring

Before finalizing a plan, review existing standards, algorithms, data structures, patterns, or compatible library interfaces when they could materially affect correctness, compatibility, security, cost, or maintenance. Keep a compact decision record with the relevant requirement and constraints; where a candidate applies and does not apply; assumptions and invariants; material failure behavior, side effects, state ownership, concurrency, and compatibility boundaries; a simple baseline and other plausible alternatives; and why each option is adopted, extended, or rejected. Cite source-backed asymptotic bounds and label empirical performance claims separately; an empirical claim needs qualified measurement evidence.

Record the work, edition or version, and a section or stable URL for the source actually consulted. If code or a package is reused, record its exact version and license compatibility separately. A book, standard, or API citation does not grant permission to copy code. Trivial choices need no decision record; when no useful prior art applies, say so briefly. Trace material assumptions and composition risks to an existing independent test or record why no new oracle is warranted. Do not build a universal pattern or algorithm catalog.

## Implementation finish and refinement

Closeout separates behavior acceptance from implementation review. First confirm that the accepted behavior and unchanged independent oracle pass with focused regressions and exact-head CI evidence. Then review whether names and boundaries make intent clear, dependencies and abstractions are warranted, and error paths, state changes, side effects, and test failures are understandable. Keep cleanup within the task's declared scope; rerun the unchanged oracle and focused regressions after cleanup. Do not use a style linter or numeric method, line, or function limits as a substitute for review.

If behavior differs from the accepted contract, stop the attempt and route the discovery to the earliest canonical authority; review or invalidate only affected downstream artifacts and native descendants under the freshness rules. A behavior-preserving refinement does not by itself require rewriting specifications or task records. A CI failure gets only the bounded repair allowed by the task's existing attempt policy; a scope or design gap becomes a separate repair rather than an unreviewed expansion.

This review is informed by Robert C. Martin, [*Clean Code: A Handbook of Agile Software Craftsmanship*, 2nd ed. (2025)](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398548), especially Chapter 3, “First Principles,” Chapter 9, “The Clean Method,” and Chapter 10, “One Thing.” These are review prompts, not prose, code, exercises, or numeric thresholds to reproduce.

Plans/tasks/issue bindings/receipts remained durable after acceptance even though their paths began with `build/`. Candidate/current rendering could be replaced; immutable accepted revisions could not. Retained code remained available. Scoped behavioral regeneration required independent clean workspaces and oracles before a scoped disposability claim; no source deletion followed from that claim.

Documentation displayed the canonical Markdown content. A local rendered site and optional authorized wiki export rewrote only navigation, links, anchors where renderer rules required, and asset locations. Wiki edits created detectable drift; a correction returned to canonical `spec/` before one-way regeneration.
