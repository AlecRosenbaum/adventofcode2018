"""
Day 6 challenge
"""
from collections import defaultdict


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def print_grid(points, x, y):
    for i in range(y):
        for j in range(x):
            print(points.get((j, i), "."), end="")
        print("\n", end="")


def solution_part_one(arg):
    points = [
        tuple(int(j) for j in i.split(", "))
        for i in arg.split("\n")
    ]
    max_x = max(tuple(zip(*points))[0]) + 1
    max_y = max(tuple(zip(*points))[1]) + 1

    closest_points = {}
    for i in range(max_x):
        for j in range(max_y):
            distances = [(manhattan_distance((i, j), point), idx) for idx, point in enumerate(points)]
            min_distance = min(distances)
            if not len([point for dist, point in distances if dist <= min_distance[0]]) > 1:
                closest_points[(i, j)] = min_distance[1]

    infinite_points = set()
    for i in range(max_x):
        infinite_points.add(closest_points.get((i, 0)))
    for i in range(max_y):
        infinite_points.add(closest_points.get((0, i)))

    finite_point_count = defaultdict(int)
    for v in closest_points.values():
        if v in infinite_points:
            continue
        finite_point_count[v] += 1

    return max(finite_point_count.values())


def solution_part_two(arg, max_distance=10000):
    points = [
        tuple(int(j) for j in i.split(", "))
        for i in arg.split("\n")
    ]
    max_x = max(tuple(zip(*points))[0]) + 1
    max_y = max(tuple(zip(*points))[1]) + 1

    closest_points_sum = {}
    for i in range(max_x):
        for j in range(max_y):
            closest_points_sum[(i, j)] = sum([manhattan_distance((i, j), point) for point in points])

    return len([i for i in closest_points_sum.values() if i < max_distance])


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
