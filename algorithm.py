from math import ceil
from random import choices, randint, random
from typing import List, Callable, Tuple

Genome = List[int]
Population = List[Genome]
FitnessFunction = Callable[[Genome], int]


def generate_genome(genome_length: int) -> Genome:
    return choices([0, 1], k=genome_length)


def populate(population_length: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(population_length)]


def select(population: Population, fitness_function: FitnessFunction) -> Tuple[Genome, Genome]:
    c = choices(population,
                [fitness_function(genome) for genome in population],
                k=2)

    return c[0], c[1]


def single_point_crossover(genome_pair: Tuple[Genome, Genome]) -> Tuple[Genome, Genome]:
    if len(genome_pair[0]) < 2:
        raise ValueError("Not possible to perform crossover on genome of length 1")

    if len(genome_pair[0]) != len(genome_pair[1]):
        raise ValueError("Two genome has different length!")

    genome_length = len(genome_pair[0])

    crossover_pos = randint(1, genome_length - 1)

    g1 = genome_pair[0][0:crossover_pos] + genome_pair[1][crossover_pos:]
    g2 = genome_pair[1][0:crossover_pos] + genome_pair[0][crossover_pos:]

    return g1, g2


def mutation(genome: Genome, num: int, probability: float) -> Genome:
    for _ in range(num):
        index = randint(0, len(genome)-1)
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)

    return genome


def run_ga(
        genome_length: int,
        population_length: int,
        fitness_function: FitnessFunction,
        generation_limit: int,
        fitness_limit: float,
        elite_gene_num: int,
        mutation_gene_num: int,
        mutation_probability: float
) -> Tuple[Population, int]:



    population = populate(population_length, genome_length)

    gen_index = 0

    for j in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_function(genome), reverse=True)

        if fitness_function(population[0]) >= fitness_limit:
            break

        if elite_gene_num > len(population):
            raise ValueError("elite genes exceed population")

        next_gen = []

        for i in range(ceil((len(population) - elite_gene_num) / 2)):
            p1, p2 = select(population, fitness_function)
            o1, o2 = single_point_crossover((p1, p2))
            o1 = mutation(genome=o1, num=mutation_gene_num, probability=mutation_probability)
            o2 = mutation(genome=o2, num=mutation_gene_num, probability=mutation_probability)
            next_gen += [o1, o2]

        if (len(population) - elite_gene_num) % 2 != 0:
            next_gen.pop(randint(0, len(next_gen)-1))

        population = population[0:elite_gene_num] + next_gen
        gen_index += 1

    # Sort in case exceeding generation limit
    population = sorted(population, key=lambda genome: fitness_function(genome), reverse=True)

    return population, gen_index
