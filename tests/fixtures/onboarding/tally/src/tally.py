"""A running tally. Existing brownfield code before onboarding."""


class Tally:
    def __init__(self) -> None:
        self.total = 0

    def add(self, amount: int) -> int:
        # Known defect surfaced during characterization: negative amounts are accepted.
        self.total += amount
        return self.total
