import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

N = 4
SEED = 42
random.seed(SEED)


def attacking(row_i, col_i, row_j, col_j):
    """Retorna True si dos reinas se atacan."""
    return row_i == row_j or abs(row_i - row_j) == abs(col_i - col_j)


def cost(state):
    """Cuenta el número de parejas de reinas que se atacan."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if attacking(state[i], i, state[j], j):
                conflicts += 1
    return conflicts


def neighbors(state):
    """Genera todos los estados vecinos moviendo una reina."""
    n = len(state)
    result = []
    for col in range(n):
        current_row = state[col]
        for new_row in range(n):
            if new_row == current_row:
                continue
            candidate = state.copy()
            candidate[col] = new_row
            result.append(candidate)
    return result


def best_neighbor(state):
    """Retorna un vecino de costo mínimo y su costo."""
    candidates = neighbors(state)
    costs = [cost(candidate) for candidate in candidates]
    min_cost = min(costs)
    best_candidates = [candidate for candidate, candidate_cost in zip(candidates, costs) if candidate_cost == min_cost]
    best_state = random.choice(best_candidates)
    return best_state, min_cost


def hill_climbing(initial_state, max_steps=100):
    """Ejecuta Hill Climbing y devuelve el estado final y la historia de estados."""
    current_state = initial_state.copy()
    history = [current_state.copy()]

    for _ in range(max_steps):
        next_state, next_cost = best_neighbor(current_state)
        if next_cost >= cost(current_state):
            break
        current_state = next_state
        history.append(current_state.copy())

    return current_state, history


def plot_cost_history(history, title="Evolución del costo"):
    """Grafica el costo de los estados visitados."""
    costs = [cost(state) for state in history]
    plt.figure(figsize=(7, 4))
    plt.plot(range(len(costs)), costs, marker="o")
    plt.xlabel("Iteración")
    plt.ylabel("Costo")
    plt.title(title)
    plt.xticks(range(len(costs)))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    initial_state = [0, 0, 0, 0]
    final_state, history = hill_climbing(initial_state)
    print("Estado inicial:", initial_state)
    print("Estado final:", final_state)
    print("Costo final:", cost(final_state))
    print("Historial de costos:", [cost(state) for state in history])
    plot_cost_history(history)
