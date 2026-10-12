# Review decisions and close out without losing authority

Adapted selectively from David Zhang's audit-choices and close-spec. The
[NOTICE](../NOTICE.md) identifies rules deliberately not adopted. Follow the
[entry contract](../SKILL.md); an audit alone does not authorize fixes.

Inspect the actual diff, relevant dependencies, accepted artifacts and evidence,
not only the implementer's self-report. Surface consequential choices affecting
interfaces, ownership, storage, data shape, dependencies, concurrency, performance,
permissions or interpretation of scope. Distinguish choices required by the plan,
choices explicitly delegated by it and unapproved material commitments.

Explain each material choice using a concrete scenario, alternative, consequence,
evidence and uncertainty. Record sound, requires repair or requires owner decision
in the existing plan review or task report; do not require a second decisions file.
A working example is not proof that an architectural choice generalizes. Verify
reported problems against source before changing anything or dismissing a finding.

A required product decision, plan contradiction or test-authority gap stops the
affected attempt. A reversible guess is not permission to continue across that
boundary. Ordinary delegated local discretion remains ordinary discretion; avoid
an approval ritual for every implementation detail. An independent reviewer should
receive the exact scope and evidence, not a suggested verdict. A missing verdict,
failed review process or unrun check must remain visibly incomplete.

Before closeout, rerun the unchanged independent oracle and relevant regressions
after bounded refinement, plus required integration checks on the actual resulting
revision. Reconcile reviewed decisions with what actually shipped and record any
remaining bridge, failure, unrun check and deployment limitation. Do not imply
merge, installation or product qualification from successful package validation.

Retain why an approach was selected or rejected and keep visual/reference fixtures
that defined acceptance. Keep the canonical finished-product specification, accepted
technical plan, independent tests, tasks, stablecode and evidence under repository
retention rules. Shipping does not turn the spec into rationale-only prose, transfer
product authority to code or authorize deleting accepted plans and test history.
A divergence returns to the correct authority instead of rewriting expectations to
match the implementation. Close the bounded task only through its existing owner.
