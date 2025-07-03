from Models.models import Rekammedis, Dokter, Pasien, PoliKlinik, RM_Obat
from Controllers import db
from flask import request, redirect, url_for, flash

#mengambil semua data
def index_rm():
    rmrs = Rekammedis.query.all()
    return rmrs

def add_rm():
    if request.method == 'POST':
        id_rm = request.form.get('ID_RM')
        id_pasien = request.form.get('ID_Pasien')
        keluhan = request.form.get('Keluhan')
        id_dokter = request.form.get('ID_Dokter')
        diagnosa = request.form.get('Diagnosa')
        id_poli = request.form.get('ID_Poli')
        tgl_periksa = request.form.get('Tgl_Periksa')

        # Validasi biar semua field diisi
        if not id_rm or not id_pasien or not keluhan or not id_dokter or not diagnosa or not id_poli or not tgl_periksa:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('tambah_rm'))
        
                # Validasi foreign key:
        # Pastikan dokter dengan id_dokter ada
        if not Dokter.query.get(id_dokter):
            flash(f"Dokter dengan ID {id_dokter} tidak ditemukan!", "error")
            return redirect(url_for('tambah_rm'))
        # Pastikan pasien dengan id_pasien ada
        if not Pasien.query.get(id_pasien):
            flash(f"Pasien dengan ID {id_pasien} tidak ditemukan!", "error")
            return redirect(url_for('tambah_rm'))
        # Pastikan Poliklinik dengan id_poli ada
        if not PoliKlinik.query.get(id_poli):
            flash(f"Poliklinik dengan ID {id_poli} tidak ditemukan!", "error")
            return redirect(url_for('tambah_rm'))

        # Membuat instance baru dari Rekammedis
        new_rm = Rekammedis(
            ID_RM=id_rm,
            ID_Pasien=id_pasien,
            Keluhan=keluhan,
            ID_Dokter=id_dokter,
            Diagnosa=diagnosa,
            ID_Poli=id_poli,
            Tgl_Periksa=tgl_periksa
        )

        # Simpan ke database
        db.session.add(new_rm)
        db.session.commit()
        flash("Data Rekam Medis berhasil ditambahkan!", "success")
        return redirect(url_for('tabel_rm'))

def delete_rm(ID_RM):
    rm_to_delete = Rekammedis.query.get(ID_RM)

    if not rm_to_delete:
        flash("Data Rekam Medis tidak ditemukan!", "error")
        return redirect(url_for('tabel_rm'))

    db.session.delete(rm_to_delete)
    db.session.commit()
    flash("Data Rekam Medis berhasil dihapus!", "success")
    return redirect(url_for('tabel_rm'))

def edit_rm(ID_RM):
    edit_rmm = Rekammedis.query.get(ID_RM)

    if not edit_rmm:
        flash("Data Rekam Medis tidak ditemukan!", "error")
        return redirect(url_for('tabel_rm'))

    if request.method == 'POST':
        # Ambil data dari form
        id_rm = request.form.get('ID_RM')
        id_pasien = request.form.get('ID_Pasien')
        keluhan = request.form.get('Keluhan')
        id_dokter = request.form.get('ID_Dokter')
        diagnosa = request.form.get('Diagnosa')
        id_poli = request.form.get('ID_Poli')
        tgl_periksa = request.form.get('Tgl_Periksa')

        if not id_rm or not id_pasien or not keluhan or not id_dokter or not diagnosa or not id_poli or not tgl_periksa:
            flash("field tidak boleh kosong, harus diisi!", "error")
            return redirect(url_for('edit_rm', ID_RM=ID_RM))

        edit_rmm.ID_RM = id_rm
        edit_rmm.ID_Pasiem = id_pasien
        edit_rmm.Keluhan = keluhan
        edit_rmm.ID_Dokter = id_dokter
        edit_rmm.Diagnosa = diagnosa
        edit_rmm.ID_Poli = id_poli
        edit_rmm.Tgl_Periksa = tgl_periksa

        db.session.commit()
        flash("Data Rekam Medis berhasil diperbarui!", "success")
        return redirect(url_for('tabel_rm'))
    return edit_rmm