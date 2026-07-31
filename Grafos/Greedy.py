from comun import Node, PriorityFrontier, reconstruct_path, graph, heuristic, start, goal

def greedy_best_first_search(graph, heuristic, start, goal):
    frontier = PriorityFrontier()
    start_node = Node(state=start, cost=0)
    frontier.add(start_node, heuristic[start])
    
    explored = set()
    expansion_order = []
    
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
            if neighbor not in explored:
                child = Node(state=neighbor, parent=current_node, cost=current_node.cost + step_cost)
                frontier.add(child, heuristic[neighbor])
                
    return None

# Ejecute esta celda cuando complete GBF.
gbf_result = greedy_best_first_search(graph, heuristic, start, goal)

print("Orden de expansión:", " → ".join(gbf_result["expansion_order"]))
print("Camino encontrado:", " → ".join(gbf_result["path"]))
print("Costo del camino:", gbf_result["cost"])

# Pruebas básicas para GBF
assert gbf_result["path"] == ["A", "C", "E", "H"]
assert gbf_result["expansion_order"] == ["A", "C", "E", "H"]
assert gbf_result["cost"] == 6

print("✓ GBF pasó las pruebas.")