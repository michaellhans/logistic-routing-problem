# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

## Tujuan Tugas
1. Review materi pathfinding pada mata kuliah Strategi Algoritma.
2. Mengenal multiple-agent TSP.
3. Melakukan visualisasi data.

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat lau kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Multiple-Agent TSP
Masalah pengantaran barang untuk satu kendaraan dengan fungsi objektif jarak minimal dapat dimodelkan oleh Travelling Salesman Problem. Akan tetapi, perusahaan logistik biasanya memiliki lebih dari satu kendaraan yang berangkat bersamaan, sehingga TSP kurang cocok digunakan. Generalisasi TSP untuk beberapa agen adalah **multiple-agent TSP (mTSP)**, dan model masalah ini akan kita gunakan. Pada mTSP, akan terdapat *m* tur yang akan dibangun. Syarat dari semua tur mirip dengan TSP, yaitu bahwa seluruh tur akan kembali ke simpul awal (mewakili kantor pusat) dan setiap tujuan hanya akan dilewati oleh satu tur.

## Tugas
Kita akan menggunakan dataset jalanan pada kota Oldenburg yang dapat diakses pada <a href="https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm">tautan ini.</a> Lakukan pengunduhan untuk kedua data jalanan di kota Oldenburg. Data pertama merupakan koordinat simpul, data kedua merupakan data sisi antar simpul. Asumsikan seluruh jalan dua arah.<br> 
Seperti yang disebutkan sebelumnya, kita akan menggunakan pendekatan mTSP dalam permasalahan ini. Untuk mempermudah anda dan mempermudah penilaian, tugas akan dibagi dalam beberapa tahap.

### Milestone 1
Pada milestone 1, anda diminta untuk membangun sebuah upagraf dari graf jalan keseluruhan kota Oldenburg. Upagraf tersebut merupakan sebuah graf lengkap tak berarah, dengan simpul-simpulnya adalah titik tujuan pengiriman barang ditambah titik yang mewakili kantor pusat perusahaan logistik. Hasilkan sebuah matriks jarak antar simpul upagraf lengkap. Nilai untuk milestone pertama maksimal adalah **600**.

### Milestone 2
Pada Milestone 2 , anda akan menggunakan upagraf yang telah dihasilkan pada Milestone 1 untuk membangun rute dari para kurir dengan pendekatan mTSP. Tampilkan rute yang diambil oleh tiap kurir. Nilai maksimal pada milestone kedua adalah **1500**

### Milestone 3
Setelah berhasil mendapatkan rute bagi para kurir, selanjutnya anda diminta untuk menggambarkan rute dari para kurir. Visualisasi rute  minimal membedakan warna rute untuk tiap kurir dan menampilkan upagraf yang digunakan untuk membuat rute. Nilai lebih akan diberikan jika anda dapat menampilkan rute beserta seluruh peta jalan di kota Oldenburg. Nilai minimal adalah **800** dan nilai maksimal adalah **1500**

## Pengerjaan
Tugas ini individual.<br>
Lakukan *fork* terhadap *repository* ini.<br>
Spek tugas cukup umum, sehingga asisten tidak membatasi algoritma maupun bahasa pemrograman yang digunakan, walaupun **penggunaan Python disarankan**. Algoritma yang digunakan untuk pathfinding harus optimal, namun hasil dari mTSP tidak harus optimal (*Note : beberapa pustaka optimization bisa menghasilkan solusi sub-optimal dalam batas waktu tertentu*). Bila merasa sudah menyelesaikan tugas, silahkan lakukan pull request dan hubungi asisten lewat email untuk melakukan demo.<br>
Pastikan ada menambahkan/menggati README ini saat mengumpulkan. README minimal mengandung :

1. Pendekatan algoritma yang digunakan untuk pathfinding dan penyelesaian mTSP, serta 
2. Cara menjalankan program, termasuk instalasi pustaka bila menggunakan bermacam pustaka

Anda bebas menggunakan pustaka maupun referensi apapun untuk mengerjakan tugas, kecuali kode/pustaka jadi yang melakukan *routing*, karena tujuan tugas adalah membuat sebuah prototipe pembuatan rute. Pastikan anda mencantumkan sumber bilamana anda menggunakan kode dari orang lain. Akan tetapi, pemahaman terhadap solusi masalah menjadi bagian penting dari penilaian , sehingga anda disarankan untuk menuliskan kode anda sendiri.<br>

## Getting Started
Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya.

### Prerequisites
Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.
```
- Python 3.x.x untuk bahasa pemrograman aplikasi
- Matplotlib Library untuk visualisasi peta
- GraphViz Library untuk visualisasi graf sederhana
```

### Installing
Berikut ini adalah langkah-langkah dalam penginstallan aplikasi:
1. Install library Matplotlib terlebih dahulu menggunakan command sebagai berikut.
```
pip install matplotlib
```
2. Install library GraphViz terlebih dahulu menggunakan command sebagai berikut.
```
pip install graphviz
```
3. Semua prerequisites sudah disiapkan dengan baik.

## How to Run Program
Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python mtsp.py
```

## Guideline: How to Use
1. Masukkan nama file yang berisi daftar koordinat setiap kota. Untuk setiap koordinat kota, digunakan format berupa 
```
ID XPosition YPosition
```
Berikut ini adalah contoh daftar koordinat kota pada FileNode.txt
```
1 200 300
2 300 400
3 100 50
```
2. Masukkan nama file untuk setiap sisi atau jalan yang menghubungkan antar kota.
```
IDEdge IDAsal IDTujuan Jarak
```
Berikut ini adalah contoh daftar jalan penghubung antar kota pada FileEdge.txt
```
1 1 2 80
2 1 3 200
3 2 3 150
```
Pastikan bahwa setiap jalan pada FileEdge.txt menghubungkan kota-kota yang bersesuaian dengan daftar kota pada FileNode.txt

3. Masukkan jumlah salesman yang diinginkan. Pastikan jumlah salesman tidak melebihi banyaknya kota.
4. Masukkan kota asal (origin city).
5. Aplikasi akan memproses masukkan pengguna untuk diolah menjadi kumpulan rute terpendek.
6. Aplikasi akan menampilkan visualisasi peta dan rute-rute yang dilewati oleh setiap salesman.

## Checklist Milestone Pengerjaan
- [X] Milestone 1 : Pembacaan File dan Representasi Graf dalam Matrix
- [X] Milestone 2 : Mengembalikan Solusi Multiple TSP
- [X] Milestone 3 : Visualisasi Rute olusi Multiple TSP

## Built With
* [Python](https://www.python.org/) - Back End dari Aplikasi

## Referensi Awal Pengerjaan Tugas
Silahkan gunakan referensi berikut sebagai awal pengerjaan tugas:
[1] Dataset : https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm<br>
[2] Pengenalan dan formulasi mTSP : https://neos-guide.org/content/multiple-traveling-salesman-problem-mtsp<br>
[3] MIP , pustaka Python untuk optimisasi : https://python-mip.readthedocs.io/en/latest/intro.html<br>
[4] OpenGL untuk Python : https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/<br>
[5]  Li, Feifei, Dihan Cheng, Marios Hadjieleftheriou, George Kollios, and Shang-Hua Teng. "On trip planning queries in spatial databases." In International symposium on spatial and temporal databases, pp. 273-290. Springer, Berlin, Heidelberg, 2005.

## Referensi Formulasi Multiple TSP
[1] Solving Multiple TSP Problem by K-Means and Crossover based Modified ACO Algorithm : https://www.ijert.org/research/solving-multiple-tsp-problem-by-k-means-and-crossover-based-modified-aco-algorithm-IJERTV5IS020474.pdf<br>
[2] Vehicle Routing Problem : https://developers.google.com/optimization/routing/vrp<br>
[3] Amazing Collection Vehicle Routing Problem : https://github.com/ashishpatel26/Amazing-Collection-Vehicle-Routing-Problem<br>
[4] Vehicle Routing Problem : https://github.com/jwang0306/vehicle-routing-problem<br>
[5] An Ant Colony Optimization Algorithm for Multiple Travelling Salesman Problem : https://www2.cs.siu.edu/~rahimi/shared/TSM/01691778.pdf<br>
[6] Dijkstra Algorithm for Pathfinding : https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2019-2020/Algoritma-Greedy-(2020).pdf<br>
[7] A* Algorithm for Pathfinding : https://www.annytab.com/a-star-search-algorithm-in-python/

## Credits
Thank you for Li Fei Fei et. al. for providing the data.

## Catatan
Pencarian rute untuk setiap agen mungkin tidak menghasilkan solusi atau rute yang optimal mengingat pembagian tugas kota-kota dilakukan secara acak.

## Author
**13518056 - Michael Hans** - *Designer, Programmer, and Tester*

## Acknowledgements
* Asisten IRK, Nur Alam Hasabie