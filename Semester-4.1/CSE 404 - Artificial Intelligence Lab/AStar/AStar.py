import heapq
import time
from AStarTerrain import Terrain, DIRECTIONS, manhattan, diagonal, euclidean
from Draw import BuildMaze


class AStar(Terrain):
    def __init__(self, filename, heuristic, display=False):
        super().__init__(filename)
        self.open_fringe = []
        self.closed = set()
        self.parent = {}
        self.g_cost = {self.start: 0}
        self.heuristic = heuristic
        self.display = display

    def push(self, cell, g):
        h = self.heuristic(cell, self.goal)
        heapq.heappush(self.open_fringe, (g + h, h, cell))

    def reconstruct_path(self, cell):
        path = []
        while cell in self.parent:
            path.append(cell)
            cell = self.parent[cell]
        path.append(self.start)
        return path[::-1]

    def show(self, cell, runtime):
        path = self.reconstruct_path(cell)
        explored = sorted(self.closed)
        print(f"===== {self.heuristic.__name__.title()} Heuristic =====")
        print("Path:", path)
        print(f"Path Cost: {self.g_cost[cell]}")
        print(f"Explored Nodes: {explored}")
        print(f"Total Explored: {len(explored)}")
        print(f"Runtime: {runtime:.3f} ms")

        if self.display:
            BuildMaze(
                self.grid, self.obstacles, self.terrain_costs, self.start, self.goal, path, explored
            )

    def run(self):
        start_time = time.perf_counter()
        self.push(self.start, 0)

        while self.open_fringe:
            _, _, current = heapq.heappop(self.open_fringe)
            if current in self.closed:
                continue
            self.closed.add(current)

            if current == self.goal:
                elapsed = (time.perf_counter() - start_time) * 1000
                self.show(current, elapsed)
                break

            for dx, dy, diag in DIRECTIONS:
                neighbor = (current[0] + dx, current[1] + dy)
                if not self.traversable(neighbor) or neighbor in self.closed:
                    continue
                cost = 1.4 * self.cost(neighbor) if diag else self.cost(neighbor)
                g = round(self.g_cost[current] + cost, 4)
                if neighbor not in self.g_cost or g < self.g_cost[neighbor]:
                    self.parent[neighbor] = current
                    self.g_cost[neighbor] = g
                    self.push(neighbor, g)


if __name__ == "__main__":
    for heuristic, display in [(euclidean, False), (manhattan, False), (diagonal, True)]:
        astar = AStar("input.txt", heuristic, display)
        astar.run()
        print()
