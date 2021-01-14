# coding : utf8
# !/usr/bin/env python
#import demo
import subprocess
import random
import string

alphabets = list(string.ascii_uppercase)
numbers = list(range(10))
mutateProbabity = 0.2
addDeleteProbabilty = 0.2

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
#  faire muterpremier parent et l'ajouter
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

def deleteGene(genotype, genePosition):
    if len(genotype) >= 13:
        genotype.replace(genePosition, '')

def addGene(genotype):
    if len(genotype) <= 17:
        genotype.join(random.choice(alphabets))

def mutate(gene):
    if gene in alphabets:
        indexAlpha = alphabets.index(gene)
        if indexAlpha not in [0, 25]:
            return random.choice(alphabets[indexAlpha+1],alphabets[indexAlpha-1])
    elif gene in numbers:
        indexNum = numbers.index(gene)
        if indexNum not in [0, 9]:
            return random.choice(numbers[indexNum + 1], numbers[indexNum - 1])

def mutateGenotype(genotype):
  for gene in genotype:
     indexGene = genotype.index(gene)
     if random() < mutateProbabity:
        genotype.replace(indexGene,mutate(gene))
     if random() < addDeleteProbabilty:
        deleteIndex = random.uniform(0, len(genotype) - 1)
        random.choice(addGene(genotype), deleteGene(genotype, deleteIndex))







#Ensuite on a une probabilité de supprimer un gène au hasard et une probabilité d'ajouter un gène au hasard (ces types de mutations s'appliquent uniquement si nous avons 13 à 17 gènes inclus).


def crossover(parent1, parent2):
    #TODO

# Génération aléatoire d'une population
population = generatePopulation()
while 1 not in check_list(STUDENT_ID, population):
    newPopulation = []
    if len(newPopulation) < len(population):
        exploitation()


print(population)