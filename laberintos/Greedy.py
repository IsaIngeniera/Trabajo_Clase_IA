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

print("h(inicio) =", manhattan(start, goal))
print("h(meta)   =", manhattan(goal, goal))

def greedy_best_first_search(graph, heuristic, start, goal):
    start_node = Node(state=start, parent=None, cost=0)
    frontier = PriorityFrontier()
    # Greedy: La prioridad es únicamente la heurística
    frontier.add(start_node, priority=heuristic(start, goal))
    
    explored = set()
    expansion_order = []
    
    while True:
        if frontier.empty():
            raise Exception("No solution found")
            
        node = frontier.remove()
        
        if node.state in explored:
            continue
            
        expansion_order.append(node.state)
        
        if node.state == goal:
            path = reconstruct_path(node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "cost": node.cost
            }
            
        explored.add(node.state)
        
        for neighbor_state, edge_cost in graph.neighbors(node.state):
            if not frontier.contains_state(neighbor_state) and neighbor_state not in explored:
                child = Node(state=neighbor_state, parent=node, cost=node.cost + edge_cost)
                # Greedy: Solo usamos la heurística como prioridad.
                frontier.add(child, priority=heuristic(neighbor_state, goal))

greedy_result = greedy_best_first_search(maze1, manhattan, start, goal)

print("Estados explorados:", len(greedy_result["expansion_order"]))
print("Longitud del camino:", len(greedy_result["path"]) - 1)
print("Costo del camino:", greedy_result["cost"])

maze1.show(
    path=greedy_result["path"],
    explored=set(greedy_result["expansion_order"]),
    title="Greedy Best-First Search"
)

# Pruebas públicas para Greedy
assert greedy_result["path"][0] == start
assert greedy_result["path"][-1] == goal
assert greedy_result["cost"] == 32

print("✓ Greedy pasó las pruebas.")