"""
Day 8 challenge
"""

import attr
import itertools


DEBUG = False


@attr.s
class Node:
    num_children = attr.ib()
    label = attr.ib(default=None)
    num_metadata = attr.ib(default=None)
    metadata = attr.ib(default=attr.Factory(list))
    children = attr.ib(default=attr.Factory(list))

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            return sum([
                self.children[i - 1].value()
                for i in self.metadata
                if i <= len(self.children)
            ])


def parse_nodes(data):
    all_nodes = []
    node_stack = []

    total_nodes = 65

    root = Node(num_children=data[0], label=chr(total_nodes))
    total_nodes += 1
    node_stack.append(root)
    all_nodes.append(root)

    for i in data[1:]:
        top_of_stack = node_stack[-1]

        while (
            len(top_of_stack.metadata) == top_of_stack.num_metadata
            and len(top_of_stack.children) == top_of_stack.num_children
        ):
            popped_node = node_stack.pop()
            if DEBUG:
                print(f"done processing { popped_node.label }")
            top_of_stack = node_stack[-1]

        if DEBUG:
            print(f"processing { i } - stack: { [i.label for i in node_stack] }")

        if top_of_stack.num_metadata is None:
            # gathering number of metadata items
            if DEBUG:
                print(f"setting { top_of_stack.label }.num_metadata = { i }")
            top_of_stack.num_metadata = i
            continue

        if len(top_of_stack.children) < top_of_stack.num_children:
            # still adding children, adding another
            if DEBUG:
                print(f"{ top_of_stack.label } children populating, creating new node num_children = { i }")
            new_node = Node(num_children=i, label=chr(total_nodes))
            total_nodes += 1
            node_stack.append(new_node)
            top_of_stack.children.append(new_node)
            all_nodes.append(new_node)
            continue

        if len(top_of_stack.metadata) < top_of_stack.num_metadata:
            # gathering metadata
            if DEBUG:
                print(f"{ top_of_stack.label }.metadata += { i }")
            top_of_stack.metadata.append(i)
            continue

        if DEBUG:
            print(f"{ top_of_stack.label } children populating, creating new node num_children = { i }")
        new_node = Node(num_children=i, label=chr(total_nodes))
        total_nodes += 1
        node_stack.append(new_node)
        all_nodes.append(new_node)

    return root, all_nodes


def solution_part_one(arg):
    numbers = list(map(int, arg.split(" ")))
    root, all_nodes = parse_nodes(numbers)

    return sum(itertools.chain(*[i.metadata for i in all_nodes]))


def solution_part_two(arg):
    numbers = list(map(int, arg.split(" ")))
    root, all_nodes = parse_nodes(numbers)

    return root.value()


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
