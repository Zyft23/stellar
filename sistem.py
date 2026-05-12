class base:
    def __init__(self):
    def
    pass

class Hunian(base):
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
            print("distribusi oksigen berhasil !")


class laboratorium(Hunian):
    def __init__(self, energi):
        super().__init__( 101.3, 1000, 0)
        self.energi = energi
    
    def info_energi(self):
        print(f"Energi laboratorium: {self.energi} watt")
 

