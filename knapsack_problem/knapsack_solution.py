from functools import partial
from time import time

from knapsack_problem import *
from algorithm import FitnessFunction
from algorithm import run_ga

# Problem specific parameter
THING_LIST = second_example
WEIGHT_LIMIT = max_weight

# Algorithm parameter
GENOME_LENGTH: int = len(THING_LIST)
POPULATION_LENGTH: int = 10
FITNESS_FUNCTION: FitnessFunction = partial(fitness, thing_list=THING_LIST, weight_limit=WEIGHT_LIMIT)
GENERATION_LIMIT: int = 100
FITNESS_LIMIT: float = 1310
ELITE_GENE_NUM: int = 2
MUTATION_GENE_NUM: int = 1
MUTATION_PROBABILITY: float = 0.5


def show_result(_generation_index, _end, _start, _knapsack_things,
                _knapsack_value, _knapsack_weight):
    print(f"Generation F{_generation_index}")
    print(f"Time: {_end - _start}s")
    print(f"Knapsack content: {_knapsack_things}")
    print(f"Knapsack value: {_knapsack_value}")
    print(f"Knapsack weight: {_knapsack_weight}")


start = time()
final_population, generation_index = run_ga(
    genome_length=GENOME_LENGTH,
    population_length=POPULATION_LENGTH,
    fitness_function=FITNESS_FUNCTION,
    generation_limit=GENERATION_LIMIT,
    fitness_limit=FITNESS_LIMIT,
    elite_gene_num=ELITE_GENE_NUM,
    mutation_gene_num=MUTATION_GENE_NUM,
    mutation_probability=MUTATION_PROBABILITY
)
end = time()

knapsack_things, knapsack_value, knapsack_weight = \
    genome_to_things(genome=final_population[0],
                     thing_list=THING_LIST)

show_result(generation_index, end, start, knapsack_things,
            knapsack_value, knapsack_weight)
