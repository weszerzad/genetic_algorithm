from collections import namedtuple
from typing import Tuple

from algorithm import Genome, List

Thing = namedtuple('Thing', ['name', 'value', 'weight'])
ThingList = List[Thing]

max_weight = 3000

first_example = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192)]

second_example = [
                     Thing('Mints', 5, 25),
                     Thing('Socks', 10, 38),
                     Thing('Tissues', 15, 80),
                     Thing('Phone', 500, 200),
                     Thing('Baseball Cap', 100, 70)
                 ] + first_example


def fitness(genome: Genome, thing_list: List[Thing], weight_limit: int) -> int:
    if len(genome) != len(thing_list):
        raise ValueError("genome and thing list must be of same length")

    value = 0
    weight = 0

    for index, i in enumerate(genome):
        if i == 1:
            value += thing_list[index].value
            weight += thing_list[index].weight

        if weight > weight_limit:
            return 0

    return value


def genome_to_things(genome: Genome, thing_list: ThingList) -> Tuple[List[str], int, int]:
    knapsack_things: List[str] = []
    knapsack_value: int = 0
    knapsack_weight: int = 0

    for index, gene in enumerate(genome):
        if gene == 1:
            knapsack_things.append(thing_list[index].name)
            knapsack_value += thing_list[index].value
            knapsack_weight += thing_list[index].weight

    return knapsack_things, knapsack_value, knapsack_weight
