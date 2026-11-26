# Current specification review

The current review validates the ten registered canonical documents, their 80
feature requirement/success-criterion/scenario identities, and the existing
independent test contracts. Passing this check establishes coverage of the test
contract. It does not establish test execution, product implementation, task
acceptance, runtime admission or deployment.

## Commands

Install the repository's `authoring` extra, then run:

```sh
python -m tools.spec_validation --root .
python -m tools.task_review --root . --check
```

`specified-validate-spec` and `specified-task-review` expose the same operations
after package installation. `python -m tools.task_review` deterministically
regenerates [the task review](task-review.md) from the existing structured records.
It never executes the declared commands. Its check rejects altered or missing
review content and source/native command-definition drift.

## Source and review boundaries

The existing `spec/manifest.json` remains the document inventory. Historical
sources and the sixty-task native contract retain their exact bytes. The small
[current review overlay](specification-review.json) pins that manifest, identifies
explicit current successors, and maps source sections to already defined
requirements. It does not copy their prose, define another requirement registry,
assign execution edges or change historical acceptance.

Only the execution capability document has a current successor:
[execution-capabilities-v2.md](specification/execution-capabilities-v2.md).
Its frontmatter records its predecessor path, exact digest and revision. The
successor retains the stable rules while dated interface and receipt facts live
in [execution-capability-observations/foundation-v1](evidence/foundation-capability-observations-v1.md).
The predecessor still applies to the frozen historical native contract. New
authoring review selects the successor explicitly; it does not silently rewrite
that old contract's inputs or admit any task for execution.

## Obligations and traceability

Finished-product past-tense prose remains the accepted writing convention.
Normative obligations appear in the existing feature requirement and success
criterion tables and in the explicitly mapped shared sections. Their reference
form is `document-id#requirement-id`, preserving the existing FR, DS-FR, SC and
scenario identifiers across paths and features. Shared contract sections refine
those requirements rather than creating duplicate requirement text.

Each section has one reviewed classification: normative, informative, example
or recommendation. Normative sections reference existing independently covered
feature requirements. Other classifications carry no obligation references.
The exact section digest makes a changed, added, removed or reclassified source
section a review decision instead of an unnoticed prose change. The checker does
not infer natural-language intent or certify that a human classification is
correct. A reviewer must assess changed text and approve its classification and
mapping before refreshing the overlay digest. Do not regenerate all trace
digests merely to make a failing check pass.

The validator reads the existing Markdown tables with markdown-it-py's CommonMark
parser and table extension. Distribution requirements, scenarios and success
criteria are checked against both independently authored cases and their explicit
coverage matrices. Directory requirements and success criteria are checked
against the case table, with scenarios checked against its scenario matrix.
Duplicate or malformed IDs, unknown references, missing coverage and inconsistent
matrices fail with typed diagnostics. The currently reviewed independent-test
corpus has no approved coverage exclusions. Distribution FR-007 permits
spec-approved exclusions; this version 1 review profile rejects new exemption
fields until their approved source/profile extension and independent oracle are
defined. This compatibility limit does not remove FR-007's product capability or
permit an ad hoc suppression.

## Metadata compatibility

The versioned [frontmatter schema](../schemas/spec-frontmatter-v1.schema.json)
keeps target intent, approval, artifact acceptance and observed delivery separate.
State values are enumerated; descriptive qualifiers are separate. Feature
documents require their stable feature ID. Implemented, qualified and deployed
claims need the corresponding source, test and deployment evidence references.
Reference presence is not independent verification of the linked claim.

The [legacy schema](../schemas/spec-frontmatter-legacy.schema.json) recognizes
only the existing metadata shapes. Validation normalizes them in memory without
rewriting frozen files:

| Legacy approval | Current review interpretation |
| --- | --- |
| architecture-approved | Architecture approved; artifact acceptance remains unspecified unless explicit. |
| architecture-approved-directory-enhancement-specified | Architecture approved; retain the enhancement qualifier separately. |
| user-requested-enhancement-design-candidate | Proposed; retain the user-requested enhancement qualifier. |
| enhancement-design-candidate | Proposed; retain the enhancement qualifier. |
| distribution-choice-approved | Decision approved; retain the distribution-choice qualifier. |
| proposed-contract-repair-parent-review-required | Review required; retain the contract-repair qualifier. |
| architecture_approval: delegated-user-directive | Architecture approved; retain the directive qualifier and the separate artifact_acceptance field. |
| No approval field | Unspecified; do not infer approval or acceptance. |

Missing legacy revision values are compatibility revision 1, not a claim of a
new acceptance event. Unknown fields/states, duplicate YAML keys, wrong types,
conflicting acceptance/approval values, role/identity disagreement, and delivery
states without their evidence fail. The live delivery table remains
[REVIEW.md](../REVIEW.md); document metadata does not promote a planned feature
merely because some validator tooling exists.

An accepted artifact additionally identifies its acceptance actor, timestamp and
evidence reference. Architecture approval alone cannot supply that acceptance.

## Implementation choices

The optional authoring dependency set uses [PyYAML SafeLoader](https://pyyaml.org/wiki/PyYAMLDocumentation)
with explicit duplicate-key rejection, [JSON Schema Draft 2020-12 validation](https://python-jsonschema.readthedocs.io/en/stable/validate/),
and [markdown-it-py's existing table parser](https://markdown-it-py.readthedocs.io/en/latest/plugins.html).
The portable bundle validator retains its independent standard-library-only
contract. The task view reuses the existing authoring parser, native projection
checks and review writer. It adds neither a new task format nor another DAG.
