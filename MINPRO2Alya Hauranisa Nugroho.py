# MINI PROJECT 2 Sistem Manajemen Pemesanan Bouquet Bunga
# Nama: Alya Hauranisa Nugroho
# NIM: 2509116005
# Kelas: Sistem Informasi 2025 (A)

# LIBRARY
from prettytable import PrettyTable
import pwinput

# TUPLEEEE
buket = ("Rosey Rose", "Majestic Lily", "Harmony of Pink Bloom",
        "Rise and Shine", "Daisy Daze", "Beautiful in White", "Tulip in Your Eyes")

addon = ("Bunga Mawar", "Bunga Matahari", "Bunga Lily",
        "Bunga Tulip", "Bunga Daisy", "Tidak Custom")

kertas = ("Putih", "Hitam", "Coklat", "Pink")

status = ("Belum dikerjakan", "Dalam proses pembuatan", "Selesai")

# LIST DENGAN DICTIONARY ORDERAN (isi sementara)
orderan = [
    {"Nama": "Alya", "No HP": "08123456789", "Paket": "Rise and Shine",
    "Add On": "Tidak Custom", "Wrap": "Coklat", "Status": "Dalam proses pembuatan", "Deadline": "25-09-2025"},

    {"Nama": "Kansa", "No HP": "081347110004", "Paket": "Tulip in Your Eyes",
    "Add On": "Bunga Tulip", "Wrap": "Pink", "Status": "Belum dikerjakan", "Deadline": "22-09-2025"},

    {"Nama": "Gita", "No HP": "081122334455", "Paket": "Daisy Daze",
    "Add On": "Tidak Custom", "Wrap": "Hitam", "Status": "Belum dikerjakan", "Deadline": "18-09-2025"},
]

# USERNAME DAN PASSWORD
users = {
    "manager": "bungaku123",
    "karyawan": "caricuan321"
}

# MENU LOGIN SESUAI ROLE (KARYAWAN & MANAGER)
def login():
    print("-----------------------------------------------------------------------------")
    print("Hai floristku! Selamat datang di Sistem Manajemen Pemesanan Bouquet Bunga <3")
    print("-----------------------------------------------------------------------------")
    print("Login dulu ya beb!")

    while True:
        print("\nSiapa kamu?")
        print("1. Manager nih bos")
        print("2. Karyawan senggol dong")
        try:
            pilihanrole = input("Masukkan pilihan (1/2): ")

            if pilihanrole == "1":
                kesempatan = 3
                while kesempatan > 0:
                    pw = pwinput.pwinput("Password Manager: ")
                    if pw == users["manager"]:
                        print("\nHAIIII manager-ku! Login berhasil yaa")
                        return "manager"
                    else:
                        kesempatan -= 1
                        print(f"Password salah. Sisa percobaan: {kesempatan}")
                print("Yahhh.. kesempatan habis :(")
                return None

            elif pilihanrole == "2":
                kesempatan = 3
                while kesempatan > 0:
                    pw = pwinput.pwinput("Password Karyawan: ")
                    if pw == users["karyawan"]:
                        print("\nHAIII karyawan, login berhasil! semangat kerjanya hihi")
                        return "karyawan"
                    else:
                        kesempatan -= 1
                        print(f"Password salah. Sisa percobaan: {kesempatan}")
                print("Yahhh.. kesempatan habis :(")
                return None

            else:
                print("Pilihannya hanya 1 atau 2 beb :)")

        except BaseException:
            print("\nTerjadi kesalahan :(")


# FUNGSI VALIDASI INPUT ANGKA
def val_angka(pesan, max_val):
    while True:
        try:
            pilihan = int(input(pesan))
            if 1 <= pilihan <= max_val:
                return pilihan
            else:
                print(f"Masukkan angka antara 1 sampai {max_val}!")
        except ValueError:
            print("Input tidak valid, masukkan angka!")

# MENU 1 TAMBAH ORDERAN
def tambah_order():
    try:
        nama = input("Nama Pemesan: ")
        nohp = input("No HP: ")

        print("\nPilih paket bouquet!")
        for i, p in enumerate(buket, start=1):
            print(f"{i}. {p}")
        pilpaket = val_angka("Pilihan paket (1-7): ", 7)
        paket = buket[pilpaket-1]

        print("\nPilih custom (+add on) bunga!")
        for i, a in enumerate(addon, start=1):
            print(f"{i}. {a}")
        pilcustom = val_angka("Pilihan add-on (1-6): ", 6) 
        custom = addon[pilcustom-1]

        print("\nWarna wrapping paper:")
        for i, k in enumerate(kertas, start=1):
            print(f"{i}. {k}")
        pilwrap = val_angka("Pilihan warna (1-4): ", 4)
        wrap = kertas[pilwrap-1]

        deadline = input("Tanggal Pengambilan (DD-MM-YYYY): ")

        orderan.append({
            "Nama": nama, "No HP": nohp, "Paket": paket,
            "Add On": custom, "Wrap": wrap,
            "Status": status[0], "Deadline": deadline
        })
        idbaru = len(orderan) 

        print("\nRingkasan Orderan Baru")
        print("-------------------------")
        print(f"ID: {idbaru} \nNama Pemesan: {nama} \nNo HP: {nohp} \nPaket: {paket} \nAdd on: {custom} \nWrapping Paper: {wrap} \nStatus: {status[0]} \nTanggal Pengambilan: {deadline}")
        print("-------------------------")
        print("Orderan baru berhasil ditambahkan YIPIII!")
    except BaseException:
        print("\nTerjadi kesalahan :(")

# MENU 2 MENAMPILKAN DAFTAR ORDERAN
def tampilkan_order():
    if not orderan:  
        print("\nBelum ada orderan, tetap semangat!!")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Detail Pesanan"]

        for id_order, isi in enumerate(orderan, 1):
            detail = (
                f"Nama      : {isi['Nama']}\n"
                f"No HP     : {isi['No HP']}\n"
                f"Paket     : {isi['Paket']}\n"
                f"Add On    : {isi['Add On']}\n"
                f"Wrap      : {isi['Wrap']}\n"
                f"Status    : {isi['Status']}\n"
                f"Deadline  : {isi['Deadline']}\n"
                "----------------------------------"
            )
            table.add_row([id_order, detail])

        print("\nDAFTAR ORDERAN")
        print(table)


# MENU 3 UPDATE STATUS ORDERAN
def update_order():
    if not orderan:                               
        print("\nBelum ada orderan yang bisa diupdate :(")
        return
    tampilkan_order()
    try:
        max_id = len(orderan) 
        noid = val_angka(f"Masukkan ID order yang ingin diupdate: ", max_id)
        index = noid - 1 

        print("\nStatus baru:")
        for i, s in enumerate(status, start=1):
            print(f"{i}. {s}")
        statusbaru = val_angka("Pilih status (1-3): ", 3)
        
        orderan[index]["Status"] = status[statusbaru-1]
        
        print("\nORDERAN YANG TELAH DIUPDATE")
        print("---------------------------")
        print(f"ID: {noid}")
        for k, v in orderan[index].items():
            print(f"{k}: {v}")
        print("---------------------------")
        print("YIPIII Status orderan berhasil diperbarui!")
        
    except BaseException:
        print("\nTerjadi kesalahan :(")

# MENU 4 HAPUS ORDERAN
def hapus_order():
    if not orderan:
        print("\nBelum ada orderan yang bisa dihapus :(")
        return
    tampilkan_order()
    try:
        max_id = len(orderan)  
        id_hapus = val_angka(f"Masukkan ID order yang akan dihapus: ", max_id)
        index = id_hapus - 1  
        orderan.pop(index)  
        if orderan:
            tampilkan_order()
            print("Orderan berhasil dihapus YAAA!")
        else:
            print("\nSekarang tidak ada orderan lagi! :D")
    except BaseException:
        print("\nTerjadi kesalahan :(")

# MENU UTAMA MANAGER
def menu_manager():
    while True:
        try:
            print("\nMENU MANAGER YANG TERSEDIA")
            print("1. Tambah Orderan")
            print("2. Lihat Orderan")
            print("3. Update Status")
            print("4. Hapus Orderan")
            print("5. Keluar >>>")
            pilihan = input("Pilih menu: ")
            if pilihan == "1": 
                tambah_order()
            elif pilihan == "2": 
                tampilkan_order()
            elif pilihan == "3": 
                update_order()
            elif pilihan == "4": 
                hapus_order()
            elif pilihan == "5": 
                break
            else: 
                print("Menu yang kamu pilih tidak valid beb!")
        except BaseException:
            print("\nTerjadi kesalahan :(")

# MENU UTAMA KARYAWAN
def menu_karyawan():
    while True:
        try:
            print("\nMENU KARYAWAN YANG TERSEDIA")
            print("1. Lihat Orderan")
            print("2. Update Status")
            print("3. Keluar >>>")
            pilihan = input("Pilih menu: ")
            if pilihan == "1": 
                tampilkan_order()
            elif pilihan == "2": 
                update_order()
            elif pilihan == "3": 
                break
            else: 
                print("Menu yang kamu pilih tidak valid beb!")
        except BaseException:
            print("\nTerjadi kesalahan :(")

def main():
    role = login()
    if role == "manager":
        menu_manager()
    elif role == "karyawan":
        menu_karyawan()
    else:
        print("\nLogin gagal. Nanti coba lagi ya!")
    print("\nTerima kasih sudah menggunakan layanan kami <3")
main()
