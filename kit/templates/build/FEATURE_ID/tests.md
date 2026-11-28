---
artifact: independent-test-contract
revision: 1
acceptance: candidate-review
---

# FEATURE_TITLE independent test contract

Each case is authored from the accepted specification before implementation. Expected results never come from running or reading the implementation. Every functional requirement and success criterion traces to at least one case; an untraced requirement is an untested gap.

| Case | Requirements | Stimulus | Expected observable result |
| --- | --- | --- | --- |
| CASE-001 | FR-001, SC-001 | Provide valid input. | The specified result is produced. |
| CASE-002 | FR-002, SC-001 | Provide invalid input. | The specified failure is reported and no state changes. |
