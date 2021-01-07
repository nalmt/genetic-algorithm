# coding : utf8
# !/usr/bin/env python
#import demo

from blackbox import check

STUDENT_ID = 11806768

def check_list(student, list_password):
    results = []
    for password in list_password:
        results.append(check(student, password))
    return results

a = check_list(STUDENT_ID, ["ALGOGEN", "PASSWORD"])

print(a)

#Génération aléatoire d'une population

population = generate_population()

while 1 not in check_list(STUDENT_ID, population):
    nouvelle_population = []

    # tant que taille nouvelle population < population
    # TODO : exploitation
    # choisir premier parent au "roulette pondéré"
    # choisir deuxième parent "roulette pondéré"

    # Si random() < P(cross_over) (cross_over = 2)
        #cross-over des deux parents et l'ajouter

    # TODO : exploration
    #  faire muter premier parent et l'ajouter
    #  faire muter deuxième parent et l'ajouter
    
    # si taille population == taille nouvelle_population
    # population = nouvelle population

print(population)