import unittest
import itertools

class TestPermutations(unittest.TestCase):
    def test_number_of_permutations(self):
        n = 2
        self.assertEqual(2, perm_count(n))

    def test_number_of_permutations(self):
        self.assertEqual(5040, perm_count(7))

    def test_get_all_permutations_for_n_3(self):
        dataset = range(1, 4)
        result = list(itertools.permutations(dataset))
    def test_real_data(self):
        test_number = 7
        dataset = range(1, 1 + test_number)
        result = list(itertools.permutations(dataset))
        save_result(perm_count(test_number), result)

def format_result(line):
    result = "".join(str(line))
    return result.replace(',', '').replace('(', '').replace(')', '')

def save_result(perm_count, permutations):
    with open('result.txt', 'w') as output:
            output.write(str(perm_count))
            output.write('\n')
            for line in permutations:
                output.write(format_result(line))
                output.write('\n')

class TestFactorial(unittest.TestCase):
    def test_it_is_1_for_0(self):
        self.assertEqual(1, factorial(0))

    def test_it_is_1_for_1(self):
        self.assertEqual(1, factorial(1))

    def test_it_is_6_for_3(self):
        self.assertEqual(6, factorial(3))


def perm_count(n):
    return int(factorial(n)/factorial(0))

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)