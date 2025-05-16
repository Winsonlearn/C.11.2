from flask import *
from app.models.kota_model import Kota

kota_blueprint = Blueprint('kota', __name__, url_prefix='/kota')

@kota_blueprint.route('/')
def index():
    try:
        kota_list = Kota.get_all()
    except Exception as e:
        kota_list = []
        flash(f"Error mengambil data kota: {str(e)}", "danger")
    return render_template('kota/index.html', kota_list=kota_list)

@kota_blueprint.route('/create')
def create():
    return render_template('kota/create.html')

@kota_blueprint.route('/store', methods=['POST'])
def store():
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kota harus diisi!", "danger")
        return redirect(url_for('kota.create'))
    
    try:
        Kota.create(nama=nama)
        flash("Kota berhasil ditambahkan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index'))

@kota_blueprint.route('/edit/<id>')
def edit(id):
    try:
        kota = Kota.get_by_id(id)
        if not kota:
            flash("Kota tidak ditemukan!", "danger")
            return redirect(url_for('kota.index'))
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('kota.index'))
    
    return render_template('kota/edit.html', kota=kota)

@kota_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kota harus diisi!", "danger")
        return redirect(url_for('kota.edit', id=id))
    
    try:
        kota = Kota.get_by_id(id)
        if kota:
            kota.update(nama=nama)
            flash("Kota berhasil diupdate!", "success")
        else:
            flash("Kota tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index'))

@kota_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        kota = Kota.get_by_id(id)
        if kota:
            kota.delete()
            flash("Kota berhasil dihapus!", "success")
        else:
            flash("Kota tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kota.index')) 