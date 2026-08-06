try:
    from Grafos.comun import reconstruct_path, Node, PriorityFrontier, graph, start, goal
except ModuleNotFoundError:
    from comun import reconstruct_path, Node, PriorityFrontier, graph, start, goal
from itertools import count

def uniform_cost_search(graph, start, goal, verbose=True):
    frontier = PriorityFrontier()
    frontier.add(Node(start, cost=0), priority=0)

    # Mejor costo conocido para cada estado.
    best_cost = {start: 0}

    explored = set()
    expansion_order = []

    while not frontier.empty():
        node, priority = frontier.remove()

        # Ignorar entradas antiguas de la cola de prioridad.
        if node.cost != best_cost.get(node.state):
            continue

        expansion_order.append(node.state)

        if verbose:
            print(f"Expandiendo {node.state}: g={node.cost}")

        if node.state == goal:
            return {
                "path": reconstruct_path(node),
                "expansion_order": expansion_order,
                "cost": node.cost
            }

        explored.add(node.state)

        for child_state, edge_cost in graph.get(node.state, []):
            new_cost = node.cost + edge_cost

            if new_cost < best_cost.get(child_state, float("inf")):
                best_cost[child_state] = new_cost

                child = Node(
                    state=child_state,
                    parent=node,
                    cost=new_cost
                )

                frontier.add(child, priority=new_cost)

    return None
    
    
if __name__ == "__main__":
    ucs_result = uniform_cost_search(graph, start, goal)

    print("Orden de expansión:", " -> ".join(ucs_result["expansion_order"]))
    print("Camino encontrado:", " -> ".join(ucs_result["path"]))
    print("Costo óptimo:", ucs_result["cost"])