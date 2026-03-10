import heapq
import math
import time

# Directions: (dx, dy, is_diagonal)
DIRECTIONS = [
    (-1, 0, False),  # left
    (1, 0, False),  # right
    (0, -1, False),  # top
    (0, 1, False),  # bottom
    (-1, -1, True),  # top-left
    (-1, 1, True),  # bottom-left
    (1, -1, True),  # top-right
    (1, 1, True),  # bottom-right
]


# ---------------- Heuristic Functions ---------------- #
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def diagonal(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def euclidean(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# ---------------- A* Implementation ---------------- #
def a_star_search(grid, start, goal, obstacles, terrain, h):
    m, n = grid
    open_fringe = []
    closed_fringe = []

    # initialize
    heapq.heappush(open_fringe, (0 + h(start, goal), 0, start, [start]))  # (fn, gn, node, path)
    g_cost = {start: 0}

    while open_fringe:
        f, g, current, path = heapq.heappop(open_fringe)
        closed_fringe.append(current)

        if current == goal:
            return path, g, closed_fringe

        for dx, dy, diag in DIRECTIONS:
            new_cell = current[0] + dx, current[1] + dy
            within_boundary = 0 <= new_cell[0] < m and 0 <= new_cell[1] < n

            if within_boundary and new_cell not in obstacles:
                # {(0, 1): 2, (1, 2): 3, (2, 2): 5}
                cost = terrain.get(new_cell, 1)

                move_cost = 1.4 * cost if diag else cost
                gn = g + move_cost

                # if new gn of current cell is not in g_cost dictionary or new gn is less than previous g_cost
                # the we will add/update
                if new_cell not in g_cost or gn < g_cost[new_cell]:
                    g_cost[new_cell] = gn

                    fn = gn + h(new_cell, goal)

                    # (fn, gn, node, path)
                    heapq.heappush(open_fringe, (fn, gn, new_cell, path + [new_cell]))

    return None, float("inf"), closed_fringe


# ---------------- Input Parser ---------------- #
def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # grid dimension
    grid = list(map(int, lines[0].split()))

    # obstacle cells
    k = int(lines[1])
    obstacles = {tuple(map(int, lines[2 + i].split())) for i in range(k)}

    # terrain costs cells
    idx = 2 + k
    c = int(lines[idx])
    terrain = {}
    for i in range(c):
        x, y, cost = map(int, lines[idx + 1 + i].split())
        terrain[(x, y)] = cost

    # start and goal
    idx = idx + 1 + c
    start = tuple(map(int, lines[idx].split()))
    goal = tuple(map(int, lines[idx + 1].split()))

    return grid, start, goal, obstacles, terrain


def AStar(filename):
    grid, start, goal, obstacles, terrain = parse_input(filename)

    heuristics = {"Manhattan": manhattan, "Diagonal": diagonal, "Euclidean": euclidean}

    for name, h in heuristics.items():
        t1 = time.time()
        path, cost, explored = a_star_search(grid, start, goal, obstacles, terrain, h)
        t2 = time.time()

        print(f"\n--- {name} Heuristic ---")
        print("Path:", path)
        print("Path Cost:", round(cost, 2))
        print("Explored Nodes:", explored)
        print("Total Explored:", len(explored))
        print("Runtime:", round(t2 - t1, 6), "seconds")


if __name__ == "__main__":
    AStar("input.txt")
