from abc import ABC, abstractmethod
class base(ABC):
    def __init__(self, tekanan_udara):
        self.__tekanan_udara = tekanan_udara
    @property
    def tekanan_udara(self):
        return self.__tekanan_udara
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
        return f"Hunian: Tekanan udara: {self.tekanan_udara} kPa, Oksigen: {self.__oksigen} liter, Cadangan Oksigen: {self.__cadangan_oksigen} liter"
    
    @property
    def distribusi_oksigen(self):
        return self.__oksigen
    @distribusi_oksigen.setter
    def distribusi_oksigen(self, jumlah):
        if jumlah > self.__cadangan_oksigen:
            print("Tidak cukup cadangan oksigen!")
        else:
            if self.__oksigen + jumlah > 100:
                print("Peringatan: Oksigen akan melebihi batas maksimum!")
            else:
                self.__cadangan_oksigen -= jumlah
                self.__oksigen += jumlah
                print(f"Berhasil")
    def darurat(self):
            print("Sistem darurat hunian diaktifkan!")
    def kondisi_aman(self):
        if self.tekanan_udara > 110:
            print("Peringatan: Tekanan udara terlalu tinggi!")
        elif self.tekanan_udara <90:
            print("Peringatan: Tekanan udara terlalu rendah!")
        elif self.__oksigen < 90:
            print("Peringatan: Oksigen hampir habis!")
        else:
            print("Kondisi aman. Tekanan udara dan oksigen dalam batas normal.")
        


class laboratorium(base):
    def __init__(self, energi,cadangan_energi):
        super().__init__(tekanan_udara=101.3)
        self.energi = energi
        self.__cadangan_energi = cadangan_energi
        
    @property
    def distribusi_energi(self):
        return self.energi
    @distribusi_energi.setter
    def distribusi_energi(self, jumlah):
        if self.energi + jumlah > 100:
            print("Peringatan: Energi akan melebihi batas maksimum!")
        elif jumlah > self.__cadangan_energi:
            print("Tidak cukup cadangan energi!")
        else:
            self.__cadangan_energi -= jumlah
            self.energi += jumlah
            print(f"Berhasil")
    @property
    def info(self):
        return f"Laboratorium: Tekanan udara: {self.tekanan_udara} kPa, Energi: {self.energi} kWh", f"Cadangan Energi: {self.__cadangan_energi} kWh"
    def darurat(self):
        self.energi = 0
        print("Sistem darurat laboratorium diaktifkan! semua energi di buang")
    def kondisi_aman(self):
        if self.tekanan_udara > 110:
            print("Peringatan: Tekanan udara terlalu tinggi!")
        elif self.tekanan_udara < 90:
            print("Peringatan: Tekanan udara terlalu rendah!")
        elif self.energi > 100:
            print("Peringatan: Energi terlalu tinggi!")
        else:
            print("Kondisi aman. Tekanan udara dan Energi dalam batas normal.")
