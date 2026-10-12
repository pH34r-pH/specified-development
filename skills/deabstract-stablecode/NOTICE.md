# Attribution and adaptation record

This package combines original Specified Development guidance with selected
adaptations of David Zhang's `dzhng/skills`. It is not a complete mirror or an
unmodified distribution of his skills, and no endorsement is implied.

Original Specified Development material is provided under [Apache-2.0](LICENSE).
Adapted upstream material retains Copyright (c) 2026 David Zhang and the complete
[MIT license](LICENSE.dzhng-skills). Retain this notice and both licenses when
redistributing the folder.

## Consulted upstream revision

Repository: [dzhng/skills](https://github.com/dzhng/skills).
Pinned commit: `d51322866ffa298838346960414d18a221b52588`.
Reviewed for this package on 2026-10-12. Sources below refer only to the SKILL.md
files actually inspected; linked upstream subsidiary references are not claimed
as read, copied or bundled.

| Inspected source at the pin | Local treatment |
| --- | --- |
| [explore-unknowns](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/explore-unknowns/SKILL.md) | [Explore unknowns](references/explore-unknowns.md): evidence, tacit expectations, blind spots and concrete examples; proportionate investigation rather than mandatory stage-by-stage interviews. |
| [refactor-clean](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/refactor-clean/SKILL.md) | [Refactor](references/refactor-clean.md): real ownership and consumers, direct platform/library use, complete scoped removal and justified compatibility. |
| [audit-tests](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/audit-tests/SKILL.md) | [Test audit](references/audit-tests.md): independent proof, coverage transfer, failing controls and explicit incomplete evidence. |
| [auto-research](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/auto-research/SKILL.md) | [Qualification](references/qualify-change.md): cheap informative loops, fixed evaluators, controlled hypotheses, all-attempt accounting and separate confirmation. |
| [audit-choices](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/audit-choices/SKILL.md) | [Decision review](references/review-decisions.md): consequential choices and readable evidence; no mandatory parallel ledger and no authority bypass to keep running. |
| [close-spec](https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/close-spec/SKILL.md) | Decision review preserves rationale and visual provenance but rejects the upstream spec-to-rationale/archive lifecycle. |

## Deliberate differences

The specification is the finished-product acceptance contract, not a technical
build plan. Languages, runtimes, dependencies and architecture belong in the plan.
Both remain retained after shipping. No automatic archival or deletion of accepted
specifications, plans, tests, tasks, source or evidence is imported.

Production computations can supply observations, but expected results remain
independent. The upstream warning about duplicating calculations does not permit
circular oracles. Required trust, persistence, recovery and compatibility duties
cannot be removed merely because an internal producer appears well-behaved.

The skill does not impose a line-count target, exhaustive interview, mandatory
three-way implementation, unrestricted rename, twelve-hour run or automatic
installation/merge. A material authority gap stops the affected attempt even when
a reversible provisional choice is imaginable. Local plan-authorized discretion
is retained. The source selection does not import upstream runners, cloud services,
provider accounts, installation hooks or network dependencies.

## Updating the adaptation

Read the relevant upstream files and license at a newly selected full commit;
compare their changes with these recorded differences. Revise the local procedures,
this pin and attribution together in an ordinary reviewable change. Re-run package
checks and affected behavioral cases; preserve negative outcomes and unrun cases.
Never update automatically from `main`, silently change accepted product behavior,
or claim coverage of the entire upstream repository.
