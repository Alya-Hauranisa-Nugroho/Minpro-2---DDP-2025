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
<img width="718" height="162" alt="image" src="https://github.com/user-attachments/assets/0ad021a9-9929-4d3a-876c-c6c23bdebb86" />

- Selanjutnya, user akan diminta password untuk role yang dipilih **(Password manager "bungaku123" - Password karyawan "caricuan321")**
<img width="338" height="95" alt="image" src="https://github.com/user-attachments/assets/72a3b63b-18ba-44eb-9942-792591575540" /> <img width="289" height="103" alt="image" src="https://github.com/user-attachments/assets/537876f7-ce29-4dee-8b02-c019fb23c69f" />

- Pengguna memiliki 3 kali kesempatan untuk input password. Apabila kesempatan habis, maka program akan selesai, serta menampilkan pesan bahwa kesempatan habis dan login gagal
<img width="460" height="282" alt="image" src="https://github.com/user-attachments/assets/61d6e9be-a056-409f-9fdf-837a4899749d" />

- Apabila password benar, maka akan masuk ke menu utama dari masing-masing role
<img width="514" height="270" alt="image" src="https://github.com/user-attachments/assets/7b2aec2b-dcfd-4642-8158-6fc27592b4b6" /> <img width="476" height="241" alt="image" src="https://github.com/user-attachments/assets/12dc7038-bae4-402f-8bb4-7bc8232d92e0" />

## Menu Manager
- Menu ini memungkinkan manager untuk mengakses seluruh **CRUD (Create, Read, Update, dan Delete)**
- Saat membuka program, pengguna akan diminta untuk input angka dari 1-5 untuk memilih menu yang tersedia
<img width="284" height="134" alt="image" src="https://github.com/user-attachments/assets/165279d8-87d2-42cf-9c60-7badc662f51f" />

- Apabila angka menu yang diinput tidak sesuai, maka program akan menampilkan pesan bahwa input tidak valid dan akan mengulang dari proses input pilihan menu.
<img width="330" height="286" alt="image" src="https://github.com/user-attachments/assets/fc0cf6d3-d9c0-44a9-add9-99985bd20f67" />


### Menu 1 - Tambah Orderan
- Menu ini memungkinkan pengguna **menambahkan orderan baru** ke dalam list orderan
- Pada menu ini, pengguna akan diminta untuk memasukkan input nama pemesan, No HP, paket bouquet yang dipilih, custom (+add on bunga), warna wrapping paper, serta tanggal pengambilan.
<img width="486" height="526" alt="image" src="https://github.com/user-attachments/assets/5c20ac79-debf-4c0c-969e-f8999faf8071" />

- Program akan menambahkan orderan baru ke dalam list orderan.
<img width="626" height="97" alt="image" src="https://github.com/user-attachments/assets/165a0522-cf0b-42f0-87ff-f8f5b2af89a3" />

- Selanjutnya, program menampilkan ringkasan pesanan dan kembali ke menu utama.
<img width="445" height="356" alt="image" src="https://github.com/user-attachments/assets/fe737e1f-8a40-4c73-8547-9d45a0b05603" />

- Apabila ditengah input paket bouquet, custom bunga, ataupun warna wrapping paper pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input
<img width="366" height="228" alt="image" src="https://github.com/user-attachments/assets/5d470403-8562-4b92-a8a7-97c5fa56a8e9" />

### Menu 2 - Lihat Orderan
- Menu ini memungkinkan pengguna untuk **melihat orderan** yang ada
- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan, tetap semangat!!" dan kembali ke menu utama.
<img width="345" height="166" alt="image" src="https://github.com/user-attachments/assets/757d11ad-c3ed-4b14-b2af-21a721911729" />

- Namun, apabila list orderan terisi, maka program akan menampilkan seluruh daftar orderan dan kembali ke menu utama.
<img width="601" height="547" alt="image" src="https://github.com/user-attachments/assets/6898b516-1437-44a9-91e1-468d53b42175" />

### Menu 3 - Update Status
- Menu ini memungkinkan pengguna untuk **update status** dari sebuah orderan
- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan yang bisa dihapus :(" dan kembali ke menu utama
<img width="397" height="188" alt="image" src="https://github.com/user-attachments/assets/1062ba45-ba3c-40b8-9b66-5adf55fad71e" />

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang statusnya ingin diupdate.
<img width="395" height="523" alt="image" src="https://github.com/user-attachments/assets/7ad74ac7-4c79-4d95-ba88-f254648c82fe" />

- Selanjutnya, pengguna diminta untuk input angka 1-3 untuk menentukan status baru, sehingga program dapat mengubah elemen list sesuai dengan index yang dimasukkan. 
<img width="247" height="94" alt="image" src="https://github.com/user-attachments/assets/9db117f1-ada5-4313-93fb-d26b4730e477" />

- Program akan menampilkan orderan yang telah ter-update dan kembali ke menu utama.
<img width="505" height="317" alt="image" src="https://github.com/user-attachments/assets/5299a942-991f-4c99-a576-243a5f9bb402" />

- Apabila ditengah menjalankan menu ini pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input
<img width="427" height="419" alt="image" src="https://github.com/user-attachments/assets/d9cde18d-e729-4d1e-9d5b-9657822495d5" />

### Menu 4 - Hapus Orderan
- Menu ini memungkinkan pengguna untuk **menghapus orderan** yang ada.
- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan yang bisa dihapus :(" dan kembali ke menu utama.
<img width="358" height="192" alt="image" src="https://github.com/user-attachments/assets/261598ef-7c4e-4175-be74-d0f0f5922535" />

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang ingin dihapus.
<img width="403" height="526" alt="image" src="https://github.com/user-attachments/assets/315844d5-498e-459c-989e-b62edbaa9c2c" />

- Selanjutnya, program akan menghapus orderan yang terpilih.
<img width="406" height="20" alt="image" src="https://github.com/user-attachments/assets/284da70a-6334-48a3-bc7c-609c96f0aff9" />

- Program akan menampilkan seluruh daftar orderan terbaru dan kembali ke halaman utama.
<img width="404" height="518" alt="image" src="https://github.com/user-attachments/assets/d4888cb1-1d85-4014-8a15-6b26379ab7b9" />

- Apabila ditengah menjalankan menu ini pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input.
<img width="390" height="456" alt="image" src="https://github.com/user-attachments/assets/a4f67bf8-a1d7-4ba4-9d94-2376c70db6f1" />

### Menu 5 - Keluar >>>
- Menampilkan "Terima kasih sudah menggunakan layanan kami <3" dan program selesai.
<img width="420" height="161" alt="image" src="https://github.com/user-attachments/assets/509fcc8b-3edf-4ec4-a378-1400af6e5d11" />

## Menu Karyawan
- Menu ini memungkinkan karyawan untuk mengakses sebagian dari **CRUD (Create, Read, Update, dan Delete)**, yakni: **Read dan Update**
- Saat membuka program, pengguna akan diminta untuk input angka dari 1-3 untuk memilih menu yang tersedia
<img width="309" height="104" alt="image" src="https://github.com/user-attachments/assets/a75c11ff-e612-4bed-aa13-38094cf5959e" />

- Apabila angka menu yang diinput tidak sesuai, maka program akan menampilkan pesan bahwa input tidak valid dan akan mengulang dari proses input pilihan menu.
<img width="333" height="221" alt="image" src="https://github.com/user-attachments/assets/945593e0-3439-4e0b-935a-b4aecb4201cf" />

### Menu 1 - Lihat Orderan
- Menu ini memungkinkan pengguna untuk **melihat orderan** yang ada
- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan, tetap semangat!!" dan kembali ke menu utama.
- Namun, apabila list orderan terisi, maka program akan menampilkan seluruh daftar orderan dan kembali ke menu utama.
<img width="395" height="530" alt="image" src="https://github.com/user-attachments/assets/e6108a3a-7af1-4ced-97e8-17723cdc6096" />

### Menu 2 - Update Status
- Menu ini memungkinkan pengguna untuk **update status** dari sebuah orderan
- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan yang bisa dihapus :(" dan kembali ke menu utama
- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang statusnya ingin diupdate.
<img width="395" height="523" alt="image" src="https://github.com/user-attachments/assets/7ad74ac7-4c79-4d95-ba88-f254648c82fe" />

- Selanjutnya, pengguna diminta untuk input angka 1-3 untuk menentukan status baru, sehingga program dapat mengubah elemen list sesuai dengan index yang dimasukkan. 
<img width="247" height="94" alt="image" src="https://github.com/user-attachments/assets/9db117f1-ada5-4313-93fb-d26b4730e477" />

- Program akan menampilkan orderan yang telah ter-update dan kembali ke menu utama.
<img width="505" height="317" alt="image" src="https://github.com/user-attachments/assets/5299a942-991f-4c99-a576-243a5f9bb402" />

- Apabila ditengah menjalankan menu ini pengguna memasukkan input yang salah, maka program melakukan ErrorHandling dengan menampilkan pesan kesalahan dan pengguna diminta untuk kembali memasukkan input
<img width="427" height="419" alt="image" src="https://github.com/user-attachments/assets/d9cde18d-e729-4d1e-9d5b-9657822495d5" />

### Menu 3 - Keluar >>>
- Menampilkan "Terima kasih sudah menggunakan layanan kami <3" dan program selesai.
<img width="381" height="147" alt="image" src="https://github.com/user-attachments/assets/841b7a0d-c05e-4b8d-bc80-ec087188727a" />



