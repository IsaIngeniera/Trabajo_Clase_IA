## PARA ESTE ES NECESARIO COMENTAR EN LA ACTIVIDAD 6 LA LIBRERIA matplotlib.use("Agg")

from comun import *
from Actividad8 import acceptance_probability
from actividad_6_grafica_costos import cost, neighbors, plot_cost_history
from Actividad7 import random_state
import matplotlib.pyplot as plt
import random

def simulated_annealing(
    initial_state,
    initial_temperature=10.0,
    cooling_rate=0.95,
    min_temperature=1e-3,
    max_steps=1000,
):
    """
    Ejecuta Simulated Annealing.

    Retorna:
        best_state: mejor estado encontrado
        history: estados aceptados durante la búsqueda
        temperatures: temperatura asociada a cada estado
    """
    current_state = initial_state
    current_cost = cost(current_state)

    best_state = current_state
    best_cost = current_cost

    temperature = initial_temperature
    history = [current_state]
    temperatures = [temperature]

    for step in range(max_steps):
        if current_cost == 0 or temperature < min_temperature:
            break

        # Seleccionamos un vecino aleatorio
        candidate = random.choice(neighbors(current_state))
        candidate_cost = cost(candidate)

        # Calculamos el cambio de costo y la probabilidad de aceptar
        probability = acceptance_probability(current_cost, candidate_cost, temperature)

        # Aceptamos siempre las mejoras, o peores según la probabilidad
        if random.random() < probability:
            current_state = candidate
            current_cost = candidate_cost
            history.append(current_state)
            temperatures.append(temperature)

            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost

        # 5. Reducimos la temperatura
        temperature *= cooling_rate

    return best_state, history, temperatures
    
if __name__ == "__main__":

    initial_state = random_state()
    sa_state, sa_history, temperatures = simulated_annealing(initial_state)

    print("Estado inicial:", initial_state)
    print("Mejor estado:", sa_state)
    print("Costo final:", cost(sa_state))
    print("Estados aceptados:", len(sa_history))

    plot_board(initial_state, "Estado inicial")
    plot_board(sa_state, f"Simulated Annealing — costo {cost(sa_state)}")
    plot_cost_history(sa_history, "Evolución del costo en Simulated Annealing")
     