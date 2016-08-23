import unittest
from iprb import Population

class TestPopulation(unittest.TestCase):

    def setUp(self):
        pass

    def test_population_has_several_organisms(self):
        self.assertEqual(7, Population(1, 3, 3).count())

    def test_probability_dominant(self):

        population = Population(1, 3, 3)

        self.assertAlmostEqual(1.0/7.0, population.p_dominant())

    def test_probability_heter(self):

        population = Population(3, 4, 1)
        self.assertAlmostEqual(0.5, population.p_hetero())

    def test_probability_recessive(self):

        population = Population(3, 3, 3)

        self.assertAlmostEqual(0.3333333, population.p_recesive())
