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
1. Jalankan XServer dengan memilih "Multiple Windows" lalu klik next hingga finish.;
2. Clone Git ke desktop kalian lalu buka di Visual Studio Code.;
3. Buka folder yang sudah di clone ke desktop pada VSCode.;
4. Buka file Dockerfile lalu ketik perintah docker build berikut
      
      docker build -t dott .

5. Tunggu hingga selesai. Lalu, jalankan docker dengan perintah berikut

      docker run dott
      
6. Game akan jalan dan sudah bisa dimainkan.;

<h4>Deskripsi Proyek :  </h4>
Game ini bernama Defense Of The Tower yang menggunakan bahasa python dalam penggunaanya. Game ini menganut konsep permainan “Tower Defense” dimana player akan menjaga sebuah Menara dari serangan musuh yang datang. </p>

<h4>Dependensi Paket : </h4>
Paket library yang dibutuhkan untuk menjalankan aplikasi ini adalah library PyGame.

<h4>Cara Bermain Game : </h4>
Lawan musuh dengan cara menembaknya dan pertahankan tower agar tidak dibobol oleh musuh. Menggunakan arrow key untuk bergerak ke arah kanan dan kiri, tombol "Spacebar" pada keyboard untuk melompat, dan tombol "F" pada keyboard untuk menembak musuh.

<h4>Kontributor Pengembangan Aplikasi : </h4>
Andika Rizki Ramadhan             = Programmer;
Pandu Wahyudi                     = Programmer;
Akhmad Fahrizal                   = Programmer;
Muhammad Bintang Fitriatuderajat  = Programmer;
Sayyid Chalil Azra                = Programmer;
Muflihin Attami                   = Programmer;

