

def dna2rna(filename):
    with open(filename, 'r') as data_file:
        dataset = data_file.read()
        return (dataset.replace('T', 'U'))
if __name__ == "__main__":
    print (dna2rna('rosalind_rna.txt'))