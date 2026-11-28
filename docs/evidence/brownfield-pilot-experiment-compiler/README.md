# Brownfield pilot: experiment-compiler, archive read policy

Gate **GB** evidence ([rollout gates](../../../spec/operations/rollout.md), issue [#51](https://github.com/pH34r-pH/specified-development/issues/51)). Recorded 2026-11-28.

| Item | Value |
| --- | --- |
| Pilot repository | [pH34r-pH/experiment-compiler](https://github.com/pH34r-pH/experiment-compiler) (public) |
| Baseline commit | `d5c579436d81207a72ec0236af2bfa5a9484eb8e` |
| Onboarded area | `archive-read-policy`: `experiment_compiler/archive_policy.py`, `experiment_compiler/archive_policy_cli.py` |
| Unspecified remainder | Everything else in the repository (declared in [`spec/index.md`](artifacts/spec/index.md)) |
| Isolation | Local clone at the baseline with its remote removed; no push, branch or file write to the original repository |
| Tools | `specified-development-tools[authoring]` installed from pinned commit `f4121458bd8a5218acbba5e8c74425d97711b60f` into a separate environment, as the [adoption kit](../../../kit/README.md) describes |
| Acceptance | Spec accepted by the repository owner (`pH34r-pH`) at 2026-11-28T00:50:32Z |

The [artifacts](artifacts/) folder holds the accepted spec, plan, independent test contract, executable independent cases, onboarding record, evidence, results and every gap report. No experiment-compiler source is copied here except the pilot's own [ARP-FR-010 change](artifacts/archive_policy-ARP-FR-010.diff).

## GB acceptance

| Criterion | Result | Evidence |
| --- | --- | --- |
| Accepted onboarding record, independent tests and initial gap list for one real area | Met | 10 requirements; 8 independent cases authored from the spec, all passing at the baseline; no known defects; initial gaps: none. `specified-check-layout`, `specified-onboarding --results` and `specified-gaps` pass. [onboarding.json](artifacts/onboarding.json), [status-baseline.json](artifacts/status-baseline.json) |
| One spec-first change propagated end to end through the gap report | Met | See below. [status-spec-change.json](artifacts/status-spec-change.json), [status-after-change.json](artifacts/status-after-change.json) |
| One scoped regeneration trial with all attempts retained and a verdict | Met (two trials) | See below. [trials](trials/) |
| No write to the original repository; no private code or credentials | Met | Original checkout untouched; the pilot clone has no remote. |
| TST-034 result recorded | Met for the core track | Core adoption readiness exists without release archives; packaged distribution readiness stays blocked (no G1–G4 evidence). |

## Spec-first change

The owner approved a new behavior, **ARP-FR-010**: a refusal reports the observed value that exceeded the budget. The revision also wrote into FR-005, FR-007 and FR-009 three behaviors that regeneration trial 1 showed code outside the area relies on (below).

1. Spec revision 2 was written first, in present tense.
2. `specified-gaps --previous status-baseline.json` reported:
   - **changed:** exactly FR-005, FR-007, FR-009 (stale) and FR-010 (untested)
   - **stale:** exactly cases ARP-004, ARP-006 and ARP-008, plus the one plan section citing those IDs
   - every other requirement stayed satisfied
3. The stale cases were refreshed and ARP-009 was added. Test-author **RED**: only ARP-009 failed, with `AttributeError: 'ResourcePolicyError' object has no attribute 'observed'`, which is the missing behavior itself, not a harness fault.
4. FR-010 was implemented (7 lines in `archive_policy.py`). **GREEN**: 9/9 cases, and the full existing suite passed (288 tests, 113 skipped on Windows).
5. The gap report at commit `79522ea9` showed all 11 requirements satisfied, with no gaps.

## Regeneration trials

Each trial gave a fresh agent a clean workspace holding only the spec, the plan, the test contract and the executable cases. The input digests are retained. The agent was told to read nothing outside the workspace; that denial was instructed, not sandbox-enforced. Outputs are retained under [trials/](trials/).

| Trial | Inputs | Oracle | Full experiment-compiler suite with the regenerated modules | Verdict |
| --- | --- | --- | --- | --- |
| 1 | spec and plan revision 1 | 8/8 on the first iteration, inputs unchanged | **5 failures**: a missing `ArchiveMemberReader.total_bytes`, a missing `ARCHIVE_POLICY_OPTIONS` (imported by `lifecycle_components`), and total-bytes refusals not naming the member | The spec passed its own oracle but was **incomplete for compatibility**: code outside the area relied on unspecified interface and behavior |
| 2 | spec and plan revision 2 (public interface, check order and message format added) | 9/9 on the first iteration, inputs unchanged | **289 tests pass** (113 skipped on Windows) | **Compatible regeneration** of the onboarded area from artifacts alone |

Ambiguities the trial 2 agent still reported, none of which affect the oracle or compatibility, recorded as follow-up spec repairs for experiment-compiler:
- the `observed` value for ratio refusals (rounded-up ratio or expanded bytes)
- members whose compressed size is 0
- whether a refused read still adds to `total_bytes`
- the check order within one read chunk
- integer forms the CLI accepts (`+3`, `1_000`)

## Findings for specified-development

1. **`build/` collides with Python build output.** experiment-compiler's `.gitignore` ignores `build/`, so `build/<feature>/` records were silently ignored, and setuptools writes to and cleans the same directory. The pilot changed the rule to `/build/*` plus `!/build/archive-read-policy/`. Repaired in the kit (layout check refuses ignored records; README documents the rule).
2. **Characterization must capture the area's public interface.** Trial 1 failed compatibility because the spec omitted names that unspecified code imports. Repaired in the onboarding guide, the checklist and the plan template (a required "Public interface" section listing everything code outside the area uses).
3. **Building gap evidence needed glue.** Recording results required a first `specified-gaps` run to obtain requirement hashes. Tracked as a follow-up.
4. **Windows path length.** A full clone of experiment-compiler under a long temporary path fails checkout (deep `examples/` evidence paths). Use a short checkout path or `core.longpaths`.
