from Models.models import Obate
from Controllers import db
from flask import request, redirect, url_for, flash

#mengambil semua data
def Obat_index():
    obat = Obate.query.all()
    return obat


def add_obat():
    if request.method == 'POST':  # Memeriksa apakah permintaan adalah metode POST (dikirim setelah formulir disubmit)
        id_obat = request.form.get('ID_Obat')  # Mengambil data Id obat yang dikirim melalui formulir
        nama_obat = request.form.get('Nama_Obat')  # Mengambil data nama obat yang dikirim melalui formulir
        ketobat = request.form.get('Keterangan_Obat')  # Mengambil data ket obat yang dikirim melalui formulir

        if not id_obat or not nama_obat or not ketobat:  # Memeriksa apakah nama data kosong
            flash("Data Obat harus diisi!", "error")  # Menampilkan pesan error jika ada kolom yang kosong
            return redirect(url_for('tambah_obat'))  # Mengarahkan kembali ke halaman tambah obat

        # Membuat instance baru dari Item (objek) dengan data yang diterima
        new_item = Obate(ID_Obat=id_obat, Nama_Obat=nama_obat, Keterangan_Obat=ketobat)  
        db.session.add(new_item)  # Menambahkan objek baru ke sesi database
        db.session.commit()  # Menyimpan perubahan ke database
        flash("Obat berhasil ditambahkan!", "success")  # Menampilkan pesan sukses jika obatberhasil ditambahkan
        return redirect(url_for('Obat'))  # Mengarahkan ke halaman obat setelah berhasil menambah

def delete_obat(obat_id):
    obat_delete = Obate.query.get(obat_id)  # Mengambil data obat berdasarkan ID_Obat
    if not obat_delete:  # Memeriksa apakah data obat ada
        flash("Data Obat tidak ditemukan!", "error")  # Menampilkan pesan error jika data obat tidak ditemukan
        return redirect(url_for('Obat'))
    
    db.session.delete(obat_delete)  # Menghapus data 
    db.session.commit()  # Menyimpan perubahan
    flash("Data Obat berhasil dihapus!", "success")  # Menampilkan pesan sukses jika obat berhasil dihapus
    return redirect(url_for('Obat'))  # Mengarahkan ke halaman daftar 

def edit_obat(obat_id):
    obat_edit = Obate.query.get(obat_id) #mengambil data obat berdasarkan ID_Obat
    if not obat_edit:  # Memeriksa apakah data obat
        flash("Data Obat tidak ditemukan!", "error")  # Menampilkan pesan error jika data obat tidak ditemukan
        return redirect(url_for('Obat'))
    if request.method == 'POST':
        id_obat = request.form.get('ID_Obat')
        nama_obat = request.form.get('Nama_Obat')
        Ketobat = request.form.get('Keterangan_Obat')
        if not id_obat or not nama_obat or not Ketobat:
            flash("Data Obat harus diisi!", "error")
            return redirect(url_for('edit_obat', obat_id=obat_id))
        
        obat_edit.ID_Obat = id_obat
        obat_edit.Nama_Obat = nama_obat
        obat_edit.Keterangan_Obat = Ketobat
        db.session.commit()
        flash("Data Obat berhasil diubah!", "success")
        return redirect(url_for('Obat'))
    return obat_edit
   
