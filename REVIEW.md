# Delivery and review

## Delivery status

The product specification describes the intended complete distribution. The table records delivery and qualification for the current repository.

| Area | Current status | Evidence or next gate |
| --- | --- | --- |
| Architecture and target | Architecture approved. The source-directory enhancement is specified. | [Product specification](spec/index.md) and [authority contract](spec/contracts/authority.md). |
| Plans and independent tests | Distribution and directory plans and independent test contracts are review candidates. The 60-task native contract is available for legacy review. | [Distribution plan](build/distribution/plan.md), [distribution tests](build/distribution/tests.md), [directory plan](build/directory-specs/plan.md), and [directory tests](build/directory-specs/tests.md). |
| Implemented tooling | The portable validator checks bundle structure, the review command renders and checks compact views, and expansion reconstructs digest-verified inputs. The foundation validator also checks planned-leaf semantics and independent issue bindings in completion evidence. | [Bundle commands](docs/bundle-validation.md), [validated source revision](https://github.com/pH34r-pH/specified-development/tree/7515ac42569274228b59e79e7b243d184ee72e09), [tooling issue #13](https://github.com/pH34r-pH/specified-development/issues/13), and [leaf validation PR #18](https://github.com/pH34r-pH/specified-development/pull/18). |
| Fixture qualification | A hermetic Linux CPython 3.12.14 fixture demonstrates exact rendering and input expansion. The independent fixture oracle rejects missing or wrong sample code and accepts the correct sample. | [Qualification record](build/bundle-qualification.json) and [regeneration receipt](build/bundle-example-review/regeneration.json). |
| Artifact acceptance | Target task acceptance requires independent authority and task-specific evidence. Structural validation and deterministic rendering establish their respective tooling checks. | [Authority contract](spec/contracts/authority.md) and [validation and acceptance boundary](docs/bundle-validation.md). |
| Complete distribution and source-directory compiler | Implementation pending for the Spec Kit preset, extension, and bundle, and for the source-directory compiler. | [Distribution feature](spec/features/distribution/index.md) and [directory feature](spec/features/directory-specs/index.md). |
| Upstream compatibility and component release | Compatibility qualification and component releases pending. | [Pinned upstream decision](spec/operations/upstream.md), [rollout gates G1 and G4](spec/operations/rollout.md), and [release payload issue #17](https://github.com/pH34r-pH/specified-development/issues/17). |
| Behavioral regeneration | Independent regeneration of a declared product module is pending. | [Rollout gate G4](spec/operations/rollout.md). |
| Deployment | Consumer adoption, activation, and publication require their own evidence and approval. Deployment remains pending. | [Rollout gates G5–G7](spec/operations/rollout.md). |

## Review current bundles

- [Read the 60-task legacy candidate in a compact review](build/bundle-review/README.md).
- [Inspect the validated hermetic example](build/bundle-example-review/README.md).
- [Use the portable validator, exact expansion, and regeneration checks](docs/bundle-validation.md).

The native contract remains the only task graph. Historical accepted evidence is retained; a structural validation result or generated review does not accept a task, authorize a model run, or permit deployment/publication.
