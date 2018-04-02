class StrandsCollection:
    def __init__(self, list_of_strands):
        if len(list_of_strands) == 0:
            raise CollectionNotValid('Cannot be empty!')

class CollectionNotValid(Exception):
    pass