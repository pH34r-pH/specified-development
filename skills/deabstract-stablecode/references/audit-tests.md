# Preserve independent proof

Adapted from David Zhang's audit-tests; see [NOTICE](../NOTICE.md). This procedure
includes the essential writing and falsification steps locally; no separate
write-tests or review skill is needed. Follow the [entry contract](../SKILL.md).

Bound the production responsibility and read candidate tests in full, including
fixtures, parameter rows, discovery rules and the real execution path. Record the
baseline revision, existing failures and checks that could not run. A currently
failing valid test may expose a defect; it is not disposable noise.

For each candidate, identify the contract and credible defect it detects. Decide
keep, repair, combine or remove, with evidence. A combine decision names the
surviving suite and all unique cases it must absorb before deleting the old test.
A remove decision identifies stronger surviving proof or shows there is no product
or operational contract to protect. Suspicion of redundancy is not evidence.

Anchor expectations to the specification, documented external contracts and
independent fixtures, not the candidate's output. Sharing production observations
is fine; computing expected output through the same helper under test is circular.
Mocks must not perform the operation the product itself is supposed to provide.
Prefer tests at meaningful consumer boundaries without test-only production hooks.
Static checks can still be the cheapest valid proof for package, wire-format,
security or architectural contracts; resemblance to code is not itself disqualifying.

When test-authority changes are authorized, transfer unique cases first. Give each
new or repaired test an independent expectation and a known failing control. A
negative case must reach the intended condition and fail for that reason, not
merely raise some earlier error. Use the existing framework and mutation tooling
where available. Isolate temporary defects in a disposable scope, restore original
bytes, and confirm the intended proof passes again. Do not mutate shared files
while another test or reviewer reads them.

Test-authority work is distinct from an implementation task's permissions. Never
weaken an accepted oracle to make the candidate pass. A port may need a new harness
adapter; review that adapter independently while retaining semantic cases and
expected results. Missing or defective expectations use the existing repair path.

Run surviving owner and affected sibling suites, then required repository checks.
Have an independent reviewer compare removed coverage with surviving claims when
available; otherwise report the missing independent review. Record actual outcomes,
not just commands. Formatting, source greps and green compilation do not prove
runtime behavior. Fewer tests is not success; preserved or improved independent
proof with lower maintenance can be.
