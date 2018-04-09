import unittest
import requests

class TestAccessinguniProt(unittest.TestCase):
    def test_getting_protein_info(self):
        protein_url = BASE_UNIPROT_REQUEST.format('P20840_SAG1_YEAST')
        r = requests.get(protein_url)
        print(r.text)

BASE_UNIPROT_REQUEST = "https://www.uniprot.org/uniprot/{}.fasta"
