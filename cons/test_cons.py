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
    def test_only_AGCT_characters_are_allowed(self):
        pass
    def test_cons_calc_for_ACGT_AGTC(self):
        sample = StrandsCollection(['ACGT', 'AGTC'])
        a = sample.consensus

    def test_cons_calc_for_sample_strands(self):
         strands = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
         sample = StrandsCollection(strands)

         self.assertEqual('ATGCAACT', sample.consensus)

    def test_profile_of_2_strands(self):
        sample = StrandsCollection(['AGCT', 'AGCT'])
        self.assertEqual(sample.profile, {'A':[2,0,0,0], 'C':[0, 0, 2, 0], 'G': [0, 2, 0, 0], 'T': [0, 0, 0, 2]})
    
    def test_profile_of_sample_strands(self):
        strands = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']

        sample = StrandsCollection(strands)
        sample_profile = {
            'A':[5, 1, 0, 0, 5, 5, 0, 0],
            'C':[0, 0, 1, 4, 2, 0, 6, 1],
            'G':[1, 1, 6, 3, 0, 1, 0, 0], 
            'T':[1, 5, 0, 0, 0, 1, 1, 6]
        }
        self.assertEqual(sample_profile, sample.profile)
    
    def test_pretty_print_of_consensus_and_profile(self):
        strands = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
        consensus = 'ATCCAGCT'

        expected = '''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
        self.assertEqual(expected, StrandsCollection(strands).pprint())
    @unittest.skip('for now')
    def test_on_sample_dataset(self):
        dataset = load_dataset('sample.txt')
        strands = parse_dataset(dataset)
        sample = StrandsCollection(strands)
        sample.pprint()
    
    
    def test_on_real_dataset(self):
        dataset = load_dataset('rosalind_cons.txt')
        strands = extract_strands(dataset)
        
        sample = StrandsCollection(list(strands.values()))
        result = sample.profile
        result = sample.consensus
        save_result(sample.pprint())

    def test_getting_key_indexes(self):
        dataset = load_dataset('rosalind_cons.txt')
        key_indexes = get_key_indexes(dataset)
        self.assertEqual([0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170], key_indexes)

    @unittest.skip('for now')
    def test_getting_key_indexes_pairs(self):
        dataset = load_dataset('rosalind_cons.txt')
        key_indexes = get_key_indexes(dataset)
        for start, end in get_start_end_indexes(key_indexes):
            print("{}:{}".format(start, end))

def extract_strands(dataset):
    result = {}
    key_indexes = get_key_indexes(dataset)
    for start, end in get_start_end_indexes(key_indexes):
        result[dataset[start]] = "".join(dataset[start+1:end])
    return result

def get_key_indexes(dataset):
    result = [index for index, line in enumerate(dataset) if line.startswith('>')]
    result.append(len(dataset))
    return result

def get_start_end_indexes(indices):
    for i in range(0, len(indices)-1):
        yield (indices[i], indices[i+1])

def load_dataset(filename):
    all_lines = []
    with open(filename, 'r') as dataset:
        for line in dataset.readlines():
            all_lines.append(line.rstrip())
    return all_lines

def save_result(dataset):
    with open('result.txt', 'w') as target:
        for line in dataset:
            target.write(line)

