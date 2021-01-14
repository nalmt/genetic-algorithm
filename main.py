# coding : utf8
# !/usr/bin/env python
#import demo
import subprocess
import random

STUDENT_ID = 11806768

def check_list(student, list_password):
    proc = subprocess.Popen(["./unlock_mac", str(student)] + list_password, stdout=subprocess.PIPE)
    results = []
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        results.append(float(str(line).split("\\t")[1].split("\\n")[0]))
    return results


a = check_list(STUDENT_ID, ["ALGOGEN", "PASSWORD"])

print(a)

# roulette pondérée
roulette = []
#Porbabilité de Crossover
crossoverPropbabilty = 0,2

def generatePopulation():
    #TODO
    return population

# tant que taille nouvelle population < population
# TODO : exploitation
# choisir premier parent au "roulette pondéré"
# choisir deuxième parent "roulette pondéré"
def exploitation():

    parent1 = roulette[0]
    parent2 = roulette[1]
    return parent1, parent2

    # Si random() < P(cross_over) (cross_over = 2)
    # cross-over des deux parents et l'ajouter
    if random.random() < crossoverPropbabilty:
        cross = crossover(parent1, parent2)
        population.add(cross)

# TODO : exploration
#  faire muter premier parent et l'ajouter
#  faire muter deuxième parent et l'ajouter
def exploitation(parent1, parent2):
    mutate(parent1)
    population.addParent(parent1)
    mutate(parent2)
    population.addParent(parent2)


    # si taille population == taille nouvelle_population
    # population = nouvelle population
    if len(population) == len(newPopulation):
        population = newPopulation

def mutate(parent):
    # TODO

def crossover(parent1, parent2):
    # TODO

# Génération aléatoire d'une population
population = generatePopulation()
while 1 not in check_list(STUDENT_ID, population):
    newPopulation = []
    if len(newPopulation) < len(population):
        exploitation()


print(population)