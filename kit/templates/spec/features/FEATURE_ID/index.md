---
schema_version: 1
document_id: PROJECT_ID/FEATURE_ID
role: feature
feature_id: FEATURE_ID
revision: 1
target_status: mature-complete-product
approval_status: proposed
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
qualifiers: [living-spec-paradigm]
---

# FEATURE_TITLE

## Product description

Describe what this feature does for its users, in present tense, as if every accepted requirement is already true. Name the inputs it accepts, the outputs it produces, how it fails and any limits users rely on. Leave implementation choices to the plan.

## Actors and acceptance scenarios

| Story | Actor and outcome | Independent acceptance scenarios |
| --- | --- | --- |
| US1 | A user accomplishes the feature's main outcome | AS1: given valid input, the feature produces the specified observable result. AS2: given invalid input, the feature rejects it with the specified failure and changes no state. |

## Functional requirements

| ID | Required observable behavior |
| --- | --- |
| FR-001 | The feature produces the specified result for valid input. |
| FR-002 | The feature rejects invalid input with the specified failure and leaves state unchanged. |

## Success criteria

| ID | Observable measure |
| --- | --- |
| SC-001 | Every independent case in the feature's test contract passes. |

## Boundaries

List what this feature explicitly does not do, and the neighboring areas that remain unspecified.
