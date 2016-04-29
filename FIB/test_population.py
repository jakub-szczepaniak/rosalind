import unittest
from population import population


class TestWascallyWabbits(unittest.TestCase):

    def test_population_is_0_after_0_months(self):
        self.assertEqual(0, population(0))

    def test_population_is_1_after_1_month(self):
        self.assertEqual(1, population(1))

    def test_population_is_1_after_2_months(self):
        self.assertEqual(1, population(2))

    def test_population_is_2_after_3_months(self):
        self.assertEqual(2, population(3))

    def test_population_is_5_after_5_months(self):
        self.assertEqual(5, population(5))

    def test_population_is_19_after_5_months_and_with_offspring_3(self):
        self.assertEqual(19, population(5, 3))

    @unittest.skip('too long to run')
    def test_my_input(self):
        self.assertEqual(1, population(36, 4))
