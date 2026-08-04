from pathlib import Path
import importlib
import heapq
from itertools import count


class Maze:
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)
        if not self.filename.is_absolute():
            self.filename = Path(__file__).resolve().parent / self.filename
        contents = self.filename.read_text(encoding="utf-8")

        if contents.count("A") != 1:
            raise ValueError("El laberinto debe tener exactamente un punto inicial A.")
        if contents.count("B") != 1:
            raise ValueError("El laberinto debe tener exactamente una meta B.")

        lines = contents.splitlines()
        self.height = len(lines)
        self.width = max(len(line) for line in lines)
        self.walls = [[False for _ in range(self.width)] for _ in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                symbol = lines[row][col] if col < len(lines[row]) else "#"

                if symbol == "A":
                    self.start = (row, col)
                elif symbol == "B":
                    self.goal = (row, col)
                elif symbol != " ":
                    self.walls[row][col] = True

    def neighbors(self, state: tuple[int, int]):
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
                and not self.walls[r][c]
            ):
                valid.append(((r, c), 1))
        return valid

    def show(self, path=None, explored=None, title="Laberinto", figsize=(6, 6)):
        try:
            plt = importlib.import_module("matplotlib.pyplot")
            ListedColormap = importlib.import_module("matplotlib.colors").ListedColormap
        except ImportError:
            print("matplotlib no está instalado; omitiendo visualización.")
            return

        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                if self.walls[row][col]:
                    grid[row][col] = 1

        if explored:
            for r, c in explored:
                if grid[r][c] == 0:
                    grid[r][c] = 2

        if path:
            for r, c in path:
                if grid[r][c] in (0, 2):
                    grid[r][c] = 3

        grid[self.start[0]][self.start[1]] = 4
        grid[self.goal[0]][self.goal[1]] = 5

        colors = ["white", "#222222", "#a9d6e5", "#ffb703", "#2a9d8f", "#e63946"]
        cmap = ListedColormap(colors)

        plt.figure(figsize=figsize)
        plt.imshow(grid, cmap=cmap, vmin=0, vmax=5)
        plt.xticks([])
        plt.yticks([])
        plt.title(title)
        plt.show()


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


class PriorityFrontier:
    def __init__(self):
        self.heap = []
        self.counter = count()

    def add(self, node, priority):
        heapq.heappush(self.heap, (priority, next(self.counter), node))

    def empty(self):
        return len(self.heap) == 0

    def remove(self):
        if self.empty():
            raise RuntimeError("La frontier está vacía.")
        priority, _, node = heapq.heappop(self.heap)
        return node, priority


def uniform_cost_search(maze, start_state, goal_state, verbose=False):
    frontier = PriorityFrontier()
    frontier.add(Node(start_state, cost=0), priority=0)

    best_cost = {start_state: 0}
    explored = set()
    expansion_order = []

    while not frontier.empty():
        node, _ = frontier.remove()

        if node.cost != best_cost.get(node.state):
            continue

        expansion_order.append(node.state)

        if verbose:
            print(f"Expandiendo {node.state}: g={node.cost}")

        if node.state == goal_state:
            return {
                "path": reconstruct_path(node),
                "expansion_order": expansion_order,
                "cost": node.cost,
            }

        explored.add(node.state)

        for child_state, edge_cost in maze.neighbors(node.state):
            new_cost = node.cost + edge_cost

            if new_cost < best_cost.get(child_state, float("inf")):
                best_cost[child_state] = new_cost
                child = Node(state=child_state, parent=node, cost=new_cost)
                frontier.add(child, priority=new_cost)

    return None


if __name__ == "__main__":
    maze1 = Maze("mazes/maze1.txt")
    start = maze1.start
    goal = maze1.goal

    # Información diagnóstica similar a la salida esperada en otras máquinas
    print("Dimensiones:", maze1.height, "x", maze1.width)
    print("Estado inicial:", start)
    print("Estado objetivo:", goal)
    print("Vecinos del estado inicial:", maze1.neighbors(start))

    ucs_result = uniform_cost_search(maze1, start, goal)

    maze1.show(title="Maze 1: problema inicial")

    # Mostrar orden de expansión y camino encontrado de forma legible
    print("Orden de expansión:", " -> ".join(str(s) for s in ucs_result["expansion_order"]))
    print("Camino encontrado:", " -> ".join(str(s) for s in ucs_result["path"]))
    print("Costo del camino:", ucs_result["cost"])

    assert ucs_result["cost"] == 28

    maze1.show(
        path=ucs_result["path"],
        explored=set(ucs_result["expansion_order"]),
        title="UCS: estados explorados y solución",
    )