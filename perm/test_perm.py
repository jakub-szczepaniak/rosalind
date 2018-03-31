import unittest

class TestPermutations(unittest.TestCase):
	def test_number_of_permutations(self):
		n = 2
		self.assertEqual(2, perm_count(n))

class TestFactorial(unittest.TestCase):
    def test_it_is_1_for_0(self):
        self.assertEqual(1, factorial(0))

    def test_it_is_1_for_1(self):
        self.assertEqual(1, factorial(1))

    def test_it_is_6_for_3(self):
        self.assertEqual(6, factorial(3))


def perm_count(n):
	return factorial(n)/factorial(0)

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)