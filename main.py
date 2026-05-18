from sistem import laboratorium, Hunian, base
import time

def main():
    while True:
        print("== Stellar base ==")
        print("1. Cek Status")
        print("2. Distribusi Oksigen dan energi")
        print("3. jalankan mode darurat")
        print("4. Cek Kondisi Aman")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")
        match pilihan:
            case "1":        
                print("== Status ==")
                print(Hunian.info())
                print(laboratorium.info_energi())
            case "2": 
                print("== Distribusi Oksigen dan Energi ==")
                distribusi_oksigen = int(input("Masukkan jumlah oksigen yang akan didistribusikan (liter): "))
                Hunian.distribusi_oksigen = distribusi_oksigen
                time.sleep(3) 
                print("Distribusi oksigen dan energi sedang berlangsung...")
            case "3":                  
                print("== Mode Darurat ==")
                darurat = input("Aktifkan mode darurat? (y/n): ")
                if darurat.lower() == 'y':
                    Hunian.darurat()
                    laboratorium.darurat()
                print("Mode darurat diaktifkan! Semua sistem berjalan dengan prioritas tinggi!")
            case "4":
                print("== Cek Kondisi Aman ==")
                Hunian.kondisi_aman()
                laboratorium.kondisi_aman()
            case "5":                  
                print("Keluar dari program. Sampai jumpa!")
                break