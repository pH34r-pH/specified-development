---
artifact: independent-test-contract
revision: 1
acceptance: candidate-review
---

# Tally independent test contract

Expected results come from the accepted tally specification, never from the implementation's output.

| Case | Requirements | Stimulus | Expected observable result |
| --- | --- | --- | --- |
| TAL-001 | TAL-FR-001, TAL-FR-003, TAL-SC-001 | Create a tally, add 2 then 3. | Total starts at 0; add returns 2 then 5; total is 5. |
| TAL-002 | TAL-FR-002, TAL-SC-001 | Add 4, then add -1. | The second add raises ValueError; total stays 4. |
