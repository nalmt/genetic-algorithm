import string
import random

alphabets = list(string.ascii_uppercase)
numbers = list(range(10))
mutateProbabity = 0.5
addDeleteProbabilty = 0.2
g = "1234567AZERTYUJ"

def deleteGene(geneIndex, genotype):
    if len(genotype) >= 13:
        print("deleting gene :")
        print("deleting " + genotype[geneIndex])
        return genotype[:geneIndex] + genotype[geneIndex + 1:]

def addGene(genotype):
    if len(genotype) <= 17:
        print("adding gene :")
        rand = random.choice([1, 2])
        if rand == 1:
            randomAlphabet = random.choice(alphabets)
            genotype.join(randomAlphabet)
            print("added " + randomAlphabet)
        else:
            randomNumber = str(random.choice(numbers))
            genotype.join(randomNumber)
            print("added " + randomNumber)
        return genotype

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
                # muter le gene vers l'alphabet précédent (Z)
                return alphabets[25]

        # si l'aphabet est un Z
        elif indexAlpha == 25:
            rand = random.choice([1, 2])
            if rand == 1:
                # muter le gene vers l'alphabet suivant (A)
                return alphabets[0]
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
            print(geneIndex)
            gene = genotype[geneIndex]

            if random.random() < mutateProbabity:
                print("mutating gene " + str(gene))
                newGene = str(mutate(gene))
                print("To " + newGene)
                genotype = genotype[:geneIndex] + str(newGene) + genotype[geneIndex + 1:]


            if random.random() < addDeleteProbabilty:
                deleteIndex = random.randrange(0, len(genotype) - 1, 1)
                rand = random.choice([1, 2])
                if rand == 1:
                    genotype = addGene(genotype)
                else:
                    genotype = deleteGene(deleteIndex, genotype)

    return genotype

newg = mutateGenotype(g)
print("before mutating : " + g)
print("after mutation : " + newg)
