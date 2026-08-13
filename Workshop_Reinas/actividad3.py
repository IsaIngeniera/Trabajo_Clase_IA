
def neighbors(state):
    
    n = len(state)
    result = []
    for col in range(n):
        fila_actual = state[col]
        for fila in range(n):
            if fila != fila_actual:
                vecino = state.copy()
                vecino[col] = fila
                result.append(vecino)
    return result





# Pruebas de la actividad 3
test_state = [0, 1, 2, 3]
test_neighbors = neighbors(test_state)
assert len(test_neighbors) == 12
assert test_state not in test_neighbors
assert len({tuple(s) for s in test_neighbors}) == 12
print("Actividad 3 - Pruebas superadas.")
 


"""
    Genera todos los estados vecinos moviendo una sola reina.
 
    Un vecino se obtiene cambiando la fila de la reina de una columna
    a cualquiera de las N-1 filas restantes, dejando fijas las demas
    columnas. Para N columnas hay N-1 movimientos posibles por columna,
    es decir N*(N-1) vecinos en total.

"""