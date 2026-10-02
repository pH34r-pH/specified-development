---
document_id: specified-development/execution-capabilities
revision: 1
target_status: mature-complete-product
approval_status: proposed-contract-repair-parent-review-required
delivery_status: designed-only
delivery_evidence: []
---

# Execution capability profiles

The versioned `execution-capability-v1` contract distinguished model selection, runtime observations, requested budgets, verified enforcement and measurement claims. The existing executor/admission owner selected one exact approved model for the entire task attempt. It retained authenticated parent/service admission evidence and never silently substituted or switched models. Selection evidence was evidence of the accepted request, not worker introspection or proof of hidden backend identity. A rejected/unavailable model request, mismatch or deliberate fallback failed the selection gate. No unsupported runtime flag was invented.

Every profile preserved accepted source/input/parent hashes, native hard dependencies, actual permission/target/scope checks, independent behavior tests, immutable receipts and existing-owner acceptance. Required tools/interfaces and any correctness-sensitive capability still needed evidence. No new scheduler, retry loop, routing model or infrastructure service was introduced.

## Profiles and decision rules

| Profile | Required evidence | Unexposed information and result |
| --- | --- | --- |
| `ordinary-implementation-v1` | Approved exact selected model and parent/service admission ref; requested options and their admission status; source/parent/permission/scope gates; requested/advisory budget and parent stop plan; required correctness capabilities. | Effective model identity/reasoning/speed/context limits, usage and backend resource enforcement were nullable with reason `unexposed-by-interface`. Their absence alone did not block a scaffold validator. Completion proved tested behavior and configured selection only. |
| `hard-limit-required-v1` | The task explicitly named each security, financial or technical hard constraint, units/value, affected operation and verified enforcing backend/control with evidence. It also met ordinary source/permission/selection gates. | Unsupported, unverified or unexposed required enforcement blocked admission before the protected operation. An advisory request, parent elapsed-time monitor or unknown quota could not satisfy a hard cap. No silent downgrade to ordinary occurred. |
| `measurement-qualified-experiment-v1` | Before execution, the experiment froze its quantitative claim, required measurement fields, definitions, source/runtime fingerprints and applicable dated rates. Qualified status required actual evidence for every declared measurement field; hard limits, if demanded, separately required verified controls. | Missing effective settings/usage/rates blocked the *measurement-qualified verdict* for claims requiring them. It did not prohibit unrelated ordinary implementation or erase independently proved behavior. Partial observations were labeled, and no full comparison or cost claim was fabricated. |

An ordinary profile could not waive an explicit hard constraint or unknown capability affecting correctness. Admission compared task requirements with declared supported capabilities, not with a blanket demand for all possible telemetry. Examples: Python/parser correctness requirements and source confinement still failed closed when unknown; an unexposed model context limit alone was optional for the bounded foundation task. A rejected requested setting differed from an admitted setting whose effective backend value was unreported.

## Admission, observations and budgets

Receipts separated `selection={exact_model, requested_reasoning_effort, requested_speed_tier, admission_status, evidence_kind, evidence_ref}` from `effective={model_identity, reasoning_effort, speed_tier, context_limit, runtime_version}` and `usage`. Each unavailable effective/usage field was null with a reason; requested values were never copied into effective fields. The current cloud profile exposed parent selection of `gpt-6-luna` and requested `xhigh`, while worker effective model/settings/context, enforceable token cap and enforced 90-minute timer were unexposed. This was a declared interface observation, not a universal provider claim.

`budget.wall_minutes=90` and legacy numeric output budgets were **requested/advisory** for ordinary work. Missing output-token capacity could stay null. `backend_enforcement` recorded only observed controls; unknown enforcement remained null. The parent recorded its best-effort stop conditions: check elapsed time/progress at existing task/status checkpoints, request pause/cancel through the existing owner when the advisory time/scope condition was observed, and preserve a bounded blocked/overrun receipt. It did not promise a real-time timer, token measurement or instant cancellation. A declared hard deadline/cost/token cap used the hard-limit profile instead.

The existing owner controlled the initial admission and separate retries. One requested initial attempt was an owner admission rule, not a backend token/timer guarantee. The task retained its exact approved model selection across an initial attempt and any separately admitted retries. A different model required a separately reviewed repair/task identity; it was not a retry of the original task. Source/policy changes required a reviewed new input/admission packet; missing instrumentation did not authorize model switching or semantic repair inside a task.

Exact token-price equivalent remained conditional on actual normalized inclusive input/cache/output counts and applicable dated rates. Cached tokens were an input subset; reasoning was an output subset. Unknown counts/rates/applicability stayed null with explicit missing fields and any justified known subtotal, never zero or an invoice. Parent-selected attribution was labeled; effective provider/tier assumptions were not invented. A behavioral regeneration result could remain scoped behavioral evidence with unqualified measurement status; a full cost/settings/model experiment needed its measurement profile and actual required observations.

## Migration and compatibility

This was an explicit reviewed correction of the previous blanket instrumentation gate. `fixed-model-v3` retained approved role defaults and no-fallback/model-history semantics. Future ordinary model records now required *selection/admission* evidence; legacy `observed_identity_required` and context-preflight flags no longer asserted unavailable worker introspection. Typed profile/budget fields governed new attempts. Explicit hard-cap requirements were preserved and could not be downgraded by migration. Existing accepted receipts retained their original fields, hashes and provenance; no history was rewritten as newly observed or enforced.

The [accepted bootstrap receipt](https://github.com/pH34r-pH/specified-development/blob/8b26481704e0483bb94c41c2c93407f234c9e0ae/build/foundation/accepted/receipts/T001/bootstrap-20261001T232906Z/bootstrap.json) stayed at commit `8b26481704e0483bb94c41c2c93407f234c9e0ae`, path `build/foundation/accepted/receipts/T001/bootstrap-20261001T232906Z/bootstrap.json`, SHA256 `ed807b05cdce8bc7d8b9bbf86dd0a7a60824374f357c4ceee79c92f37ffb411e`. Its T001 behavior/scope/issue identity and accepted verdict were unchanged by this model-telemetry correction. The existing owner could retain that parent evidence after verifying this scoped compatibility; the older frozen T002 input list inside it remained historical. [Issue 2](https://github.com/pH34r-pH/specified-development/issues/2) and [issue 3](https://github.com/pH34r-pH/specified-development/issues/3) kept their markers and native dependency; an accepted receipt did not imply either issue was closed. A new T002 claim packet froze this reviewed source/input set and the same parent receipt; no issue recreation, parent replay, model fallback or automatic resumption followed.

Unknown-capability fixtures tested profile conversion and diagnostics against the actual adapter interface. Source/artifact review, permissions, native scheduling readiness and parent verification still preceded admission. This proposed revision did not accept new artifacts, dispatch T002, change the receipt/evidence ref, merge, release or modify a consumer.
