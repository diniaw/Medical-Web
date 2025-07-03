from flask import Flask, render_template, request, redirect, url_for
from Controllers.Pasiencontrollers import index_pasien, add_pasien, delete_pasien, edit_pasien
from Controllers.Doktercontrollers import index_dokter, add_dokter, delete_dokter, edit_dokter
from Controllers.Rekammediscontrollers import index_rm, add_rm, delete_rm, edit_rm
from Controllers.poliklinikController import Poliklinik_index,add_poli,delete_poli,edit_poli
from Controllers.ObatController import Obat_index,add_obat,delete_obat,edit_obat 
from Controllers.RM_ObatController import RM_Obat_index,add_rm_obat,delete_rm_obat,edit_rm_obat
from config import Config
from Controllers.AdminController import signup_post, login_post, logout as logout_user_action, User 
from flask_login import LoginManager, login_user,login_required,logout_user,current_user
from Controllers import db
from Models.models import Rekammedis, Obate, Pasien, Dokter, PoliKlinik

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Inisialisasi LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect ke halaman login jika belum login

# Fungsi untuk memuat pengguna berdasarkan ID (user_loader)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required 
def Home():
    return render_template('Home.html')
    
#<====================Pasien====================>
@app.route('/pasien')
@login_required 
def tabel_pasien():
    pasienrs = index_pasien()
    return render_template('Pasien.html', pasienrs=pasienrs)

@app.route('/tambahpasien', methods=['GET', 'POST'])
@login_required 
def tambah_pasien():
    if request.method == 'POST':
        return add_pasien()
    return render_template('Tambahpasien.html')

@app.route("/delete_pasien/<ID_Pasien>")
@login_required 
def hapus_pasien(ID_Pasien):
    return delete_pasien(ID_Pasien)

@app.route('/edit_pasien/<ID_Pasien>', methods=['GET', 'POST'])
@login_required 
def ubah_pasien(ID_Pasien):
    if request.method == 'POST':
        return edit_pasien(ID_Pasien)
    ubahke_pasien = edit_pasien(ID_Pasien)
    return render_template('Editpasien.html', pasien=ubahke_pasien)

#<====================Dokter====================>
@app.route('/dokter')
@login_required 
def tabel_dokter():
    dokters = index_dokter()
    return render_template('Dokter.html', dokters=dokters)

@app.route('/tambahdokter', methods=['GET', 'POST'])
@login_required 
def tambah_dokter():
    if request.method == 'POST':
        return add_dokter()
    return render_template('Tambahdokter.html')

@app.route("/delete_dokter/<ID_Dokter>")
@login_required 
def hapus_dokter(ID_Dokter):
    return delete_dokter(ID_Dokter)

@app.route('/edit_dokter/<ID_Dokter>', methods=['GET', 'POST'])
@login_required 
def ubah_dokter(ID_Dokter):
    if request.method == 'POST':
        return edit_dokter(ID_Dokter)
    ubahke_dokter = edit_dokter(ID_Dokter)
    return render_template('Editdokter.html', dokter=ubahke_dokter)


#<====================Poliklinik====================>
@app.route('/Poliklinik')
@login_required 
def Poliklinik():
    polik = Poliklinik_index()
    return render_template('Poliklinik.html', polik=polik)

@app.route('/tambah_poli', methods=['GET', 'POST'])
@login_required 
def tambah_poli():
    if request.method == 'POST':
        return add_poli()
    return render_template('tambah_poli.html')

@app.route("/hapus_poli/<poli_id>")
@login_required 
def hapus_poli(poli_id):
    return delete_poli(poli_id)

@app.route('/edit_poliklinik/<poli_id>', methods=['GET', 'POST'])
@login_required 
def edit_poliklinik(poli_id):
    if request.method == 'POST':
        return edit_poli(poli_id)
    
    item_to_edit = edit_poli(poli_id)
    return render_template('edit_poli.html', polis=item_to_edit)


#<====================Obat====================>
@app.route('/obat')
@login_required 
def Obat():
    obat = Obat_index()
    return render_template('Obat.html', obat=obat)

@app.route('/tambah_obat', methods=['GET', 'POST'])
@login_required 
def tambah_obat():
    if request.method == 'POST':
        return add_obat()
    return render_template('Tambah_Obat.html')


@app.route("/hapus_obat/<obat_id>")
@login_required 
def hapus_obat(obat_id):
    return delete_obat(obat_id)

@app.route('/EditObat/<obat_id>', methods=['GET', 'POST'])
@login_required 
def EditObat(obat_id):
    if request.method == 'POST':
        return edit_obat(obat_id)
    
    obat_to_edit = edit_obat(obat_id)
    return render_template('Edit_Obat.html', obat=obat_to_edit)


#<====================Rekam Medis====================>
@app.route('/rekammedis')
@login_required 
def tabel_rm():
    rmrs = index_rm()
    return render_template('Rekammedis.html', rmrs=rmrs)

@app.route('/tambahrm', methods=['GET', 'POST'])
@login_required 
def tambah_rm():
    if request.method == 'POST':
        return add_rm()
    else:
        pasien = Pasien.query.all()
        dokter = Dokter.query.all()
        poli = PoliKlinik.query.all()
    return render_template('Tambahrekammedis.html', pasien=pasien, dokter=dokter, poli=poli)

@app.route("/delete_rm/<ID_RM>")
@login_required 
def hapus_rm(ID_RM):
    return delete_rm(ID_RM)

@app.route('/edit_rm/<ID_RM>', methods=['GET', 'POST'])
@login_required 
def ubah_rm(ID_RM):
    if request.method == 'POST':
        return edit_rm(ID_RM)
    pasien = Pasien.query.all()
    dokter = Dokter.query.all()
    poli = PoliKlinik.query.all()
    ubahke_rm = edit_rm(ID_RM)
    return render_template('Editrekammedis.html', rm=ubahke_rm, pasien=pasien, dokter=dokter, poli=poli)


#<====================Rekam Medis Obat====================>
@app.route('/RM_Obat')
@login_required 
def RM_Obat():
    # Mengambil semua data RM_Obat menggunakan fungsi controller RM_Obat_index()
    rm_obat = RM_Obat_index()
    # Render template RM_Obat.html dan kirimkan data rm_obat ke template
    return render_template('RM_Obat.html', rm_obat=rm_obat)

@app.route('/tambah_rm_obat', methods=['GET', 'POST'])
@login_required 
def tambah_rm_obat():
    # Jika request POST, panggil fungsi add_rm_obat() untuk memproses data
    if request.method == 'POST':
        return add_rm_obat()
    # Jika GET, tampilkan form penambahan
    
    else:
        rekam_medis = Rekammedis.query.all()
        obat_list = Obate.query.all()  # <-- Ambil semua data Obat
    return render_template('Tambah_RM_Obat.html', rekam_medis=rekam_medis, obat_list=obat_list)
   


@app.route("/hapus_rm_obat/<rm_obat_id>")
@login_required 
def hapus_rm_obat(rm_obat_id):
    # Panggil fungsi delete_rm_obat() dengan parameter rm_obat_id untuk menghapus data
    return delete_rm_obat(rm_obat_id)

@app.route('/edit_rmobat/<rm_obat_id>', methods=['GET', 'POST'])   
@login_required 
def edit_rmobat(rm_obat_id):
    # Jika request POST, panggil fungsi edit_rm_obat() untuk melakukan update data
    if request.method == 'POST':
        return edit_rm_obat(rm_obat_id)
    
    # Jika GET, ambil data RM_Obat yang akan diedit
    rmobat_to_edit = edit_rm_obat(rm_obat_id)
    rekam_medis = Rekammedis.query.all()
    obat_list = Obate.query.all()  # <-- Ambil semua data Obat
    # Render template Edit_Rm_Obat.html dan kirimkan data yang akan diedit ke template
    return render_template('Edit_Rm_Obat.html', rm_obat=rmobat_to_edit, rekam_medis=rekam_medis, obat_list=obat_list)


# Rute untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()  # Memanggil fungsi controller untuk login
    return render_template('Login.html')  # Pastikan Anda memiliki template Login.html

# Rute untuk halaman signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return signup_post()  # Memanggil fungsi controller untuk signup
    return render_template('Signup.html')  # Pastikan Anda memiliki template Signup.html

# Rute untuk logout
@app.route('/logout')
def logout_user():
    return logout_user_action()  # Memanggil fungsi controller untuk logout




if __name__ == "__main__":
    app.run(debug=True)