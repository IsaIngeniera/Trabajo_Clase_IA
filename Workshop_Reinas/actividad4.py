import random
from Actividad2 import cost
from actividad3 import neighbors

def best_neighbor(state):
  
    vecinos = neighbors(state)
    costos = [cost(v) for v in vecinos]
    costo_minimo = min(costos)
 
    mejores = [v for v, c in zip(vecinos, costos) if c == costo_minimo]
    elegido = random.choice(mejores)
 
    return elegido, costo_minimo


# Prueba de la actividad 4
state = [0, 0, 0, 0]
next_state, next_cost = best_neighbor(state)
 
assert next_state in neighbors(state)
assert next_cost == cost(next_state)
assert next_cost == min(cost(s) for s in neighbors(state))
print("Actividad 4 - Pruebas superadas.")
 

"""
    Retorna un vecino de costo minimo y su costo.
 
    Si hay varios vecinos con el mismo costo minimo, se selecciona
    uno de ellos al azar.

"""