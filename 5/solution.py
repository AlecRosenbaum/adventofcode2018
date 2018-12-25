"""
Day 5 challenge
"""
import itertools

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
REACTIONS = list(itertools.chain(*[(i + i.upper(), i.upper() + i) for i in ALPHABET]))


def react(arg):
    output = arg
    old_output = None
    while old_output != output:
        old_output = output
        for reaction in REACTIONS:
            output = output.replace(reaction, "")

    return output


def solution_part_one(arg):
    return len(react(arg))


def solution_part_two(arg):
    return min([
        len(react(arg.replace(i, "").replace(i.upper(), "")))
        for i in ALPHABET
    ])


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
