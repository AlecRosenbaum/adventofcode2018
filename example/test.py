import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_one(3), 638)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution_part_two(3), 1222153)


if __name__ == "__main__":
    unittest.main()
