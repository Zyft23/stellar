class oksigen:
    def __init__(self,tekanan_udara,cadangan_oksigen,oksigen):
        self._tekanan_udara = tekanan_udara
        self.oksigen = oksigen
        self._cadangan_oksigen = cadangan_oksigen
    def info(self):
        print(f"Tekanan udara: {self._tekanan_udara} kPa")
        print(f"Cadangan oksigen: {self._cadangan_oksigen} liter")
        print(f"Oksigen: {self.oksigen} liter")

class laboratorium(oksigen):
    def __init__(self, name):
        super().__init__(name)
    self.energi 
