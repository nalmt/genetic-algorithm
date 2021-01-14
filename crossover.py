# coding : utf8
# !/usr/bin/env python

import random
import unittest

def end_crossover(person_1, person_2, index):
    if index >= len(person_1) and index >= len(person_2):
        new_person_1 = person_1
        new_person_2 = person_2
    elif index >= len(person_1) and index < len(person_2):
        # Add to person_1 end of person_2 and remove end of person_2
        new_person_1 = person_1 + person_2[index:]
        new_person_2 = person_2[:index]
    elif index >= len(person_2) and index < len(person_1):
        # Add to person_2 end of person_1 and remove end of person_1
        new_person_1 = person_1[:index]
        new_person_2 = person_2 + person_1[index:]
    else:
        # Exchange end of both
        new_person_1 = person_1[:index] + person_2[index:]
        new_person_2 = person_2[:index] + person_1[index:]
    return new_person_1, new_person_2

def random_crossover(person_1, person_2, number_of_genes_exchanged):
    min_len = min(len(person_1), len(person_2))
    r = random.sample(range(0, min_len), number_of_genes_exchanged)

    for i in r:
        person_1, person_2 = exchange_genes(person_1, person_2, i)
    
    return person_1, person_2

def exchange_genes(person_1, person_2, index):
    if index >= len(person_1) and index >= len(person_2):
        new_person_1 = person_1
        new_person_2 = person_2
    elif index >= len(person_1) and index < len(person_2):
        new_person_1 = person_1 + person_2[index]
        new_person_2 = person_2[:index] + person_2[index + 1:]
    elif index >= len(person_2) and index < len(person_1):
        new_person_1 = person_1[:index] + person_1[index + 1:]
        new_person_2 = person_2 + person_1[index]
    else:
        new_person_1 = person_1[:index] + person_2[index] + person_1[index + 1:]
        new_person_2 = person_2[:index] + person_1[index] + person_2[index + 1:]

    return new_person_1, new_person_2

class TestEndCrossover(unittest.TestCase):
    def test_same_len_1(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = end_crossover(person_1, person_2, 4)

        self.assertEqual(child_1, "ABCDQRS5UVWX")
        self.assertEqual(child_2, "MNO7E1GH2JKL")

    def test_same_len_2(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = end_crossover(person_1, person_2, 11)

        self.assertEqual(child_1, "ABCDE1GH2JKX")
        self.assertEqual(child_2, "MNO7QRS5UVWL")

    def test_same_len_3(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = end_crossover(person_1, person_2, 12)

        self.assertEqual(child_1, "ABCDE1GH2JKL")
        self.assertEqual(child_2, "MNO7QRS5UVWX")

    def test_same_len_4(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = end_crossover(person_1, person_2, 0)

        self.assertEqual(child_1, "MNO7QRS5UVWX")
        self.assertEqual(child_2, "ABCDE1GH2JKL")

    def test_different_len_1(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5"

        child_1, child_2 = end_crossover(person_1, person_2, 4)

        self.assertEqual(child_1, "ABCDQRS5")
        self.assertEqual(child_2, "MNO7E1GH2JKL")

    def test_different_len_2(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5"

        child_1, child_2 = end_crossover(person_1, person_2, 7)

        self.assertEqual(child_1, "ABCDE1G5")
        self.assertEqual(child_2, "MNO7QRSH2JKL")

    def test_different_len_3(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5"

        child_1, child_2 = end_crossover(person_1, person_2, 8)

        self.assertEqual(child_1, "ABCDE1GH")
        self.assertEqual(child_2, "MNO7QRS52JKL")

    def test_different_len_4(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5"

        child_1, child_2 = end_crossover(person_1, person_2, 0)

        self.assertEqual(child_1, "MNO7QRS5")
        self.assertEqual(child_2, "ABCDE1GH2JKL")

    def test_different_len_5(self):
        person_1 = "MNO7QRS5"
        person_2 = "ABCDE1GH2JKL"

        child_1, child_2 = end_crossover(person_1, person_2, 4)

        self.assertEqual(child_1, "MNO7E1GH2JKL")
        self.assertEqual(child_2, "ABCDQRS5")

    def test_different_len_6(self):
        person_1 = "MNO7QRS5"
        person_2 = "ABCDE1GH2JKL"

        child_1, child_2 = end_crossover(person_1, person_2, 7)

        self.assertEqual(child_1, "MNO7QRSH2JKL")
        self.assertEqual(child_2, "ABCDE1G5")

    def test_different_len_7(self):
        person_1 = "MNO7QRS5"
        person_2 = "ABCDE1GH2JKL"

        child_1, child_2 = end_crossover(person_1, person_2, 8)

        self.assertEqual(child_1, "MNO7QRS52JKL")
        self.assertEqual(child_2, "ABCDE1GH")

    def test_different_len_8(self):
        person_1 = "MNO7QRS5"
        person_2 = "ABCDE1GH2JKL"

        child_1, child_2 = end_crossover(person_1, person_2, 0)

        self.assertEqual(child_1, "ABCDE1GH2JKL")
        self.assertEqual(child_2, "MNO7QRS5")

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

    def test_exchange_exceeds_len(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1))

        self.assertEqual(child_1, "ABCDE1GH2JKL")
        self.assertEqual(child_2, "MNO7QRS5UVWX")

    def test_exchange_letter_number(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, 3)

        self.assertEqual(child_1, "ABC7E1GH2JKL")
        self.assertEqual(child_2, "MNODQRS5UVWX")

    def test_exchange_different_len(self):
        person_1 = "ABCDE1GH2JKLM"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 2)

        self.assertEqual(child_1, "ABCDE1GH2JKXM")
        self.assertEqual(child_2, "MNO7QRS5UVWL")

    def test_exchange_different_len_exceeds_1(self):
        person_1 = "ABCDE1GH2JKLM"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 1)

        self.assertEqual(child_1, "ABCDE1GH2JKL")
        self.assertEqual(child_2, "MNO7QRS5UVWXM")

    def test_exchange_different_len_exceeds_2(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWXM"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 1)

        self.assertEqual(child_1, "ABCDE1GH2JKX")
        self.assertEqual(child_2, "MNO7QRS5UVWLM")

    def test_exchange_different_len_exceeds_3(self):
        person_1 = "ABCDE1GH2JKLMN"
        person_2 = "MNO7QRS5UVWX"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_1) - 2)

        self.assertEqual(child_1, "ABCDE1GH2JKLN")
        self.assertEqual(child_2, "MNO7QRS5UVWXM")

    def test_exchange_different_len_exceeds_4(self):
        person_1 = "ABCDE1GH2JKL"
        person_2 = "MNO7QRS5UVWXMN"

        child_1, child_2 = exchange_genes(person_1, person_2, len(person_2) - 2)

        self.assertEqual(child_1, "ABCDE1GH2JKLM")
        self.assertEqual(child_2, "MNO7QRS5UVWXN")

if __name__ == '__main__':
    unittest.main()
