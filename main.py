from sistem import RuangOksigen, laboratorium
modul = {
    "ruang1": RuangOksigen(tekanan_udara=101.3, cadangan_oksigen=500, oksigen=300)
         }
def main():
    while True:
        print("== Stellar base ==")
        print("1. Cek Status")
        print("2. Distribusi Oksigen dan energi")
        print("3. Tambah modul")
        print("4. jalankan mode darurat")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")
        match pilihan:
            case "1":        
                print("== Status ==")
                
            case "2": 
                print("== Distribusi Oksigen dan Energi ==")
                print("Distribusi oksigen dan energi sedang berlangsung...")
            case "3":
                print("== Tambah Modul ==")
                print("Modul baru sedang ditambahkan...")
            case "4":                  
                print("== Mode Darurat ==")
                print("Mode darurat diaktifkan! Semua sistem berjalan dengan prioritas tinggi!")
            case "5":                  
                print("Keluar dari program. Sampai jumpa!")
                break