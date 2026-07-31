from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Maze:
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)
        contents = self.filename.read_text(encoding="utf-8")

        if contents.count("A") != 1:
            raise ValueError("El laberinto debe tener exactamente un punto inicial A.")
        if contents.count("B") != 1:
            raise ValueError("El laberinto debe tener exactamente una meta B.")

        lines = contents.splitlines()
        self.height = len(lines)
        self.width = max(len(line) for line in lines)
        self.walls = np.zeros((self.height, self.width), dtype=bool)

        for row in range(self.height):
            for col in range(self.width):
                symbol = lines[row][col] if col < len(lines[row]) else "#"

                if symbol == "A":
                    self.start = (row, col)
                elif symbol == "B":
                    self.goal = (row, col)
                elif symbol != " ":
                    self.walls[row, col] = True

    def neighbors(self, state: tuple[int, int]):
        """Devuelve vecinos en el MISMO formato que graph[node.state]:
        una lista de tuplas (estado_vecino, costo_de_la_arista)."""
        row, col = state
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        valid = []
        for r, c in candidates:
            if (
                0 <= r < self.height
                and 0 <= c < self.width
                and not self.walls[r, c]
            ):
                valid.append(((r, c), 1))
        return valid

    def show(self, path=None, explored=None, title="Laberinto", figsize=(6, 6)):
        # 0: libre, 1: muro, 2: explorado, 3: camino, 4: inicio, 5: meta
        grid = np.zeros((self.height, self.width), dtype=int)
        grid[self.walls] = 1

        if explored:
            for r, c in explored:
                if grid[r, c] == 0:
                    grid[r, c] = 2

        if path:
            for r, c in path:
                if grid[r, c] in (0, 2):
                    grid[r, c] = 3

        grid[self.start] = 4
        grid[self.goal] = 5

        colors = ["white", "#222222", "#a9d6e5", "#ffb703", "#2a9d8f", "#e63946"]
        cmap = ListedColormap(colors)

        plt.figure(figsize=figsize)
        plt.imshow(grid, cmap=cmap, vmin=0, vmax=5)
        plt.xticks([])
        plt.yticks([])
        plt.title(title)
        plt.show()

maze1 = Maze("mazes/maze1.txt")

print("Dimensiones:", maze1.height, "x", maze1.width)
print("Estado inicial:", maze1.start)
print("Estado objetivo:", maze1.goal)
print("Vecinos del estado inicial:", maze1.neighbors(maze1.start))

maze1.show(title="Maze 1: problema inicial")

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return f"{self.state}(g={self.cost})"

def reconstruct_path(node):
    path = []

    while node is not None:
        path.append(node.state)
        node = node.parent

    return list(reversed(path))

