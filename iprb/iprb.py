class Population():
    def __init__(self, dominant_count, hetero_count, recesive_count):
        self._dominant = dominant_count
        self._hetero = hetero_count
        self.recesive = recesive_count
        self._count = self.count()

    def count(self):
        return self._dominant + self._hetero + self.recesive

    def p_dominant(self):
        return self._dominant/self._count

    def p_hetero(self):
        return self._hetero/self._count

    def p_recesive(self):
        return self.recesive/self._count