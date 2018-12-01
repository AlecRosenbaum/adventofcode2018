"""
Day 1 challenge
"""
from functools import reduce


def solution_part_one(arg):
    return reduce(
        lambda agg, x: agg + (int(x[1:]) if x[0] == "+" else -1 * int(x[1:])),
        arg.split(),
        0,
    )


def solution_part_two(arg):
    curr_freq = 0
    seen_frequencies = set()
    idx = 0
    args = arg.split()

    while curr_freq not in seen_frequencies:
        seen_frequencies.add(curr_freq)
        curr_freq += (
            int(args[idx % len(args)][1:])
            if args[idx % len(args)][0] == "+"
            else -1 * int(args[idx % len(args)][1:])
        )
        idx += 1

    return curr_freq

if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print("Part 1:", solution_part_one(problem_input))
    print("Part 1:", solution_part_two(problem_input))
