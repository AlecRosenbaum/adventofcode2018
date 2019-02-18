"""
Day N challenge
"""

import math
import re
import statistics
import sys

import attr


@attr.s(frozen=True)
class Vector:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

    def __add__(self, other):
        assert isinstance(other, Vector)

        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Vector)

        return Vector(x=self.x - other.x, y=self.y - other.y)

    def dist(self, other):
        assert isinstance(other, Vector)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


@attr.s
class Star:
    position = attr.ib(validator=attr.validators.instance_of(Vector))
    velocity = attr.ib(validator=attr.validators.instance_of(Vector))

    def advance(self):
        self.position += self.velocity
        return self.position

    def rewind(self):
        self.position -= self.velocity
        return self.position

    def dist(self, *args, **kwargs):
        return self.position.dist(*args, **kwargs)

    @classmethod
    def from_coordinates(cls, coordinates):
        """parse star coordinates in the input format"""
        # Example coordinates:
        #   position=<-52592,  31869> velocity=< 5, -3>
        regex_parse = re.compile(
            r"position=<(?P<x>-?\d+),(?P<y>-?\d+)>"
            r"velocity=<(?P<dx>-?\d+),(?P<dy>-?\d+)>"
        )

        s = regex_parse.search(coordinates.replace(" ", ""))
        try:
            return cls(
                position=Vector(x=s.group("x"), y=s.group("y")),
                velocity=Vector(x=s.group("dx"), y=s.group("dy")),
            )
        except AttributeError:
            raise ValueError("Could not parse coordinates: '{}'".format(coordinates))


@attr.s
class Sky:
    stars = attr.ib(default=attr.Factory(list))

    def advance(self):
        """move all stars by one time iteration or their velovity units"""
        for star in self.stars:
            star.advance()

    def rewind(self):
        """move all stars by negative one time iteration or their velovity units"""
        for star in self.stars:
            star.rewind()

    def add_star(self, star_coordiantes):
        """Parse and start tracking a star"""
        self.stars.append(Star.from_coordinates(star_coordiantes))

    def stdev(self):
        """return the stdev of all stars"""
        zero = Vector(x=0, y=0)
        return statistics.stdev(i.dist(zero) for i in self.stars)

    def bounds(self):
        return {
            "x": {
                "from": min(star.position.x for star in self.stars),
                "to": max(star.position.x for star in self.stars),
            },
            "y": {
                "from": min(star.position.y for star in self.stars),
                "to": max(star.position.y for star in self.stars),
            },
        }

    def print(self, file=sys.stdout):
        bounds = self.bounds()
        max_dimension = max(
            bounds["y"]["to"] - bounds["y"]["from"],
            bounds["x"]["to"] - bounds["x"]["from"],
        )
        if not max_dimension < 10000:
            print("board with dimension {} too big".format(max_dimension), file=file)
            return

        # star_positions = {
        #     star.position + Vector(x=-1*bounds["x"]["from"], y=-1*bounds["x"]["from"])
        #     for star in self.stars
        # }
        # file.write("\n===========================================\n")
        # for y in range(bounds["y"]["to"] - bounds["y"]["from"] + 1):
        #     for x in range(bounds["x"]["to"] - bounds["x"]["from"] + 1):
        #         if Vector(x=x, y=y) in star_positions:
        #             print("#", file=file, end="")
        #         else:
        #             print(" ", file=file, end="")
        #     print("\n", file=file, end="")

        out_str = [
            [" " for _ in range(bounds["x"]["to"] - bounds["x"]["from"] + 1)]
            for _ in range(bounds["y"]["to"] - bounds["y"]["from"] + 1)
        ]
        for star in self.stars:
            translated_y = star.position.y - bounds["y"]["from"]
            translated_x = star.position.x - bounds["x"]["from"]
            out_str[translated_y][translated_x] = "#"

        file.write("\n===========================================\n")
        file.writelines("".join(line) + "\n" for line in out_str)

    def all_have_neighbors(self):
        directions = (
            Vector(x=1, y=0),
            Vector(x=-1, y=0),
            Vector(x=0, y=1),
            Vector(x=0, y=-1),
        )

        occupied_positions = {star.position for star in self.stars}
        for star in self.stars:
            if not any(
                True for d in directions if star.position + d in occupied_positions
            ):
                return False
        return True


def solution_part_one(arg):
    sky = Sky()

    # populate the sky
    for star in arg.split("\n"):
        sky.add_star(star)

    # iterate over time to try to find when all stars have neighbors
    timestamp = 0
    dimensions = [None, None]
    while (
        None in dimensions
        or dimensions[timestamp % 2] > dimensions[(timestamp - 1) % 2]
    ):
        sky.advance()

        bounds = sky.bounds()
        dimensions[timestamp % 2] = min(
            bounds["y"]["to"] - bounds["y"]["from"],
            bounds["x"]["to"] - bounds["x"]["from"],
        )
        timestamp += 1

    sky.rewind()
    sky.print()

    return timestamp - 1  # remove extra advance


def solution_part_two(arg):
    return solution_part_one(arg)


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
