from Controllers import db
from sqlalchemy import Enum, Text


class Pasien(db.Model):
    __tablename__ = 'pasien'
    ID_Pasien = db.Column(db.String(50), primary_key=True)
    Nomor_Identitas = db.Column(db.String(30), nullable=False)
    Nama_Pasien = db.Column(db.String(80), nullable=False)
    Jenis_Kelamin = db.Column(Enum("L","P"), nullable=False)
    Alamat = db.Column(db.Text, nullable=False)
    No_Telepon = db.Column(db.String(15), nullable=False)

class Dokter(db.Model):
    _tablename_ = 'dokter'
    ID_Dokter = db.Column(db.String(50), primary_key=True)
    Nama_Dokter = db.Column(db.String(80), nullable=False)
    Spesialis = db.Column(db.String(50), nullable=False)
    Hari = db.Column(db.String(20), nullable=False)
    Jam_Mulai = db.Column(db.Time, nullable=False)
    Jam_Selesai = db.Column(db.Time, nullable=False)
    No_Telp = db.Column(db.String(15), nullable=False)

class Rekammedis(db.Model):
    __tablename__='rekam_medis'
    ID_RM = db.Column(db.String(50), primary_key=True)
    ID_Pasien = db.Column(db.String(50), nullable=False)
    Keluhan = db.Column(db.Text, nullable=False)
    ID_Dokter = db.Column(db.String(50), nullable=False)
    Diagnosa = db.Column(Text, nullable=False)
    ID_Poli = db.Column(db.String(50), nullable=False)
    Tgl_Periksa = db.Column(db.Date, nullable=False)

# Mendefinisikan relasi ke RM_Obat
    rm_obat = db.relationship('RM_Obat', backref='rekammedis', lazy=True)
    
    
class PoliKlinik(db.Model):
    __tablename__='poliklinik'
    ID_Poli = db.Column(db.String(50), primary_key=True)
    Nama_Poli = db.Column(db.String(50), nullable=False)
    Gedung = db.Column(db.String(80), nullable=False)

class Obate(db.Model):
    __tablename__='obat'
    ID_Obat = db.Column(db.String(50), primary_key=True)
    Nama_Obat = db.Column(db.String(200), nullable=False)
    Keterangan_Obat = db.Column(Text, nullable=False)
    # Mendefinisikan relasi ke RM_Obat
    rm_obat = db.relationship('RM_Obat', backref='obat', lazy=True)
    

class RM_Obat(db.Model):
    __tablename__='rm_obat'
    ID_RM_Obat = db.Column(db.Integer, primary_key=True)
   # foreign key untuk kolom ID_RM yang mengacu ke Rekammedis
    ID_RM = db.Column(db.String(50), db.ForeignKey('rekam_medis.ID_RM'), nullable=False)
    # foreign key untuk kolom ID_Obat yang mengacu ke Obat
    ID_Obat = db.Column(db.String(50), db.ForeignKey('obat.ID_Obat'), nullable=False)
    
