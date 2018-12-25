import unittest

from solution import solution_part_one, solution_part_two


PROBLEM_INPUT = "\n".join([
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
])


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(PROBLEM_INPUT), "CABDFE")


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(PROBLEM_INPUT, num_workers=2, step_delay=0), 15)


if __name__ == "__main__":
    unittest.main()
