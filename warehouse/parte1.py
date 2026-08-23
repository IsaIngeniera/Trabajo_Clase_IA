import numpy as np

class WarehouseMDP:
    def __init__(self):
        self.height = 5
        self.width = 6

        # TODO: completa a partir de la imagen
        self.start = (0, 0)
        self.walls = {(0, 3), (1, 1), (2, 4), (4, 2)}
        self.slippery_states = {(1, 2), (2, 1), (3, 3)}

        self.terminal_states = {
            (0, 5): 10.0,
            (2, 2): 2.0,
            (3, 5): -10.0
        }

        self.danger_states = {
            (1, 4): -3.0,
            (4, 1): -3.0
        }

        self.living_reward = -1.0
        self.gamma = 0.9

        self.actions = [
            (-1, 0),  # UP
            ( 1, 0),  # DOWN
            ( 0,-1),  # LEFT
            ( 0, 1),  # RIGHT
        ]

    def is_valid_state(self, state):
        r, c = state
        return 0 <= r < self.height and 0 <= c < self.width and state not in self.walls

    def states(self):
        S = []
        for r in range(self.height):
            for c in range(self.width):
                if self.is_valid_state((r, c)):
                    S.append((r, c))
        return S

    def is_terminal(self, state):
        return state in self.terminal_states

    def get_reward(self, state):
        if state in self.terminal_states:
            return self.terminal_states[state]
        if state in self.danger_states:
            return self.danger_states[state]
        return self.living_reward

    def get_transition_probs(self, state, action):
        """
        Devuelve:
            [(next_state, probability), ...]

        Recuerda:
        - las probabilidades dependen de si 'state' es resbaloso;
        - si golpea pared/borde, next_state = state.
        """
        if self.is_terminal(state):
            return [(state, 1.0)]

        if state in self.slippery_states:
            success_prob = 0.6
            fail_prob = 0.2
        else:
            success_prob = 0.8
            fail_prob = 0.1

        if action in [(-1, 0), (1, 0)]:
            deviations = [(0, -1), (0, 1)]
        else:
            deviations = [(-1, 0), (1, 0)]
            
        def move(s, act):
            r, c = s
            ar, ac = act
            ns = (r + ar, c + ac)
            return ns if self.is_valid_state(ns) else s
            
        outcomes = {}
        
        # Forward
        n_s = move(state, action)
        outcomes[n_s] = outcomes.get(n_s, 0) + success_prob
        
        # Deviations
        for dev in deviations:
            n_s = move(state, dev)
            outcomes[n_s] = outcomes.get(n_s, 0) + fail_prob
            
        return [(s_prime, p) for s_prime, p in outcomes.items()]

grid = WarehouseMDP()

S = grid.states()
print("Número de estados:", len(S))

# Cada distribución T(s,a,·) debe sumar 1.
for s in S:
    for a in grid.actions:
        transitions = grid.get_transition_probs(s, a)
        total = sum(p for _, p in transitions)
        assert abs(total - 1.0) < 1e-12

print("✓ Todas las distribuciones de transición suman 1.")