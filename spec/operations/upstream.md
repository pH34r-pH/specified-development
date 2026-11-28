---
schema_version: 1
document_id: specified-development/upstream
role: operation
revision: 2
target_status: mature-complete-product
approval_status: decision-approved
artifact_acceptance: unspecified
delivery_status: researched-only
delivery_evidence: []
qualifiers: [distribution-choice-approved]
---

# Distribution rather than fork

The design selects a versioned preset plus executable extension plus bundle. A fork is unnecessary for the observed supported override boundaries and would add upstream maintenance. A fork decision reopens only after a concrete supported extension/preset path fails a documented independent compatibility test.

Research is pinned to GitHub Spec Kit **v1.0.13**, released **2026-09-29T12:55:06Z**, commit **`f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9`** (annotated tag object `ec1423f75fe315ff8492f586141ae00958c3dd41`). Proposed unpublished components are `ph34r-lifecycle@1.0.0`, `ph34r-contracts@1.0.0` and `ph34r-standard@1.0.0`. No catalog registration, release or install is claimed.

Upstream uses per-feature `specs/<feature>/spec.md`, rather than one monolithic project spec. Its [common path resolver](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/scripts/bash/common.sh#L164-L237) supports `SPECIFY_FEATURE_DIRECTORY` and no-persist behavior but fixes sibling `spec.md`, `plan.md`, `tasks.md`, `research.md` and `contracts`. The environment override alone does not split canonical source from build outputs. [setup-plan](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/scripts/bash/setup-plan.sh) uses those paths; [clarify](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/templates/commands/clarify.md#L180-L208) writes FEATURE_SPEC directly. Canonical-edit commands therefore require replacement, and a read-only generated adapter preserves primitive compatibility.

[Presets](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/docs/reference/presets.md) override relevant templates, commands and scripts; [extensions](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/docs/reference/extensions.md) supply executable guards and projectors. Stock MVP and optional-test directions are replaced. The stock task command performs model decomposition; setup-tasks only scaffolds prerequisites, and taskstoissues is agent-driven. This distribution authors semantic metadata once and uses deterministic projection afterward.

The [bundle implementation](https://github.com/github/spec-kit/tree/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli) can skip existing component IDs without comparing versions. Refresh/update does not provide complete rollback. Bundle ZIPs represent manifests and assets, not an offline payload pack. Native bundle installation accepts catalog IDs or local paths, not invented `bundle --from` release URLs; download and hash verification precede local-path installation. Separate component archives, lock/checksums and generated-asset checks are required. Upgrades stage and retain journaled rollback artifacts.

The pinned Codex adapter supports model selection but does not demonstrate per-step reasoning translation. Runtime, permissions and settings are observed before dispatch; unsupported parameters block instead of being fabricated. The existing executor's limitations are qualified privately per consumer; no public foundation claims undocumented production compatibility.

[MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/) supports source/site directories and navigation. [GitHub wiki guidance](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages) documents a separate Git-backed wiki. These are optional projection targets, not authority or deployed services. Apache-2.0 is explicitly selected for original distribution work; the [license text](https://www.apache.org/licenses/LICENSE-2.0) is included verbatim.
