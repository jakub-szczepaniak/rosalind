class Organism():
    def __init__(self, factor_1, factor_2):
        self._X = factor_1
        self._Y = factor_2

    def factor_1(self):
        return self._X

    def factor_2(self):
        return self._Y


def get_dominant():
    return Organism(True, True)


def get_recessive():
    return Organism(False, False)
