"""
Day 7 challenge
"""
import re
import itertools

import attr


STEP_REGEX = re.compile(r"Step (.) must be finished before step (.) can begin\.")


@attr.s
class Graph:
    nodes = attr.ib(default=attr.Factory(dict))

    def available(self):
        for node in self.nodes.values():
            if not node.completed and not len(
                [i for i in node.depends_on if not i.completed]
            ):
                yield node

    def get(self, node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(name=node_name)
        return self.nodes[node_name]


@attr.s
class Node:
    name = attr.ib()
    depends_on = attr.ib(default=attr.Factory(list), cmp=False)
    completed = attr.ib(default=False, cmp=False)


@attr.s
class Worker:
    id = attr.ib()
    curr_node = attr.ib(default=None)
    completion_time = attr.ib(default=None)


def solution_part_one(arg):
    g = Graph()

    for step in arg.split("\n"):
        depends_on, node = STEP_REGEX.match(step).groups()
        g.get(node).depends_on.append(g.get(depends_on))

    output = []
    while any(g.available()):
        next_step = min(list(g.available()))
        next_step.completed = True
        output.append(next_step.name)

    return "".join(output)


def solution_part_two(arg, num_workers=5, step_delay=60):
    g = Graph()

    for step in arg.split("\n"):
        depends_on, node = STEP_REGEX.match(step).groups()
        g.get(node).depends_on.append(g.get(depends_on))

    workers = [Worker(id=i) for i in range(num_workers)]

    curr_time = 0
    while any(g.available()):
        # finish any current jobs
        for worker in workers:
            if worker.completion_time == curr_time:
                worker.curr_node.completed = True
                worker.curr_node = None
                worker.completion_time = None

        # assign work
        for node in sorted(g.available()):
            if node in [i.curr_node for i in workers]:
                continue

            worker = next(filter(lambda x: x.curr_node is None, workers), None)
            if worker:
                worker.curr_node = node
                worker.completion_time = curr_time + step_delay + ord(node.name) - 64

        # advance time
        curr_time = min(
            [i.completion_time for i in workers if i.curr_node] or [curr_time]
        )

    return curr_time


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
