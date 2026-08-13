import random
import numpy as np
import matplotlib.pyplot as plt
from comun import genetic_algorithm, SEED


best_elit, hist_elit = genetic_algorithm(seed=SEED, generations=100, elitism=True)
best_noelit, hist_noelit = genetic_algorithm(seed=SEED, generations=100, elitism=False)


def count_decreases(history):
    bests = [h['best'] for h in history]
    return sum(1 for i in range(1, len(bests)) if bests[i] < bests[i - 1])


print('--- Con elitismo ---')
print('Fitness final:', hist_elit[-1]['best'], 'en', hist_elit[-1]['generation'], 'generaciones')
print('Veces que bajó el mejor fitness:', count_decreases(hist_elit))

print()
print('--- Sin elitismo ---')
print('Fitness final:', hist_noelit[-1]['best'], 'en', hist_noelit[-1]['generation'], 'generaciones')
print('Veces que bajó el mejor fitness:', count_decreases(hist_noelit))


plt.figure(figsize=(8, 4))
plt.plot([h['generation'] for h in hist_elit], [h['best'] for h in hist_elit],
         label='Con elitismo', marker='o', markersize=3)
plt.plot([h['generation'] for h in hist_noelit], [h['best'] for h in hist_noelit],
         label='Sin elitismo', marker='x', markersize=3)
plt.xlabel('Generación')
plt.ylabel('Mejor fitness')
plt.title('Efecto del elitismo sobre el mejor fitness por generación')
plt.legend()
plt.grid(True)
plt.show()
