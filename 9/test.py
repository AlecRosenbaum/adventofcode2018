import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution_part_one(players=9, largest_marble=25), 32)

    def test_2(self):
        self.assertEqual(solution_part_one(players=10, largest_marble=1618), 8317)

    def test_3(self):
        self.assertEqual(solution_part_one(players=13, largest_marble=7999), 146373)

    def test_4(self):
        self.assertEqual(solution_part_one(players=17, largest_marble=1104), 2764)

    def test_5(self):
        self.assertEqual(solution_part_one(players=21, largest_marble=6111), 54718)

    def test_6(self):
        self.assertEqual(solution_part_one(players=30, largest_marble=5807), 37305)


class TestPartTwo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution_part_two(players=9, largest_marble=25), 32)

    def test_2(self):
        self.assertEqual(solution_part_two(players=10, largest_marble=1618), 8317)

    def test_3(self):
        self.assertEqual(solution_part_two(players=13, largest_marble=7999), 146373)

    def test_4(self):
        self.assertEqual(solution_part_two(players=17, largest_marble=1104), 2764)

    def test_5(self):
        self.assertEqual(solution_part_two(players=21, largest_marble=6111), 54718)

    def test_6(self):
        self.assertEqual(solution_part_two(players=30, largest_marble=5807), 37305)


if __name__ == "__main__":
    unittest.main()
