import unittest
from strands_collection import StrandsCollection, CollectionNotValid
class TestStrandsConsensusAndProfile(unittest.TestCase):
    def test_collection_of_strands_takes_list_of_items(self):
        with self.assertRaises(CollectionNotValid):
            StrandsCollection([])