import unittest
from grph import Node


class TestOverlappinGrpahs(unittest.TestCase):
    def test_calculate_prefix_for_O_3(self):
        test_node = Node('some_id', 'abdadbbdbd')

        self.assertEqual('abd', test_node.prefix)

    def test_calculate_sufix_for_O_3(self):
        test_node = Node('some_id', 'abdadbbdbd')
        self.assertEqual('dbd', test_node.sufix)

    def test_nodes_overlap(self):
        first_node = Node('some_id', 'adbadbbdd')
        second_node = Node('other_id', 'bddadwewee')

        self.assertTrue(first_node.overlap(second_node))

    def test_return_false_when_2nd_operand_null(self):
        first_node = Node('some_id', 'asljhd')

        self.assertFalse(first_node.overlap(None))

    def test_overlap_sample_examples(self):
        first_node = Node('Rosalind_0498', 'AAATAAA')
        second_node = Node('Rosalind_2391', 'AAATTTT')

        self.assertTrue(first_node.overlap(second_node))
