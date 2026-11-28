---
artifact: implementation-plan
revision: 1
acceptance: candidate-review
---

# Tally implementation plan

## Implementation targets and direct path

The current implementation is a single Python 3.12 class in `src/tally.py`, characterized during onboarding. It stays in Python; no port is planned. State is one integer owned by each `Tally` instance.

## Public interface

- `tally.Tally()`: a new tally; attribute `total: int`.
- `Tally.add(amount: int) -> int`: returns the new total; raises `ValueError` for a negative amount.

## Accumulation

`Tally.add` updates and returns the running total for TAL-FR-001; a new instance starts at zero for TAL-FR-003.

## Input validation

`Tally.add` rejects negative amounts before mutating state, satisfying TAL-FR-002.

## Qualification

The independent cases in `tests/test_tally.py` are the oracle for TAL-SC-001.
