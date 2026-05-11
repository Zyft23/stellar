class oksigen:
    def __init__(self, name):
        self._tekanan_udara = 0
        self._cadangan_oksigen = 0
    @property
    def tekanan_udara(self):
        return self._tekanan_udara
    @property
    def cadangan_oksigen(self):
        return self._cadangan_oksigen
    @tekanan_udara.setter
    def tekanan_udara(self, value):
        self._tekanan_udara = value
    @cadangan_oksigen.setter
    def cadangan_oksigen(self, value):
        self._cadangan_oksigen = value

class laboratorium(oksigen):
    def __init__(self, name):
        super().__init__(name)
        self._tekanan_udara = 100
        self._cadangan_oksigen = 1000
