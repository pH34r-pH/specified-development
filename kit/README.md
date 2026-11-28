# Specified Development adoption kit

This kit lets an existing or new repository adopt the Specified Development paradigm now, before the packaged Spec Kit preset, extension and bundle exist. It contains:

| Path | Purpose |
| --- | --- |
| [`templates/spec/`](templates/spec/index.md) | Canonical spec tree: overview, manifest, navigation and one feature page with requirement tables. |
| [`templates/build/FEATURE_ID/`](templates/build/FEATURE_ID/plan.md) | Plan (with the implementation-targets section) and independent test contract for one feature. |
| [`templates/onboarding.json`](templates/onboarding.json) | Brownfield onboarding record for one area. |
| [`templates/evidence.json`](templates/evidence.json) | Requirement evidence input for the gap report. |
| [`AGENTS.md`](AGENTS.md) | Instructions fragment for coding agents (Claude Code, Codex and others). |
| [`ci/specified-development.yml`](ci/specified-development.yml) | Read-only GitHub Actions workflow that runs the checks. |
| [`ONBOARDING.md`](ONBOARDING.md) | Step-by-step brownfield onboarding checklist. |

## What the paradigm asks of a repository

- `spec/` is a living, present-tense description of the software. It owns observable behavior and is the acceptance criteria.
- `build/<feature>/plan.md` owns technology choices and the direct implementation path; `tests.md` holds independent cases authored from the spec.
- Every change starts as a spec edit written as if already true. The difference from demonstrated behavior is a gap, and only that gap propagates through plan, tests and tasks.

Read the [lifecycle guide](../spec/usage/lifecycle.md) and the [onboarding guide](../spec/usage/onboarding.md) for the full rules.

## Install from a pinned revision

There is no release yet. Pin an exact reviewed commit of this repository; never a branch:

```sh
REV=<reviewed 40-character commit>
python -m pip install "specified-development-tools[authoring] @ git+https://github.com/pH34r-pH/specified-development@$REV"
```

Copy the kit files from the same revision:

```sh
git clone https://github.com/pH34r-pH/specified-development /tmp/specified-development
git -C /tmp/specified-development checkout "$REV"
cp -R /tmp/specified-development/kit/templates/spec ./spec
mkdir -p build && cp -R /tmp/specified-development/kit/templates/build/FEATURE_ID "build/<feature>"
mv spec/features/FEATURE_ID "spec/features/<feature>"
```

Then replace the placeholders `PROJECT_ID`, `PROJECT_TITLE`, `FEATURE_ID` and `FEATURE_TITLE` in the copied files and run:

```sh
specified-check-layout --root .
```

Add `AGENTS.md` (or include it from `CLAUDE.md`) and copy `ci/specified-development.yml` into `.github/workflows/`, replacing its `REVIEWED_COMMIT` placeholder with the same pinned commit.

## Commands

| Command | Purpose |
| --- | --- |
| `specified-check-layout` | Validate the spec tree, frontmatter, requirement tables, plan targets section and test contract references. Untested requirements are reported, not rejected. |
| `specified-onboarding` | Validate a brownfield onboarding record against the accepted spec. |
| `specified-gaps` | Report requirement status, gaps and stale descendants from independent evidence. |

## Not included yet

The kit does not replace Spec Kit commands, ship release archives, perform staged install or recovery, record model admission receipts, account for cost, or export a site or wiki. Those belong to the packaged distribution and its own rollout gates. Adoption is always a separate, reviewed change in the adopting repository.
