import pwinput
import os


#DATA PENGGUNA
pengguna = {
    "admin": {
        "password": "chis24",
        "role": "admin"
    },
    "user": {
        "password": "123",
        "role": "user"
    }
}


kontak = {}


#FUNCTION LOGIN
def login():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== LOGIN =====")

    username = input("Pengguna (admin/user): ")
    password = pwinput.pwinput("Password: ")

    if username in pengguna:
        if pengguna[username]["password"] == password:
            print("Login berhasil!")
            print("Role:", pengguna[username]["role"])
            return pengguna[username]["role"]
        else:
            print("Password salah!")
            return None
    else:
        print("Pengguna tidak ditemukan!")
        return None


#FUNCTION TAMBAH KONTAK
def tambah_kontak():
    os.system("cls" if os.name == "nt" else "clear")
    nama = input("Masukkan nama: ")

    if nama == "":
        print("Nama tidak boleh kosong!")
        return

    if nama in kontak:
        print("Kontak sudah ada!")
        return

    nomor = input("Masukkan nomor HP: ")

    if nomor == "":
        print("Nomor HP tidak boleh kosong!")
        return

    kontak[nama] = nomor
    print("Kontak berhasil ditambahkan!")


#FUNCTION LIHAT KONTAK
def lihat_kontak():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== DAFTAR KONTAK =====")

    if kontak == {}:
        print("Belum ada kontak.")
    else:
        for nama, nomor in kontak.items():
            print("Nama :", nama)
            print("Nomor:", nomor)
            print("-----------------")


#FUNCTION UBAH KONTAK
def ubah_kontak():
    os.system("cls" if os.name == "nt" else "clear")
    nama_lama = input("Masukkan nama kontak yang ingin diubah: ")

    if nama_lama in kontak:
        nama_baru = input("Masukkan nama baru: ")
        nomor_baru = input("Masukkan nomor HP baru: ")

        if nama_baru == "" or nomor_baru == "":
            print("Data tidak boleh kosong!")
        else:
            del kontak[nama_lama]
            kontak[nama_baru] = nomor_baru
            print("Kontak berhasil diubah!")
    else:
        print("Kontak tidak ditemukan!")


#FUNCTION HAPUS KONTAK
def hapus_kontak():
    os.system("cls" if os.name == "nt" else "clear")
    nama = input("Masukkan nama kontak yang ingin dihapus: ")

    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan!")


#MENU ADMIN
def menu_admin():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("===== MENU ADMIN =====")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Ubah Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        pilihan = input("Pilih (1-5): ")

        if pilihan == "1":
            tambah_kontak()

        elif pilihan == "2":
            lihat_kontak()

        elif pilihan == "3":
            ubah_kontak()

        elif pilihan == "4":
            hapus_kontak()

        elif pilihan == "5":
            print("Keluar dari menu admin.")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")


#MENU USER
def menu_user():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("===== MENU USER =====")
        print("1. Lihat Kontak")
        print("2. Keluar")

        pilihan = input("Pilih (1-2): ")

        if pilihan == "1":
            lihat_kontak()

        elif pilihan == "2":
            print("Keluar dari menu user.")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-2.")


#MENU UTAMA
def main():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("INFO KONTAK")

        role = login()

        if role == "admin":
            menu_admin()

        elif role == "user":
            menu_user()

        else:
            print("Login gagal.")

        ulang = input("Login kembali? (y/n): ")

        if ulang == "n":
            print("Program selesai.")
            break

        elif ulang != "y":
            print("Pilihan tidak valid. Program selesai.")
            break

main()