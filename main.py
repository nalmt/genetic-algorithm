# coding : utf8
# !/usr/bin/env python
import subprocess
import random
import string
from crossover import *
from mutation import *

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
def random_person(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def generatePopulation(population_size):
    population = []
    for i in range(0, population_size):
        random_length = random.randint(12, 18)
        population.append(random_person(random_length))
    return population

def roulette_wheel(population, number_to_select):
    weights = check_list(STUDENT_ID, population)
    return random.choices(population, weights, k=number_to_select)

def sortSecond(val):
    return val[1]

def roulette_wheel_by_linear_rank(population, number_to_select):
    weights = check_list(STUDENT_ID, population)

    population_sorted_by_score = []
    for i in range(0, len(population)):
        population_sorted_by_score.append([population[i], weights[i]])

    population_sorted_by_score.sort(key = sortSecond)

    weights_by_rank = []
    N = len(population_sorted_by_score)

    for i in range(0, N):
        r = i+1
        w = (2/(N * (N - 1))) * (r - 1)
        weights_by_rank.append(w)

    new_population = [item[0] for item in population_sorted_by_score]

    return random.choices(new_population, weights_by_rank, k=number_to_select)


# Génération aléatoire d'une population
population = generatePopulation(POPULATION_SIZE)

while 1 not in check_list(STUDENT_ID, population):
    print(max(check_list(STUDENT_ID, population)))

    newPopulation = []

    while len(newPopulation) < POPULATION_SIZE:
        person_1, person_2 = roulette_wheel(population, 2)
        newPopulation.extend([person_1, person_2])

        if random.random() < CROSSOVER_PROBABILITY:
            person_3, person_4 = random_crossover(person_1, person_2, 8)
            newPopulation.extend([person_3, person_4])

        person_5 = mutateGenotype(person_1)
        person_6 = mutateGenotype(person_2)
        newPopulation.extend([person_5, person_6])

    population = newPopulation

print(population)