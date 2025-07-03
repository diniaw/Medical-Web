from Models.models import PoliKlinik
from Controllers import db
from flask import request, redirect, url_for, flash

#mengambil semua data
def Poliklinik_index():
    polis = PoliKlinik.query.all()
    return polis


def add_poli():
    if request.method == 'POST':  # Memeriksa apakah permintaan adalah metode POST (dikirim setelah formulir disubmit)
        id_poli = request.form.get('ID_Poli')  # Mengambil data Id poli yang dikirim melalui formulir
        nama_poli = request.form.get('Nama_Poli')  # Mengambil data nama poli yang dikirim melalui formulir
        gedung = request.form.get('Gedung')  # Mengambil data gedung yang dikirim melalui formulir

        if not id_poli or not nama_poli or not gedung:  # Memeriksa apakah nama data kosong
            flash("Data Obat harus diisi!", "error")  # Menampilkan pesan error jika ada kolom yang kosong
            return redirect(url_for('tambah_poli'))  # Mengarahkan kembali ke halaman tambah poliklinik

        # Membuat instance baru dari Item (objek poli) dengan data yang diterima
        new_item = PoliKlinik(ID_Poli=id_poli, Nama_Poli=nama_poli, Gedung=gedung)  
        db.session.add(new_item)  # Menambahkan objek baru ke sesi database
        db.session.commit()  # Menyimpan perubahan ke database
        flash("Poliklinik Baru berhasil ditambahkan!", "success")  # Menampilkan pesan sukses jika poli berhasil ditambahkan
        return redirect(url_for('Poliklinik'))  # Mengarahkan ke halaman daftar poli setelah berhasil menambah

def delete_poli(poli_id):
    poli_delete = PoliKlinik.query.get(poli_id)  # Mengambil data poli berdasarkan ID_Poli
    if not poli_delete:  # Memeriksa apakah data poli ada
        flash("Data Poliklinik tidak ditemukan!", "error")  # Menampilkan pesan error jika data poli tidak ditemukan
        return redirect(url_for('Poliklinik'))
    
    db.session.delete(poli_delete)  # Menghapus data poli
    db.session.commit()  # Menyimpan perubahan
    flash("Poliklinik berhasil dihapus!", "success")  # Menampilkan pesan sukses jika poli berhasil dihapus
    return redirect(url_for('Poliklinik'))  # Mengarahkan ke halaman daftar poli

def edit_poli(poli_id):
    edit_poliklinik = PoliKlinik.query.get(poli_id)  # Mengambil data poli berdasarkan ID_Poli
    if not edit_poliklinik:  # Memeriksa apakah data poli ada
        flash("Data Poliklinik tidak ditemukan!", "error")  # Menampilkan pesan error jika data poli tidak ditemukan
        return redirect(url_for('Poliklinik'))
    if request.method == 'POST':
        id_poli = request.form.get('ID_Poli')
        nama_poli = request.form.get('Nama_Poli')
        gedung = request.form.get('Gedung')
        if not id_poli or not nama_poli or not gedung:
            flash("Data poliklinik harus diisi!", "error")
            return redirect(url_for('edit_poli', poli_id=poli_id))
        
        edit_poliklinik.ID_Poli = id_poli
        edit_poliklinik.Nama_Poli = nama_poli
        edit_poliklinik.Gedung = gedung
        db.session.commit()
        flash("Data Poliklinik berhasil diubah!", "success")
        return redirect(url_for('Poliklinik'))
    return edit_poliklinik
