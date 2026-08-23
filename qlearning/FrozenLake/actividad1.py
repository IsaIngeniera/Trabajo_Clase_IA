import gymnasium as gym
from comun import initialize_q_table

def main():
    # 2. Crear FrozenLake
    env = gym.make(
        "FrozenLake-v1",
        map_name="4x4",
        is_slippery=False,
        render_mode="rgb_array"
    )

    state, info = env.reset()

    print("Estado inicial:", state)
    print("Número de estados:", env.observation_space.n)
    print("Número de acciones:", env.action_space.n)

    # 💬 Actividad 1 — La Q-table
    """
    Respuestas / discusión:
    - ¿Cuántas filas debe tener la Q-table?: 
      Debe tener tantas filas como el número de estados en el entorno. En este caso (FrozenLake 4x4), son 16 filas (estados del 0 al 15).
    - ¿Cuántas columnas?: 
      Debe tener tantas columnas como el número de acciones posibles. En FrozenLake hay 4 acciones (Left, Down, Right, Up).
    - ¿Qué representa una celda (Q[s,a])?: 
      Representa el valor Q o la utilidad esperada de tomar la acción 'a' estando en el estado 's', y de ahí en adelante seguir una política óptima.
    """

    state_space = env.observation_space.n
    action_space = env.action_space.n

    # Inicializar la Q-table usando la función del archivo comun.py
    Q = initialize_q_table(state_space, action_space)

    print("Q-table shape:", Q.shape)
    print("Q-table inicial:")
    print(Q)

if __name__ == "__main__":
    main()
