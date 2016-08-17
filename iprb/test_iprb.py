import unittest
from iprb import Organism

class TestOrganism(unittest.TestCase):

    def setUp(self):
        pass

    def test_organism_can_have_2_factors(self):

        subject = Organism(True, False)

        self.assertEqual(True, subject.factor_1())
        self.assertEqual(False, subject.factor_2())
