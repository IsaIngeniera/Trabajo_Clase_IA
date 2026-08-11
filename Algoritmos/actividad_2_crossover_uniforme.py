import random


def create_individual(length, rng):
    return [rng.randint(0, 1) for _ in range(length)]


def as_string(individual):
    return ''.join(map(str, individual))


def uniform_crossover(parent1, parent2, crossover_rate, rng):
    if rng.random() >= crossover_rate:
        return parent1.copy(), parent2.copy()

    child1 = []
    child2 = []
    for gene1, gene2 in zip(parent1, parent2):
        if rng.random() < 0.5:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)

    return child1, child2


if __name__ == '__main__':
    rng = random.Random(14)
    p1 = [1, 1, 1, 1, 0, 0, 0, 0]
    p2 = [0, 0, 0, 0, 1, 1, 1, 1]
    c1, c2 = uniform_crossover(p1, p2, 1.0, rng)
    print('Padre 1:', as_string(p1))
    print('Padre 2:', as_string(p2))
    print('Hijo 1 :', as_string(c1))
    print('Hijo 2 :', as_string(c2))
