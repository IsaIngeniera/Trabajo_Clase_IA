
import gymnasium as gym
from comun import initialize_q_table, epsilon_greedy_policy

def main():
    # 2. Crear FrozenLake (Igual que en actividad1.py)
    env = gym.make(
        "FrozenLake-v1",
        map_name="4x4",
        is_slippery=False,
        render_mode="rgb_array"
    )

    state_space = env.observation_space.n
    action_space = env.action_space.n

    Q = initialize_q_table(state_space, action_space)

    # 💬 Actividad 2 — Inicio del aprendizaje
    ##
    ##Respuestas / discusión:
    ## ¿Esto significa que todas las acciones son malas, o que el agente todavía no sabe nada?:
    ## Significa que el agente todavía no sabe nada. Al iniciar en cero, el agente asume desconocimiento sobre las utilidades, no necesariamente que sean malas (a menos que todas las recompensas sean positivas).
    ## ¿Qué ocurre si varias acciones tienen exactamente el mismo valor máximo?:
    ## Se debe desempatar (usualmente de forma aleatoria) entre aquellas acciones que comparten el valor máximo para evitar sesgos y permitir exploración.
    ##

    # 3. Ejecutar una transición
    print("--- Ejecutando una transición ---")
    state, _ = env.reset()

    epsilon = 1.0
    action = epsilon_greedy_policy(Q, state, epsilon, env)

    next_state, reward, terminated, truncated, _ = env.step(action)

    print("state      =", state)
    print("action     =", action)
    print("reward     =", reward)
    print("next_state =", next_state)
    print("done       =", terminated or truncated)

if __name__ == "__main__":
    main()
