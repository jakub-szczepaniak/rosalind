import unittest
from unittest.mock import Mock
import requests

class TestAccessinguniProt(unittest.TestCase):
    @unittest.skip('for now')
    def test_getting_protein_info(self):
        protein_url = BASE_UNIPROT_REQUEST.format('P20840_SAG1_YEAST')
        r = requests.get(protein_url)
        print(r.text)

    def test_accessor_invokes_get_from_driver(self):
        mock = Mock()
        test_subject = UniprotAccessor(mock)
        
        test_subject.get_fasta('ABCS')
        
        mock.get.assert_called_with("https://www.uniprot.org/uniprot/ABCS.fasta")

BASE_UNIPROT_REQUEST = "https://www.uniprot.org/uniprot/{}.fasta"


class UniprotAccessor():
    def __init__(self, driver):
        self._driver = driver
        self.BASE_UNIPROT_REQUEST = "https://www.uniprot.org/uniprot/{}.fasta"
    def get_fasta(self, uniprot_id):
        self._driver.get(self.BASE_UNIPROT_REQUEST.format(uniprot_id))