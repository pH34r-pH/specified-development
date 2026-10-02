---
document_id: specified-development/overview
target_status: mature-complete-product
approval_status: architecture-approved-directory-enhancement-specified
delivery_status: designed-only
delivery_evidence: []
---

# Specified Development

The product gave repositories a consistent specification lifecycle through a versioned Spec Kit preset, extension, and bundle. A well-organized canonical `spec/` tree described the entire intended product, its usage, feature behavior, contracts, and operation. The same source content served as documentation; generated compatibility files, site pages, and optional wiki pages were derived views.

The [distribution feature](features/distribution/index.md) defined lifecycle, installation, execution, regeneration, and accounting. The [directory feature](features/directory-specs/index.md) defined document discovery, feature selection, input closure, adapters, freshness, and documentation views. Neither feature reduced mature intent to an MVP ladder.

The [lifecycle guide](usage/lifecycle.md) explained authoring and approval. Contracts defined [authority](contracts/authority.md), [document compilation](contracts/documents.md), and [distribution execution](contracts/distribution.md). [Upstream compatibility](operations/upstream.md) and [rollout gates](operations/rollout.md) bounded operation.

`manifest.json` selected normative document dependencies. `navigation.json` selected reading order. Document dependencies only selected inputs; native `execution-contract.yaml` parents alone governed task scheduling. Navigation never became a scheduler or silently selected unrelated features.
