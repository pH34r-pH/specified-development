# Plan-owned targets and direct implementation

Use this compact record within the existing plan, not as a new required document
or machine-readable target schema. Link product requirements rather than copying
or redefining them. See the [entry contract](../SKILL.md).

| Record | Question answered |
| --- | --- |
| Component and real consumers | What responsibility and supported deployments are in scope? |
| Current implementation and candidate | What exists, and which bounded alternative is being considered? |
| Target status | Is it desired, authorized for experiment, accepted in the plan, or qualified by evidence? |
| Language/runtime, versions and libraries | Why does this target fit the platform/ecosystem and requirements? What existing solution was inspected? |
| Workload and alternatives | What scale, operation mix, invariants and failure cases matter? Compare the simplest viable baseline and relevant alternatives. |
| Direct path and ownership | Which concrete operations and state owners deliver the product without speculative runtime machinery? |
| Variation placement | Which choices are fixed at build time, and which must remain runtime-variable? |
| Acceptance and selection | Which independent product gates cannot regress, and what plan objective distinguishes conforming candidates? |
| Qualification and recovery | Which commands, fixtures, environments, measurements, stop rules and rollback scope justify the decision? |
| Permitted discretion | Which local implementation choices need no further approval? |

A desired target is not migration authorization. A qualified target needs actual
consumer-level evidence, not just a successful compile. Product quality and
security gates are not weighted against performance in one score.

For each material layer choose retain, remove, specialize at build time, or keep
as an explicit external/migration boundary. State the required duty and identified
consumers. Removing a package while recreating its parser, lifecycle or renderer
can increase what we own; count those obligations rather than celebrating fewer
dependencies. Useful compile-time abstraction may already impose no comparable
runtime machinery. Do not infer a benefit from a language or API name.

Example: the product must export documented records offline and preserve ordering
and failure semantics. One plan may use the current runtime and a standard library;
another may justify a compiled portable core. The specification does not acquire
Rust structs, FFI calls or package names merely because the second plan is chosen.
A failed offline experiment rejects/repairs that plan, not the offline requirement.

Use incumbent versus simpler same-language version versus target-language version
when causal attribution requires separating deletion from migration. Do not demand
three implementations when there is no incumbent, no such claim or no useful
information gained. Changes to algorithm, precision or behavior are distinct
factors; qualify a necessarily coupled change as a bundle rather than attributing
its result to language alone.
