## PARA ESTE ES NECESARIO COMENTAR EN LA ACTIVIDAD 6 LA LIBRERIA matplotlib.use("Agg")

from comun import N, SEED, random, plot_board
import matplotlib.pyplot as plt
from actividad_6_grafica_costos import cost, plot_cost_history, hill_climbing

def random_state(n=N):
    """Genera un estado aleatorio."""
    return [random.randrange(n) for _ in range(n)]

def random_restart_hill_climbing(max_restarts=50, max_steps=100):
    """
    Ejecuta Hill Climbing desde varios estados iniciales.

    Retorna:
        best_state: mejor estado encontrado
        best_history: trayectoria de la mejor ejecución
        restarts_used: número de reinicios realizados
    """
    best_overall_state = None
    best_overall_cost = float('inf')
    best_overall_history = []
    restarts_used = 0
    
    for _ in range(max_restarts):
        restarts_used += 1
        
        current_initial = random_state(N)
        
        final_state, history = hill_climbing(current_initial, max_steps)
        final_cost = cost(final_state)
        
        if final_cost < best_overall_cost:
            best_overall_cost = final_cost
            best_overall_state = final_state
            best_overall_history = history
            
        if best_overall_cost == 0:
            break
            
    return best_overall_state, best_overall_history, restarts_used

best_state, best_history, restarts = random_restart_hill_climbing()

print("Mejor estado:", best_state)
print("Costo:", cost(best_state))
print("Reinicios utilizados:", restarts)

plot_board(best_state, f"Random Restart — costo {cost(best_state)}")
plot_cost_history(best_history, "Mejor ejecución de Random Restart")
plt.show()