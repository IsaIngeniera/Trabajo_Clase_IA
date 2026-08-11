import random


def create_individual(length, rng):
    return [rng.randint(0, 1) for _ in range(length)]


def fitness(individual):
    return sum(individual)


def roulette_selection(population, rng):
    if not population:
        raise ValueError('La población no puede estar vacía')

    fitnesses = [fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)

    if total_fitness <= 0:
        return rng.choice(population).copy()

    spin = rng.uniform(0, total_fitness)
    cumulative = 0
    for individual, value in zip(population, fitnesses):
        cumulative += value
        if cumulative >= spin:
            return individual.copy()

    return population[-1].copy()


if __name__ == '__main__':
    rng = random.Random(14)
    population = [create_individual(12, rng) for _ in range(8)]
    selected = roulette_selection(population, rng)
    print('Población:', population)
    print('Seleccionado:', selected)
    print('Fitness:', fitness(selected))
