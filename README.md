Name : Celine Nafisa Setiawan

NPM : 2506590201

Class : PBP D

Jurusan : Ilmu Komputer

-------------- Pertanyaan Relatif --------------

### Tugas 1

1. Iya, saya menggunakan <section> seperti pada template Tutorial 1. Elemen <section> ini dapat membantu saya dalam membuat static web karena digunakan untuk mengelompokkan konten-konten yang berhubungan dalam satu grup yang dimana grup tersebut bisa dikasih class seperti 'hero-section' dan 'experiences' untuk dikasih style dengan menggunakan css agar rapih dan dalam satu theme. Hal ini agar konten-konten tertata rapih pada web (setiap section terpisah dari yang lain) dan bisa diatur agar stylenya berbeda-beda persection.

2. Agar web saya tetap responsive, tantangan tata letak yang saya temukan adalah headernya yang tidak mengadaptasi ke layar hp yang kecil. Saya berpikir untuk memindahkan navbar ke tengah saat pada mobile view, saya research cara melakukannya dengan mencari di inspect website lain dan meminta bantuan ke Gemini untuk menjelaskan kode inspect dari website lainnya tersebut.

3. Batasan yang saya rasakan dalam penyajian informasi pada portofolio saya adalah bahwa saya tidak dapat menambahkan animasi-animasi yang interaktif dengan cursor saya dan tidak dapat memaukkan form untuk kontak jika ada yang ingin meng-hire saya. Yang paling ingin saya persiapkan dan tambahkan adalah form working contact itu karena dengan adanya form tersebut, user yang ingin meng-hire saya saat nanti saya pakai web ini secara official dapat kontak saya dengan mudah lewat form tersebut.


-------------- Pernyataan Penggunaan AI --------------

Saya munggunakan bantuan AI, lebih tepatnya Gemini, dalam pengerjaan Tugas 1 ini.

Proses saya mengerjakan Tugas ini dan detail penggunaan AI (detail penggunaan AI terdapat pada poin 4 & 5):

1. Saya list dulu section apa yang ingin saya tambahkan berdasarkan ketentuan soal Tugas dan kemampuan diri sendiri

2. Saya analisis sintaks html dari template Tutorial 1, seperti penggunaan section dan classnya yang nanti akan dihubungkan ke file style.css dengan membuat style dengan nama class tersebut, dan website W3schools.com dalam pengerjaan section 'Experiences' dan 'Education'

3. Saya lanjut ke style.css dengan pertama menggunakan website coolors.co untuk membuat color palette yang saya inginkan dan mencari inspirasi wireframe dari Pinterest

4. Saya mulai mengatur style dari warna-warnanya, di sini saya ingin membuat warna-warna gradient yang nanti dapat saya pakai pada border photo saya, jadi saya meminta bantuan ke Gemini untuk menjelaskan bagaimana cara membuat warna gradient dalam css, bahkan saya meminta bantuan ke Gemini untuk membuatkan web html gradient maker untuk membuat dan mengetes gradient-gradient yang saya inginkan
--> mungkin saya cantumkan file 'gradient_maker.html' yang dibuat Gemini dalam /portfolio/css untuk transparansi
--> sebagai pernyataan 'SAYA TIDAK MEMBUAT WEBSITE gradient_maker.html SENDIRI, WEBSITE TERSEBUT DIBUAT OLEH GEMINI, DAN SAYA TIDAK MEMBUAT WEBSITE INI UNTUK DIMASUKKAN KE NILAI SEBAGAI PLUS POIN ATAU MINUS POIN, WEBSITE TERSEBUT HANYA UNTUK MEMBANTU SAYA DALAM PEMBUATAN GRADIENT COLORS'

5. Selanjutnya saya mengatur tata letak container-container section 'Experiences' dan 'Education' dengan bantuan Gemini lagi saat saya bingung dalam membuat animasi hovernya (cara membuat dia ada shadownya, animasi hovernya gimana, dan lain-lain). Namun saat saya prompting, saya tidak mencantumkan kode css ataupun html saya agar Gemini hanya membuatkan contoh dan penjelasan sintaks saja. Saya baca contoh dan penjelasan tersebut, terus lanjut mencoba buatkan hoverin animationnya sendiri.



============== Pertanyaan Relatif ==============

### Tugas 2

1. Alur yang terjadi ketika pengguna membuka halaman portofolio baru adalah adanya HTTPS request dari browser yang digunakan pengguna. Request ini masuk ke project urls.py yang kemudian akan memeriksa berkas url utama project dan meneruskan penanganan rute ke aplikasi urls.py. Selanjutnya, aplikasi urls.py akan mencocokkan pola rute dengan fungsi atau class view yang tepat. Selanjutnya, view akan memanggil model untuk mengambil data portofolio seperti list experience dan education dari basis data dan kemudian akan memanggil template yang sesuai dengan data model yang diambil. Model ini mengambil data portofolio yang tersimpan dalam basis data dan mengembalikannya ke view. Selanjutnya, template memanggil berkas HTML yang menerima data dari view dan kemudian merender data tersebut menjadi sebuah halaman mengikui style yang sudah ada di css file.

2. Karena dengan data disimpan dalam bentuk model, bukan hardcoded, kita sebagai developer akan lebih mudah jika ingin menambahkan data baru seperti a new experience or education, karena sudah ada "template" isi datanya seperti title, description, category, dll. yang nanti akan secara otomatis kerender oleh template dengan style yang sesuai. Jika kita hardcode ke dlm index.html, kita sebagai developer akan kesusahan setiap menambah data baru karena perlu menambah section baru, div baru, dll.

3. Perbedaan antara makemigrations dan migrate adalah bahwa makemigrations membaca perubahan pada file models.py, seperti penambahan model baru atau pergantian field pada model, dan membuat skrip migrasi baru. Sedangkan migrate mengeksekusikan skrip migrasi yang baru tsb ke dalam basis data nyata. Saya pikirnya ini seperti commit dan push pada git, makemigrations seperti commit dan migrate seperti push.


-------------- Pernyataan Penggunaan AI --------------

Saya TIDAK munggunakan bantuan AI sama sekali dalam pengerjaan Tugas 2 ini. Saya hanya mengikuti langkah-langkah dari Tutorial 2.

Proses saya mengerjakan Tugas ini:

1. Saya lihat model apa yang ingin saya tambahkan (in this case, education, karena mengikuti yang saya tambahkan pada Tugas 1).

2. Saya ikuti langkah-langkah pada Tutorial 2 dan menambahkan model education dengan field-field yang menurut saya cocok seperti school, dll.

3. Saya kemudian menambahkan file baru di templates dengan nama education.html

4. Selanjutnya, saya menambahkan rute url untuk education pada urls.py dan pada navbar di index.html

5. Selanjutnya saya membuat unit testing dengan mengikuti template dari Tutorial 2 dan cek apakah sudah benar dengan menggunakan python manage.py test

6. Jika sudah OK testnya, saya push ke github dan pws dan mengakhiri pengerjaan Tugas ini dengan menulis README.md ini.



============== Pertanyaan Relatif ==============

### Tugas 3

1. Dengan menggunakan ModelForm, django secara otomatis menghasilkan field form berdasarkan struktur Model pada Django kita, sehingga kita tidak perlu menulis ulang tag input satu persatu pada file html. Form ini juga memudahkan proses validasi data dari input user dan proses penyimpanannya ke dalam database (.save()) tanpa perlu mengambil dan memetakan satu persatu request.POST secara manual. Penambahan {% csrf_token %} adalah untuk mencegah adanya pengiriman data dari pihak luar untuk mengecoh current usernya. Basically, saat user menekan tombol submit (POST request), Django akan memverifikasi apakah token tersebut cocok dengan sesi user yang sedang aktif.

2. Selain karena sintaks JSON yang lebih bersih dan rapih, JSON berbasis sintaks objek JavaScript, jadi dapat langsung diubah menjadi objek JS secara instan di sisi frontend tanpa memerlukan library atau parser tambahan seperti XML.

3. Ketika user mengakses API, Django akan memanggil fungsi view terkait seperti get_experiences_json. View tersebut akan mengambil query data dari database menggunakan QuerySet model Django yang akan kemudian melewati proses serialization untuk mengubah objek Python/Django menjadi JSON. Terakhir, view akan mengembalikan data tersebut dalam bentuk objek HttpResponse dengan content_type="application/json" agar browser tahu bahwa data yang dikirim adalah format JSON.


-------------- Pernyataan Penggunaan AI --------------

Saya TIDAK munggunakan bantuan AI sama sekali dalam pengerjaan Tugas 3 ini. Saya hanya mengikuti langkah-langkah dari Tutorial 3.

Proses saya mengerjakan Tugas ini:

1. Saya sebenarnya sudah menambahkan form untuk kedua model yang saya awalnya miliki (experience dan education) pada saat mengerjakan Tutorial 3. Jadi pada Tugas 3 ini saya menambahkan model baru, yakni Skill agar bisa meluaskan portfolio saya dan menambahkan form baru lagi dan mengikuti langkah-langkah Tugas 3 ini.

2. Saya ikuti langkah-langkah pada Tutorial 3 dan menambahkan model skill dengan field-field yang menurut saya cocok, dan juga formnya.

3. Saya kemudian menambahkan file-file html yang diperlukan sesuah Tutorial 3 seperti skill.html, skills_form.html, dan skill_delete_modal.html dalam components.

4. Selanjutnya, saya menambahkan rute url untuk skill pada urls.py dan pada navbar di index.html

5. Selanjutnya saya membuat unit testing dengan mengikuti template dari Tutorial 2 dan cek apakah sudah benar dengan menggunakan python manage.py test

6. Jika sudah OK testnya, saya push ke github dan pws dan mengakhiri pengerjaan Tugas ini dengan menulis README.md ini.