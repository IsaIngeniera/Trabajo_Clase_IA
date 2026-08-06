from DFS import StackFrontier
from comun import goal, start, graph, Node, reconstruct_path
from collections import deque

class QueueFrontier(StackFrontier):
    def __init__(self):
        self.frontier = deque()

    def remove(self):
        if self.empty():
            raise Exception("La frontier está vacía.")
        return self.frontier.popleft()

def breadth_first_search(graph, start, goal, verbose=True):
    frontier = QueueFrontier()
    frontier.add(Node(start))

    explored = set()
    expansion_order = []

    while not frontier.empty():
        node = frontier.remove()
        expansion_order.append(node.state)

        if verbose:
            print(f"Expandiendo: {node.state}")
            print(f"Frontier antes de agregar vecinos: {frontier.states()}")

        if node.state == goal:
            return {
                "path": reconstruct_path(node),
                "expansion_order": expansion_order,
                "cost": node.cost
            }

        explored.add(node.state)

        for child_state, edge_cost in graph.get(node.state, []):
            if (
                child_state not in explored
                and not frontier.contains_state(child_state)
            ):
                child = Node(
                    state=child_state,
                    parent=node,
                    cost=node.cost + edge_cost
                )
                frontier.add(child)

        if verbose:
            print(f"Frontier después de expandir: {frontier.states()}")
            print("-" * 45)

if __name__ == "__main__":
    bfs_result = breadth_first_search(graph, start, goal)

    print("Orden de expansión:", " -> ".join(bfs_result["expansion_order"]))
    print("Camino encontrado:", " -> ".join(bfs_result["path"]))
    print("Costo del camino:", bfs_result["cost"])

    # Pruebas básicas para BFS
    assert bfs_result["path"] == ["A", "B", "D", "H"]
    assert bfs_result["expansion_order"] == ["A", "B", "C", "D", "E", "H"]

    print("[OK] BFS pasó las pruebas.")