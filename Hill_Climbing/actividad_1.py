import math
import random
import matplotlib.pyplot as plt
import comun
from comun import (
    HEIGHT, WIDTH, NUM_HOSPITALS, SEED,
    houses, initial_hospitals,
    total_cost as total_cost_manhattan,
    neighbors_of_state, plot_state
)

def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_cost_euclidean(houses, hospitals):
    return sum(min(euclidean(house, hospital) for hospital in hospitals)
               for house in houses)

def hill_climbing_custom(height, width, houses, num_hospitals, cost_fn,
                         initial_state=None, max_iterations=200, rng=None):
    rng = rng or random.Random()
    available = list(set((r, c) for r in range(height) for c in range(width)) - houses)
    current = set(initial_state) if initial_state is not None else set(rng.sample(available, num_hospitals))
    history = [cost_fn(houses, current)]
    states = [set(current)]

    for _ in range(max_iterations):
        neighbors = neighbors_of_state(height, width, houses, current)
        if not neighbors:
            break

        costs = [cost_fn(houses, n) for n in neighbors]
        best_cost = min(costs)
        current_cost = history[-1]

        if best_cost >= current_cost:
            break

        best_neighbors = [n for n, c in zip(neighbors, costs) if c == best_cost]
        current = set(rng.choice(best_neighbors))
        history.append(best_cost)
        states.append(set(current))

    return current, history, states

sol_manhattan, hist_manhattan, _ = hill_climbing_custom(
    HEIGHT, WIDTH, houses, NUM_HOSPITALS,
    cost_fn=total_cost_manhattan,
    initial_state=initial_hospitals,
    rng=random.Random(SEED)
)

sol_euclidean, hist_euclidean, _ = hill_climbing_custom(
    HEIGHT, WIDTH, houses, NUM_HOSPITALS,
    cost_fn=total_cost_euclidean,
    initial_state=initial_hospitals,
    rng=random.Random(SEED)
)

print("=== RESULTADOS DE COMPARACIÓN ===")
print(f"Manhattan — Costo final: {hist_manhattan[-1]:.2f} (Iteraciones: {len(hist_manhattan)-1})")
print(f"Euclídea  — Costo final: {hist_euclidean[-1]:.2f} (Iteraciones: {len(hist_euclidean)-1})")

plot_state(HEIGHT, WIDTH, houses, sol_manhattan,
           title=f'Solución Manhattan — Costo Manhattan: {hist_manhattan[-1]:.2f}')

plot_state(HEIGHT, WIDTH, houses, sol_euclidean,
           title=f'Solución Euclídea — Costo Euclídeo: {hist_euclidean[-1]:.2f}')