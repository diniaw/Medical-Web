from Models.models import RM_Obat, Rekammedis, Obate
from Controllers import db
from flask import request, redirect, url_for, flash

#mengambil semua data
def RM_Obat_index():
    rm_obat = RM_Obat.query.all()
    return rm_obat

def add_rm_obat():
    if request.method == 'POST':  # Memeriksa apakah permintaan adalah metode POST (dikirim setelah formulir disubmit)
        id_rm_obat = request.form.get('ID_RM_Obat')  # Mengambil data Id RM Obat yang dikirim melalui formulir
        id_rm = request.form.get('ID_RM')  # Mengambil data Id RM yang dikirim melalui formulir
        id_obat = request.form.get('ID_Obat')  # Mengambil data ID_Obat yang dikirim melalui formulir

        if not id_rm_obat or not id_rm or not id_obat:  # Memeriksa apakah nama data kosong
            flash("Data Rekam Medis Obat harus diisi!", "error")  # Menampilkan pesan error jika ada kolom yang kosong
            return redirect(url_for('tambah_rm_obat'))  # Mengarahkan kembali ke halaman tambah rm obat
        
        # Validasi foreign key:
        # Pastikan Rekammedis dengan id_rm ada
        if not Rekammedis.query.get(id_rm):
            flash(f"Rekam Medis dengan ID {id_rm} tidak ditemukan!", "error")
            return redirect(url_for('tambah_rm_obat'))
        # Pastikan Obat dengan id_obat ada
        if not Obate.query.get(id_obat):
            flash(f"Obat dengan ID {id_obat} tidak ditemukan!", "error")
            return redirect(url_for('tambah_rm_obat'))
        
        # Membuat instance baru dari Item (objek) dengan data yang diterima
        new_item = RM_Obat(ID_RM_Obat=id_rm_obat, ID_RM=id_rm, ID_Obat=id_obat)  
        db.session.add(new_item)  # Menambahkan objek baru ke sesi database
        db.session.commit()  # Menyimpan perubahan ke database
        flash("Rekam Medis Obat berhasil ditambahkan!", "success")  # Menampilkan pesan sukses jika rm obat berhasil ditambahkan
        return redirect(url_for('RM_Obat'))  # Mengarahkan ke halaman obat setelah berhasil menambah

def delete_rm_obat(rm_obat_id):
    rm_obat_delete = RM_Obat.query.get(rm_obat_id)  # Mengambil data rm obat berdasarkan ID_RM_Obat
    if not rm_obat_delete:  # Memeriksa apakah data rm obat ada
        flash("Data Rekam Medis Obat tidak ditemukan!", "error")  # Menampilkan pesan error jika data rm obat tidak ditemukan
        return redirect(url_for('RM_Obat'))
    
    db.session.delete(rm_obat_delete)  # Menghapus data rm obat
    db.session.commit()  # Menyimpan perubahan
    flash("Data Rekam Medis Obat berhasil dihapus!", "success")  # Menampilkan pesan sukses jika rm obat berhasil dihapus
    return redirect(url_for('RM_Obat'))  # Mengarahkan ke halaman daftar

def edit_rm_obat(rm_obat_id):
    rm_obat_edit = RM_Obat.query.get(rm_obat_id) #mengambil data rm obat berdasarkan ID_RM_Obat
    if not rm_obat_edit:  # Memeriksa apakah data rm obat
        flash("Data Rekam Medis Obat tidak ditemukan!", "error")  # Menampilkan pesan error jika data rm obat tidak ditemukan
        return redirect(url_for('RM_Obat'))
    if request.method == 'POST':
        id_rm_obat = request.form.get('ID_RM_Obat')
        id_rm = request.form.get('ID_RM')
        id_obat = request.form.get('ID_Obat')
        if not id_rm_obat or not id_rm or not id_obat:
            flash("Data Rekam Medis Obat harus diisi!", "error")
            return redirect(url_for('edit_rmobat', rm_obat_id=rm_obat_id))
        
        # Validasi foreign key
        if not Rekammedis.query.get(id_rm):
            flash(f"Rekam Medis dengan ID {id_rm} tidak ditemukan!", "error")
            return redirect(url_for('edit_rm_obat', rm_obat_id=rm_obat_id))
        if not Obate.query.get(id_obat):
            flash(f"Obat dengan ID {id_obat} tidak ditemukan!", "error")
            return redirect(url_for('edit_rm_obat', rm_obat_id=rm_obat_id))
        
        rm_obat_edit.ID_RM_Obat = id_rm_obat
        rm_obat_edit.ID_RM = id_rm
        rm_obat_edit.ID_Obat = id_obat
        db.session.commit()
        flash("Data Rekam Medis Obat berhasil diubah!", "success")
        return redirect(url_for('RM_Obat'))
    return rm_obat_edit
  
