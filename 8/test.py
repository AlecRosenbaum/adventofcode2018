import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"), 138)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"), 66)


if __name__ == "__main__":
    unittest.main()
