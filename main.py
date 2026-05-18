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
                time.sleep(1)
                print(o2.info)
                time.sleep(1)
            case "2": 
                print("== Distribusi Oksigen dan Energi ==")
                try:                    
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
                    time.sleep(1)
                except ValueError:
                    print("Input tidak valid. Pastikan memasukkan angka.")
                    continue
            case "3":                  
                print("== Mode Darurat ==")
                darurat = input("Aktifkan mode darurat? (y/n): ")
                if darurat.lower() == 'y':
                    o1.darurat()
                    time.sleep(1)
                    o2.darurat()
                    print("Mode darurat diaktifkan! Semua sistem berjalan dengan prioritas tinggi!")
                    time.sleep(1)
                elif darurat.lower() == 'n':
                    print("Mode darurat dibatalkan.")
                else:
                    print("Input tidak valid. Mode darurat dibatalkan.")
            case "4":
                print("== Cek Kondisi Aman ==")
                o1.kondisi_aman()
                time.sleep(1)
                o2.kondisi_aman()
                time.sleep(1)
            case "5":                  
                print("Keluar dari program. Sampai jumpa!")
                time.sleep(1)
                break
if __name__ == "__main__":
    main()