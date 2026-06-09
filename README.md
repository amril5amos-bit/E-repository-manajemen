# E-Repository Manajemen

Aplikasi E-Repository Manajemen adalah sistem manajemen dokumen digital yang dirancang untuk mengelola berbagai jenis dokumen seperti skripsi, tesis, artikel jurnal, dan dokumen lainnya dengan fitur pencarian, download, dan manajemen pengguna.

## Fitur Utama

### 1. Dashboard
- Total dokumen, pengguna, download, dan kategori
- Grafik upload dokumen dan pengunjung
- Dokumen terbaru dan terpopuler

### 2. Manajemen Pengguna
- Kelola data pengguna (CRUD)
- 3 Role: Administrator, Operator, User/Pengunjung
- Hak akses berbeda untuk setiap role

### 3. Manajemen Repository
- CRUD Dokumen
- Upload PDF, DOCX, XLSX
- Preview PDF
- Download dokumen

### 4. Klasifikasi Dokumen
- 12 kategori dokumen
- Filter berdasarkan kategori

### 5. Pencarian Dokumen
- Pencarian sederhana: Judul, Penulis, Kata Kunci

### 6. Statistik dan Laporan
- Statistik upload, download, viewer
- Laporan dokumen dan pengguna
- Export ke PDF, Excel, CSV

### 7. Keamanan
- Autentikasi login
- Reset password
- Backup database

## Teknologi

- Backend: Python Flask
- Database: SQLite
- Frontend: Bootstrap 5
- Grafik: Chart.js
- PDF Preview: PDF.js
- ORM: SQLAlchemy
- Login: Flask-Login
- Export: OpenPyXL

## Instalasi

1. Clone repository:
   ```bash
   git clone <repository-url>
   cd e-repository-manajemen
   ```

2. Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\\Scripts\\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```bash
   cp .env.example .env
   ```

5. Jalankan aplikasi:
   ```bash
   python run.py
   ```

6. Akses aplikasi di: `http://localhost:5000`

## Default Login

- Username: `admin`
- Password: `admin123`

## Struktur Database

### Tabel Users
- id (INTEGER PRIMARY KEY)
- nama (TEXT)
- username (TEXT UNIQUE)
- email (TEXT UNIQUE)
- password (TEXT)
- role (TEXT) - 'admin', 'operator', 'user'
- jabatan (TEXT)
- unit_kerja (TEXT)
- created_at (DATETIME)

### Tabel Kategori
- id (INTEGER PRIMARY KEY)
- nama_kategori (TEXT UNIQUE)
- deskripsi (TEXT)

### Tabel Dokumen
- id (INTEGER PRIMARY KEY)
- judul (TEXT)
- penulis (TEXT)
- abstrak (TEXT)
- kata_kunci (TEXT)
- kategori_id (INTEGER FOREIGN KEY)
- tahun (INTEGER)
- file_pdf (TEXT)
- cover (TEXT)
- status (TEXT) - 'draft', 'published'
- created_at (DATETIME)
- updated_at (DATETIME)

### Tabel Download
- id (INTEGER PRIMARY KEY)
- dokumen_id (INTEGER FOREIGN KEY)
- user_id (INTEGER FOREIGN KEY)
- tanggal_download (DATETIME)

### Tabel LogAktivitas
- id (INTEGER PRIMARY KEY)
- user_id (INTEGER FOREIGN KEY)
- aktivitas (TEXT)
- waktu (DATETIME)

## Lisensi

MIT
