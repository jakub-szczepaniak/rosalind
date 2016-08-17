import unittest
from iprb import Organism

class TestOrganism(unittest.TestCase):

    def setUp(self):
        pass

    def test_organism_can_have_1_factor(self):

        subject = Organism(True)

        self.assertEqual(True, subject.factor_1())