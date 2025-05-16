from flask import *
from app.models.kategori_model import Kategori

kategori_blueprint = Blueprint('kategori', __name__, url_prefix='/kategori')

@kategori_blueprint.route('/')
def index():
    try:
        kategori_list = Kategori.get_all()
    except Exception as e:
        kategori_list = []
        flash(f"Error mengambil data kategori: {str(e)}", "danger")
    return render_template('kategori/index.html', kategori_list=kategori_list)

@kategori_blueprint.route('/create')
def create():
    return render_template('kategori/create.html')

@kategori_blueprint.route('/store', methods=['POST'])
def store():
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kategori harus diisi!", "danger")
        return redirect(url_for('kategori.create'))
    
    try:
        Kategori.create(nama=nama)
        flash("Kategori berhasil ditambahkan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kategori.index'))

@kategori_blueprint.route('/edit/<id>')
def edit(id):
    try:
        kategori = Kategori.get_by_id(id)
        if not kategori:
            flash("Kategori tidak ditemukan!", "danger")
            return redirect(url_for('kategori.index'))
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('kategori.index'))
    
    return render_template('kategori/edit.html', kategori=kategori)

@kategori_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    nama = request.form.get('nama')
    
    if not nama:
        flash("Nama kategori harus diisi!", "danger")
        return redirect(url_for('kategori.edit', id=id))
    
    try:
        kategori = Kategori.get_by_id(id)
        if kategori:
            kategori.update(nama=nama)
            flash("Kategori berhasil diupdate!", "success")
        else:
            flash("Kategori tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kategori.index'))

@kategori_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        kategori = Kategori.get_by_id(id)
        if kategori:
            kategori.delete()
            flash("Kategori berhasil dihapus!", "success")
        else:
            flash("Kategori tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('kategori.index')) 