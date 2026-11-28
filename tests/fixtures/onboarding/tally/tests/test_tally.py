"""Independent cases authored from the accepted tally specification, not from the code."""
import unittest

from tally import Tally


class TallyCases(unittest.TestCase):
    def test_TAL_001(self) -> None:
        """TAL-FR-001, TAL-FR-003: a new tally is zero and keeps the sum of added amounts."""
        tally = Tally()
        self.assertEqual(tally.total, 0)
        self.assertEqual(tally.add(2), 2)
        self.assertEqual(tally.add(3), 5)
        self.assertEqual(tally.total, 5)

    def test_TAL_002(self) -> None:
        """TAL-FR-002: a negative amount raises ValueError and leaves the total unchanged."""
        tally = Tally()
        tally.add(4)
        with self.assertRaises(ValueError):
            tally.add(-1)
        self.assertEqual(tally.total, 4)
