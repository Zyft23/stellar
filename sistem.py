from abc import ABC, abstractmethod
class base(ABC):
    def __init__(self, tekanan_udara):
        self.__tekanan_udara = tekanan_udara
    @abstractmethod
    def darurat(self):
        pass
    @abstractmethod
    def kondisi_aman(self):
        pass

class Hunian(base):
    def __init__(self,cadangan_oksigen,oksigen):
        super().__init__(tekanan_udara=101.3)
        self.__oksigen = oksigen
        self.__cadangan_oksigen = cadangan_oksigen
    @property
    def info(self):
        return f"Hunian: Tekanan udara: {self._base__tekanan_udara} kPa, Oksigen: {self.__oksigen} liter, Cadangan Oksigen: {self.__cadangan_oksigen} liter"
    
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
        
        

        print("Sistem darurat hunian diaktifkan!")
    def kondisi_aman(self):
        if self.__tekanan_udara > 110:
            print("Peringatan: Tekanan udara terlalu tinggi!")
        elif self.__tekanan_udara <90:
            print("Peringatan: Tekanan udara terlalu rendah!")
        elif self.__oksigen < 90:
            print("Peringatan: Oksigen hampir habis!")
        else:
            print("Kondisi aman. Tekanan udara dan oksigen dalam batas normal.")
        


class laboratorium(base):
    def __init__(self, energi):
        super().__init__(tekanan_udara=101.3)
        self.energi = energi
    
    def info_energi(self):
        print(f"Energi laboratorium: {self.energi} watt")
    def darurat(self):

        print("Sistem darurat laboratorium diaktifkan!")
    def kondisi_aman(self):
        if self.__tekanan_udara > 110:
            print("Peringatan: Tekanan udara terlalu tinggi!")
        elif self.__tekanan_udara <90:
            print("Peringatan: Tekanan udara terlalu rendah!")
        elif self.__oksigen < 90:
            print("Peringatan: Oksigen hampir habis!")
        else:
            print("Kondisi aman. Tekanan udara dan oksigen dalam batas normal.")
