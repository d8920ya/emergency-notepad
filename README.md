# My Emergency Notepad App
---
Merupakan sebuah aplikasi ringkas yang digunakan untuk menulis catatan dengan atribut Judul (Title) dan Isi (Body). Aplikasi ini menggunakan FLASK, sebuah microframework yang berjalan di Python, ditambah JavaScript sebagai penghubung HTML dengan FLASK. Pada file `app.py` terdapat 3 route yaitu : `/` untuk menampilkan template index.html, `/dataProvider` yang digunakan untuk menampilkan tabel dari data JSON yang dikirim oleh backend, `/submit` yang digunakan untuk menambahkan data notes/catatan dan disimpan pada backend dalam format JSON. Python menyimpan objek JSON pada variabel myNotes dan data tersebut dikomunikasikan dengan Javascript menggunakan method POST. Dengan bantuan AJAX dan Route pada FLASK, aplikasi yang dibuat cukup ringkas, sehingga cukup hanya 1 template saja yang dibuat.

###### Fitur :
- Menampilkan catatan
- Menambahkan catatan

###### Rencana pengembangan :
- Akses Edit notes
- Akses Delete notes
- Atribut Waktu

Untuk mendukung multi-container service, diberikan informasi nama hostname di bagian footer. Harapannya, ketika aplikasi dijalankan di atas stack/replication, hostname container dapat diketahui dan apabila ada container yang bermasalah dapat dengan mudah diketahui. Karena berjalan dalam container stateless, ketika container mengalami restart data akan hilang dan kondisi container akan kembali ke posisi default mengikuti docker image.

# Cara Menjalankan Aplikasi di Docker
---
Aplikasi ini berjalan di virtualisasi docker. Jalankan aplikasi dengan perintah berikut :
```
docker run -d -p 5000:80 --name notepad d8920ya/emergency-notepad
```

Perintah di atas akan mengunduh image `emergency-notepad` yang ada di repository `d8920ya` dan menjalankan docker container menggunakan template dari image yang baru diunduh. Docker akan memberikan nama `notepad` pada container yang dibuat, serta melakukan forwarding port `5000` pada Dockerhost ke port `80` container. Dengan demikian, service pada container dapat diakses menggunakan port `5000` dari Dockerhost.

---

# Kustomisasi Docker Image
Dalam penggunaan aplikasi ini, terkadang kita membutuhkan fitur lain untuk disematkan pada aplikasi, oleh karena itu kita perlu merubah beberapa kode agar aplikasi berjalan sesuai dengan kebutuhan. 

```
git clone https://github.com/d8920ya/emergency-notepad.git
cd emergency-notepad

## Lakukan beberapa perubahan di direktory Apps
## Pastikan perubahan sudah tersimpan dan tidak ada error
## Kembali ke direktory emergency-notepad

docker build -t emergency-notepad -f Dockerfile/Dockerfile .
docker run -d -p 5000:80 --name custom_notepad emergency-notepad
```

Setelah menjalankan perintah di atas, kita akan memiliki docker image baru dengan versi/tag  default latest. 

---

# My Emergency Notepad App on Kubernetes
![alt text](https://github.com/d8920ya/emergency-notepad/tree/master/Kubernetes "[Lihat Dokumentasi di link berikut.]")
