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
        mock.get.return_value.status_code=200
        test_subject = UniprotAccessor(mock)
        
        test_subject.get_fasta('ABCS')
        
        mock.get.assert_called_with("https://www.uniprot.org/uniprot/ABCS.fasta")

    def test_accessor_get_result_has_text_attribute(self):
        mock = Mock()
        mock.get.return_value.text = '>AFSFG'
        mock.get.return_value.status_code=200

        test_subject = UniprotAccessor(mock)
        result = test_subject.get_fasta('ABCS')
        self.assertEqual('>AFSFG', result)

    def test_accessor_throws_exception_when_status_not_200(self):
        mock = Mock()
        mock.get.return_value.status_code = 404

        with self.assertRaises(UniprotException):
            test_subject = UniprotAccessor(mock)
            test_subject.get_fasta('ABCS')
    
    def test_getting_list_of_fastas(self):
        accessor = UniprotAccessor(requests)
        result = accessor.get_list_of_fastas(['A2Z669','B5ZC00','P07204_TRBM_HUMAN','P20840_SAG1_YEAST'])
        print(result)


BASE_UNIPROT_REQUEST = "https://www.uniprot.org/uniprot/{}.fasta"

class UniprotException(Exception):
    pass

class UniprotAccessor():
    def __init__(self, driver):
        self._driver = driver
        self.BASE_UNIPROT_REQUEST = "https://www.uniprot.org/uniprot/{}.fasta"
    def get_fasta(self, uniprot_id):
        result = self._driver.get(self.BASE_UNIPROT_REQUEST.format(uniprot_id))
        if result.status_code != 200:
            raise UniprotException('Connection failed')
        return result.text
    def get_list_of_fastas(self,list_of_ids):
        return [self.get_fasta(item_id) for item_id in list_of_ids]