"""
Day 17 challenge
"""
import re

import attr


def solution_part_one(arg):
    buff = [0]
    idx = 0

    for i in range(1, 2018):
        idx = (idx + arg) % len(buff)
        buff.insert((idx % len(buff)) + 1, i)
        idx += 1


    return buff[(idx + 1) % len(buff)]


def solution_part_two(arg):
    idx = 0
    buff_len = 1
    pos_zero = 0
    after_zero = None


    for i in range(1, 50000001):
        # cycle the index
        idx = (idx + arg) % buff_len

        if idx % buff_len < pos_zero:
            pos_zero += 1
        elif idx % buff_len == pos_zero:
            after_zero = i
        else:
            # insert idx > 0, do nothing
            pass

        # bump the index
        idx += 1

        # bump the size of the list
        buff_len += 1

    return after_zero


if __name__ == "__main__":
    problem_input = 367
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
