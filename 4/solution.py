"""
Day 4 challenge
"""

import datetime
import re
from collections import defaultdict
from itertools import groupby

DATETIME_REGEX = re.compile(
    r"\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] (?P<message>.*)"
)
GUARD_BEGINS_REGEX = re.compile(r"Guard #(?P<guard_id>\d+) begins shift")


def parse_logs(arg):
    # parse the logs
    logs = []
    for i in arg.split("\n"):
        log_match = DATETIME_REGEX.match(i)
        if not log_match:
            print(i)
            return
        logs.append(
            (
                datetime.datetime(
                    year=int(log_match.group("year")),
                    month=int(log_match.group("month")),
                    day=int(log_match.group("day")),
                    hour=int(log_match.group("hour")),
                    minute=int(log_match.group("minute")),
                ),
                log_match.group("message"),
            )
        )

    logs.sort()
    return logs


def get_occupancy(logs):
    occupancy = defaultdict(list)

    # determine occupancy
    curr_guard = None
    asleep_since = None
    for timestamp, log in logs:
        guard_start_match = GUARD_BEGINS_REGEX.match(log)
        if guard_start_match:
            curr_guard = int(guard_start_match.group("guard_id"))
            asleep_since = None
        elif log == "falls asleep":
            asleep_since = timestamp
        elif log == "wakes up":
            for i in range(int((timestamp - asleep_since).seconds/60)):
                occupancy[(asleep_since + datetime.timedelta(minutes=i)).time()].append(curr_guard)

    return occupancy


def solution_part_one(arg):
    logs = parse_logs(arg)
    occupancy = get_occupancy(logs)

    # analyze occupancy
    minutes_asleep = defaultdict(list)
    for k, v in occupancy.items():
        for i in v:
            minutes_asleep[i].append(k)

    sleepiest_guard = max(minutes_asleep.items(), key=lambda x: len(x[1]))[0]
    sleepiest_minute = max([(len([i for i in v if i == sleepiest_guard]), k) for k, v in occupancy.items()])[1].minute

    return sleepiest_guard * sleepiest_minute


def solution_part_two(arg):
    logs = parse_logs(arg)
    occupancy = get_occupancy(logs)

    sleepiest_minute, sleepiest_guard = max(
        [
            (k, max([(len(list(group)), group_key) for group_key, group in groupby(v)]))
            for k, v
            in occupancy.items()
        ],
        key=lambda x: x[1],
    )

    return sleepiest_guard[1] * sleepiest_minute.minute


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
