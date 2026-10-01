---
document_id: specified-development/authority
revision: 2
target_status: mature-complete-product
approval_status: architecture-approved
delivery_status: designed-only
delivery_evidence: []
---

# Authority and retention

Canonical `spec/` documents/contracts/fixtures plus dependency locks and accepted generation instructions defined intended behavior. Accepted plan, independent test and task revisions compiled that intent. Code was a retained regenerable output; existing source was evidence for compatibility/regression, not permission to invent behavior.

Target, approval, artifact acceptance, implementation, test, deployment and regeneration fields were separate. Candidate prose could describe completed product behavior without asserting delivered behavior. Accepted revisions recorded exact predecessor hashes, authority provenance, acceptance actor/time and immutable revision identity. A generated `spec.md`, site or wiki carried a derived label and could never supersede source.

`build/<feature>/plan.md`, `tests.md`, and `tasks.md` were tracked candidate/current authoring records. This central program retained its sole native graph at `build/execution-contract.yaml` and its identity table at `build/native-bindings.json`. Acceptance archived exact source closure, locks, plan/tests/tasks/native contract and nonsecret evidence beneath `build/<feature>/accepted/<revision>/`. Accepted directories were append-only. An input revision could stale them for future execution but could not alter their historical verdicts. Git retention or an explicitly approved durable store preserved them; location under build did not imply disposability.

Only `build/site/`, `build/wiki-stage/`, feature `.tmp/`, `candidate/`, `runtime/`, generated `spec.md`, `source-map.json`, `inputs.lock.json`, and copied `contracts/` were cleanable. Cleanup used an explicit managed inventory, real-path confinement and before-hash checks; it refused symlinks, unknown paths and accepted/code locations. Source code deletion was never an authorized cleanup operation.

Task metadata contained semantic parents as authoring input. Deterministic projection placed the sole executable edge set in native `execution-contract.yaml` `tasks.<id>.parents`; projected namespaced records omitted parents. Document dependencies selected input closure only. Existing Kanban aggregate semantics and the selected executor's claims/retries remained unchanged.

Any missing assumption created a separate earliest-authority repair leaf. The current attempt stopped with evidence; the repair froze its own model and inputs. Accepted changes invalidated changed task contracts and their native descendants, preserving unaffected receipts. Scripts did not infer missing semantics or switch models.

## Foundation receipts and read authorization

Foundation acceptance required sanitized durable records at `build/foundation/accepted/receipts/T001/<attempt-id>/bootstrap.json` and `build/foundation/accepted/receipts/T002/<attempt-id>/completion.json`. The exact qualified task ID, native ID and attempt slug were bound before writing. These paths were tracked, excluded from cleanup, and append-only; existing files were never overwritten. A path containing accepted did not make a record accepted: an actual authorized verdict, actor/time and accepted source revision remained required.

The foundation used the existing repository's append-only `evidence/foundation-receipts` branch as its declared durable receipt store, subject to observed write permission and existing-owner approval before claim. A receipt commit and its immutable file/blob reference were recorded in the existing task owner. A completion receipt referenced the tested PR head and exact check-run heads and was retained on that separate evidence ref after checks, preserving the tested source head. Updating tested source required new check evidence and a new receipt. Receipt storage added no task scheduler or independent execution ledger. If durable storage or evidence permission was unavailable, completion remained blocked.

The selected existing task owner promoted the exact sanitized receipt file with its approved Git/GitHub operations; the model leaf's validation commands did not grant arbitrary shell/API write permission. Product payload inventory described the tested source/implementation snapshot. The separate evidence ref admitted only the task's declared sanitized receipt paths alongside unchanged source provenance, and did not alter that tested payload or identity graph. CI validated source PRs/controlled source branches and excluded receipt-only evidence-ref pushes; CI remained read-only and never promoted receipts.

The bootstrap record retained qualified/native/attempt IDs, accepted contract/source hashes, actual repository/base/seed commit and README/LICENSE hashes, issue identity/creator, permission/disclosure evidence, timestamp and actual acceptance verdict. The completion record additionally retained the accepted parent receipt's immutable reference/hash, observed fixed model/runtime and requested/effective settings, bound context/output budget, permission evidence, changed-path/input inventory, issue/native-parent readback, PR/tested-head/check-run evidence and actual verdict. Observed usage/rates or explicit missing fields accompanied cost evidence. Secrets, raw prompts/logs, signed URLs and private source paths were excluded.

Raw private runtime logs remained under ignored/cleanable `build/foundation/runtime/<task-id>/<attempt-id>/`; they could not substitute for those durable records and were never public inventory entries. Retention validation checked both task receipt paths with actual gitignore rules and refused cleanup of accepted/history/code locations. This design repair created no acceptance receipt or evidence branch.

At claim, explicit read scope and approved permissions bounded every read. Every frozen authoritative input and claim-time control file had to fall inside the closed read allowlist; freezing a hash alone never expanded permission. Deterministic validation could read all files explicitly declared by the sanitized public inventory after confinement/symlink checks, including all 60 source task records and the sole native graph. It supplied only assigned-leaf semantics and bounded diagnostics to the model. A read allowlist did not grant write permission, and output scope did not authorize changing frozen authority or publishing raw private logs. Known control/self-referential artifact hashes were frozen in the external claim packet instead of embedded recursively.
