from itertools import zip_longest

def main():
    with open('rosalind_prot.txt', 'r') as datafile:
        rna_strand = datafile.read().rstrip()
    with open('output.txt', 'w') as result:
        result.write(encode_protein(rna_strand))


def encode_protein(rna):
    print(len(PROTEINS))
    print(len(CODONS))
    chunks = grouper(list(rna), 3)
    result = []
    for chunk in chunks:
        codon = "".join(chunk)
        result.append(CODONS_MAP[codon])
    return "".join(result)


def grouper(iterable, size):
    args = [iter(iterable)] * size
    return zip_longest(*args)

CODONS = ['UUU', 'UUC', 'UUA', 'UUG',
          'UCU', 'UCC', 'UCA', 'UCG',
          'UAU', 'UAC', 'UAA', 'UAG',
          'UGU', 'UGC', 'UGA', 'UGG',
          'CUU', 'CUC', 'CUA', 'CUG',
          'CCU', 'CCC', 'CCA' , 'CCG',
          'CAU', 'CAC', 'CAA', 'CAG',
          'CGU', 'CGC', 'CGA', 'CGG',
          'AUU', 'AUC', 'AUA', 'AUG',
          'ACU', 'ACC', 'ACA', 'ACG',
          'AAU', 'AAC', 'AAA', 'AAG',
          'AGU', 'AGC', 'AGA', 'AGG',
          'GUU', 'GUC', 'GUA', 'GUG',
          'GCU', 'GCC', 'GCA', 'GCG',
          'GAU', 'GAC', 'GAA', 'GAG',
          'GGU', 'GGC', 'GGA', 'GGG']
PROTEINS = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S',
            'Y', 'Y', '', '', 'C', 'C', '', 'W',
            'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P',
            'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R',
            'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T',
            'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R',
            'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A',
            'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']

CODONS_MAP = dict(zip(CODONS, PROTEINS))

if __name__ == "__main__":
    main()

