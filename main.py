# coding : utf8
# !/usr/bin/env python
import subprocess
import random
import string
from crossover import *
from mutation import *
from roulette import *

STUDENT_ID = 11806768
POPULATION_SIZE = 15
CROSSOVER_PROBABILITY = 0.2

def check_list(student, list_password):
    proc = subprocess.Popen(["./unlock_mac", str(student)] + list_password, stdout=subprocess.PIPE)
    results = []
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        results.append(float(str(line).split("\\t")[1].split("\\n")[0]))
    return results

# https://pynative.com/python-generate-random-string/
def randomly_generate_person(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def randomly_generate_population(population_size):
    population = []
    for i in range(0, population_size):
        random_length = random.randint(12, 18)
        population.append(randomly_generate_person(random_length))
    return population

population = randomly_generate_population(POPULATION_SIZE)

while 1 not in check_list(STUDENT_ID, population):
    weights = check_list(STUDENT_ID, population)

    print(max(weights))

    newPopulation = []

    while len(newPopulation) < POPULATION_SIZE:
        person_1, person_2 = roulette_wheel_by_exponential_rank_sampled(population, weights, 2, 0.35)
        newPopulation.extend([person_1, person_2])

        if random.random() < CROSSOVER_PROBABILITY:
            person_3, person_4 = random_crossover(person_1, person_2, 8)
            newPopulation.extend([person_3, person_4])

        person_5 = mutateGenotype(person_1)
        person_6 = mutateGenotype(person_2)
        newPopulation.extend([person_5, person_6])

    population = newPopulation

print(population)