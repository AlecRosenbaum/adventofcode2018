import unittest

from solution import solution_part_one, solution_part_two


class TestPartOne(unittest.TestCase):
    def test_one(self):
        problem_input = "\n".join(["+1", "+1", "+1"])
        self.assertEqual(3, solution_part_one(problem_input))

    def test_two(self):
        problem_input = "\n".join(["+1", "+1", "-2"])
        self.assertEqual(0, solution_part_one(problem_input))

    def test_three(self):
        problem_input = "\n".join(["-1", "-2", "-3"])
        self.assertEqual(-6, solution_part_one(problem_input))


class TestPartTwo(unittest.TestCase):
    def test_one(self):
        problem_input = "\n".join(["+1", "-1"])
        self.assertEqual(0, solution_part_two(problem_input))

    def test_two(self):
        problem_input = "\n".join(["+3", "+3", "+4", "-2", "-4"])
        self.assertEqual(10, solution_part_two(problem_input))

    def test_three(self):
        problem_input = "\n".join(["-6", "+3", "+8", "+5", "-6"])
        self.assertEqual(5, solution_part_two(problem_input))

    def test_four(self):
        problem_input = "\n".join(["+7", "+7", "-2", "-7", "-4"])
        self.assertEqual(14, solution_part_two(problem_input))


if __name__ == "__main__":
    unittest.main()
