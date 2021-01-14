# coding : utf8
# !/usr/bin/env python

import random
import unittest

def end_crossover(person_1, person_2, index):
    if index >= len(person_1) and index >= len(person_2):
        raise Exception("Exchange outside person_1, index = " + str(index_gene_to_exchange) + " len = " + str(len(person_1)))
    elif index >= len(person_1) and index < len(person_2):
        # Add to person_1 end of person_2 and remove end of person_2
    elif index >= len(person_2) and index < len(person_1):
        # Add to person_2 end of person_1 and remove end of person_1
    else:
        # Exchange end of both

def random_crossover(person_1, person_2, number_of_genes_exchanged):
    min_len = min(len(person_1), len(person_2))
    r = random.sample(range(0, min_len), number_of_genes_exchanged)
    
    new_person_1 = person_1
    new_person_2 = person_2
    for i in r:
        new_person_1, new_person_2 = exchange_genes(new_person_1, new_person_2, i)
    
    return new_person_1, new_person_2

def exchange_genes(person_1, person_2, index_gene_to_exchange):
    if index_gene_to_exchange >= len(person_1):
        raise Exception("Exchange outside person_1, index = " + str(index_gene_to_exchange) + " len = " + str(len(person_1)))
    elif index_gene_to_exchange >= len(person_2):
        raise Exception("Exchange outside person_2, index = " + str(index_gene_to_exchange) + " len = " + str(len(person_2)))
    else:
        new_person_1 = person_1[:index_gene_to_exchange] + person_2[index_gene_to_exchange] + person_1[index_gene_to_exchange+1:]
        new_person_2 = person_2[:index_gene_to_exchange] + person_1[index_gene_to_exchange] + person_2[index_gene_to_exchange+1:]

        return (new_person_1, new_person_2)

class TestRandomCrossover(unittest.TestCase):

    def test_exchange_first(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, 0)

        self.assertEqual(child_1, "MBCDE1GH2JKL")
        self.assertEqual(child_2, "ANO7QRS5UVWX")

class TestExchangeGenes(unittest.TestCase):

    def test_exchange_first(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, 0)

        self.assertEqual(child_1, "MBCDE1GH2JKL")
        self.assertEqual(child_2, "ANO7QRS5UVWX")

    def test_exchange_last(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 1)

        self.assertEqual(child_1, "ABCDE1GH2JKX")
        self.assertEqual(child_2, "MNO7QRS5UVWL")

    def test_exchange_exceeds_len(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        with self.assertRaises(Exception) as context:
            exchange_genes(person_1, person_2, len(person_1))

        self.assertEqual('Exchange outside person_1, index = 12 len = 12', str(context.exception))

    def test_exchange_letter_number(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, 3)

        self.assertEqual(child_1, "ABC7E1GH2JKL")
        self.assertEqual(child_2, "MNODQRS5UVWX")

    def test_exchange_different_lens(self):
        person_1 = "ABCDE1GH2JKLM"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 2)

        self.assertEqual(child_1, "ABCDE1GH2JKXM")
        self.assertEqual(child_2, "MNO7QRS5UVWL")

    def test_exchange_different_lens_exceeds_len(self):
        person_1 = "ABCDE1GH2JKLM"
        person_2 = "MNO7QRS5UVWX"

        with self.assertRaises(Exception) as context:
            exchange_genes(person_1, person_2, len(person_1) - 1)

        self.assertEqual('Exchange outside person_2, index = 12 len = 12', str(context.exception))

if __name__ == '__main__':
    #unittest.main()

    print("coucou")
    a1 = "ABC"
    a2 = "DEFG"
    p1, p2, = random_crossover(a1, a2, 2)
    print(p1, p2, a1, a2)
