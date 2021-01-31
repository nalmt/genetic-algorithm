# coding : utf8
# !/usr/bin/env python
import string
import random

alphabets = list(string.ascii_uppercase)
numbers = list(range(10))


def addGene():
    rand = random.choice([1, 2])
    if rand == 1:
        randomAlphabet = random.choice(alphabets)
        return randomAlphabet
    else:
        randomNumber = str(random.choice(numbers))
        return randomNumber

def mutate(gene):

    if gene in alphabets:
        indexAlpha = alphabets.index(gene)

        #si l'aphabet n'est ni Z ni A
        if indexAlpha not in [0, 25]:
            rand = random.choice([1, 2])
            if rand == 1:
                #muter le gene vers l'alphabet suivant
                return alphabets[indexAlpha + 1]
            elif rand == 2:
                # muter le gene vers l'alphabet précédent
                return alphabets[indexAlpha - 1]

        #si l'aphabet est un A
        elif indexAlpha == 0:
            rand = random.choice([1, 2])
            if rand == 1:
                # muter le gene vers l'alphabet suivant (B)
                return alphabets[1]
            elif rand == 2:
                # muter le gene vers 9
                return '9'

        # si l'aphabet est un Z
        elif indexAlpha == 25:
            rand = random.choice([1, 2])
            if rand == 1:
                # muter le gene vers 0
                return '0'
            elif rand == 2:
                # muter le gene vers l'alphabet précédent (Y)
                return alphabets[24]

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
                return 'Z'

        elif gene == 9:
            rand = random.choice([1, 2])
            if rand == 1:
                return 'A'
            else:
                return 8

        else:
            return gene


def mutateGenotype(genotype, mutateProbabity, addDeleteProbabilty):
    newGenotype=""
    for geneIndex in range(0, len(genotype)):
      #  print("iteration", geneIndex)
        gene = genotype[geneIndex]

        #mutation
        if random.random() < mutateProbabity:
            newGene = str(mutate(gene))
            #print("mutating gene", gene, "To", newGene)
            newGenotype = newGenotype + newGene
        #sans mutation
        else:
            newGenotype = newGenotype + gene

    #ajout ou suppression de gene
    if random.random() < addDeleteProbabilty:
        rand = random.choice([1, 2])
        lenG = len(newGenotype)
      #  print("apres mutation",lenG)

        if rand == 1:
            if lenG < 18:
                added = addGene()
           #     print("adding gene", added)
                newGenotype = newGenotype + added

        else:
            if lenG >= 13:
               # deleted = newGenotype[-1]
              #  print("deleting gene", deleted)
                #newGenotype = newGenotype[:-1]
                index = random.randint(0, len(newGenotype) - 1)
                newGenotype = newGenotype[:index] + newGenotype[index + 1:]






    return newGenotype




