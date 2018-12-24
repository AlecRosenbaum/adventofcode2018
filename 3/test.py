import unittest

from solution import solution_part_one, solution_part_two

PROBLEM_INPUT = "\n".join([
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2",
])


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(PROBLEM_INPUT), 4)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(PROBLEM_INPUT), 3)


if __name__ == "__main__":
    unittest.main()
