import unittest
from itertools import zip_longest

class TestSharedMotifDatasetExtraction(unittest.TestCase):
    def test_loading_dataset(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        self.assertEqual(1800, len(dataset))

    def test_merging_strands_from_dataset(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        strands = parse_dataset(dataset)
        self.assertEqual(100, len(strands))

class TestSharedPrepareStrandCandidates(unittest.TestCase):
    def test_prepare_substrand_set(self):
        sample_strand = 'abca'
        result = {'b', 'c', 'ab', 'ca', 'abc', 'a', 'abca', 'bc', 'bca'}

        self.assertEqual(result, prepare_set(sample_strand))

    def test_for_sample_data(self):
        dataset = load_dataset('rosalind_lcsm.txt')
        strands = parse_dataset(dataset)
        found = find_motif(strands)
        self.assertEqual('ABC', found)
    
    def test_verify_contained_all_returns_false(self):
        strands = ['GATTACA', 'TAGACCA', 'ATACA']
        self.assertEqual(False, motif_in_all_strands('GATTA', strands))

    def test_verify_contained_all_returns_true(self):
        strands = ['GATTACA', 'TAGACCA', 'ATACA']
        self.assertEqual(True, motif_in_all_strands('TA', strands))



        
def find_motif(strands):
    reference = sorted(prepare_set(strands[0]), reverse=True)
    for motif in reference:
        if motif_in_all_strands(motif, strands):
            return motif
def motif_in_all_strands(motif, strands):
    return all(motif in strand for strand in strands)

def prepare_set(input_string):
  length = len(input_string)
  return set([input_string[i:j+1] for i in range(length) for j in range(i, length)])
        
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
