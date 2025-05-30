# Aplikasi Web Tabel Periodik Interaktif

Sebuah aplikasi web interaktif yang dibangun menggunakan Flask. Aplikasi ini memungkinkan pengguna untuk menjelajahi tabel periodik unsur, melihat informasi detail, mengelola data unsur (Tambah, Baca, Perbarui, Hapus), dan membandingkan unsur-unsur.

## Fitur Utama

*   **Tampilan Tabel Periodik Interaktif:** Menampilkan unsur-unsur di halaman utama, dengan kode warna berdasarkan jenisnya. Setiap unsur yang diklik akan mengarahkan ke halaman detail unsur tersebut.
*   **Halaman Detail Unsur:** Halaman khusus untuk setiap unsur (`/element/view/<nomor_atom>`) yang menampilkan informasi komprehensif, termasuk gambar (jika tersedia) dan properti spesifik seperti kulit elektron dan energi ionisasi.
*   **Fungsi Pencarian:** Pencarian *real-time* berdasarkan nama atau simbol unsur di halaman utama tabel periodik.
*   **Filter Berdasarkan Jenis Unsur:** Tombol untuk memfilter unsur di halaman utama berdasarkan klasifikasinya (misalnya, logam alkali, gas mulia).
*   **Operasi CRUD Unsur:**
    *   **Tambah (Create):** Menambahkan unsur baru ke database melalui formulir khusus (`/element/new`) dengan validasi input.
    *   **Baca (Read):** Melihat data unsur melalui tabel utama, halaman detail, dan halaman "Kelola Unsur".
    *   **Perbarui (Update):** Mengedit informasi unsur yang sudah ada menggunakan formulir yang sudah terisi (`/element/edit/<nomor_atom>`).
    *   **Hapus (Delete):** Menghapus unsur dari database dengan konfirmasi, dapat diakses dari halaman detail unsur atau halaman kelola.
*   **Halaman Kelola Unsur:** Tampilan tabel (`/elements`) dari semua unsur, yang dilengkapi dengan:
    *   Pencarian/pemfilteran di sisi klien dalam tabel.
    *   Kolom yang dapat diurutkan.
    *   Tautan langsung untuk melihat, mengedit, atau menghapus setiap unsur.
*   **Halaman Bandingkan Unsur:** Alat (`/compare`) untuk memilih hingga tiga unsur dan melihat perbandingan propertinya secara berdampingan.
*   **Tooltip:** Mengarahkan kursor ke sebuah unsur di tabel utama akan menampilkan tooltip berisi nomor atom, simbol, dan nama unsur tersebut.
*   **Populasi Data:** Data unsur dimuat dari `PeriodicTableJSON.json` menggunakan skrip Python (`populate_db.py`).
*   **Desain Responsif:** Antarmuka pengguna dirancang agar fungsional di berbagai ukuran layar.

## Teknologi yang Digunakan

*   **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Migrate
*   **Database:** SQLite
*   **Frontend:** HTML, CSS, JavaScript
*   **Sumber Data:** `PeriodicTableJSON.json` untuk data awal unsur.

## Struktur Proyek

Proyek ini secara umum mengikuti pola MVC (Model-View-Controller).

```
project-final/
├── periodic_table_app/         # Direktori aplikasi utama
│   ├── app/                    # Paket inti aplikasi
│   │   ├── __init__.py         # Inisialisasi aplikasi Flask, ekstensi
│   │   ├── models.py           # Model database (Unsur)
│   │   ├── routes.py           # Logika controller, endpoint API
│   │   ├── forms.py            # Definisi WTForms
│   │   ├── static/             # CSS, JavaScript, gambar
│   │   │   └── css/style.css
│   │   └── templates/          # Template HTML
│   │       ├── layout.html
│   │       ├── index.html
│   │       ├── element_view.html
│   │       ├── create_element.html
│   │       ├── edit_element.html
│   │       ├── element_list.html
│   │       ├── compare_elements.html
│   │       └── macros.html
│   ├── migrations/             # Skrip migrasi database Flask-Migrate
│   ├── image/                  # Direktori untuk gambar screenshot aplikasi (BARU DIPINDAHKAN KE SINI)
│   │   ├── Screenshot 2025-05-30 at 23.19.54.png
│   │   ├── Screenshot 2025-05-30 at 23.20.09.png
│   │   └── Screenshot 2025-05-30 at 23.20.30.png
│   ├── run.py                  # Titik masuk untuk menjalankan aplikasi Flask
│   ├── config.py               # Konfigurasi aplikasi (URI DB, Kunci Rahasia)
│   ├── populate_db.py          # Skrip untuk mengisi database
│   └── PeriodicTableJSON.json  # Data mentah unsur
├── requirements.txt            # Dependensi Python
├── .gitignore                  # File yang akan diabaikan oleh Git
└── README.md                   # File ini
```
*(Catatan: Lingkungan virtual `.venv` diharapkan berada satu tingkat di atas `project-final/`, contohnya di `sql/project/.venv`)*

## Prasyarat

*   Python (versi 3.8+ direkomendasikan)
*   `pip` (pengelola paket Python)
*   `git` (untuk kloning repositori)

## Pengaturan dan Instalasi

1.  **Kloning repositori:**
    ```bash
    git clone <url-repositori-anda>
    cd project-final
    ```

2.  **Atur dan aktifkan lingkungan virtual:**
    Proyek ini mengharapkan lingkungan virtual (`.venv`) berada di direktori induk dari `project-final` (misalnya `sql/project/.venv`).

    *   Jika Anda berada di direktori `project-final`:
        ```bash
        # Buat .venv di direktori induk jika belum ada
        # python -m venv ../.venv # Hilangkan komentar dan jalankan jika .venv belum ada di induk

        # Aktifkan lingkungan virtual (dari direktori project-final)
        source ../.venv/bin/activate  # Pada Linux/macOS
        # ..\\.venv\\Scripts\\activate  # Pada Windows
        ```

3.  **Instal dependensi:**
    (Pastikan lingkungan virtual Anda aktif dan Anda berada di direktori `project-final`)
    ```bash
    pip install -r requirements.txt
    ```

## Pengaturan Database

Semua perintah database harus dijalankan dari direktori `periodic_table_app`, dengan lingkungan virtual aktif.

1.  **Navigasi ke direktori aplikasi:**
    ```bash
    cd periodic_table_app
    ```

2.  **Inisialisasi Flask-Migrate (jika baru pertama kali mengatur):**
    Langkah ini hanya diperlukan jika folder `migrations` belum ada di `periodic_table_app/`.
    ```bash
    flask db init
    ```

3.  **Buat migrasi database:**
    Jika Anda baru saja menjalankan `flask db init` atau melakukan perubahan pada `models.py`:
    ```bash
    flask db migrate -m "Pengaturan awal database"
    ```
    *(Gunakan pesan yang deskriptif untuk migrasi berikutnya.)*

4.  **Terapkan migrasi ke database:**
    Ini akan membuat/memperbarui file SQLite `app.db`.
    ```bash
    flask db upgrade
    ```

## Mengisi Database

Set data unsur awal dimuat dari `PeriodicTableJSON.json`.

1.  Pastikan Anda berada di direktori `project-final/periodic_table_app/`.
2.  Pastikan lingkungan virtual Anda aktif.
3.  Jalankan skrip populasi:
    ```bash
    python populate_db.py
    ```
    Ini akan mengisi tabel `element` di database `app.db` Anda.

## Menjalankan Aplikasi

1.  Pastikan Anda berada di direktori `project-final/periodic_table_app/`.
2.  Pastikan lingkungan virtual Anda (`../.venv` relatif terhadap `project-final`) aktif.
    ```bash
    # Jika belum aktif dan Anda berada di periodic_table_app/
    # source ../../.venv/bin/activate # Linux/macOS
    # ..\\..\\.venv\\Scripts\\activate # Windows
    ```
3.  Mulai server pengembangan Flask:
    ```bash
    python run.py
    ```
4.  Buka browser web Anda dan navigasikan ke `http://127.0.0.1:5000/`.

## Cara Menggunakan

*   **Halaman Utama (`/` atau `/index`):**
    *   **Lihat Tabel:** Tabel periodik utama ditampilkan. Unsur-unsur ditata berdasarkan jenisnya.
    *   **Arahkan Kursor untuk Tooltip:** Arahkan kursor ke unsur mana pun untuk melihat tampilan cepat nomor atom, simbol, dan namanya.
    *   **Klik untuk Detail:** Mengklik sebuah unsur akan mengarahkan Anda ke halaman detail lengkap unsur tersebut.
    *   **Pencarian:** Gunakan bilah pencarian di bagian atas untuk memfilter unsur berdasarkan nama atau simbol secara *real-time*.
    *   **Filter berdasarkan Jenis:** Klik tombol di bawah bilah pencarian (misalnya, "Logam Alkali", "Gas Mulia") untuk memfilter unsur yang ditampilkan berdasarkan jenisnya. Klik "Semua Jenis" untuk mereset.
    *   **Navigasi:** Gunakan bilah navigasi atas untuk pergi ke "Kelola Unsur", "Bandingkan Unsur", atau "Tambah Unsur Baru".

*   **Halaman Detail Unsur (`/element/view/<nomor_atom>`):**
    *   Diakses dengan mengklik unsur pada tabel utama atau dari halaman "Kelola Unsur".
    *   Menampilkan semua informasi yang tersedia untuk satu unsur, termasuk gambar (jika ada), konfigurasi kulit elektron, dan energi ionisasi, disajikan dalam format terstruktur.

*   **Tambah Unsur Baru (`/element/new`):**
    *   Dapat diakses melalui tombol "Tambah Unsur Baru" di navigasi/layout.
    *   Menyediakan formulir untuk memasukkan semua detail relevan untuk unsur kimia baru. Bidang termasuk nomor atom, simbol, nama, fase, jenis, dan berbagai sifat fisik.
    *   Termasuk validasi formulir untuk memastikan integritas data (misalnya, nomor atom dan simbol harus unik).

*   **Edit Unsur (`/element/edit/<nomor_atom>`):**
    *   Dapat diakses dari halaman detail unsur atau halaman "Kelola Unsur".
    *   Formulir sudah diisi sebelumnya dengan data unsur yang dipilih saat ini, memungkinkan modifikasi.

*   **Halaman Kelola Unsur (`/elements`):**
    *   Mencantumkan semua unsur dari database dalam tabel yang dapat diurutkan dan difilter.
    *   **Pencarian Tabel:** Gunakan bidang input untuk memfilter tabel berdasarkan nama atau simbol.
    *   **Urutkan Kolom:** Klik pada header kolom (misalnya, "Nama", "Nomor Atom") untuk mengurutkan tabel.
    *   **Tindakan:** Setiap baris menyediakan tautan/tombol untuk "Lihat" halaman unsur lengkap, "Edit" unsur, atau "Hapus" unsur.

*   **Halaman Bandingkan Unsur (`/compare`):**
    *   Memungkinkan pemilihan hingga tiga unsur berbeda dari daftar dropdown.
    *   Setelah mengirimkan pilihan, menampilkan perbandingan berdampingan dari properti unsur yang dipilih dalam format kisi, memudahkan untuk melihat perbedaan dan kesamaan.

## Tangkapan Layar

Berikut adalah beberapa tangkapan layar dari aplikasi:

![Tampilan Utama Tabel Periodik](image/Screenshot%202025-05-30%20at%2023.19.54.png)
*Tampilan utama tabel periodik dengan unsur-unsur, pencarian, dan filter.*

![Tampilan Detail Unsur](image/Screenshot%202025-05-30%20at%2023.20.09.png)
*Halaman khusus yang menampilkan informasi rinci untuk sebuah unsur dan proses CRUD.*

![Halaman Kelola Unsur](image/Screenshot%202025-05-30%20at%2023.20.30.png)
*Halaman Kelola perbandingan Unsur dengan tabel yang dapat diurutkan dan difilter.*

