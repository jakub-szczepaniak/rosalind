import unittest
from strands_collection import StrandsCollection, CollectionNotValid
class TestStrandsConsensusAndProfile(unittest.TestCase):
    def test_collection_of_strands_takes_list_of_items(self):
        with self.assertRaises(CollectionNotValid):
            StrandsCollection([])
    def test_collection_stores_strands(self):
        sample = ['123', '123']
        self.assertEqual(StrandsCollection(sample).strands, sample)

    def test_profile_is_equal_to_when_single_strands(self):
        sample = StrandsCollection(['AGCT'])
        self.assertEqual(sample.consensus, 'AGCT')