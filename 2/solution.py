"""
Day 2 challenge
"""
from collections import defaultdict
from itertools import combinations


def solution_part_one(arg):
    n_letters_total = defaultdict(int)

    for box_id in arg.split():
        n_letters = defaultdict(int)
        for i in box_id:
            n_letters[i] += 1

        for v in set(n_letters.values()):
            n_letters_total[v] += 1

    return n_letters_total[2] * n_letters_total[3]


def solution_part_two(arg):
    def common(a, b):
        """
        commonality between two srings -- how many letters are the same in both
        strings?

        return all characters (by index) that aren't common
        """
        assert len(a) == len(b)

        return "".join(i[0] for i in filter(lambda x: x[0] == x[1], zip(a, b)))

    return max(
        map(lambda x: common(*x), combinations(arg.split(), 2)), key=lambda x: len(x)
    )


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
