# Minpro 2 - DDP 2025
# Profil
Nama: Alya Hauranisa Nugroho\
NIM: 2509116005\
Kelas: Sistem Informasi A 2025

# Deskripsi Singkat
Program Python sederhana yang saya buat ini berjudul **"Sistem Manajemen Pemesanan Bouquet Bunga"**. Program ini dapat dimanfaatkan oleh pengguna(manager dan karyawan) 
untuk mencatat dan memilah orderan yang masuk, sehingga memudahkan pengguna untuk memanajemen dan mengatur pesanan yang ada. Selain itu, 
program ini juga telah memuat seluruh sistem CRUD (Create, Read, Update, dan Delete).
### **Untuk manager, program ini memiliki beberapa menu yang tersedia, yakni:**
1. Dapat memasukkan orderan baru
2. Dapat melihat orderan yang ada
3. Dapat mengupdate status orderan
4. Dapat menghapus orderan
5. Keluar dari program
### **Untuk karyawan, program ini memiliki beberapa menu yang tersedia, yakni:**
1. Dapat melihat orderan yang ada
2. Dapat mengupdate status orderan
3. Keluar dari program

# Flowchart
Berikut merupakan flowchart dari program **Sistem Manajemen Pemesanan Bouquet Bunga**\
<img width="16384" height="11743" alt="MINPRO2AlyaHauranisa Nugroho drawio" src="https://github.com/user-attachments/assets/86a4c196-5311-407a-be8d-6e8a162ff575" />

# Alur Program
## Login
- Saat membuka program, user akan diminta untuk memasukkan angka 1 atau 2 untuk memilih role sebagai manager ataupun karyawan.

- Selanjutnya, user akan diminta password untuk role yang dipilih (Password manager "bungaku123" - Password karyawan "caricuan321")

- Pengguna memiliki 3 kali kesempatan untuk input password. Apabila kesempatan habis, maka program akan selesai dan menampilkan pesan bahwa kesempatan habis dan login gagal

- Apabila password benar, maka akan masuk ke menu utama dari masing- masing role

# Menu Manager
- Menu ini memungkinkan manager untuk mengakses seluruh CRUD (Create, Read, Update, dan Delete)
- Saat membuka program, pengguna akan diminta untuk input angka dari 1-5 untuk memilih menu yang tersedia

- Apabila angka menu yang diinput tidak sesuai, maka program akan menampilkan pesan bahwa input tidak valid dan akan mengulang dari proses input pilihan menu.


## Menu 1 - Tambah Orderan
- Menu ini memungkinkan pengguna menambahkan orderan baru ke dalam list orderan

- Pada menu ini, pengguna akan diminta untuk memasukkan input nama pemesan, No HP, paket bouquet yang dipilih, custom (+add on bunga), warna wrapping paper, serta tanggal pengambilan.

- Program akan menambahkan orderan baru ke dalam list orderan.

- Selanjutnya, program menampilkan ringkasan pesanan dan kembali ke menu utama.


- Apabila ditengah input paket bouquet, custom bunga, ataupun warna wrapping paper pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input


## Menu 2 - Lihat Orderan
- Menu ini memungkinkan pengguna untuk melihat orderan yang ada


- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan, nih :("


- Namun, apabila list orderan terisi, maka program akan menampilkan seluruh daftar orderan dan kembali ke menu utama.


## Menu 3 - Update Status
- Menu ini memungkinkan pengguna untuk update status dari sebuah orderan

- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan, tetap semangat!!" dan kembali ke menu utama

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang statusnya ingin diupdate.

- Selanjutnya, pengguna diminta untuk input angka 1-3 untuk menentukan status baru, sehingga program dapat mengubah elemen list sesuai dengan index yang dimasukkan. 

- Program akan menampilkan orderan yang telah ter-update dan kembali ke menu utama.

- Apabila ditengah menjalankan menu ini pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input



## Menu 4 - Hapus Orderan
- Menu ini memungkinkan pengguna untuk menghapus orderan yang ada

- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan yang bisa dihapus :p"

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang ingin dihapus.

- Selanjutnya, program akan menghapus orderan yang terpilih

- Program akan menampilkan orderan yang telah dihapus, serta seluruh daftar orderan terbaru.

- Apabila ditengah menjalankan menu ini terdapat input yang salah, maka program akan terhenti dan menampilkan "Pilihan kamu tidak valid :("


## Menu 5 - Keluar >>>
- Menampilkan "HEHEHE Terima kasih sudah menggunakan layanan kami <3" dan program selesai.
<img width="697" height="263" alt="image" src="https://github.com/user-attachments/assets/2a9b74fe-72d0-4cec-906c-ce1029f807fe" />
