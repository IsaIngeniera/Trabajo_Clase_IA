import heapq
from laberintos.comun import maze1, Node, reconstruct_path

start = maze1.start
goal = maze1.goal

class PriorityFrontier:
    def __init__(self):
        self.frontier = []
        self.counter = 0

    def add(self, node, priority):
        heapq.heappush(self.frontier, (priority, self.counter, node))
        self.counter += 1

    def contains_state(self, state):
        return any(item[2].state == state for item in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("La frontier está vacía.")
        return heapq.heappop(self.frontier)[2]

def manhattan(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def a_star_search(graph, heuristic, start, goal):
    start_node = Node(state=start, parent=None, cost=0)
    frontier = PriorityFrontier()
    frontier.add(start_node, priority=heuristic(start, goal))
    
    explored = set()
    expansion_order = []
    
    best_cost = {start: 0}
    
    while True:
        if frontier.empty():
            raise Exception("No solution found")
            
        node = frontier.remove()
        
        # Ignorar nodos obsoletos
        if node.state in explored and node.cost > best_cost.get(node.state, float('inf')):
            continue
            
        if node.state not in explored:
            expansion_order.append(node.state)
            explored.add(node.state)
        
        if node.state == goal:
            path = reconstruct_path(node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "cost": node.cost
            }
            
        for neighbor_state, edge_cost in graph.neighbors(node.state):
            new_cost = node.cost + edge_cost
            
            # Mejoras de ruta según UCS
            if neighbor_state not in best_cost or new_cost < best_cost[neighbor_state]:
                best_cost[neighbor_state] = new_cost
                child = Node(state=neighbor_state, parent=node, cost=new_cost)
                # Prioridad: new_cost + heuristic(child_state, goal)
                priority = new_cost + heuristic(neighbor_state, goal)
                frontier.add(child, priority=priority)

astar_result = a_star_search(maze1, manhattan, start, goal)

print("Estados explorados:", len(astar_result["expansion_order"]))
print("Longitud del camino:", len(astar_result["path"]) - 1)
print("Costo óptimo:", astar_result["cost"])

maze1.show(
    path=astar_result["path"],
    explored=set(astar_result["expansion_order"]),
    title="A* con distancia Manhattan"
)

# Pruebas públicas para A*
assert astar_result["path"][0] == start
assert astar_result["path"][-1] == goal
assert astar_result["cost"] == 28

print("✓ A* pasó las pruebas.")