---
artifact: implementation-plan
revision: 1
acceptance: candidate-review
---

# FEATURE_TITLE implementation plan

This plan owns technical choices for the FEATURE_TITLE feature. Product behavior and acceptance live in its specification; requirements are referenced by ID, never copied or weakened.

## Implementation targets and direct path

**Component and consumers.** Name the bounded component, the requirements it implements (for example FR-001 and FR-002) and its real consumers.

**Current and target implementation.** State the current implementation, then the candidate and intended language/runtime targets, each labeled as aspiration, authorized experiment, accepted implementation decision or qualified result.

**Reuse.** List existing libraries and platform features to reuse, pinned through the project's existing locks.

**Direct path and state.** Describe the direct implementation path, who owns each piece of state, and which variation is fixed at build time versus genuinely required at runtime.

**Layer dispositions.**

| Layer | Disposition | Duty |
| --- | --- | --- |
| Example layer | Retain, remove, specialize at build time, or preserve as a boundary | The requirement or consumer it serves, and any temporary bridge's exit condition. |

**Objective and preserved acceptance.** State the improvement objective and the acceptance requirements it must preserve. Comparative evidence is required before claiming an improvement.

**Unresolved decisions and local discretion.** List open technical decisions and the local choices implementation tasks may make on their own.

## Public interface

List every name, signature, attribute, constant and message format that code outside this feature imports or relies on. Search the rest of the repository for uses of the feature's modules. Write "None" only when nothing outside the feature uses it.

- `module.Name(argument: type) -> type`: what callers rely on.

## Prior-art decisions

Record material choices of standards, algorithms, data structures or libraries: the requirement and constraints, a simple baseline, alternatives, why each is adopted or rejected, and the exact source and version consulted. Trivial choices need no record.
