import unittest
from subs import locations

class TestFindingMotifs(unittest.TestCase):
    def test_check_if_it_works(self):
        self.assertEquals(True, True)

    def test_calculate_interface(self):
        strand = "GATATATGCATATACTT"
        substrand = "ATAT"
        self.assertEqual([2, 4, 10], locations(strand, substrand))

    def test_position_is_one_for_2_equal_strands(self):
        strand = "ATAT"

        self.assertEqual([1], locations(strand, strand))

    def test_single_item_in_the_strand(self):
        strand = "ATCG"

        self.assertEqual([2], locations(strand, 'T'))

    def test_single_items_twice_in_the_strand(self):
        strand = "ATACG"

        self.assertEqual([1, 3], locations(strand, 'A'))
