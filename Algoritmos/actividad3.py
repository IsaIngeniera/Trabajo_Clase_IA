import string
import random
import numpy as np
import matplotlib.pyplot as plt
from comun import one_point_crossover, SEED

# Alfabeto: letras mayúsculas + espacio
ALPHABET = string.ascii_uppercase + " "


def create_individual_phrase(length, rng, alphabet=ALPHABET):
    return [rng.choice(alphabet) for _ in range(length)]


def fitness_phrase(individual, target):
    return sum(1 for a, b in zip(individual, target) if a == b)


def as_phrase(individual):
    return ''.join(individual)


def mutate_phrase(individual, mutation_rate, rng, alphabet=ALPHABET):
    child = individual.copy()
    for i in range(len(child)):
        if rng.random() < mutation_rate:
            child[i] = rng.choice(alphabet)
    return child

def genetic_algorithm_phrase(
    target,
    population_size=200,
    generations=500,
    crossover_rate=0.9,
    mutation_rate=0.02,
    tournament_size=3,
    elitism=True,
    alphabet=ALPHABET,
    seed=0
):
    length = len(target)
    rng = random.Random(seed)
    population = [create_individual_phrase(length, rng, alphabet)
                  for _ in range(population_size)]
    history = []

    def fit(ind):
        return fitness_phrase(ind, target)

    for generation in range(generations + 1):
        fitnesses = [fit(ind) for ind in population]
        best_index = int(np.argmax(fitnesses))
        best = population[best_index].copy()

        history.append({
            'generation': generation,
            'best': max(fitnesses),
            'mean': float(np.mean(fitnesses)),
            'best_individual': best
        })

        if fit(best) == length or generation == generations:
            break

        new_population = [best] if elitism else []

        while len(new_population) < population_size:
            # reutilizamos selección por torneo, pero con el fitness de frase
            parent1 = max(rng.sample(population, tournament_size), key=fit).copy()
            parent2 = max(rng.sample(population, tournament_size), key=fit).copy()
            child1, child2 = one_point_crossover(parent1, parent2, crossover_rate, rng)
            child1 = mutate_phrase(child1, mutation_rate, rng, alphabet)
            child2 = mutate_phrase(child2, mutation_rate, rng, alphabet)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return history[-1]['best_individual'], history


target = "INTELIGENCIA ARTIFICIAL"
best, hist = genetic_algorithm_phrase(target, seed=SEED)

print('Objetivo :', target)
print('Resultado:', as_phrase(best))
print('Fitness  :', fitness_phrase(best, target), '/', len(target))
print('Generaciones ejecutadas:', hist[-1]['generation'])



gens = [h['generation'] for h in hist]
bests = [h['best'] for h in hist]
means = [h['mean'] for h in hist]

plt.figure(figsize=(8, 4))
plt.plot(gens, bests, label='Mejor fitness')
plt.plot(gens, means, label='Fitness medio')
plt.axhline(len(target), color='gray', linestyle='--', label='Óptimo')
plt.xlabel('Generación')
plt.ylabel('Caracteres correctos')
plt.title(f'Evolución hacia la frase objetivo: "{target}"')
plt.legend()
plt.grid(True)
plt.show()

