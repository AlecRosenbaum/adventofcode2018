"""
Day 9 challenge
"""
from collections import defaultdict
import sys

import attr


DEBUG = False


def solution_part_one(players=None, largest_marble=None):
    scores = defaultdict(int)
    circle = [0]
    curr_marble = 0

    for i in range(1, largest_marble + 1):
        if i % 23 == 0:
            # special handling
            pass

            curr_player = i % players

            # current player keeps their marble
            if DEBUG:
                print(f"giving player { curr_player } { i }pts")
            scores[curr_player] += i

            # current player removes current_idx - 7, keeps it, and then that
            # index becomes the current marble
            remove_marble = curr_marble - 7
            if remove_marble < 0:
                remove_marble += len(circle)

            popped_marble = circle.pop(remove_marble)
            if DEBUG:
                print(f"giving player { curr_player } { popped_marble }pts from index { remove_marble }")
            scores[curr_player] += popped_marble

            curr_marble = remove_marble % len(circle)

        else:
            # place between 1 and 2 clockwise of current marble
            insert_idx = ((curr_marble + 1) % len(circle)) + 1
            circle.insert(insert_idx, i)
            curr_marble = insert_idx

        if DEBUG:
            print(
                " ".join(
                    map(
                        lambda x: f"({x[1]})" if x[0] == curr_marble else f"{x[1]: >2}",
                        enumerate(circle)
                    )
                ),
                # f"curr_marble: {curr_marble} - ",
                # " ".join(map("{0: >2}".format, circle[:curr_marble])),
                # f"({circle[curr_marble]}) ",
                # " ".join(map("{0: >2}".format, circle[curr_marble+1:] if curr_marble < len(circle) else [])),
                sep="",
            )

        if i % 10000 == 0 or i == largest_marble:
            sys.stdout.write("\033[K")  # Clear to the end of line
            print(f"Progress: { i }/{ largest_marble }")
            if i != largest_marble:
                sys.stdout.write("\033[F")  # cursor up one line

    return max(scores.values())


@attr.s
class Node(object):
    data = attr.ib()
    prev = attr.ib(default=None)
    next = attr.ib(default=None)

    def insert_after(self, val):
        new_node = Node(data=val, prev=self, next=self.next)

        if self.next:
            self.next.prev = new_node

        self.next = new_node

        return new_node

    def remove(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev

        return self


def solution_part_two(players=None, largest_marble=None):
    scores = defaultdict(int)
    curr_marble = Node(0)
    curr_marble.next = curr_marble.prev = curr_marble  # circular list
    root_marble = curr_marble

    for i in range(1, largest_marble + 1):
        if i % 23 == 0:
            # special handling
            pass

            curr_player = i % players

            # current player keeps their marble
            if DEBUG:
                print(f"giving player { curr_player } { i }pts")
            scores[curr_player] += i

            # current player removes current_idx - 7, keeps it, and then that
            # index becomes the current marble
            for _ in range(7):
                curr_marble = curr_marble.prev

            popped_marble = curr_marble.remove()
            curr_marble = popped_marble.next

            if DEBUG:
                print(f"giving player { curr_player } { popped_marble.data }pts")
            scores[curr_player] += popped_marble.data

        else:
            # place between 1 and 2 clockwise of current marble
            curr_marble = curr_marble.next
            curr_marble = curr_marble.insert_after(i)

        if DEBUG:
            seen_data = set()
            marbles = []
            iter_marble = root_marble
            while iter_marble.data not in seen_data:
                marbles.append(iter_marble)
                seen_data.add(iter_marble.data)
                iter_marble = iter_marble.next
            print(
                " ".join(
                    map(
                        lambda x: f"({x.data})" if x == curr_marble else f"{x.data: >2}",
                        marbles
                    )
                ),
            )

        if i % 10000 == 0 or i == largest_marble:
            sys.stdout.write("\033[K")  # Clear to the end of line
            print(f"Progress: { i }/{ largest_marble }")
            if i != largest_marble:
                sys.stdout.write("\033[F")  # cursor up one line

    return max(scores.values())


if __name__ == "__main__":
    print(solution_part_one(players=428, largest_marble=70825))
    print(solution_part_two(players=428, largest_marble=70825*100))
