class StrandsCollection:
    def __init__(self, list_of_strands):
        if len(list_of_strands) == 0:
            raise CollectionNotValid('Cannot be empty!')
        self.strands = list_of_strands
        self._consensus = self.strands[0]
        self._profile = {}

    @property
    def consensus(self):
        return self._consensus
    @property
    def profile(self):
        self.calculate_profile()
        return self._profile

    def calculate_profile(self):
        length = len(self.consensus)
        self._profile = {'A':[0]*length, 'C': [0]*length, 'G':[0]*length, 'T':[0]*length}
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