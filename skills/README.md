# Specified Development skills

This directory is the repository-owned source for portable authoring and refinement
skills. Start with [De-abstract Stablecode](deabstract-stablecode/SKILL.md) and its
[usage guide](deabstract-stablecode/README.md). Copy the complete skill directory,
not just its entry file. All required procedures and notices travel with it; no
David Zhang skill installation, network fetch, model service or custom runner is
required to read and use the guidance.

## Relationship to the lifecycle

The [canonical lifecycle](../spec/usage/lifecycle.md) and
[authority contract](../spec/contracts/authority.md) remain authoritative.
The specification describes the finished working product and supplies acceptance
criteria. The plan owns language-specific details and technical implementation
choices. Independent tests establish expected behavior before task decomposition;
stablecode implements the accepted plan without redefining the product.

The skill provides local procedures for exploration, plan-owned target selection,
scoped simplification, test audits, bounded experiments and decision review. It
extends the existing stages rather than adding a second lifecycle, scheduler,
acceptance registry or compulsory intermediate document. Read only the references
needed for the authorized stage. Research findings are not product authority until
accepted into the appropriate specification or plan.

The [distribution plan](../build/distribution/plan.md) still describes the broader
Spec Kit preset/extension/installer work. This source bundle is independently
usable; it does not claim those installers or generated command integrations have
shipped. Future integration should package this same directory and point command
instructions at the installed local procedure, not duplicate its text or fetch a
moving upstream branch. Installation paths remain the selected host's concern.

## Maintenance and qualification

Run `python tools/validate_skills.py` and
`python -m unittest discover -s tests -p test_skills.py -v` from the repository.
The existing foundation workflow also runs these checks. The public payload
inventory covers the source, notices, tests and validation tooling.

These checks establish package structure, local reference closure, license
preservation and rejection of malformed packages. They do not establish agent
behavior or product performance. Reviewer-only behavioral scenarios live in
`tests/fixtures/foundation/skill-behavioral-cases.md`; do not install them with the
worker-facing skill or give their expected decisions to the agent under test.
Run fresh-agent trials only through the existing authorized execution owner.

Upstream provenance, adaptation boundaries and update instructions are retained in
the skill's [NOTICE](deabstract-stablecode/NOTICE.md). This is a selected synthesis,
not a mirror of David's complete repository. No automatic upstream update occurs.
