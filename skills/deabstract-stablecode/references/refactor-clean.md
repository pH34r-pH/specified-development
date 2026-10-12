# Remove unnecessary layers

Adapted from David Zhang's refactor-clean; see [NOTICE](../NOTICE.md). Apply only to
an authorized task under the [entry contract](../SKILL.md).

Identify the concept, every current owner, real producers and consumers, and the
required behavior each layer enforces. Trace the complete path, including storage,
imports/exports, retries, cancellation, external callers and failures. Absence of a
caller in a local grep does not prove a published interface has no consumers.

Inspect what the platform and chosen libraries already provide before adding guards,
retries, cleanup services, translation objects or lifecycle code around them.
Prefer direct calls to established interfaces. A layer may be a real trust,
compatibility or state-ownership boundary; do not delete it simply because it wraps
another function. Persisted data and external inputs are not trustworthy merely
because our code originally wrote them.

Choose the natural owner and move consumers to it. Consolidate duplicated owners;
split an overloaded module when it actually contains distinct responsibilities.
Names should describe current responsibilities, not the historical experiment that
created them. Keep renames inside the approved scope and preserve real external
names until the accepted migration allows them to change.

Before relaxing a check or making an input optional, ask whether the mechanism
should disappear entirely. A justified deletion removes obsolete call sites,
configurations, tests/support code and documentation residue in the same bounded
change. A retained bridge needs an identified consumer, behavior and removal
condition. A permanent protocol boundary is not a temporary bridge and need not
have a fabricated retirement date.

Do not trade enforceable product promises for prose. Retain a check or move its
required duty to the correct boundary with independent negative tests. Keep
runtime-editable policy and capability negotiation required by the product.
Do not flatten cohesive modules, replace mature cryptography, duplicate useful
generics or create a bespoke framework just to remove a dependency.

Before and after the change, exercise real consumer paths and independent expected
results, including relevant ordering, failure, side-effect, concurrency, recovery
and compatibility cases. A structural-looking diff is not proof of equivalence.
Use [test audit](audit-tests.md) when coverage moves, and
[qualification](qualify-change.md) when claiming measured improvements.

Record removed mechanisms and added obligations separately. Production lines,
tests, documentation, services, flags and build steps can be useful observations;
none is a deletion target or substitute for behavior. A justified retention or a
smaller refactor than initially expected is an acceptable outcome.
