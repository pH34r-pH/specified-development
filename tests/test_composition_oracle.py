"""Independent composition oracle for directory closure and order (DIR-003, issue #7).

The expected order is hand-authored from the accepted invariants. The property
check judges a candidate order; it is not an implementation and never supplies
its own expectation.
"""
from __future__ import annotations

import unittest

# Normative dependency edges: document -> documents it depends on.
WITNESS = {"feature/r": ["c/b", "c/m"], "c/b": ["c/z"], "c/m": [], "c/z": [], "u/x": []}
ROOT = "feature/r"
EXPECTED = ["c/m", "c/z", "c/b", "feature/r"]  # Fixed by hand before implementation.


def closure(graph: dict[str, list[str]], root: str) -> set[str]:
    selected: set[str] = set()
    pending = [root]
    while pending:
        node = pending.pop()
        if node not in selected:
            selected.add(node)
            pending.extend(graph[node])
    return selected


def violations(graph: dict[str, list[str]], root: str, order: list[str]) -> list[str]:
    """Return every invariant a candidate order breaks; an empty list means it is acceptable."""
    found: list[str] = []
    selected = closure(graph, root)
    # A node lies on a cycle when it is reachable again from one of its own dependencies.
    if any(node in closure(graph, dependency) for node in selected for dependency in graph[node]):
        return ["cycle: no order is valid"]
    if len(order) != len(set(order)):
        found.append("duplicate document")
    if set(order) != selected:
        found.append(f"closure: missing={sorted(selected - set(order))} extra={sorted(set(order) - selected)}")
    emitted: set[str] = set()
    for node in order:
        if node not in selected:
            continue
        if not set(graph[node]) <= emitted:
            found.append(f"dependency order: {node} before {sorted(set(graph[node]) - emitted)}")
        ready = sorted(candidate for candidate in selected - emitted if set(graph[candidate]) <= emitted)
        if ready and node != ready[0]:
            found.append(f"tie rule: chose {node} while {ready[0]} was the smallest ready ID")
        emitted.add(node)
    return found


class CompositionOracleTests(unittest.TestCase):
    def test_hand_authored_expected_order_satisfies_every_invariant(self) -> None:
        self.assertEqual(violations(WITNESS, ROOT, EXPECTED), [])

    def test_enumeration_order_does_not_change_the_oracle(self) -> None:
        reversed_graph = {node: list(reversed(edges)) for node, edges in reversed(list(WITNESS.items()))}
        self.assertEqual(violations(reversed_graph, ROOT, EXPECTED), [])

    def test_representative_incorrect_results_are_rejected(self) -> None:
        incorrect = {
            "sorted depth-first postorder": (["c/z", "c/b", "c/m", "feature/r"], "tie rule"),
            "insertion-order topological order": (["c/z", "c/m", "c/b", "feature/r"], "tie rule"),
            "includes unrelated document": (["c/m", "c/z", "c/b", "u/x", "feature/r"], "closure"),
            "omits a dependency": (["c/m", "c/b", "feature/r"], "closure"),
            "repeats a document": (["c/m", "c/z", "c/z", "c/b", "feature/r"], "duplicate"),
            "dependent before dependency": (["c/m", "c/b", "c/z", "feature/r"], "dependency order"),
        }
        for name, (order, expected) in incorrect.items():
            with self.subTest(name=name):
                problems = violations(WITNESS, ROOT, order)
                self.assertTrue(any(problem.startswith(expected) for problem in problems), problems)

    def test_cycle_rejects_every_order(self) -> None:
        cyclic = dict(WITNESS, **{"c/z": ["feature/r"]})
        for order in (EXPECTED, ["c/m", "c/b", "c/z", "feature/r"]):
            with self.subTest(order=order):
                self.assertEqual(violations(cyclic, ROOT, order), ["cycle: no order is valid"])


if __name__ == "__main__":
    unittest.main()
