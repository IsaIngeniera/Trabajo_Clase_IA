from actividad_5_hill_climbing import hill_climbing, cost
from Actividad9 import simulated_annealing
from Actividad7 import random_restart_hill_climbing, random_state
def compare_algorithms(trials=100):
    results = {
        "Hill Climbing": 0,
        "Random Restart": 0,
        "Simulated Annealing": 0,
    }

    for _ in range(trials):
        initial_state = random_state()

        hc_state, _ = hill_climbing(initial_state)
        if cost(hc_state) == 0:
            results["Hill Climbing"] += 1

        rr_state, _, _ = random_restart_hill_climbing(max_restarts=20)
        if cost(rr_state) == 0:
            results["Random Restart"] += 1

        sa_state, _, _ = simulated_annealing(initial_state)
        if cost(sa_state) == 0:
            results["Simulated Annealing"] += 1

    return results

if __name__ == "__main__":
    results = compare_algorithms(trials=100)
    for algorithm, successes in results.items():
        print(f"{algorithm:20s}: {successes}/100")