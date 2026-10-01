---
document_id: specified-development/authority
target_status: mature-complete-product
approval_status: architecture-approved
delivery_status: designed-only
delivery_evidence: []
---

# Authority and retention

Canonical `spec/` documents/contracts/fixtures plus dependency locks and accepted generation instructions defined intended behavior. Accepted plan, independent test and task revisions compiled that intent. Code was a retained regenerable output; existing source was evidence for compatibility/regression, not permission to invent behavior.

Target, approval, artifact acceptance, implementation, test, deployment and regeneration fields were separate. Candidate prose could describe completed product behavior without asserting delivered behavior. Accepted revisions recorded exact predecessor hashes, authority provenance, acceptance actor/time and immutable revision identity. A generated `spec.md`, site or wiki carried a derived label and could never supersede source.

`build/<feature>/plan.md`, `tests.md`, `tasks.md`, and `execution-contract.yaml` were tracked candidate/current authoring records. Acceptance archived exact source closure, locks, plan/tests/tasks/native contract and nonsecret evidence beneath `build/<feature>/accepted/<revision>/`. Accepted directories were append-only. An input revision could stale them for future execution but could not alter their historical verdicts. Git retention or an explicitly approved durable store preserved them; location under build did not imply disposability.

Only `build/site/`, `build/wiki-stage/`, feature `.tmp/`, `candidate/`, `runtime/`, generated `spec.md`, `source-map.json`, `inputs.lock.json`, and copied `contracts/` were cleanable. Cleanup used an explicit managed inventory, real-path confinement and before-hash checks; it refused symlinks, unknown paths and accepted/code locations. Source code deletion was never an authorized cleanup operation.

Task metadata contained semantic parents as authoring input. Deterministic projection placed the sole executable edge set in native `execution-contract.yaml` `tasks.<id>.parents`; projected namespaced records omitted parents. Document dependencies selected input closure only. Existing Kanban aggregate semantics and the selected executor's claims/retries remained unchanged.

Any missing assumption created a separate earliest-authority repair leaf. The current attempt stopped with evidence; the repair froze its own model and inputs. Accepted changes invalidated changed task contracts and their native descendants, preserving unaffected receipts. Scripts did not infer missing semantics or switch models.
