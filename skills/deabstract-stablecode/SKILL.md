---
name: deabstract-stablecode
description: Apply Specified Development to explore material unknowns, plan language or runtime targets, simplify retained implementation code, audit independent tests, and qualify a bounded change. Use for redundant wrappers, speculative runtime generality, framework replacement or target-language experiments. Keep product acceptance in the specification and technical choices in the plan; implement only an authorized task.
license: Apache-2.0 AND MIT
---

# De-abstract Stablecode

The specification defines the finished working product and serves as acceptance
criteria. The plan owns language-specific details and implementation strategy.
Stablecode is the retained implementation, not the authority for what the product
was meant to do. Product concepts need not become runtime frameworks.

This skill supplies guidance, not new authority, an executor, a deletion quota or
permission to modify accepted inputs. It is self-contained: all procedures below
are local. The [usage guide](README.md) explains packaging and the
[NOTICE](NOTICE.md) records David Zhang's contributions and deliberate differences.

## Bind the work

Read the consuming repository's instructions, accepted specification, plan,
independent tests, authorized task, relevant locks and real consumers. Establish
the starting revision, unrelated work, baseline failures and unrun checks. Identify
whether this is research, planning, audit, experiment, implementation or closeout.
An audit reports findings; it does not authorize edits. Use the existing artifact
locations and execution owner; do not add a parallel task or evidence registry.

## Use the procedure for the current stage

| Stage | Local procedure | Result in the existing workflow |
| --- | --- | --- |
| Research or unresolved design | [Explore unknowns](references/explore-unknowns.md) | Evidence and consequential decisions, routed to specification or plan. |
| Technical planning | [Plan targets](references/plan-targets.md) | Bounded language/runtime target, reuse decision, direct path and qualification rule. |
| Authorized implementation/refinement | [Remove unnecessary layers](references/refactor-clean.md) | Simpler stablecode with required duties preserved. |
| Independent tests or coverage audit | [Audit tests](references/audit-tests.md) | Contract-to-proof map and justified retention, transfer or removal. |
| Optimization or migration experiment | [Qualify a candidate](references/qualify-change.md) | Reproducible comparison and consumer-level verdict. |
| Review or closeout | [Audit decisions](references/review-decisions.md) | Explained decisions, checked evidence and unresolved gaps. |

Use only relevant procedures. A local rename does not need an exhaustive interview
or three competing implementations. Frontload choices that affect product promises,
interfaces, ownership, security or major technical commitments; keep useful local
discretion within the accepted plan and task.

## Authority and repair

A missing or changed product promise requires specification repair. A technical
choice that invalidates the accepted plan requires plan repair. A defective oracle
requires independent test-authority repair. Stop the affected attempt and use the
existing repair process; accept the new authority and refresh only affected
subsequent artifacts before resuming. Never silently change goals, frozen inputs,
model binding, permissions or expected results. A permitted local choice does not
need another process gate.

Product acceptance remains fixed while comparing implementations. The plan can
set candidate-selection preferences without lowering those requirements. A new
language may need a new harness adapter; independently review it against the same
semantic fixtures and expectations rather than demanding byte-identical tooling.

## Non-negotiable boundaries

Preserve security, privacy, numerical meaning, persistence, cancellation and real
compatibility. Removing a boundary is valid only when its required duty remains
enforced correctly elsewhere. Runtime policy or capability variation required by
the product stays runtime-variable. Useful types, cohesive modules and mature
libraries are not automatically abstraction debt.

Production observation may expose the owner's computed value, but the expected
result must remain independent of the candidate. No optimization by weakened tests,
hidden-answer access, reduced required quality or redefined success is permitted.

Keep canonical specifications authoritative after shipping. Retain accepted plans,
tests, tasks, stablecode and evidence under repository policy. Shipping is not
permission to replace acceptance with a rationale-only document or delete source.
No install, merge, release or deployment is implied by using this skill.

## Completion

Report the accepted plan decision, requirement references, removed and retained
duties, exact revisions, independent behavioral evidence, scoped gains/regressions,
bridges and removal conditions, unrun checks, and actual integration/deployment
status. Distinguish retain incumbent, accept candidate, reject candidate and
insufficient evidence. A justified no-change result is success. Format/link checks
are not fresh-agent behavioral qualification or a performance result.
