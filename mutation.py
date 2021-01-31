# coding : utf8
# !/usr/bin/env python
import random
import string
import random

MUTATE_PROBABILITY = 0.2
ADD_DELETE_PROBABILITY = 0.2

alphabet = list(string.ascii_uppercase)
numbers = list(range(10))

def deleteGene(geneIndex, genotype):
    if len(genotype) >= 13:
        return genotype[:geneIndex] + genotype[geneIndex + 1:]

def addGene(genotype):
    if len(genotype) <= 17:
        rand = random.choice([1, 2])
        if rand == 1:
            randomAlphabet = random.choice(alphabet)
            genotype.join(randomAlphabet)
        else:
            randomNumber = str(random.choice(numbers))
            genotype.join(randomNumber)
        return genotype

def mutate(gene):

    if gene in alphabet:
        indexAlpha = alphabet.index(gene)

        #si l'aphabet n'est ni Z ni A
        if indexAlpha not in [0, 25]:
            rand = random.choice([1, 2])
            if rand == 1:
                #muter le gene vers l'alphabet suivant
                return alphabet[indexAlpha + 1]
            elif rand == 2:
                # muter le gene vers l'alphabet précédent
                return alphabet[indexAlpha - 1]

        #si l'aphabet est un A
        elif indexAlpha == 0:
            rand = random.choice([1, 2])
            if rand == 1:
                # muter le gene vers l'alphabet suivant (B)
                return alphabet[1]
            elif rand == 2:
                # muter le gene vers l'alphabet précédent (Z)
                return alphabet[25]

        # si l'aphabet est un Z
        elif indexAlpha == 25:
            rand = random.choice([1, 2])
            if rand == 1:
                # muter le gene vers l'alphabet suivant (A)
                return alphabet[0]
            elif rand == 2:
                # muter le gene vers l'alphabet précédent (Y)
                return alphabet[24]
        else:
            return gene

    elif int(gene) in numbers:
        gene = int(gene)
        if gene not in [0, 9]:
            rand = random.choice([1, 2])
            if rand == 1:
                return gene + 1
            else:
                return gene - 1
        elif gene == 0:
            rand = random.choice([1, 2])
            if rand == 1:
                return 1
            else:
                return 9
        elif gene == 9:
            rand = random.choice([1, 2])
            if rand == 1:
                return 0
            else:
                return 8
        else:
            return gene

def mutateGenotype(genotype):
    for geneIndex in range(0, len(genotype) - 1):
        if geneIndex in range(0, len(genotype) - 1):
            gene = genotype[geneIndex]

            if random.random() < MUTATE_PROBABILITY:
                newGene = str(mutate(gene))
                genotype = genotype[:geneIndex] + str(newGene) + genotype[geneIndex + 1:]

            if random.random() < ADD_DELETE_PROBABILITY:
                deleteIndex = random.randrange(0, len(genotype) - 1, 1)
                rand = random.choice([1, 2])
                if rand == 1:
                    genotype = addGene(genotype)
                else:
                    genotype = deleteGene(deleteIndex, genotype)

    return genotype

# Ensuite on a une probabilité de supprimer un gène au hasard et une probabilité d'ajouter un gène 
# au hasard (ces types de mutations s'appliquent uniquement si nous avons 13 à 17 gènes inclus).
