# Using the skill

This folder is a complete portable Agent Skills package. Its entry point is
[SKILL.md](SKILL.md); local references contain all required procedures. Upstream
links in [NOTICE.md](NOTICE.md) are provenance, not prerequisites at invocation.
Original work uses [Apache-2.0](LICENSE); adapted David Zhang material retains the
[MIT notice](LICENSE.dzhng-skills). Keep both licenses and the notice when copying.

## Start in a repository

Ask a skill-capable agent to use `deabstract-stablecode` for a named scope and stage,
then provide that repository's accepted artifacts and ordinary permissions. A
host that does not discover skills can read SKILL.md directly and follow its local
references. Use the host's supported skill installation mechanism to copy this
whole directory; this package does not install itself or run shell commands.

Examples:

- "Use deabstract-stablecode to audit the exporter; report only, do not edit."
- "During plan authoring, compare our current runtime with a bounded Rust/Wasm
  target. Preserve the accepted product specification and explain qualification."
- "Refine the authorized task using deabstract-stablecode, preserving independent
  tests and all failure behavior. Stop for any material authority gap."

These prompts select a procedure; they do not supply missing approval or rewrite
an accepted task's scope. The same accepted product can have different technical
plans, languages and harness adapters.

## Existing workflow, not an alternate one

Exploration informs the specification and the plan. The specification remains the
finished-product acceptance contract; the plan selects implementation details.
Independent tests precede tasks. De-abstraction is a planning/refinement technique
within that lifecycle, not a late justification to change expected behavior.

Keep compact decisions and evidence in the consuming repository's existing plan,
tests, task reports and retained receipts. Do not create extra mandatory ledgers,
a new universal target schema, an executor or a provider account. No particular
implementation language, model provider or session duration is required here.

## What has and has not been qualified

Repository tooling checks this folder's required files, simple frontmatter, local
links, license bytes, and refusal of missing or unsafe resources. Its validator
supports this package's deliberately small frontmatter subset, not arbitrary YAML
or every Markdown extension. These are packaging checks, not proof that an agent
follows the instructions.

Fresh-agent cases are maintained separately in the source repository, outside
this installable directory. Use an independent reviewer and record the actual
fixture, skill revision, model selection and observed actions. Keep evaluation
answers out of worker context. Qualify host discovery/installation separately from
an agent's behavior, and both separately from the consuming product's acceptance.
