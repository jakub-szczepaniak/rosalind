import unittest
from itertools import zip_longest

class TestSharedMotif(unittest.TestCase):
    def test_loading_dataset(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        self.assertEqual(1800, len(dataset))

    def test_merging_strands_from_dataset(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        strands = parse_dataset(dataset)
        self.assertEqual(100, len(strands))


def extract_strands_from(dataset):
    for i in range(0, len(dataset), 18):
        yield dataset[i+1:i + 18]

def parse_dataset(dataset):
    return ["".join(strand) for strand in extract_strands_from(dataset)]

def load_dataset(filename):
    all_lines = []
    with open(filename, 'r') as dataset:
        for line in dataset.readlines():
            all_lines.append(line.rstrip())
    return all_lines
