# Minpro-2-DDP-ProgramDaftarKontak
Nama: Sabichisma Sania Rachman <br>
NIM: 2609116013 <br>
Kelas: A <br>

- Penjelasan kode:
1. import pwinput digunakan untuk memasukkan password agar tidak terlihat saat diketik.
2. import os digunakan untuk menjalankan perintah sistem, seperti membersihkan layar.
3. pengguna = {...} merupakan dictionary yang menyimpan data akun.
4. kontak = {} merupakan dictionary kosong untuk menyimpan daftar kontak.
5. def login (): merupakan function untuk login.
6. os.system("cls"...) untuk membersihkan terminal agar program tidak menumpuk.
7. username = input("Pengguna (admin/user): ") untuk memasukkan jenis pengguna.
8. password = pwinput.pwinput("Password: ") untuk memasukkan password dan menggunakan pwinput agar password tidak terlihat saat diketik.
9. def tambah_kontak(): merupakan function untuk menambahkan kontak.
10. kontak[nama] = nomor untuk menambahkan nama dan nomor ke dictioary.
11. return merupakan nilai hasil akhir yang dikirimkan kembali oleh sebuah fungsi setelah tugasnya selesai.
12. def lihat_kontak(): merupakan function untuk menampilkan daftar kontak.
13. for nama, nomor in kontak.items(): untuk melakukan perulangan dan items untuk mengambil kunci (key) dan nilai (value) secara bersamaan dari sebuah dictionary.
14. def ubah_kontak(): merupakan function untuk mengubah daftar kontak.
15. def hapus_kontak(): merupakan function untuk menghapus daftar kontak.
16. def menu_admin(): merupakan function untuk menampilkan menu admin yang memiliki CRUD lengkap.
17. def menu_user(): merupakan function untuk menampilkan menu user yang hanya bisa melihat daftar kontak.
18. while true digunakan untuk terus menampilkan menu.
19. def main(): merupakan menu utama sebelum masuk ke program daftar kontak.

- Flowchart dan penjelasannya: <br>
 1. Mulai <br>
Program dimulai dari simbol Mulai, kemudian melakukan login dengan memilih pengguna dan memasukkan password.
2. Program mengecek role dan menampilkan menu sesuai role pengguna. <br>
Jika admin, program akan menampilkan menu admin: Tambah, lihat, ubah, hapus.
Kemudian pengguna memasukkan pilihan 1–5.
3. Validasi Pilihan Menu
Setelah pilihan dimasukkan, program melakukan pengecekan secara berurutan.
* Jika pilihan = 1 → masuk ke menu Tambah
* Jika pilihan = 2 → masuk ke menu Lihat
* Jika pilihan = 3 → masuk ke menu Ubah
* Jika pilihan = 4 → masuk ke menu Hapus
* Jika pilihan = 5 → program selesai
* Jika bukan 1–5 maka tampil "Pilihan tidak valid", kemudian kembali ke menu.
4. Pilihan 1 – Tambah Kontak
Pengguna memasukkan nama kontak.
Setelah berhasil, muncul:
"Kontak berhasil ditambahkan"
Kemudian program kembali ke menu.
5. Pilihan 2 – Lihat Kontak
Program menampilkan daftar kontak yang tersimpan.
Setelah daftar ditampilkan, alur kembali ke menu.
Jika tidak ada data kontak, program dapat menampilkan informasi bahwa daftar kontak masih kosong.
6. Pilihan 3 – Ubah Kontak
Pengguna memasukkan nama kontak yang ingin diubah.
Program melakukan pengecekan:
Apakah kontak ada?
* Jika tidak ditemukan maka tampilkan "Kontak tidak ditemukan" lalu kembali ke menu.
* Jika ditemukan maka pengguna memasukkan nama dan nomor HP baru.
Data kontak diperbarui dan muncul:
"Kontak berhasil diubah"
Kemudian kembali ke menu utama.
7. Pilihan 4 – Hapus Kontak
Pengguna memasukkan nama kontak yang ingin dihapus.
Program mengecek apakah nama tersebut terdapat dalam daftar.
* Jika tidak ditemukan maka  tampilkan "Kontak tidak ditemukan" lalu kembali ke menu.
* Jika ditemukan maka kontak dihapus.
Setelah berhasil, muncul:
"Kontak berhasil dihapus"
Kemudian program kembali ke menu utama.
8. Pilihan 5 – Keluar
Jika pengguna memilih **5**, program menampilkan:
"Program selesai"
Kemudian program menuju simbol End.
  <img width="1685" height="1662" alt="minpro 2 ddp" src="https://github.com/user-attachments/assets/a2e1f12a-cbc7-42c7-b245-df2c882184ef" />

  
- Output menu login yang dimana kita diminta untuk memasukkan pengguna dan password. <br>
  <img width="295" height="163" alt="Screenshot 2026-10-06 120539" src="https://github.com/user-attachments/assets/1bb21f63-a6ec-4473-b1e3-a81962f1378f" /> <br>
- Output jika login sebagai admin, kita akan diminta untuk memilih menu 1-5. <br>
  <img width="308" height="229" alt="Screenshot 2026-10-06 120553" src="https://github.com/user-attachments/assets/65c5acf3-5107-41dd-8317-63d1af687ca1" /> <br>
- Output jika kita menginput selain 1-5, dan akan diminta input ulang. <br>
  <img width="392" height="395" alt="Screenshot 2026-10-06 120623" src="https://github.com/user-attachments/assets/c8a1308f-47b3-4b10-acf4-47c7a7799185" /> <br>
- Output jika kita memilih pilihan 1, kita akan diminta memasukkan nama dan nomor yang ingin ditambahkan ke kontak. <br>
  <img width="301" height="143" alt="Screenshot 2026-10-06 120741" src="https://github.com/user-attachments/assets/abe5ee44-7433-41b2-ad43-56bf344434d3" /> <br>
- Output setelah menambahkan kontak, kita akan dikembalikan ke menu admin. <br>
  <img width="315" height="295" alt="Screenshot 2026-10-06 120757" src="https://github.com/user-attachments/assets/7102081f-0725-4c3d-bc75-d1b5ed5db5ca" /> <br>
- Output jika kita memilih pilihan 2 yaitu menampilkan daftar kontak. <br>
  <img width="297" height="301" alt="Screenshot 2026-10-06 120826" src="https://github.com/user-attachments/assets/5f38ccb2-db2c-4902-81f3-3fa074eaa0cd" /> <br>
- Output jika kita memilih pilihan 3 yaitu mengubah kontak, kita akan diminta memasukkan nama kontak yang ingin diubah. Jika kontak tidak ditemukan maka tampilannya sebagai berikut. <br>
  <img width="446" height="279" alt="Screenshot 2026-10-06 120851" src="https://github.com/user-attachments/assets/b29838ef-6629-485c-9d9e-9dc5a675bd0d" /> <br>
- Output jika kontak ditemukan maka kita akan diminta untuk memasukkan nama baru dan nomor baru. <br>
  <img width="438" height="310" alt="Screenshot 2026-10-06 120923" src="https://github.com/user-attachments/assets/e2b31639-d981-4d1d-b70c-f8db7d43451d" /> <br>
- Output jika kita memilih pilhan 4 yaitu menghapus kontak, kita akan diminta untuk memasukkan nama kontak yang ingin dihapus. <br>
  <img width="469" height="266" alt="Screenshot 2026-10-06 120949" src="https://github.com/user-attachments/assets/0d42c3b5-5afd-4153-99b3-cd4969e51780" /> <br>
- Output jika kita memilih pilihan 5 yaitu keluar dan akan ditanya apakah ingin login lagi dengan menginputkan y/n, dan berikut adalah tampilannya jika kita memilih selain y/n. <br>
 <img width="429" height="263" alt="Screenshot 2026-10-06 121047" src="https://github.com/user-attachments/assets/cee65ece-559b-49dc-9679-cddd69dd69b0" /> <br>
- Output jika kita memasukkan "n" yaitu tidak login lagi, dan program akan selesai. <br>
  <img width="301" height="307" alt="Screenshot 2026-10-06 121131" src="https://github.com/user-attachments/assets/1c0b5125-965a-4abd-b9d2-81a490695c1b" /> <br>
- Output jika memasukkan "y" yaitu kita akan diminta login kembali, dan kita akan login sebagai user. <br>
  <img width="325" height="153" alt="Screenshot 2026-10-06 121229" src="https://github.com/user-attachments/assets/65213446-36a4-4159-b9da-ac2f4f0dbdd9" /> <br>
- Output menu user yaitu hanya bisa melihat daftar kontak dan keluar. <br>
  <img width="303" height="152" alt="Screenshot 2026-10-06 121258" src="https://github.com/user-attachments/assets/48bd4fe8-9c77-4e92-bcd5-843ba26183f4" /> <br>










  

