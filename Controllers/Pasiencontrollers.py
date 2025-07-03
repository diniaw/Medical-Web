from Models.models import Pasien
from Controllers import db
from flask import request, redirect, url_for, flash

#mengambil semua data
def index_pasien():
    pasienrs = Pasien.query.all()
    return pasienrs

def add_pasien():
    if request.method == 'POST':
        id_pasien = request.form.get('ID_Pasien')
        nomor_identitas = request.form.get('Nomor_Identitas')
        nama_pasien = request.form.get('Nama_Pasien')
        jenis_kelamin = request.form.get('Jenis_Kelamin')
        alamat = request.form.get('Alamat')
        no_telepon = request.form.get('No_Telepon')

        # Validasi biar semua field diisi
        if not id_pasien or not nomor_identitas or not nama_pasien or not jenis_kelamin or not alamat or not no_telepon:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('tambah_pasien'))

        # Membuat instance baru dari Dokter
        new_pasien = Pasien(
            ID_Pasien=id_pasien,
            Nomor_Identitas=nomor_identitas,
            Nama_Pasien=nama_pasien,
            Jenis_Kelamin=jenis_kelamin,
            Alamat=alamat,
            No_Telepon=no_telepon
        )

        # Simpan ke database
        db.session.add(new_pasien)
        db.session.commit()
        flash("Data Pasien berhasil ditambahkan!", "success")
        return redirect(url_for('tabel_pasien'))

def delete_pasien(ID_Pasien):
    pasien_to_delete = Pasien.query.get(ID_Pasien)

    if not pasien_to_delete:
        flash("Data Pasien tidak ditemukan!", "error")
        return redirect(url_for('tabel_pasien'))

    db.session.delete(pasien_to_delete)
    db.session.commit()
    flash("Data Pasien berhasil dihapus!", "success")
    return redirect(url_for('tabel_pasien'))

def edit_pasien(ID_Pasien):
    edit_pasienn = Pasien.query.get(ID_Pasien)

    if not edit_pasienn:
        flash("Data Pasien tidak ditemukan!", "error")
        return redirect(url_for('tabel_pasien'))

    if request.method == 'POST':
        # Ambil data dari form
        id_pasien = request.form.get('ID_Pasien')
        nomor_identitas = request.form.get('Nomor_Identitas')
        nama_pasien = request.form.get('Nama_Pasien')
        jenis_kelamin = request.form.get('Jenis_Kelamin')
        alamat = request.form.get('Alamat')
        no_telepon = request.form.get('No_Telepon')

        if not id_pasien or not nomor_identitas or not nama_pasien or not jenis_kelamin or not alamat or not no_telepon:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('edit_pasien', ID_Pasien=ID_Pasien))

        edit_pasienn.ID_Pasien = id_pasien
        edit_pasienn.Nomor_Identitas = nomor_identitas
        edit_pasienn.Nama_Pasien = nama_pasien 
        edit_pasienn.Jenis_Kelamin = jenis_kelamin
        edit_pasienn.Alamat = alamat
        edit_pasienn.No_Telepon = no_telepon

        db.session.commit()
        flash("Data Pasien berhasil diperbarui!", "success")
        return redirect(url_for('tabel_pasien'))

    return edit_pasienn
