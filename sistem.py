from abc import ABC, abstractmethod
class base(ABC):
    def __init__(self, tekanan_udara):
        self.__tekanan_udara = tekanan_udara
    @abstractmethod
    def darurat(self):
        print("Sistem darurat diaktifkan!")
    pass

class Hunian(base):

    def __init__(self,cadangan_oksigen,oksigen):
        super().__init__(tekanan_udara=101.3)
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
    def darurat(self):
        super().darurat()
        print("Sistem darurat hunian diaktifkan!")


class laboratorium(base):
    def __init__(self, energi):
        super().__init__(tekanan_udara=101.3)
        self.energi = energi
    
    def info_energi(self):
        print(f"Energi laboratorium: {self.energi} watt")
    def darurat(self):
        super().darurat()
        print("Sistem darurat laboratorium diaktifkan!")
 

