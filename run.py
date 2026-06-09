import os
import sys
from app import create_app, db
from app.models import User, Kategori, Dokumen, Download, LogAktivitas

app = create_app(os.getenv('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Kategori': Kategori,
        'Dokumen': Dokumen,
        'Download': Download,
        'LogAktivitas': LogAktivitas
    }

@app.cli.command()
def init_db():
    """Initialize database with default data."""
    with app.app_context():
        db.create_all()
        print('Database initialized')
        
        # Create default admin user
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                nama='Administrator',
                username='admin',
                email='admin@erepository.com',
                role='administrator',
                jabatan='Administrator',
                unit_kerja='IT Department'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Default admin user created (username: admin, password: admin123)')
        
        # Create default categories
        categories = [
            ('Skripsi', 'Tugas akhir mahasiswa program S1'),
            ('Tesis', 'Tugas akhir mahasiswa program S2'),
            ('Disertasi', 'Tugas akhir mahasiswa program S3'),
            ('Artikel Jurnal', 'Artikel yang diterbitkan di jurnal'),
            ('Prosiding', 'Makalah dalam prosiding seminar/konferensi'),
            ('Buku', 'Buku dan buku teks'),
            ('Modul Pembelajaran', 'Materi pembelajaran dan modul ajar'),
            ('Laporan Penelitian', 'Laporan hasil penelitian'),
            ('Laporan Pengabdian', 'Laporan kegiatan pengabdian kepada masyarakat'),
            ('Surat Keputusan', 'Dokumen surat keputusan resmi'),
            ('Dokumen Administrasi', 'Dokumen administrasi dan tata usaha'),
            ('Arsip Digital', 'Dokumen arsip yang telah digitalisasi')
        ]
        
        for nama, deskripsi in categories:
            if not Kategori.query.filter_by(nama_kategori=nama).first():
                kategori = Kategori(nama_kategori=nama, deskripsi=deskripsi)
                db.session.add(kategori)
        
        db.session.commit()
        print('Default categories created')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
