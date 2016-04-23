from collections import OrderedDict
def count_nucleotides(dataset_file):
    with open(dataset_file, 'r') as data:
        dataset = list(data.read())
        count = OrderedDict()
        count['A'], count['C'], count['G'], count['T'] = 0, 0, 0, 0
        
        for nucleotyde in dataset[:-1]:
            count[nucleotyde] += 1
        
        return " ".join([str(x) for x in count.values()])

if __name__ == "__main__":
    print(count_nucleotides('rosalind_dna.txt'))