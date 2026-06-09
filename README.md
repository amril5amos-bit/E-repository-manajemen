# E-Repository Manajemen

Aplikasi E-Repository untuk manajemen dokumen digital dengan teknologi Python Flask, SQLite, Bootstrap 5, dan Chart.js.

## Fitur Utama

### 1. Dashboard
- Total Dokumen, Pengguna, Download, dan Kategori
- Grafik Upload Dokumen dan Pengunjung
- Dokumen Terbaru dan Terpopuler

### 2. Manajemen Pengguna
- CRUD Pengguna
- Role-Based Access Control (Admin, Operator, User)
- Hak Akses Berbeda per Role

### 3. Manajemen Repository
- CRUD Dokumen
- Upload PDF, DOCX, XLSX
- Preview PDF dan Download
- Cetak Metadata

### 4. Klasifikasi Dokumen
- 12 Kategori Dokumen
- Manajemen Kategori

### 5. Pencarian Dokumen
- Pencarian berdasarkan Judul, Penulis, Kata Kunci
- Filter Kategori

### 6. Statistik & Laporan
- Statistik Upload, Download, Viewer
- Grafik per Kategori
- Export PDF, Excel, CSV

### 7. Keamanan
- Autentikasi Login/Logout
- Reset Password
- Backup Database dan File

## Teknologi

- **Backend**: Python Flask
- **Database**: SQLite + SQLAlchemy
- **Frontend**: Bootstrap 5
- **Grafik**: Chart.js
- **PDF Preview**: PDF.js
- **Login**: Flask-Login
- **Upload**: Flask-Upload
- **Export Excel**: OpenPyXL

## Setup & Instalasi

```bash
# 1. Clone repository
git clone https://github.com/amril5amos-bit/e-repository-manajemen.git
cd e-repository-manajemen

# 2. Buat virtual environment
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan aplikasi
python run.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## Default User

- **Username**: admin
- **Password**: admin123

## Struktur Project

```
e-repository-manajemen/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── kategori.py
│   │   ├── dokumen.py
│   │   ├── download.py
│   │   └── log_aktivitas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── users.py
│   │   ├── dokumen.py
│   │   ├── kategori.py
│   │   ├── search.py
│   │   ├── reports.py
│   │   └── backup.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   ├── users/
│   │   ├── dokumen/
│   │   └── reports/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── uploads/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   ├── helpers.py
│   │   └── validators.py
│   └── forms.py
├── migrations/
├── tests/
├── config.py
├── requirements.txt
└── run.py
```
