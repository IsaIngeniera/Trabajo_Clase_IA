class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

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

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("La frontier está vacía.")
        return self.frontier.pop(0)

def breadth_first_search(graph, start, goal):
    start_node = Node(state=start, parent=None, cost=0)
    frontier = QueueFrontier()
    frontier.add(start_node)
    
    explored = []
    expansion_order = []
    
    while True:
        if frontier.empty():
            raise Exception("No solution found")
            
        node = frontier.remove()
        expansion_order.append(node.state)
        
        if node.state == goal:
            path = []
            current = node
            while current is not None:
                path.append(current.state)
                current = current.parent
            path.reverse()
            return {
                "expansion_order": expansion_order,
                "path": path,
                "cost": node.cost
            }
            
        explored.append(node.state)
        
        for neighbor, edge_cost in graph.get(node.state, []):
            if not frontier.contains_state(neighbor) and neighbor not in explored:
                child = Node(state=neighbor, parent=node, cost=node.cost + edge_cost)
                frontier.add(child)


graph = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 2), ("E", 1)],
    "C": [("E", 3)],
    "D": [("H", 1)],
    "E": [("H", 2)],
    "H": []
}

start = "A"
goal = "E"

# Ejecute esta celda cuando complete BFS.
bfs_result = breadth_first_search(graph, start, goal)

print("Orden de expansión:", " → ".join(bfs_result["expansion_order"]))
print("Camino encontrado:", " → ".join(bfs_result["path"]))
print("Costo del camino:", bfs_result["cost"])

# Pruebas básicas para BFS
assert bfs_result["path"] == ["A", "B", "D", "H"]
assert bfs_result["expansion_order"] == ["A", "B", "C", "D", "E", "H"]

print("✓ BFS pasó las pruebas.")