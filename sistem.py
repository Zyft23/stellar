class RuangOksigen:
    def __init__(self,tekanan_udara,cadangan_oksigen,oksigen):
        self.__tekanan_udara = tekanan_udara
        self.__oksigen = oksigen
        self.__cadangan_oksigen = cadangan_oksigen
    def info(self):
        print(f"Tekanan udara: {self.__tekanan_udara} kPa")
        print(f"Cadangan oksigen: {self.__cadangan_oksigen} liter")
        print(f"Oksigen: {self.__oksigen} liter")

    @property
    def distribusi_oksigen(self):
        return self.__oksigen

    @distribusi_oksigen.setter
    def distribusi_oksigen(self, jumlah):
        if jumlah > self.__cadangan_oksigen:
            print("Tidak cukup cadangan oksigen!")
        else:
            self.__cadangan_oksigen -= jumlah
            self.__oksigen += jumlah


class laboratorium(RuangOksigen):
    def __init__(self, energi):
        super().__init__(tekanan_udara=0, cadangan_oksigen=0, oksigen=0) 

