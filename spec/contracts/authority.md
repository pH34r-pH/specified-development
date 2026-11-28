---
schema_version: 1
document_id: specified-development/authority
role: contract
revision: 4
target_status: mature-complete-product
approval_status: architecture-approved
artifact_acceptance: unspecified
delivery_status: designed-only
delivery_evidence: []
qualifiers: [living-spec-paradigm]
---

# Authority and retention

Canonical `spec/` documents, contracts and fixtures, plus dependency locks and accepted generation instructions, define product behavior. The canonical spec is a living present-tense document revised in place; it is the authority over behavior at every revision. Accepted plan, independent test and task revisions compile that intent. Code is a retained regenerable output; existing source is evidence for compatibility and regression, not permission to invent behavior.

Target, approval, artifact acceptance, implementation, test, deployment and regeneration fields are separate. Present-tense prose describes specified behavior without asserting delivered behavior; delivery is established only by evidence, and a requirement is satisfied only by passing independent evidence at an exact source revision. Accepted revisions record exact predecessor hashes, authority provenance, acceptance actor and time, and immutable revision identity. A generated `spec.md`, site or wiki carries a derived label and can never supersede source.

Brownfield [onboarding](../usage/onboarding.md) has one bounded exception: in characterization mode, an onboarded area's first specification and plan are drafted from its existing code, documentation, tests and observed behavior, with sources recorded per requirement. A human reviewer's acceptance of that specification ends characterization mode for the area; afterwards existing code is evidence only. Independent test expectations are never derived from implementation output, during or after onboarding. Paths outside onboarded areas are unspecified and carry no authority.

Revising a living source never rewrites history. Historical frozen inputs are retained as content-addressed snapshots, and every recorded frozen hash resolves against its retained snapshot rather than the current working tree. A changed requirement invalidates only its own evidence and its dependent descendants.

`build/<feature>/plan.md`, `tests.md` and `tasks.md` are tracked candidate/current authoring records. This central program retains its native graph at `build/execution-contract.yaml` and its identity table at `build/native-bindings.json`. Acceptance archives the exact source closure, locks, plan/tests/tasks/native contract and nonsecret evidence beneath `build/<feature>/accepted/<revision>/`. Accepted directories are append-only. An input revision can stale them for future execution but cannot alter their historical verdicts. Git retention or an explicitly approved durable store preserves them; location under build does not imply disposability.

Only `build/site/`, `build/wiki-stage/`, feature `.tmp/`, `candidate/`, `runtime/`, generated `spec.md`, `source-map.json`, `inputs.lock.json` and copied `contracts/` are cleanable. Cleanup uses an explicit managed inventory, real-path confinement and before-hash checks; it refuses symlinks, unknown paths and accepted/code locations. Source code deletion is never an authorized cleanup operation.

Task metadata contains semantic parents as authoring input. Deterministic projection places the sole executable edge set in native `execution-contract.yaml` `tasks.<id>.parents`; projected namespaced records omit parents. Document dependencies select input closure only. Existing Kanban aggregate semantics and the selected executor's claims and retries remain unchanged.

Any missing assumption creates a separate earliest-authority repair leaf. The current attempt stops with evidence; the repair freezes its own model and inputs. Accepted changes invalidate changed task contracts and their native descendants, preserving unaffected receipts. Scripts do not infer missing semantics or switch models.

## Foundation receipts and read authorization

Foundation acceptance requires sanitized durable records at `build/foundation/accepted/receipts/T001/<attempt-id>/bootstrap.json` and `build/foundation/accepted/receipts/T002/<attempt-id>/completion.json`. The exact qualified task ID, native ID and attempt slug are bound before writing. These paths are tracked, excluded from cleanup and append-only; existing files are never overwritten. A path containing accepted does not make a record accepted: an actual authorized verdict, actor and time, and accepted source revision remain required.

The foundation uses the existing repository's append-only `evidence/foundation-receipts` branch as its declared durable receipt store, subject to observed write permission and existing-owner approval before claim. A receipt commit and its immutable file/blob reference are recorded in the existing task owner. A completion receipt references the tested PR head and exact check-run heads and is retained on that separate evidence ref after checks, preserving the tested source head. Updating tested source requires new check evidence and a new receipt. Receipt storage adds no task scheduler or independent execution ledger. If durable storage or evidence permission is unavailable, completion remains blocked.

The selected existing task owner promotes the exact sanitized receipt file with its approved Git/GitHub operations; the model leaf's validation commands do not grant arbitrary shell or API write permission. Product payload inventory describes the tested source/implementation snapshot. The separate evidence ref admits only the task's declared sanitized receipt paths alongside unchanged source provenance, and does not alter that tested payload or identity graph. CI validates source PRs and controlled source branches and excludes receipt-only evidence-ref pushes; CI remains read-only and never promotes receipts.

The bootstrap record retains qualified/native/attempt IDs, accepted contract and source hashes, actual repository/base/seed commit and README/LICENSE hashes, issue identity and creator, permission and disclosure evidence, timestamp and actual acceptance verdict. The completion record additionally retains the accepted parent receipt's immutable reference and hash, parent-selected model and admission evidence, separately nullable effective runtime and settings, requested/advisory budgets or verified hard limits by capability profile, permission evidence, changed-path and input inventory, issue/native-parent readback, PR/tested-head/check-run evidence and actual verdict. Observed usage and rates, or explicit missing fields, accompany cost evidence. Secrets, raw prompts and logs, signed URLs and private source paths are excluded.

Raw private runtime logs remain under ignored, cleanable `build/foundation/runtime/<task-id>/<attempt-id>/`; they cannot substitute for those durable records and are never public inventory entries. Retention validation checks both task receipt paths with actual gitignore rules and refuses cleanup of accepted, history and code locations.

At claim, explicit read scope and approved permissions bound every read. Every frozen authoritative input and claim-time control file falls inside the closed read allowlist; freezing a hash alone never expands permission. Deterministic validation can read all files explicitly declared by the sanitized public inventory after confinement and symlink checks, including all source task records and the native graph. It supplies only assigned-leaf semantics and bounded diagnostics to the model. A read allowlist does not grant write permission, and output scope does not authorize changing frozen authority or publishing raw private logs. Known control and self-referential artifact hashes are frozen in the external claim packet instead of embedded recursively.

Execution and model evidence follow the [execution capability contract](execution-capabilities.md): the selected request and effective telemetry are separate. Ordinary unexposed telemetry does not create a hard gate; explicit hard protection, correctness, permission, source/input/parent and actual acceptance requirements remain strict. Receipt field absence is labeled rather than filled from requested values. The accepted bootstrap receipt retains its original commit, hash and verdict; later profile corrections never rewrite it or automatically resume its dependent task.
