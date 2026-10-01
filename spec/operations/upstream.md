---
document_id: specified-development/upstream
target_status: mature-complete-product
approval_status: distribution-choice-approved
delivery_status: researched-only
delivery_evidence: []
---

# Distribution rather than fork

The design selected a versioned preset plus executable extension plus bundle. A fork was unnecessary for the observed supported override boundaries and would add upstream maintenance. A fork decision reopened only after a concrete supported extension/preset path failed a documented independent compatibility test.

Research was pinned to GitHub Spec Kit **v1.0.13**, released **2026-09-29T12:55:06Z**, commit **`f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9`** (annotated tag object `ec1423f75fe315ff8492f586141ae00958c3dd41`). Proposed unpublished components were `ph34r-lifecycle@1.0.0`, `ph34r-contracts@1.0.0`, and `ph34r-standard@1.0.0`. No catalog registration/release/install was claimed.

Upstream used per-feature `specs/<feature>/spec.md`, rather than one monolithic project spec. Its [common path resolver](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/scripts/bash/common.sh#L164-L237) supported `SPECIFY_FEATURE_DIRECTORY` and no-persist behavior but fixed sibling `spec.md`, `plan.md`, `tasks.md`, `research.md` and `contracts`. The environment override alone did not split canonical source from build outputs. [setup-plan](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/scripts/bash/setup-plan.sh) used those paths; [clarify](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/templates/commands/clarify.md#L180-L208) wrote FEATURE_SPEC directly. Canonical-edit commands therefore required replacement, and a read-only generated adapter preserved primitive compatibility.

[Presets](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/docs/reference/presets.md) overrode relevant templates/commands/scripts; [extensions](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/docs/reference/extensions.md) supplied executable guards/projectors. Stock MVP and optional-test directions were replaced. The stock task command performed model decomposition; setup-tasks only scaffolded prerequisites, and taskstoissues was agent-driven. This distribution authored semantic metadata once and used deterministic projection afterward.

[Bundle implementation](https://github.com/github/spec-kit/tree/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli) could skip existing component IDs without comparing versions. Refresh/update did not provide complete rollback. Bundle ZIPs represented manifests/assets, not an offline payload pack. Native bundle installation accepted catalog IDs or local paths, not invented `bundle --from` release URLs; download/hash verification preceded local-path installation. Separate component archives, lock/checksums and generated-asset checks were required. Upgrades staged and retained journaled rollback artifacts.

The pinned Codex adapter supported model selection but did not demonstrate per-step reasoning translation. Runtime/permissions/settings were observed before dispatch; unsupported parameters blocked instead of being fabricated. The existing executor's limitations were qualified privately per consumer; no public foundation claimed undocumented production compatibility.

[MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/) supported source/site directories and navigation. [GitHub wiki guidance](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages) documented a separate Git-backed wiki. These were optional projection targets, not authority or deployed services. Apache-2.0 was explicitly selected for original distribution work; [license text](https://www.apache.org/licenses/LICENSE-2.0) was included verbatim.
