import matplotlib.pyplot as plt
from AStarTerrain import Terrain


def BuildMaze(grid, obstacles, terrain_costs, start, goal, path=None, explored=None):
    rows, cols = grid["x"], grid["y"]

    # grid configuration
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.invert_yaxis()
    ax.set_aspect("equal")
    ax.tick_params(axis="both", which="both", length=0)

    # grid lines
    for i in range(rows + 1):
        ax.axhline(i, color="lightgray", linewidth=1)
    for j in range(cols + 1):
        ax.axvline(j, color="lightgray", linewidth=1)

    # x and y labels
    ax.xaxis.set_ticks_position("top")
    ax.set_xticks([i + 0.5 for i in range(cols)], labels=range(cols))
    ax.yaxis.set_ticks_position("left")
    ax.set_yticks([i + 0.5 for i in range(rows)], labels=range(rows))

    # obstacles
    for x, y in obstacles:
        ax.add_patch(plt.Rectangle((x, y), 1, 1, color="#444444", linewidth=0, edgecolor=None))

    # terrain cost cells
    for x, y in terrain_costs:
        ax.text(x + 0.5, y + 0.5, terrain_costs[(x, y)], ha="center", va="center")

    # start cell
    ax.add_patch(
        plt.Rectangle((start[0], start[1]), 1, 1, color="orange", linewidth=0, edgecolor=None)
    )
    # goal cell
    ax.add_patch(
        plt.Rectangle((goal[0], goal[1]), 1, 1, color="#04C975", linewidth=0, edgecolor=None)
    )

    # start to goal navigation path
    if path:
        x_coords = [x + 0.5 for x, y in path]
        y_coords = [y + 0.5 for x, y in path]
        ax.plot(x_coords, y_coords, color="red", linewidth=2, marker="o")

    # explored cells
    if explored:
        for cell in explored:
            if cell != start and cell != goal:
                ax.add_patch(
                    plt.Rectangle(cell, 1, 1, color="#f2f2f2", linewidth=0, edgecolor=None)
                )

    # Set same color and width for all outer borders
    for spine in ax.spines.values():
        spine.set_color("gray")

    ax.format_coord = lambda x, y: ""
    plt.show()


if __name__ == "__main__":
    terrain = Terrain("input.txt")
    BuildMaze(terrain.grid, terrain.obstacles, terrain.terrain_costs, terrain.start, terrain.goal)
