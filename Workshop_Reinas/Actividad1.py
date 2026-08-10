def attacking(row_i, col_i, row_j, col_j):
    """Retorna True si dos reinas se atacan."""
    return row_i == row_j or abs(row_i - row_j) == abs(col_i - col_j)

# Pruebas de la actividad 1
assert attacking(0, 0, 0, 3) is True       # misma fila
assert attacking(0, 0, 3, 3) is True       # misma diagonal
assert attacking(0, 0, 1, 3) is False      # no se atacan

print("Pruebas superadas.")     