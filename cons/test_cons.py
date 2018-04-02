import unittest
from strands_collection import StrandsCollection, CollectionNotValid
class TestStrandsConsensusAndProfile(unittest.TestCase):
    def test_collection_of_strands_takes_list_of_items(self):
        with self.assertRaises(CollectionNotValid):
            StrandsCollection([])
    def test_collection_stores_strands(self):
        sample = ['123', '123']
        self.assertEqual(StrandsCollection(sample).strands, sample)

    def test_consensus_is_equal_to_when_single_strands(self):
        sample = StrandsCollection(['AGCT'])
        self.assertEqual(sample.consensus, 'AGCT')

    def test_profile_is_a_dict_of_list(self):
        sample = StrandsCollection(['AGCT'])

        self.assertEqual(sample.profile, {'A':[1,0,0,0], 'C':[0, 0, 1, 0], 'G': [0, 1, 0, 0], 'T': [0, 0, 0, 1]})

    def test_items_have_the_same_length(self):
        with self.assertRaises(CollectionNotValid):
            StrandsCollection(['ABC', 'C'])
    @unittest.skip('for now')
    def test_only_4_characters_are_allowed(self):
        pass