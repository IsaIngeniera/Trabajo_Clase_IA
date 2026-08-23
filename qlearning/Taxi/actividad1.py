from comun import env, Q
import random
import numpy as np

# Pregunta 1
"""
¿Cuántos estados y cuántas acciones tiene Taxi-v4?
- Tiene 500 estados y 6 acciones.

Explique brevemente por qué Taxi tiene muchos más estados que FrozenLake.
- En FrozenLake (4x4) el estado solo depende de la posición en la cuadrícula (16).
- En Taxi, el estado combina tres elementos: 
  1. La posición del taxi en la cuadrícula (5x5 = 25 posibles).
  2. La ubicación actual del pasajero (4 paradas posibles + 1 estado si está dentro del taxi = 5).
  3. El destino del pasajero (4 paradas posibles).
  En total: 25 * 5 * 4 = 500 combinaciones (estados) posibles.
"""

# Pregunta 2
"""
¿Qué representa cada elemento devuelto por env.step(action)?
- state: El estado actual del entorno antes de realizar la acción.
- action: La acción elegida para ejecutar (ej. moverse en alguna dirección, recoger o dejar).
- next_state: El estado resultante en el entorno después de realizar la acción.
- reward: La recompensa obtenida al realizar esa acción desde el estado previo.
- terminated: Un valor booleano (True/False) que indica si el episodio terminó (ej. el pasajero fue entregado en su destino).
"""

# Pregunta 3
"""
¿Cuántos valores debe aprender el agente en total?
- Debe aprender un valor Q por cada par estado-acción. 
  Por lo tanto: 500 estados * 6 acciones = 3,000 valores totales.
"""

# Actividad 1
def choose_action(Q, state, epsilon, env):
    """
    Política epsilon-greedy para seleccionar acciones
    """
    # 1. decidir si explorar o explotar
    if random.random() < epsilon:
        # Explorar: retornar una acción aleatoria
        return env.action_space.sample()
    else:
        # Explotar: retornar la mejor acción para el estado actual según Q
        q_values = Q[state]
        max_q = np.max(q_values)
        
        # En caso de empate entre varias acciones con el mismo valor máximo Q,
        # seleccionamos aleatoriamente entre ellas.
        best_actions = np.flatnonzero(q_values == max_q)
        return int(np.random.choice(best_actions))

if __name__ == "__main__":
    print("\nRespuestas a las preguntas cargadas como comentarios en el archivo.")
    
    # Prueba rápida de la función de Actividad 1
    state, info = env.reset(seed=42)
    epsilon = 0.1
    action = choose_action(Q, state, epsilon, env)
    print(f"Probando choose_action en el estado {state} con epsilon {epsilon} -> Acción seleccionada: {action}")
