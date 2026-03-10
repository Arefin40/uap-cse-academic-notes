import math
from typing import Tuple


def manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def diagonal(c1, c2):
    return max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))


def euclidean(c1, c2):
    return round(math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2), 4)


DIRECTIONS = [
    (-1, 0, False),  # left
    (1, 0, False),  # right
    (0, -1, False),  # up
    (0, 1, False),  # down
    (-1, -1, True),  # upward-left
    (-1, 1, True),  # downward-left
    (1, -1, True),  # upward-right
    (1, 1, True),  # downward-right
]


class Terrain:
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()

        # iterator for iterating over each line
        it = iter(lines)

        # grid dimension
        grid_size = self.__parseInt(next(it))
        self.grid = {"x": grid_size[0], "y": grid_size[1]}

        # obstacle cells
        k = self.__parseInt(next(it))
        self.obstacles = set(self.__parseInt(next(it)) for _ in range(k))

        # terrain costs cells
        c = self.__parseInt(next(it))
        self.terrain_costs = {}
        for _ in range(c):
            x, y, cost = self.__parseInt(next(it))
            self.terrain_costs[(x, y)] = cost

        # start and goal
        self.start = self.__parseInt(next(it))
        self.goal = self.__parseInt(next(it))

    def __parseInt(self, text: str):
        numbers = [int(n) for n in text.strip().split()]
        return numbers[0] if len(numbers) == 1 else tuple(numbers)

    def is_obstacle(self, cell: Tuple[int, int]):
        return cell in self.obstacles

    def within_boundary(self, cell: Tuple[int, int]):
        return 0 <= cell[0] < self.grid["x"] and 0 <= cell[1] < self.grid["y"]

    def traversable(self, cell: Tuple[int, int]):
        return self.within_boundary(cell) and cell not in self.obstacles

    def cost(self, cell: Tuple[int, int]):
        return 1 if cell not in self.terrain_costs else self.terrain_costs[cell]


if __name__ == "__main__":
    terrain = Terrain("input.txt")
    print(f"grid: {terrain.grid}")
    print(f"start: {terrain.start}")
    print(f"goal: {terrain.goal}", end="\n\n")
    print(f"obstacles: {terrain.obstacles}")
    print(f"terrain costs cells: {terrain.terrain_costs}", end="\n\n")

    print(f"Is cell (1,1) is a obstacle? {terrain.is_obstacle((1, 1))}")
    print(f"Is cell (2,1) is a obstacle? {terrain.is_obstacle((2, 1))}", end="\n\n")

    print(f"Cost of cell (2, 3): {terrain.cost((2, 3))}")
    print(f"Cost of cell (2, 2): {terrain.cost((2, 2))}")
