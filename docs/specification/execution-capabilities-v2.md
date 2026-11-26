---
schema_version: 1
document_id: specified-development/execution-capabilities
role: contract
revision: 2
target_status: mature-complete-product
approval_status: review-required
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
qualifiers: [rules-separated-from-observations]
supersedes:
  path: spec/contracts/execution-capabilities.md
  sha256: 0861d156a5f0c9a06d36d46c00dfae271568a384689477dcd7a46050ab0af17e
  revision: 1
---

# Execution capability profiles

This current review successor preserves the execution-capability-v1 behavior. The existing executor/admission owner selected one exact approved model for the entire task attempt. It retained authenticated parent/service admission evidence and never silently substituted or switched models. Selection evidence recorded the accepted request, not worker introspection or proof of hidden backend identity. A rejected or unavailable model request, mismatch, or deliberate fallback failed selection. Unsupported runtime flags were never invented.

Every profile preserved accepted source/input/parent hashes, native hard dependencies, actual permission/target/scope checks, independent behavior tests, immutable receipts, and existing-owner acceptance. Required tools/interfaces and correctness-sensitive capabilities needed evidence. This contract added no scheduler, retry loop, routing model, or infrastructure service.

## Profiles and decision rules

| Profile | Required evidence | Unexposed information and result |
| --- | --- | --- |
| ordinary-implementation-v1 | Approved exact selected model and parent/service admission reference; requested options and admission status; source, parent, permission and scope gates; requested/advisory budget and parent stop plan; required correctness capabilities. | Effective model identity, reasoning, speed, context limits, usage and backend enforcement were nullable with reason unexposed-by-interface. Their absence alone did not block ordinary implementation. Completion proved tested behavior and configured selection only. |
| hard-limit-required-v1 | Each explicit security, financial or technical hard constraint included units/value, affected operation and a verified enforcing backend/control with evidence. Ordinary source, permission and selection gates also applied. | Unsupported, unverified or unexposed required enforcement blocked admission before the protected operation. An advisory request, parent elapsed-time monitor or unknown quota did not satisfy a hard cap. No silent downgrade to ordinary occurred. |
| measurement-qualified-experiment-v1 | The experiment froze its quantitative claim, measurement fields and definitions, source/runtime fingerprints, and applicable dated rates. Qualification required actual evidence for every declared measurement field. Required hard limits separately required verified controls. | Missing effective settings, usage or rates blocked measurement-qualified verdicts for claims requiring them. It did not prohibit unrelated ordinary implementation or erase independently proved behavior. Partial observations were labeled. |

An ordinary profile did not waive an explicit hard constraint or an unknown capability affecting correctness. Admission compared task requirements with supported capabilities rather than requiring all possible telemetry. A rejected requested setting differed from an admitted setting whose effective backend value was unreported.

## Admission, observations and budgets

Receipts separated selection fields (exact model, requested reasoning/speed, admission status, evidence kind/reference) from effective model identity, reasoning, speed, context limit, runtime version and usage. Unavailable effective or usage fields were null with a reason. Requested values were never copied into effective fields. Unknown enforcement remained unknown rather than being reported as disabled or absent.

Ordinary budgets were requested/advisory unless the task explicitly required verified hard enforcement. Missing output-token capacity could remain null. The parent recorded its best-effort stop conditions: check elapsed time/progress at existing task/status checkpoints, request pause/cancel through the existing owner when the advisory time/scope condition was observed, and preserve a bounded blocked/overrun receipt. A best-effort monitor did not promise a real-time timer, token measurement or instant cancellation. A declared hard deadline, cost or token cap used the hard-limit profile.

The existing owner controlled initial admission and separate retries. An owner attempt limit was not a backend token/timer guarantee. The task retained the exact approved model selection across the initial attempt and separately admitted retries. A different model required a separately reviewed repair/task identity, not a retry of the original task. Source or policy changes required a reviewed new input/admission packet. Missing instrumentation did not authorize model switching or semantic repair inside a task.

Exact token-price equivalent depended on observed normalized inclusive input/cache/output counts and applicable dated rates. Cached tokens were an input subset; reasoning was an output subset. Unknown counts, rates or applicability remained null with explicit missing fields and any justified known subtotal, never zero or an invoice. Parent-selected attribution was labeled; effective provider/tier assumptions were not invented. Scoped behavioral evidence could have unqualified measurement status; full cost/settings/model comparisons required actual observations under the measurement profile.

## Migration and compatibility

The fixed-model-v3 policy retained approved role defaults and no-fallback/model-history semantics. Ordinary model records required selection/admission evidence; legacy introspection/context-preflight flags did not assert observations unavailable through the interface. Typed profile/budget fields governed new attempts. Explicit hard-cap requirements could not be downgraded by migration.

Accepted receipts retained original fields, hashes, provenance and verdicts. A contract successor could stale future execution inputs without rewriting historical observations or enforcement claims. Existing-owner review verified scoped compatibility and fresh source/input/parent evidence before another attempt. A new review revision did not replay parents, recreate issue identities, change native dependencies, admit a retry or resume a task automatically.

Unknown-capability fixtures checked conversion and diagnostics against the actual adapter interface. Source/artifact review, permissions, native readiness, and parent verification preceded admission. Candidate review did not imply artifact acceptance, merge, release or consumer activation.

## Evidence reference

The stable record [execution-capability-observations/foundation-v1](../evidence/foundation-capability-observations-v1.md) retains the historical interface observations and bootstrap receipt pointer. It is informative evidence, separate from these behavior rules. The frozen predecessor remains available at its original path for historical native contracts; the current review overlay selects this successor explicitly.
