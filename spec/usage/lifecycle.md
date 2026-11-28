---
schema_version: 1
document_id: specified-development/lifecycle
role: usage
revision: 2
target_status: mature-complete-product
approval_status: proposed
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: [user-requested-enhancement-design-candidate, living-spec-paradigm]
---

# Authoring and using the lifecycle

Research and ideas stay in free-form Markdown outside canonical product authority until they are accepted into a mature design. Each optional proof of concept records a decision that it could invalidate, the smallest useful experiment, its stopping condition and evidence. Spec authors describe the complete product directly in present tense. Explicit target and approval fields accompany separate implementation, test, deployment and regeneration evidence; prose tense never advances delivery status.

Authors edit `spec/` and choose stable feature IDs. A deterministic guard discovers the entire tree, validates every declared document, link and asset, and assembles the selected feature's normative closure. Approval records source hashes and an accepted revision. A planner produces `build/<feature>/plan.md`; independent expected behavior becomes `tests.md`; semantic decomposition then produces `tasks.md` and complete structured metadata. Each step requires fresh accepted upstream artifacts.

The compatibility `build/<feature>/spec.md` is labeled generated, read-only and derived. It carries source IDs, input hashes and a source map. Canonical edits go through replacement specify/clarify commands to `spec/`; direct edits to generated adapters are rejected. Existing domain constitutions remain consumer-owned authority and are included in frozen inputs.

The selected existing executor claims dependency-ready leaves only after exact accepted inputs, native parent outputs, selected-model admission, capability-profile requirements and permissions are verified; unexposed optional effective settings and usage remain explicit. A missing design assumption stops that attempt and produces a separate bounded repair task at the earliest authority. Models never change mid-attempt. Deterministic validation, projection, scheduling in the existing owner, and cache/cost accounting use scripts after semantic decomposition.

## Living specification

The canonical spec is a living document. It always describes the software as it is specified to behave now, in present tense, including accepted changes that are not yet implemented. It is revised in place; it is never replaced by a successor copy. Accepted revisions are identified by exact content hashes and retained history, so revising the working tree never rewrites a historical verdict.

The spec owns observable behavior: capabilities, inputs and outputs, failure behavior, runtime variability, interoperability, security, privacy and accepted operational or performance requirements. The plan owns language, runtime, dependencies, architecture and implementation strategy. Spec, plan, independent tests and tasks together are complete enough for an AI model to reproduce a compatible program without reading retained implementation code; scoped regeneration trials measure that completeness.

## Spec-first change and gaps

Every behavior change starts in the spec. The author writes the new or changed behavior in present tense, as if it already exists, and has the revision reviewed and accepted. Code is never changed first and documented afterwards.

A gap is an accepted requirement that lacks passing independent evidence at the current source revision. A new requirement is a gap until its independent tests pass. A changed requirement invalidates its previous evidence and becomes a gap. A requirement whose evidence starts failing has regressed and is also a gap.

A spec change propagates only through its gap, as computed by the [requirement status and gap contract](../contracts/documents.md#requirement-status-and-gap-propagation). The plan sections, independent test cases and tasks that depend on changed requirements become stale and are refreshed in that order; unaffected accepted descendants, receipts and identities remain valid. New tasks are produced only for the gap. A technical discovery that invalidates the plan repairs the plan; a product discovery repairs the spec first. Neither lowers the acceptance bar.

## Specification and plan authority

The specification defines the finished working product and is its acceptance criteria. It states required capabilities, observable inputs and outputs, failure behavior, user and runtime variability, interoperability, security, privacy and accepted operational or performance requirements. It is not a container for internal implementation architecture. Public interoperability requirements stay in the specification; the internal mechanism that satisfies them belongs in the plan.

The plan selects languages and runtimes, dependency and toolchain versions, algorithms and data structures, internal architecture, build and deployment mechanisms, and the direct implementation strategy. It references product requirements by ID rather than copying or weakening them. A plan preference, stretch goal, faster kernel, smaller dependency list or reduced line count cannot redefine product acceptance, and a declared target is not evidence that it is reached.

Two plans can target the same specification and the same independent behavioral oracle. A language or runtime migration that preserves the product contract revises the plan and its affected downstream artifacts, never the specification, so the specification hash is unchanged. A new or changed product promise requires specification review first.

Each plan carries a compact implementation-targets section rather than a separate registry or configuration format:

- the bounded component, its traced product requirements and its real consumers;
- the current implementation and the candidate and intended language/runtime targets, labeled as aspiration, authorized experiment, accepted implementation decision or qualified result;
- existing libraries and platform features to reuse, pinned through existing locks;
- the direct implementation path, state ownership, and which variation is fixed at build time versus genuinely required at runtime;
- for each material layer, a disposition of retain, remove, specialize at build time, or preserve as an external or migration boundary, with the duty it serves and any temporary bridge's exit condition;
- the improvement objective, preserved acceptance requirements, comparative evidence, qualified environments, and rollback or migration obligations;
- explicit unresolved decisions and the local discretion an implementation task may exercise.

Prefer a simpler same-language implementation before proposing a migration when that answers the question. When gains are attributed separately to simplification and language choice, compare current, simplified same-language and optional port under the same behavioral contract; do not require three implementations when no such causal claim is made. A microbenchmark is not end-to-end performance. Product performance requirements stay in the specification; a technical threshold for choosing a candidate stays in the plan and cannot lower the product's acceptance bar.

## Prior-art review before plan authoring

Before finalizing a plan, review existing standards, algorithms, data structures, patterns or compatible library interfaces when they could materially affect correctness, compatibility, security, cost or maintenance. Keep a compact decision record with the relevant requirement and constraints; where a candidate applies and does not apply; assumptions and invariants; material failure behavior, side effects, state ownership, concurrency and compatibility boundaries; a simple baseline and other plausible alternatives; and why each option is adopted, extended or rejected. Cite source-backed asymptotic bounds and label empirical performance claims separately; an empirical claim needs qualified measurement evidence.

Record the work, edition or version, and a section or stable URL for the source actually consulted. If code or a package is reused, record its exact version and license compatibility separately. A book, standard or API citation does not grant permission to copy code. Trivial choices need no decision record; when no useful prior art applies, say so briefly. Trace material assumptions and composition risks to an existing independent test or record why no new oracle is warranted. Do not build a universal pattern or algorithm catalog.

## Implementation finish and refinement

Closeout separates behavior acceptance from implementation review. First confirm that the accepted behavior and unchanged independent oracle pass with focused regressions and exact-head CI evidence. Then review whether names and boundaries make intent clear, dependencies and abstractions are warranted, and error paths, state changes, side effects and test failures are understandable. Keep cleanup within the task's declared scope; rerun the unchanged oracle and focused regressions after cleanup. Do not use a style linter or numeric method, line or function limits as a substitute for review.

If behavior differs from the accepted contract, stop the attempt and route the discovery to the earliest canonical authority; review or invalidate only affected downstream artifacts and native descendants under the freshness rules. A behavior-preserving refinement does not by itself require rewriting specifications or task records. A CI failure gets only the bounded repair allowed by the task's existing attempt policy; a scope or design gap becomes a separate repair rather than an unreviewed expansion.

This review is informed by Robert C. Martin, [*Clean Code: A Handbook of Agile Software Craftsmanship*, 2nd ed. (2025)](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398548), especially Chapter 3, “First Principles,” Chapter 9, “The Clean Method,” and Chapter 10, “One Thing.” These are review prompts, not prose, code, exercises or numeric thresholds to reproduce.

Plans, tasks, issue bindings and receipts remain durable after acceptance even though their paths begin with `build/`. Candidate and current rendering can be replaced; immutable accepted revisions cannot. Retained code remains available. Scoped behavioral regeneration requires independent clean workspaces and oracles before a scoped disposability claim; no source deletion follows from that claim.

Documentation displays the canonical Markdown content. A local rendered site and optional authorized wiki export rewrite only navigation, links, anchors where renderer rules require, and asset locations. Wiki edits create detectable drift; a correction returns to canonical `spec/` before one-way regeneration.
