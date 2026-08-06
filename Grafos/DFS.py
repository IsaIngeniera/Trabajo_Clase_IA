from comun import goal, start, graph, Node, reconstruct_path

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
            raise Exception("La frontier está vacía.")

        return self.frontier.pop()

    def states(self):
        return [node.state for node in self.frontier]


def depth_first_search(graph, start, goal, verbose=True):
    frontier = StackFrontier()
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

    return None

if __name__ == "__main__":
    dfs_result = depth_first_search(graph, start, goal)

    print("Orden de expansión:", " -> ".join(dfs_result["expansion_order"]))
    print("Camino encontrado:", " -> ".join(dfs_result["path"]))
    print("Costo del camino:", dfs_result["cost"])