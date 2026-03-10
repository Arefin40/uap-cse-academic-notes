def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # grid dimension
    m, n = map(int, lines[0].split())

    # obstacles
    k = int(lines[1])
    obstacles = {tuple(map(int, lines[2 + i].split())) for i in range(k)}

    # terrain cost cells
    idx = 2 + k
    c = int(lines[idx])
    terrain = {}
    for i in range(c):
        x, y, cost = map(int, lines[idx + 1 + i].split())
        terrain[(x, y)] = cost

    # start and goal
    start = tuple(map(int, lines[idx + 1 + c].split()))
    goal = tuple(map(int, lines[idx + 2 + c].split()))

    return m, n, obstacles, start, goal, terrain


if __name__ == "__main__":
    parse_input("input.txt")
