"""
Day 3 challenge
"""
import re
from collections import defaultdict

CLAIM_REGEX = re.compile(
    r"#(?P<claim_id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)"
)


def solution_part_one(arg):
    claims = defaultdict(list)
    for claim in arg.split("\n"):
        claim_match = CLAIM_REGEX.match(claim)
        groups = ["claim_id", "x", "y", "width", "height"]
        vals = {group: int(claim_match.group(group)) for group in groups}

        for i in range(vals["width"]):
            for j in range(vals["height"]):
                claims[(vals["x"] + i, vals["y"] + j)].append(vals["claim_id"])

    return len([k for k, v in claims.items() if len(v) > 1])


def solution_part_two(arg):
    claims = defaultdict(list)
    for claim in arg.split("\n"):
        claim_match = CLAIM_REGEX.match(claim)
        groups = ["claim_id", "x", "y", "width", "height"]
        vals = {group: int(claim_match.group(group)) for group in groups}

        for i in range(vals["width"]):
            for j in range(vals["height"]):
                claims[(vals["x"] + i, vals["y"] + j)].append(vals["claim_id"])

    overlapping_claims = defaultdict(set)
    for v in claims.values():
        for claim in v:
            for overlap in v:
                overlapping_claims[claim].add(overlap)

    return list(filter(lambda x: len(x[1]) == 1, overlapping_claims.items()))[0][0]


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
