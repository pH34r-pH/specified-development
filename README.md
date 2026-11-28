# Specified Development

![Specified Development — Make intent explicit. Build from reviewed specifications.](spec/assets/hero.png)

Specified Development is a programming paradigm built on GitHub Spec Kit. A repository's `spec/` tree is a living, present-tense description of its software. It expands through **spec → plan → independent tests → tasks** into artifacts detailed enough for an AI model to reproduce a compatible program from them alone. Changes are spec-first: describe the change in the spec as if it already exists, then propagate the resulting gap through plan, tests and tasks. Existing projects join through brownfield onboarding.

**Status:** active. The paradigm, the canonical specification and the validator tooling are available now. The packaged Spec Kit preset, extension and bundle are specified but not implemented, released or qualified. See [delivery status](REVIEW.md#delivery-status). Present-tense specification prose describes specified behavior; delivery is established only by evidence.

**Next milestone:** a minimal adoption kit ([#41](https://github.com/pH34r-pH/specified-development/issues/41)) and a brownfield onboarding procedure ([#39](https://github.com/pH34r-pH/specified-development/issues/39)), so existing projects can adopt the paradigm before the packaged distribution exists. The campaign is tracked in [#38](https://github.com/pH34r-pH/specified-development/issues/38).

To adopt the paradigm in another repository today, use the [adoption kit](kit/README.md).

Start at [the specification](spec/index.md) and the [lifecycle guide](spec/usage/lifecycle.md), which defines the living spec and spec-first change. Read the [authority contract](spec/contracts/authority.md), the [directory feature](spec/features/directory-specs/index.md) and the [upstream decision](spec/operations/upstream.md). Candidate plans, independent test contracts and structured leaf tasks live under `build/<feature>/`; accepted revisions and evidence there are durable records.

The repository uses Apache-2.0 for its original tooling and documentation. Upstream Spec Kit keeps its own license; releases need dependency and license notices. See [LICENSING.md](LICENSING.md).

The completed foundation work is recorded in the [foundation implementation handoff](build/foundation/handoff.md).
