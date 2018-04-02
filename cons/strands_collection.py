class StrandsCollection:
    def __init__(self, list_of_strands):
        self.validate(list_of_strands)
        length = len(list_of_strands[0])

        self.strands = list_of_strands
        self._consensus = self.strands[0]
        
        self._profile = {'A':[0]*length, 'C': [0]*length, 'G':[0]*length, 'T':[0]*length}

    def validate(self, list_of_strands):
        if len(list_of_strands) == 0:
            raise CollectionNotValid('Cannot be empty!')
        length = len(list_of_strands[0])
        if any(len(strand) != length for strand in list_of_strands):
            raise CollectionNotValid('Strands have to have same length!')

    @property
    def consensus(self):
        return self._consensus
    @property
    def profile(self):
        self.calculate_profile()
        return self._profile

    def calculate_profile(self):
        for index, allel in enumerate(self.strands[0]):
            if allel == 'A':
                self._profile['A'][index] +=1
            elif allel == 'C':
                self._profile['C'][index] +=1
            elif allel == 'G':
                self._profile['G'][index] +=1
            elif allel == 'T':
                self._profile['T'][index] +=1

class CollectionNotValid(Exception):
    pass