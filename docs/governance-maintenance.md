# Shared governance ownership and maintenance

Specified Development uses the repository family's shared governance profile
and validator. The namespace in
[`governance/repository-profile.json`](../governance/repository-profile.json)
identifies that shared schema; it is not the name of this repository and is not
evidence that the local profile was accidentally copied.

## Classification decision

Retain `prototype-device-protocol`. The shared
[profile vocabulary](https://github.com/pH34r-pH/long-haul/blob/28b9afbd17faa2baea9f2fb302abe7db71ee9882/docs/repository-governance-profile.md)
explicitly includes bounded protocols and simulations in this category.
Specified Development defines a method and task-bundle protocol with portable
validators; the complete distribution remains pre-alpha. Hardware is one member
of this category, not a requirement for using it. The local authority fields
identify the reviewed method specification, validator, generated bundle rules
and target-repository acceptance boundary more precisely than the category name.

This provides a justified fit within the existing taxonomy. A new enum value
would add shared migration and compatibility work without changing the local
authority model. Reconsider the category when the repository's actual role
changes or the shared vocabulary gains a more precise applicable category.

## Dependency and enforcement boundary

The [repository-governance workflow](../.github/workflows/repository-governance.yml)
calls Long-Haul's reusable action at
`28b9afbd17faa2baea9f2fb302abe7db71ee9882`. The pinned
[action](https://github.com/pH34r-pH/long-haul/blob/28b9afbd17faa2baea9f2fb302abe7db71ee9882/.github/actions/repository-governance/action.yml)
invokes its dependency-free
[validator](https://github.com/pH34r-pH/long-haul/blob/28b9afbd17faa2baea9f2fb302abe7db71ee9882/.github/actions/repository-governance/validate.py).
It checks required fields, allowed vocabulary, repository identity and declared
authority/data/evidence boundaries. Its exact `profile_id` and resource-policy
namespace are shared compatibility identities.

Passing this check establishes a complete governance declaration. It does not
prove that every declared safeguard is implemented, qualify a task result,
authorize model execution or publication, or grant control of the target
repository. The portable bundle tools do not import Long-Haul Python code and
do not need this action at runtime. The current delivery claims remain in
[REVIEW.md](../REVIEW.md#delivery-status).

## Updating the pinned action

1. Inspect the proposed immutable Long-Haul commit, the composite action and
   validator diff, and the shared profile documentation. Check the action's
   transitive workflow/tool dependencies as well as its entry point.
2. Run that exact validator against this repository's current profile, with
   `GITHUB_REPOSITORY=pH34r-pH/specified-development`. Review changed vocabulary,
   required fields, diagnostics and compatibility. A locally renamed
   `profile_id` is not a substitute for a shared schema migration.
3. When a new category or schema is needed, land its shared definition,
   compatibility behavior and tests in Long-Haul first. Then update this
   consumer's profile and action SHA together; retain predecessor identities.
4. In an ordinary reviewed PR, update the workflow pin, this documented source
   identity and affected public-inventory hashes. Run local foundation checks,
   the actual pinned governance validator and the existing CI gates. Keep
   read-only workflow permissions and the target's acceptance authority.
5. Record the tested commit, result and any semantic changes in the PR. Dependency
   update automation can propose a new SHA; it does not replace review or
   demonstrate compatibility by itself.

No local fork of the shared validator or parallel profile registry is needed.
This decision resolves the naming question raised in
[issue #30](https://github.com/pH34r-pH/specified-development/issues/30) while
preserving the existing repository-family contract.

The pinned validator was run against the unchanged local profile on 26 November
2026 with the repository identity above. It returned exit 0 and reported
`prototype-device-protocol` as valid, with the existing review-required resource
actions intact. This validates the declaration and classification compatibility;
it does not extend the enforcement claim described above.
