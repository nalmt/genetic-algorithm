# coding : utf8
# !/usr/bin/env python
import subprocess
import random
import string
from crossover import *
from mutation import *
from roulette import *

STUDENT_ID = 11806768
POPULATION_SIZE = 120
CROSSOVER_PROBABILITY = 0.2

def check_list(student, list_password):
    proc = subprocess.Popen(["./unlock", str(student)] + list_password, stdout=subprocess.PIPE)
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

best_population = []

for i in range(0, 100):
    population = randomly_generate_population(POPULATION_SIZE)

    for i in range(0, 80):
        weights = check_list(STUDENT_ID, population)

        # print(max(weights))

        newPopulation = []

        while len(newPopulation) < POPULATION_SIZE:
            person_1, person_2 = roulette_wheel_by_exponential_rank_sampled(population, weights, 2, 0.7)
            #newPopulation.extend([person_1, person_2])

            if random.random() < 0.6:
                person_3, person_4 = random_crossover(person_1, person_2, 8)
                newPopulation.extend([person_3, person_4])

            person_5 = mutateGenotype(person_1, 0.6, 0.1)
            person_6 = mutateGenotype(person_2, 0.6, 0.1)
            person_7 = mutateGenotype(person_1, 0, 1)
            person_8 = mutateGenotype(person_2, 0, 1)
            person_9 = mutateGenotype(person_1, 0.3, 0.1)
            person_10 = mutateGenotype(person_2, 0.3, 0.1)
            person_11 = mutateGenotype(person_1, 0.1, 0.1)
            person_12 = mutateGenotype(person_2, 0.1, 0.1)

            newPopulation.extend([person_5, person_6, person_7, person_8, person_9, person_10, person_11, person_12])

        population = newPopulation

    w = check_list(STUDENT_ID, population)
    if max(w) > 0.84:
        a = w.index(max(w))
        print(population[a], max(w))
        ws = weighted_sample(w, len(population))

        for i in range(1, 5):
            best_population.append(population[ws[-i]])


truc = check_list(STUDENT_ID, best_population)
a = truc.index(max(truc))
print(population[a], max(truc))

print("---------------")

while 1 not in check_list(STUDENT_ID, best_population):
    weights = check_list(STUDENT_ID, best_population)
    a = weights.index(max(weights))
    print(best_population[a], max(weights))

    newPopulation = []

    while len(newPopulation) < POPULATION_SIZE:
        person_1, person_2 = roulette_wheel_by_exponential_rank_sampled(best_population, weights, 2, 0.7)
        
        if random.random() < 0.8:
            person_3, person_4 = random_crossover(person_1, person_2, 1)
            person_11, person_12 = random_crossover(person_1, person_2, 2)
            person_13, person_14 = random_crossover(person_1, person_2, 3)

            person_15, person_16 = end_crossover(person_1, person_2, 8)
            person_17, person_18 = random_crossover(person_1, person_2, 12)


            newPopulation.extend([person_3, person_4, person_11, 
            person_12, person_13, person_14, person_15, person_16, person_17, person_18])

        person_5 = mutateGenotype(person_1, 0.7, 0)
        person_6 = mutateGenotype(person_2, 0.7, 0)
        person_7 = mutateGenotype(person_1, 0, 1)
        person_8 = mutateGenotype(person_2, 0, 1)

        newPopulation.extend([person_5, person_6, person_7, person_8])

    best_population = newPopulation

print(best_population)