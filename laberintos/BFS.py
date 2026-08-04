from pathlib import Path
import importlib


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


def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise RuntimeError("La frontier está vacía.")
        return self.frontier.pop()


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise RuntimeError("La frontier está vacía.")
        return self.frontier.pop(0)


def breadth_first_search(maze_graph, start_state, goal_state):
    start_node = Node(state=start_state, parent=None, cost=0)
    frontier = QueueFrontier()
    frontier.add(start_node)

    explored = set()

    while True:
        if frontier.empty():
            raise RuntimeError("No solution found")

        node = frontier.remove()
        explored.add(node.state)

        if node.state == goal_state:
            return {
                "path": reconstruct_path(node),
                "cost": node.cost,
                "explored": explored,
            }

        for neighbor_state, edge_cost in maze_graph.neighbors(node.state):
            if neighbor_state not in explored and not frontier.contains_state(neighbor_state):
                child = Node(state=neighbor_state, parent=node, cost=node.cost + edge_cost)
                frontier.add(child)


if __name__ == "__main__":
    maze1 = Maze("mazes/maze1.txt")
    start = maze1.start
    goal = maze1.goal
    # Información diagnóstica
    print("Dimensiones:", maze1.height, "x", maze1.width)
    print("Estado inicial:", start)
    print("Estado objetivo:", goal)
    print("Vecinos del estado inicial:", maze1.neighbors(start))

    bfs_result = breadth_first_search(maze1, start, goal)

    # Salida legible: camino encontrado
    print("Camino encontrado:", " -> ".join(str(s) for s in bfs_result["path"]))
    print("Costo del camino:", bfs_result["cost"])

    print("Estados explorados:", len(bfs_result["explored"]))
    print("Longitud del camino:", len(bfs_result["path"]) - 1)

    maze1.show(
        path=bfs_result["path"],
        explored=bfs_result["explored"],
        title="BFS: estados explorados y solución"
    )

    assert bfs_result["path"][0] == start
    assert bfs_result["path"][-1] == goal
    assert bfs_result["cost"] == 28

    print("✓ BFS pasó las pruebas.")
    print("BFS encuentra el camino más corto que DFS en maze1.")
