import math

def acceptance_probability(current_cost, candidate_cost, temperature):
    """Calcula la probabilidad de aceptar un estado candidato."""
    
    if candidate_cost <= current_cost:
        return 1.0
        
    return math.exp((current_cost - candidate_cost) / temperature)

assert acceptance_probability(3, 2, 1.0) == 1.0
assert acceptance_probability(3, 3, 1.0) == 1.0
    
p = acceptance_probability(2, 3, 1.0)
assert math.isclose(p, math.exp(-1), rel_tol=1e-9)
    
print("Pruebas superadas.")