# coding : utf8
# !/usr/bin/env python
import numpy as np
import random

def roulette_wheel(population, weights, number_to_select):
    return random.choices(population, weights, k=number_to_select)

def sortSecond(val):
    return val[1]

def roulette_wheel_by_linear_rank(population, weights, number_to_select):
    population_sorted_by_score = []
    for i in range(0, len(population)):
        population_sorted_by_score.append([population[i], weights[i]])

    population_sorted_by_score.sort(key = sortSecond)

    weights_by_rank = []
    N = len(population_sorted_by_score)

    for i in range(0, N):
        r = i+1
        w = (2/(N * (N - 1))) * (r - 1)
        weights_by_rank.append(w)

    new_population = [item[0] for item in population_sorted_by_score]

    return random.choices(new_population, weights_by_rank, k=number_to_select)

def roulette_wheel_by_exponential_rank(population, weights, number_to_select, c):
    population_sorted_by_score = []
    for i in range(0, len(population)):
        population_sorted_by_score.append([population[i], weights[i]])

    population_sorted_by_score.sort(key = sortSecond)

    weights_by_rank = []
    N = len(population_sorted_by_score)

    for i in range(0, N):
        r = i+1
        w = ((c - 1)/(c**N - 1)) * (c**(N - r))
        weights_by_rank.append(w)

    new_population = [item[0] for item in population_sorted_by_score]

    return random.choices(new_population, weights_by_rank, k=number_to_select)

# https://gist.github.com/cvanweelden/4971289
def weighted_sample(weights, sample_size):
    totals = np.cumsum(weights)
    sample = []
    for i in range(sample_size):
        rnd = random.random() * totals[-1]
        idx = np.searchsorted(totals,rnd,'right')
        sample.append(idx)
        totals[idx:] -= weights[idx]
    return sample

def roulette_wheel_by_exponential_rank_sampled(population, weights, number_to_select, c):
    population_sorted_by_score = []
    for i in range(0, len(population)):
        population_sorted_by_score.append([population[i], weights[i]])

    population_sorted_by_score.sort(key = sortSecond)

    weights_by_rank = []
    N = len(population_sorted_by_score)

    for i in range(0, N):
        r = i+1
        w = ((c - 1)/(c**N - 1)) * (c**(N - r))
        weights_by_rank.append(w)

    new_population = [item[0] for item in population_sorted_by_score]
    ws = weighted_sample(weights_by_rank, len(new_population))

    selection = []
    for i in range(0, number_to_select):
        selection.append(new_population[ws[i]])

    return selection
