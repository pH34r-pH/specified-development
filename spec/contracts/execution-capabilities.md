---
schema_version: 1
document_id: specified-development/execution-capabilities
role: contract
revision: 3
target_status: mature-complete-product
approval_status: review-required
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
qualifiers: [rules-separated-from-observations]
---

# Execution capability profiles

The versioned `execution-capability-v1` contract distinguishes model selection, runtime observations, requested budgets, verified enforcement and measurement claims. The existing executor/admission owner selects one exact approved model for the entire task attempt. It retains authenticated parent/service admission evidence and never silently substitutes or switches models. Selection evidence records the accepted request, not worker introspection or proof of hidden backend identity. A rejected or unavailable model request, mismatch or deliberate fallback fails selection. Unsupported runtime flags are never invented.

Every profile preserves accepted source/input/parent hashes, native hard dependencies, actual permission/target/scope checks, independent behavior tests, immutable receipts and existing-owner acceptance. Required tools/interfaces and correctness-sensitive capabilities need evidence. This contract adds no scheduler, retry loop, routing model or infrastructure service.

## Profiles and decision rules

| Profile | Required evidence | Unexposed information and result |
| --- | --- | --- |
| ordinary-implementation-v1 | Approved exact selected model and parent/service admission reference; requested options and admission status; source, parent, permission and scope gates; requested/advisory budget and parent stop plan; required correctness capabilities. | Effective model identity, reasoning, speed, context limits, usage and backend enforcement are nullable with reason unexposed-by-interface. Their absence alone does not block ordinary implementation. Completion proves tested behavior and configured selection only. |
| hard-limit-required-v1 | Each explicit security, financial or technical hard constraint includes units/value, affected operation and a verified enforcing backend/control with evidence. Ordinary source, permission and selection gates also apply. | Unsupported, unverified or unexposed required enforcement blocks admission before the protected operation. An advisory request, parent elapsed-time monitor or unknown quota does not satisfy a hard cap. No silent downgrade to ordinary occurs. |
| measurement-qualified-experiment-v1 | The experiment freezes its quantitative claim, measurement fields and definitions, source/runtime fingerprints, and applicable dated rates. Qualification requires actual evidence for every declared measurement field. Required hard limits separately require verified controls. | Missing effective settings, usage or rates block measurement-qualified verdicts for claims requiring them. They do not prohibit unrelated ordinary implementation or erase independently proved behavior. Partial observations are labeled. |

An ordinary profile does not waive an explicit hard constraint or an unknown capability affecting correctness. Admission compares task requirements with supported capabilities rather than requiring all possible telemetry. A rejected requested setting differs from an admitted setting whose effective backend value is unreported.

## Admission, observations and budgets

Receipts separate selection fields (exact model, requested reasoning/speed, admission status, evidence kind/reference) from effective model identity, reasoning, speed, context limit, runtime version and usage. Unavailable effective or usage fields are null with a reason. Requested values are never copied into effective fields. Unknown enforcement remains unknown rather than being reported as disabled or absent.

Ordinary budgets are requested/advisory unless the task explicitly requires verified hard enforcement. Missing output-token capacity can remain null. The parent records its best-effort stop conditions: check elapsed time/progress at existing task/status checkpoints, request pause/cancel through the existing owner when the advisory time/scope condition is observed, and preserve a bounded blocked/overrun receipt. A best-effort monitor does not promise a real-time timer, token measurement or instant cancellation. A declared hard deadline, cost or token cap uses the hard-limit profile.

The existing owner controls initial admission and separate retries. An owner attempt limit is not a backend token/timer guarantee. The task retains the exact approved model selection across the initial attempt and separately admitted retries. A different model requires a separately reviewed repair/task identity, not a retry of the original task. Source or policy changes require a reviewed new input/admission packet. Missing instrumentation does not authorize model switching or semantic repair inside a task.

Exact token-price equivalent depends on observed normalized inclusive input/cache/output counts and applicable dated rates. Cached tokens are an input subset; reasoning is an output subset. Unknown counts, rates or applicability remain null with explicit missing fields and any justified known subtotal, never zero or an invoice. Parent-selected attribution is labeled; effective provider/tier assumptions are not invented. Scoped behavioral evidence can have unqualified measurement status; full cost/settings/model comparisons require actual observations under the measurement profile.

## Migration and compatibility

The fixed-model-v3 policy retains approved role defaults and no-fallback/model-history semantics. Ordinary model records require selection/admission evidence; legacy introspection/context-preflight flags do not assert observations unavailable through the interface. Typed profile/budget fields govern new attempts. Explicit hard-cap requirements cannot be downgraded by migration.

Accepted receipts retain original fields, hashes, provenance and verdicts. A revision of this contract can stale future execution inputs without rewriting historical observations or enforcement claims. Existing-owner review verifies scoped compatibility and fresh source/input/parent evidence before another attempt. A new revision does not replay parents, recreate issue identities, change native dependencies, admit a retry or resume a task automatically.

Unknown-capability fixtures check conversion and diagnostics against the actual adapter interface. Source/artifact review, permissions, native readiness and parent verification precede admission. Candidate review does not imply artifact acceptance, merge, release or consumer activation.

## Evidence reference

The stable record [execution-capability-observations/foundation-v1](https://github.com/pH34r-pH/specified-development/blob/main/docs/evidence/foundation-capability-observations-v1.md) retains the historical interface observations and bootstrap receipt pointer. It is informative evidence, separate from these behavior rules. Earlier revisions of this contract remain available in the retained historical snapshot for historical native contracts.
