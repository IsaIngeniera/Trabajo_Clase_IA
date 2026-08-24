from parte1 import * 



def expected_next_value(grid, state, action, V):
    return sum(
        prob * V[next_state]
        for next_state, prob in grid.get_transition_probs(state, action)
    )
    # sum_{s'} T(s,a,s') V(s')


def value_iteration(grid, threshold=1e-4, max_iter=10_000):
    V = {state: 0.0 for state in grid.states()}
    deltas = []
    for iteration in range(max_iter):
        V_new = V.copy()
        biggest_change = 0.0


        # Aplicamos la ecuación de Bellman a cada estado s.
        for state in grid.states():
            if grid.is_terminal(state):
                V_new[state] = grid.get_reward(state)
            else:
                best_expected_value = max(
                    expected_next_value(grid, state, action, V)
                    for action in grid.actions
                )

                V_new[state] = (
                    grid.get_reward(state)
                    + grid.gamma * best_expected_value
                )

            biggest_change = max(
                biggest_change,
            # Cambio local del estado:
            # |V_{k+1}(s) - V_k(s)|
                abs(V_new[state] - V[state])
            )


        # Terminamos la iteración:
        # V_{k+1} pasa a ser V_k para la siguiente vuelta.
        V = V_new
        deltas.append(biggest_change)


        
        if biggest_change < threshold:
            break

    return V, iteration + 1, deltas


def extract_policy(grid, V):
    policy = {}


   
    for state in grid.states():
        if grid.is_terminal(state):
            continue

        policy[state] = max(
            grid.actions,
            key=lambda action: expected_next_value(
                grid, state, action, V
            )
        )

    return policy


def print_values(grid, V, fmt="{:+.3f}"):
    for row in range(grid.height):
        line = []
        for col in range(grid.width):
            s = (row, col)
            if not grid.is_valid_state(s):
                line.append("  WALL  ")
            else:
                line.append(fmt.format(V[s]))
        print(" | ".join(line))

def print_policy(grid, policy):
    for row in range(grid.height):
        line = []
        for col in range(grid.width):
            s = (row, col)
            if not grid.is_valid_state(s):
                line.append(" # ")
            elif grid.is_terminal(s):
                line.append(" + " if grid.get_reward(s) > 0 else " - ")
            else:
                line.append(f" {ARROWS[policy[s]]} ")
        print(" | ".join(line))



#PRUEBA

V_star, iterations, deltas = value_iteration(grid)

print(f"Convergió en {iterations} iteraciones")
print("\nV*(s):")
ARROWS = {
    (0, 1): "→",
    (1, 0): "↓",
    (0, -1): "←",
    (-1, 0): "↑",
}
print_values(grid, V_star)
policy_star = extract_policy(grid, V_star)

print("π*(s):")
print_policy(grid, policy_star)

