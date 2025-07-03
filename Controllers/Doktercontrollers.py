from Models.models import Dokter
from Controllers import db
from flask import request, redirect, url_for, flash, render_template
from sqlalchemy.exc import IntegrityError

#mengambil semua data
def index_dokter():
    dokters = Dokter.query.all()
    return dokters

def add_dokter():
    if request.method == 'POST':
        id_dokter = request.form.get('ID_Dokter')
        nama_dokter = request.form.get('Nama_Dokter')
        spesialis = request.form.get('Spesialis')
        hari = request.form.get('Hari')
        jam_mulai = request.form.get('Jam_Mulai')
        jam_selesai = request.form.get('Jam_Selesai')
        no_telp = request.form.get('No_Telp')

        # Validasi biar semua field diisi
        if not id_dokter or not nama_dokter or not spesialis or not hari or not jam_mulai or not jam_selesai or not no_telp:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('tambah_dokter'))

        # Membuat instance baru dari Dokter
        new_dokter = Dokter(ID_Dokter=id_dokter,Nama_Dokter=nama_dokter,Spesialis=spesialis,Hari=hari,Jam_Mulai=jam_mulai,Jam_Selesai=jam_selesai,No_Telp=no_telp)

        try:
            db.session.add(new_dokter)
            db.session.commit()
            flash("Data Dokter berhasil ditambahkan!", "success")
        except IntegrityError:
            db.session.rollback()
            flash(f"Error: Data dokter dengan ID '{id_dokter}' sudah ada.", "danger")
        return redirect(url_for('tabel_dokter'))
    
    return render_template('Tambahdokter.html')


def delete_dokter(ID_Dokter):
    dokter_to_delete = Dokter.query.get(ID_Dokter)

    if not dokter_to_delete:
        flash("Data Dokter tidak ditemukan!", "error")
        return redirect(url_for('tabel_dokter'))

    db.session.delete(dokter_to_delete)
    db.session.commit()
    flash("Data Dokter berhasil dihapus!", "success")
    return redirect(url_for('tabel_dokter'))

def edit_dokter(ID_Dokter):
    edit_dokterr = Dokter.query.get(ID_Dokter)

    if not edit_dokterr:
        flash("Data Dokter tidak ditemukan!", "error")
        return redirect(url_for('tabel_dokter'))

    if request.method == 'POST':
        # Ambil data dari form
        id_dokter = request.form.get('ID_Dokter')
        nama_dokter = request.form.get('Nama_Dokter')
        spesialis = request.form.get('Spesialis')
        hari = request.form.get('Hari')
        jam_mulai = request.form.get('Jam_Mulai')
        jam_selesai = request.form.get('Jam_Selesai')
        no_telp = request.form.get('No_Telp')

        if not id_dokter or not nama_dokter or not spesialis or not hari or not jam_mulai or not jam_selesai or not no_telp:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('edit_dokter', ID_Dokter=ID_Dokter))

        edit_dokterr.ID_Dokter = id_dokter
        edit_dokterr.Nama_Dokter = nama_dokter
        edit_dokterr.Spesialis = spesialis
        edit_dokterr.Hari = hari
        edit_dokterr.Jam_Mulai = jam_mulai
        edit_dokterr.Jam_Selesai = jam_selesai
        edit_dokterr.No_Telp = no_telp
        
  
        db.session.commit()
        flash("Data Dokter berhasil diperbarui!", "success")
        return redirect(url_for('tabel_dokter'))
    return edit_dokterr