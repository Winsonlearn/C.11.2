from flask import *
from app.models.kota_model import KotaModel

kota_blueprint = Blueprint('kota', __name__, url_prefix='/kota')

@kota_blueprint.route('/')
def index():
    kota_model = KotaModel()
    try:
        kota_list = kota_model.get_all_kota()
    except Exception as e:
        kota_list = []
        flash(f"Error mengambil data kota: {str(e)}", "danger")
    return render_template('kota/index.html', kota_list=kota_list)

@kota_blueprint.route('/create')
def create():
    return render_template('kota/create.html')

@kota_blueprint.route('/store', methods=['POST'])
def store():
    kota_model = KotaModel()
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kota harus diisi!", "danger")
        return redirect(url_for('kota.create'))
    
    try:
        kota_model.insert_kota(nama)
        flash("Kota berhasil ditambahkan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index'))

@kota_blueprint.route('/edit/<id>')
def edit(id):
    kota_model = KotaModel()
    try:
        kota = kota_model.get_kota_by_id(id)
        if not kota:
            flash("Kota tidak ditemukan!", "danger")
            return redirect(url_for('kota.index'))
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('kota.index'))
    
    return render_template('kota/edit.html', kota=kota)

@kota_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    kota_model = KotaModel()
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kota harus diisi!", "danger")
        return redirect(url_for('kota.edit', id=id))
    
    try:
        kota_model.update_kota(id, nama)
        flash("Kota berhasil diupdate!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index'))

@kota_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    kota_model = KotaModel()
    try:
        kota_model.delete_kota(id)
        flash("Kota berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index')) 