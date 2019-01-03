import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        problem_input = "\n".join([
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab",
        ])
        self.assertEqual(solution_part_one(problem_input), 12)


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        problem_input = "\n".join([
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz",
        ])
        self.assertEqual(solution_part_two(problem_input), "fgij")


if __name__ == "__main__":
    unittest.main()
