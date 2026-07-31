from comun import Node, PriorityFrontier, reconstruct_path, graph, heuristic, start, goal

def a_star_search(graph, heuristic, start, goal):
    frontier = PriorityFrontier()
    start_node = Node(state=start, cost=0)
    frontier.add(start_node, heuristic[start])
    
    explored = set()
    expansion_order = []
    best_cost = {start: 0}
    
    while not frontier.empty():
        current_node, _ = frontier.remove()
        
        if current_node.state in explored:
            continue
            
        explored.add(current_node.state)
        expansion_order.append(current_node.state)
        
        if current_node.state == goal:
            return {
                "path": reconstruct_path(current_node),
                "expansion_order": expansion_order,
                "cost": current_node.cost
            }
            
        for neighbor, step_cost in graph.get(current_node.state, []):
            new_cost = current_node.cost + step_cost
            
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                child = Node(state=neighbor, parent=current_node, cost=new_cost)
                priority = new_cost + heuristic[neighbor]
                frontier.add(child, priority)
                
    return None

# Ejecute esta celda cuando complete A*.
astar_result = a_star_search(graph, heuristic, start, goal)

print("Orden de expansión:", " → ".join(astar_result["expansion_order"]))
print("Camino encontrado:", " → ".join(astar_result["path"]))
print("Costo óptimo:", astar_result["cost"])

# Pruebas básicas para A*
assert astar_result["path"] in (
    ["A", "B", "D", "H"],
    ["A", "B", "E", "H"]
)
assert astar_result["cost"] == 5

print("✓ A* pasó las pruebas.")