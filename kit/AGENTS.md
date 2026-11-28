# Specified Development

This repository follows the Specified Development paradigm. Apply these rules to every change.

## Authority

- `spec/` is the living, present-tense description of what the software does. It is the acceptance criteria and the authority over behavior.
- `build/<feature>/plan.md` owns language, runtime, dependencies, architecture and the direct implementation path. It references requirements by ID and never weakens them.
- `build/<feature>/tests.md` lists independent cases authored from the spec. Expected results never come from running or reading the implementation.
- Code is evidence of behavior, not authority. Never change behavior in code without a spec change first.

## Making a change

1. Edit the spec first. Describe the new or changed behavior in present tense, as if it already exists. Add or update requirement IDs in the feature's requirement tables.
2. Have the spec change reviewed and accepted before implementing it.
3. Treat the change as a gap. Update only the plan sections, test cases and tasks that trace the changed requirements; leave unaffected ones untouched.
4. Write or update independent test cases from the spec, then implement until they pass.
5. Run `specified-check-layout` and, when evidence is available, `specified-gaps`.

If implementation reveals a technical limitation, repair the plan. If it reveals a missing or wrong product decision, stop and repair the spec first. Neither lowers the acceptance bar. A pure language or runtime change revises the plan, never the spec.

## Writing the spec

- Present tense only: "The service rejects…", never "will reject" or "rejected".
- Behavior only: inputs, outputs, failures, limits, security and interoperability. Internal design belongs in the plan.
- Present tense never claims delivery. Delivery is shown only by passing independent evidence.

## Unspecified code

Paths outside onboarded areas are explicitly unspecified. Do not treat them as conforming or non-conforming, and do not cite them as specification sources. To bring them under the spec, onboard them as described in the onboarding checklist.
