import unittest
from prot import encode_protein
class TestProteinMapping(unittest.TestCase):

    def test_full_sample_dataset(self):
        protein = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

        self.assertEqual('MAMAPRTEINSTRING', encode_protein(protein))

if __name__ == "__main__":
    unittest.main()