import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one("dabAcCaCBAcCcaDA"), 10)
        self.assertEqual(solution_part_one("aA"), 0)
        self.assertEqual(solution_part_one("abBA"), 0)
        self.assertEqual(solution_part_one("abAB"), 4)
        self.assertEqual(solution_part_one("aabAAB"), 6)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two("dabAcCaCBAcCcaDA"), 4)


if __name__ == "__main__":
    unittest.main()
