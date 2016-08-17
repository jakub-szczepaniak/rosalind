import unittest
from iprb import Organism, get_dominant, get_recessive

class TestOrganism(unittest.TestCase):

    def setUp(self):
        pass

    def test_organism_can_have_2_factors(self):

        subject = Organism(True, False)

        self.assertEqual(True, subject.factor_1())
        self.assertEqual(False, subject.factor_2())

    def test_creating_dominant_organism(self):

        dominant = get_dominant()

        self.assertEqual(True, dominant.factor_1())
        self.assertEqual(True, dominant.factor_2())

    def test_creating_recessive_organism(self):

        recessive = get_recessive()

        self.assertEqual(False, recessive.factor_1())
        self.assertEqual(False, recessive.factor_2())
