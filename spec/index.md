---
schema_version: 1
document_id: specified-development/overview
role: overview
revision: 2
target_status: mature-complete-product
approval_status: architecture-approved
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: [directory-enhancement-specified, living-spec-paradigm]
---

# Specified Development

Specified Development is a programming paradigm built on GitHub Spec Kit. A repository's canonical `spec/` tree is a living, present-tense description of its software. The spec expands into plans, independent tests and tasks that together carry enough detail for an AI model to reproduce a compatible program from those artifacts alone. Software changes are made spec-first: an author describes the change in the spec as if it already exists, and the difference between the spec and demonstrated behavior is a gap that propagates through plan, tests and tasks. Existing projects join through brownfield onboarding, which characterizes their current behavior into a reviewed spec.

The product is delivered as a versioned Spec Kit preset, extension and bundle. The canonical `spec/` tree describes the entire product, its usage, feature behavior, contracts and operation. The same source content serves as documentation; generated compatibility files, site pages and optional wiki pages are derived views. Present-tense prose describes specified behavior; it never asserts delivery. Delivery status comes only from evidence.

The [distribution feature](features/distribution/index.md) defines lifecycle, installation, execution, regeneration and accounting. The [directory feature](features/directory-specs/index.md) defines document discovery, feature selection, input closure, adapters, freshness and documentation views. Neither feature reduces mature intent to an MVP ladder.

The [lifecycle guide](usage/lifecycle.md) explains authoring, spec-first change and approval. Contracts define [authority](contracts/authority.md), [document compilation](contracts/documents.md) and [distribution execution](contracts/distribution.md). [Upstream compatibility](operations/upstream.md) and [rollout gates](operations/rollout.md) bound operation.

`manifest.json` selects normative document dependencies. `navigation.json` selects reading order. Document dependencies only select inputs; native `execution-contract.yaml` parents alone govern task scheduling. Navigation never becomes a scheduler or silently selects unrelated features.
