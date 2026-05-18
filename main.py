from sistem import laboratorium, Hunian
import time
o1 = Hunian(cadangan_oksigen=60, oksigen=60)
o2 = laboratorium(energi=40,cadangan_energi=60)
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
                print(o1.info)
                print(o2.info)
            case "2": 
                print("== Distribusi Oksigen dan Energi ==")
                distribusi_oksigen = int(input("Masukkan jumlah oksigen yang akan didistribusikan (liter): "))
                o1.distribusi_oksigen = distribusi_oksigen
                distribusi_energi = int(input("Masukkan jumlah energi yang akan didistribusikan (kWh): "))
                o2.distribusi_energi = distribusi_energi
                print("Distribusi oksigen dan energi sedang berlangsung.")
                time.sleep(1) 
                print("Distribusi oksigen dan energi sedang berlangsung..")
                time.sleep(1)
                print("Distribusi oksigen dan energi sedang berlangsung...")
                time.sleep(1)
                print("Distribusi oksigen dan energi selesai!")
            case "3":                  
                print("== Mode Darurat ==")
                darurat = input("Aktifkan mode darurat? (y/n): ")
                if darurat.lower() == 'y':
                    o1.darurat()
                    o2.darurat()
                print("Mode darurat diaktifkan! Semua sistem berjalan dengan prioritas tinggi!")
            case "4":
                print("== Cek Kondisi Aman ==")
                o1.kondisi_aman()
                o2.kondisi_aman()
            case "5":                  
                print("Keluar dari program. Sampai jumpa!")
                break
if __name__ == "__main__":
    main()