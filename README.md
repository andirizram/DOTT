<h2>Defense Of The Tower (DOTT)  (TUBES PBO RB-08) </h2>

<h4>Anggota Kelompok : </h4>

1. Andika Rizki Ramadhan            (120140002) (andirizram)

2. Pandu Wahyudi						        (120140010) (Pandu160402)

3. Akhmad Fahrizal						      (120140024) (afahrizal)

4. Muhamad Bintang Fitriatuderajat	(120140040) (Daenerysl)

5. Sayyid Chalil Azra						    (120140242) (Sayyid-120140242)

6. Muflihin Attami						      (120140243) (Muf29)

<h4>Cara Menjalankan Kontainer :  </h4>
Untuk menjalankan kontainer diperlukannya Docker Desktop for Windows dan XServer untuk Display Output pada Windows.

[Klik Disini](https://sourceforge.net/projects/vcxsrv/) untuk download XServer for Windows lalu install.

Langkah - langkah yang harus dilakukan untuk menjalankan kontainer :

1. Jalankan XServer dengan memilih "Multiple Windows" lalu klik next hingga finish.

2. Clone Git ke desktop kalian lalu buka di Visual Studio Code.

3. Buka folder yang sudah di clone ke desktop pada VSCode.

4. Buka file Dockerfile lalu ketik perintah docker build berikut
      
            docker build -t dott .

5. Tunggu hingga selesai. Lalu, jalankan docker dengan perintah berikut

            docker run dott
      
6. Game akan jalan dan sudah bisa dimainkan.

<h4> Video Demo Kontainer : </h4>

[![Video Demo](https://img.youtube.com/vi/_eAW2l46GD8/hqdefault.jpg)](https://youtu.be/_eAW2l46GD8)


<h4>Deskripsi Proyek :  </h4>
Game ini bernama Defense Of The Tower yang menggunakan bahasa python dalam penggunaanya. Game ini menganut konsep permainan “Tower Defense” dimana player akan menjaga sebuah Menara dari serangan musuh yang datang. </p>

<h4>Dependensi Paket : </h4>
Paket library yang dibutuhkan untuk menjalankan aplikasi ini adalah library PyGame dan library PyGame Menu.

<h4>Cara serta Alur Bermain Game : </h4>
Untuk bermain game silahkan jalankan file main_menu.py terlebih dahulu.

Pada awal masuk ke dalam game, pemain akan disajikan sebuah main menu sederhana yang memiliki fungsi seperti mulai dan keluar. Lalu apabila pemain memilih mulai maka game akan langsung dimulai yaitu melawan musuh dengan cara menembaknya dan mempertahankan tower agar tidak dibobol oleh musuh. lalu pemain bisa menggunakan arrow key untuk bergerak ke arah kanan dan kiri, tombol "Spacebar" pada keyboard untuk melompat, dan tombol "F" pada keyboard untuk menembak musuh. Selanjutnya apabila health pada pemain atau tower telah habis maka game dengan sendiri nya akan berhenti dan menampilkan output score tertinggi pemain serta munculnya restrart screen untuk mengulang game tersebut. Apabila pemain sudah selesai bermain maka mereka bisa menekan tombol "X" pada pojok kanan atas.

<h4>UML Class Diagram : </h4>
<img width="436" alt="image" src="https://user-images.githubusercontent.com/95036143/171549405-d15cf872-dce7-42b2-a536-24202dd7e23e.png">


<h4>Kontributor Pengembangan Aplikasi : </h4>

1. Andika Rizki Ramadhan             = Programmer

2. Pandu Wahyudi                     = Programmer

3. Akhmad Fahrizal                   = Programmer

4. Muhammad Bintang Fitriatuderajat  = Programmer

5. Sayyid Chalil Azra                = Programmer

6. Muflihin Attami                   = Programmer

