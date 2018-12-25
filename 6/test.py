import unittest

from solution import solution_part_one, solution_part_two


PROBLEM_INPUT = "\n".join([
    "1, 1",
    "1, 6",
    "8, 3",
    "3, 4",
    "5, 5",
    "8, 9",
])


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(PROBLEM_INPUT), 17)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(PROBLEM_INPUT, max_distance=32), 16)


if __name__ == "__main__":
    unittest.main()
