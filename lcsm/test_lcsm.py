import unittest

class TestSharedMotif(unittest.TestCase):
    def test_parsing_input(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        print(dataset)


def load_dataset(filename):
    all_lines = []
    with open(filename, 'r') as dataset:
        for line in dataset.readlines():
            all_lines.append(line.rstrip())
    return all_lines
