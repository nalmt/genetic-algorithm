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


def deleteGene(geneIndex, genotype):
    if len(genotype) >= 13:
        genotype = genotype[:geneIndex] + genotype[geneIndex + 1:]



def addGene(genotype):
    if len(genotype) <= 17:
        genotype.join(random.choice(alphabets))



def mutate(gene):
    if gene in alphabets:
        indexAlpha = alphabets.index(gene)
        if indexAlpha not in [0, 25]:
            rand = random.choice([1, 2])
            if rand == 1:
                return alphabets[indexAlpha + 1]
            else:
                return alphabets[indexAlpha - 1]
        else:
            return gene
    elif gene in numbers:
        indexNum = numbers.index(gene)
        if indexNum not in [0, 9]:
            rand = random.choice([1, 2])
            if rand == 1:
                return numbers[indexNum + 1]
            else:
                return numbers[indexNum - 1]

        else:
            return gene


def mutateGenotype(genotype):
    for geneIndex in range(0, len(genotype) - 1):
        gene = genotype[geneIndex]


        if random.random() < mutateProbabity:
            newGene = mutate(gene)
            genotype = genotype[:geneIndex] + str(newGene) + genotype[geneIndex + 1:]


        if random.random() < addDeleteProbabilty:
            deleteIndex = random.randrange(0, len(genotype) - 1, 1)
            rand = random.choice([1, 2])
            if rand == 1:
                addGene(genotype)
            else:
                deleteGene(deleteIndex, genotype)







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