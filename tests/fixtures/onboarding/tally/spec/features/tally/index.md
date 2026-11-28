---
schema_version: 1
document_id: tally/feature
role: feature
feature_id: tally
revision: 1
target_status: mature-complete-product
approval_status: architecture-approved
artifact_acceptance: candidate-review
delivery_status: designed-only
delivery_evidence: []
qualifiers: [brownfield-onboarded]
---

# Running tally

## Product description

The tally keeps a running integer total. A new tally starts at zero, and each added amount increases the total. Negative amounts are rejected.

## Actors and acceptance scenarios

| Story | Actor and outcome | Independent acceptance scenarios |
| --- | --- | --- |
| TAL-US1 | A user keeps a running total | AS1: adding non-negative amounts to a new tally returns and keeps their sum. AS2: adding a negative amount raises ValueError and leaves the total unchanged. |

## Functional requirements

| ID | Required observable behavior |
| --- | --- |
| TAL-FR-001 | Adding a non-negative integer amount increases the total by that amount and returns the new total. |
| TAL-FR-002 | Adding a negative amount raises ValueError and leaves the total unchanged. |
| TAL-FR-003 | A new tally has a total of zero. |

## Success criteria

| ID | Observable measure |
| --- | --- |
| TAL-SC-001 | Every independent tally case passes. |
