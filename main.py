# coding : utf8
# !/usr/bin/env python
#import demo

from blackbox import check

STUDENT_ID = 11806768

def check_list(list_password):
    results = []
    for password in list_password:
        results.append(check(STUDENT_ID, password))
    return results

# Génération aléatoire d'une population

population = generate_population()

while 1 not in check_list(STUDENT_ID, population):
    nouvelle population = []
    for individu in population:
        # TODO
    population = nouvelle_population

print(population)