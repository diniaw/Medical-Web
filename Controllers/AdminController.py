from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, flash
from Models.AdminModel import User
from Controllers import db
from flask_login import login_user, logout_user

# Fungsi untuk menangani proses pendaftaran (signup)
def signup_post():
    if request.method == 'POST':
        # Mengambil data username dan password dari form
        username = request.form.get('username')
        password = request.form.get('password')

        # Debug: Cetak data yang diterima
        print("DEBUG - Username:", username)
        print("DEBUG - Password:", password)

        # Pastikan data tidak kosong
        if not username or not password:
            flash("Username dan password tidak boleh kosong!", "error")
            return redirect(url_for('signup'))

        # Mengecek apakah username sudah ada
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username sudah terdaftar, silakan coba dengan username lain!", "error")
            return redirect(url_for('signup'))

        # Membuat pengguna baru dengan password yang telah di-hash
        new_user = User(
            username=username,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )

        # Menyimpan data ke database
        db.session.add(new_user)
        db.session.commit()

        flash("Pendaftaran berhasil! Silakan login.", "success")
        return redirect(url_for('login'))

# Fungsi untuk menangani proses login
def login_post():
    if request.method == 'POST':
        # Mengambil data username dan password dari form yang dikirimkan
        username = request.form.get('username')
        password = request.form.get('password')

        # Mencari pengguna berdasarkan username yang dimasukkan
        user = User.query.filter_by(username=username).first()

        if user is None:
            flash("Username tidak ditemukan.", "error")
            return redirect(url_for('login'))  # Jika username tidak ditemukan, kembali ke halaman login
        
        # Mengecek apakah password yang dimasukkan sesuai dengan yang ada di database
        if check_password_hash(user.password, password):
            login_user(user)  # Jika password benar, lakukan proses login
            flash("Login berhasil!", "success")
            return redirect(url_for('Home'))  # Jika login berhasil, arahkan ke halaman home
        else:
            flash("Password salah. Silakan coba lagi.", "error")
            return redirect(url_for('login'))  # Jika password salah, kembali ke halaman login

# Fungsi untuk menangani proses logout
def logout():
    logout_user()  # Melakukan proses logout
    # Menampilkan pesan bahwa pengguna telah logout dan mengarahkan kembali ke halaman login
    flash("Anda berhasil logout.", "info")
    return redirect(url_for('login'))
