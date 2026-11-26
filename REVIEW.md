# Delivery and review

## Delivery status

The product specification describes the intended complete distribution. The table records delivery and qualification for the current repository.

| Area | Current status | Evidence or next gate |
| --- | --- | --- |
| Architecture and target | Architecture approved. The source-directory enhancement is specified. | [Product specification](spec/index.md) and [authority contract](spec/contracts/authority.md). |
| Plans and independent tests | Distribution and directory plans and independent test contracts are review candidates. The 60-task native contract is available for legacy review. | [Distribution plan](build/distribution/plan.md), [distribution tests](build/distribution/tests.md), [directory plan](build/directory-specs/plan.md), and [directory tests](build/directory-specs/tests.md). |
| Implemented tooling | Version 2 bundle validation binds command definitions and source bytes to an independent review pin, rejects portable path aliases, and supports the qualified CPython 3.12 family. Compact review and exact expansion retain the original bytes. The foundation validator checks planned leaves and independent completion issue bindings. | [Bundle commands and scope](docs/bundle-validation.md), [installed commands and diagnostics](docs/tooling.md), and [tooling issue #13](https://github.com/pH34r-pH/specified-development/issues/13). |
| Specification and task authoring | A versioned review overlay validates frontmatter, section classifications, document-qualified requirements and independent coverage. A generated 60-task view is checked against the existing structured authoring records and native graph. | [Specification review](docs/specification-review.md), [current capability contract](docs/specification/execution-capabilities-v2.md), and [task review](docs/task-review.md). |
| Fixture qualification | The original Linux CPython 3.12.14 qualification is retained as historical evidence. Current checks cover both 3.12.12 and 3.12.14, exact rendering and lossless expansion, independent red/green oracle behavior, and clean installed/module/portable invocations. | [Historical qualification](build/bundle-qualification.json), [version 2 regeneration receipt](build/bundle-v2-review/regeneration.json), and [required quality gates](docs/quality-checks.md). |
| Artifact acceptance | Target task acceptance requires independent authority and task-specific evidence. Structural validation and deterministic rendering establish their respective tooling checks. | [Authority contract](spec/contracts/authority.md) and [validation and acceptance boundary](docs/bundle-validation.md). |
| Complete distribution and source-directory compiler | Implementation pending for the Spec Kit preset, extension, and bundle, and for the source-directory compiler. | [Distribution feature](spec/features/distribution/index.md) and [directory feature](spec/features/directory-specs/index.md). |
| Upstream compatibility and component release | Compatibility qualification and component releases pending. | [Pinned upstream decision](spec/operations/upstream.md), [rollout gates G1 and G4](spec/operations/rollout.md), and [release attribution](LICENSING.md). |
| Behavioral regeneration | Independent regeneration of a declared product module is pending. | [Rollout gate G4](spec/operations/rollout.md). |
| Deployment | Consumer adoption, activation, and publication require their own evidence and approval. Deployment remains pending. | [Rollout gates G5–G7](spec/operations/rollout.md). |

## Review current bundles

- [Read the 60-task legacy candidate in a compact review](build/bundle-review/README.md).
- [Inspect the version 2 example with reviewed command identities](build/bundle-v2-review/README.md).
- [Inspect the historical version 1 structural example](build/bundle-example-review/README.md).
- [Read the complete generated task view](docs/task-review.md).
- [Use the portable validator, exact expansion, and regeneration checks](docs/bundle-validation.md).

The native contract remains the only task graph. Historical accepted evidence is retained; a structural validation result or generated review does not accept a task, authorize a model run, or permit deployment/publication.
