import unittest
from strands_collection import StrandsCollection
class TestStrandsConsensusAndProfile(unittest.TestCase):
    def test_collection_of_strands_can_be_created(self):
        self.assertEquals(StrandsCollection(), None)