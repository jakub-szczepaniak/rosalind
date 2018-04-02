class StrandsCollection:
    def __init__(self, list_of_strands):
        if len(list_of_strands) == 0:
            raise CollectionNotValid('Cannot be empty!')
        self.strands = list_of_strands
        self._consensus = self.strands[0]

    @property
    def consensus(self):
        return self._consensus

class CollectionNotValid(Exception):
    pass