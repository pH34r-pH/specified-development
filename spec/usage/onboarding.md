---
schema_version: 1
document_id: specified-development/onboarding
role: usage
revision: 1
target_status: mature-complete-product
approval_status: proposed
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: [living-spec-paradigm]
---

# Brownfield onboarding

Brownfield onboarding brings an existing project that has working code but no specification into the living-spec lifecycle. It produces a reviewed, present-tense specification of the project's current behavior, a plan of its current implementation, independent tests and an initial gap list. After onboarding, the project follows the ordinary [spec-first change workflow](lifecycle.md). Each onboarding is a separate, consumer-owned change; it never mutates other repositories.

## Scope one area at a time

Onboarding covers one bounded area at a time: a module, service or feature, recorded as a stable feature ID and the source paths it covers. Everything outside onboarded areas is explicitly unspecified. Unspecified code has no specification authority, produces no gaps and is never treated as non-conforming. A partially specified repository is valid, and later onboarding passes add areas without reopening accepted ones.

## Characterization mode

Characterization mode is the single, bounded exception to the rule that specifications are not derived from implementation. While an area is being onboarded, authors draft its present-tense specification (behavior only) and plan (language, architecture, dependencies and reused libraries) from the existing code, documentation, tests and observed behavior. Every drafted requirement records the sources it was characterized from.

Characterization also captures the area's public interface: every name, signature, attribute, constant and observable behavior that code outside the area imports or relies on, found by searching the rest of the repository for uses of the area. Unspecified code that depends on the area makes that dependency part of the area's specified interoperability, so the specification states the observable behavior and the plan's public-interface section fixes the exact names. A specification that passes its own independent cases but omits behavior that unspecified consumers rely on cannot regenerate a compatible implementation.

A human reviewer then reviews the drafted specification and accepts it as authority. Acceptance ends characterization mode for that area. From then on, the ordinary rules apply: code is evidence, not authority, and every behavior change is spec-first.

## Known defects

Characterization can surface behavior that the reviewer does not intend. For each such known defect, the onboarding record names the requirement and one explicit choice:

- **Specify actual behavior.** The specification records what the code does now, so the requirement is satisfied at onboarding; the intended correction is recorded as a follow-up spec-first change.
- **Specify intended behavior.** The specification records the intended behavior, so the code starts out non-conforming and the requirement is in the initial gap list.

Neither choice may silently encode a known defect as intended behavior. A known defect without a recorded choice blocks acceptance.

## Independent tests and baseline

Independent tests are authored from the accepted specification. Existing project tests are supporting evidence; one can be adopted as an independent case only when it checks specification-level behavior and traces to a requirement. No expected value is computed from, or copied out of, the implementation's own output, during or after onboarding.

The current code becomes the first conforming implementation for every requirement whose independent tests pass. The remaining accepted requirements form the initial gap list, which feeds ordinary gap propagation.

## Existing Spec Kit projects

A project that already uses Spec Kit is onboarded by mapping its existing `specs/<feature>/` artifacts into the canonical `spec/` tree and `build/<feature>/` records. Feature history and consumer constitutions are preserved, prose is converted to present tense and the structure is completed, without rewriting accepted decisions.

## Onboarding record

Each onboarded area has one onboarding record. It names the repository and exact baseline revision, the onboarded areas and their paths, the characterization sources for every accepted requirement, every known-defect decision, the independent oracle sources, the acceptance state with actor and time, the initial gap list and any existing Spec Kit layout mapping. A deterministic validator checks a record against the accepted specification; it does not judge whether the characterization is correct, which remains a review decision.
