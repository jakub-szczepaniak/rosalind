class StrandsCollection:
    def __init__(self, list_of_strands):
        self.validate(list_of_strands)

        length = len(list_of_strands[0])
        self.strands = list_of_strands
        self._consensus = self.strands[0]
        self._profile = self.empty_profile(length)

    def validate(self, list_of_strands):
        if len(list_of_strands) == 0:
            raise CollectionNotValid('Cannot be empty!')
        length = len(list_of_strands[0])
        if any(len(strand) != length for strand in list_of_strands):
            raise CollectionNotValid('Strands have to have same length!')
    def empty_profile(self, length):
       return {'A':[0]*length, 'C': [0]*length, 'G':[0]*length, 'T':[0]*length}        
    @property
    def consensus(self):
        return self._consensus
    @property
    def profile(self):
        self._profile = self.empty_profile(len(self.strands[0]))
        self.calculate_profile()
        return self._profile

    def calculate_profile(self):
        for strand in self.strands:
            for index, allel in enumerate(strand):
                self._profile[allel][index] +=1
    def pprint(self):
        result = self._consensus + '\n' 
        
        for key in sorted(self.profile.keys()):
            as_string = [str(val) for val in self.profile[key]]    
            line = "{}: {}\n".format(key, " ".join(as_string))
            result+=line

        return result

class CollectionNotValid(Exception):
    pass