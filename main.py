# coding : utf8
# !/usr/bin/env python
import subprocess
from crossover import *
from mutation import *
from roulette import *
import numpy
import matplotlib.pyplot as plt
STUDENT_ID = 11806768
POPULATION_SIZE = 600
CROSSOVER_PROBABILITY = 0.5
MUTATE_PROBABILITY = 0.4
ADD_DELETE_PROBABILITY = 0.2
ELITES = 2

generation = 0

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

def elitisme(population, n):
    weights = check_list(STUDENT_ID, population)
    weights = sorted(weights)
    elites = []
    for i in range(n):
        indexbestfitness = weights[i]
        bestindividual = population[int(indexbestfitness)]
        elites.append(bestindividual)
    return elites



def plotting(generation, bestfitness):
    figure = plt.figure()
    plt.plot(generation, bestfitness)
    figure.suptitle('Best fitness by Generation')
    ax = figure.add_subplot(1, 1, 1)
    ax.set_xlabel('Generation')
    ax.set_ylabel('Best fitness')
    plt.show()

while 1 not in check_list(STUDENT_ID, population):
    weights = check_list(STUDENT_ID, population)
    bestfitness= max(weights)
    print(bestfitness)
    newPopulation = []
    newPopulation.extend(elitisme(population,ELITES))


    while len(newPopulation) < POPULATION_SIZE:
        person_1, person_2 = roulette_wheel_by_exponential_rank_sampled(population, weights, 2, 0.35)
        #person_1, person_2 = roulette_wheel_by_linear_rank(population, weights, 2)

        if random.random() < CROSSOVER_PROBABILITY:
            person_3, person_4 = random_crossover(person_1, person_2, 8)
            newPopulation.extend([person_3, person_4])

        person_5 = mutateGenotype(person_1, MUTATE_PROBABILITY, ADD_DELETE_PROBABILITY)
        person_6 = mutateGenotype(person_2, MUTATE_PROBABILITY, ADD_DELETE_PROBABILITY)
        newPopulation.extend([person_5, person_6])

    population = newPopulation
    generation += 1
   # plotting(generation, bestfitness)


print(population)