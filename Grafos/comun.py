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

heuristic = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 2,
    "E": 1,
    "H": 0
}

graph = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 2), ("E", 1)],
    "C": [("E", 3)],
    "D": [("H", 1)],
    "E": [("H", 2)],
    "H": []
}

start = "A"
goal = "H"

import heapq
from itertools import count

class PriorityFrontier:
    def __init__(self):
        self.heap = []
        self.counter = count()

    def add(self, node, priority):
        # El contador permite desempatar respetando el orden de inserción.
        heapq.heappush(
            self.heap,
            (priority, next(self.counter), node)
        )

    def empty(self):
        return len(self.heap) == 0

    def remove(self):
        if self.empty():
            raise Exception("La frontier está vacía.")

        priority, _, node = heapq.heappop(self.heap)
        return node, priority
