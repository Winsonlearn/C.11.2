from flask import *
from app.models.penjual_model import Penjual
from app.models.kota_model import Kota

penjual_blueprint = Blueprint('penjual', __name__, url_prefix='/penjual')

@penjual_blueprint.route('/')
def index():
    penjual_list = Penjual.get_all()
    return render_template('penjual/index.html', penjual_list=penjual_list)

@penjual_blueprint.route('/create')
def create():
    kota_list = Kota.get_all()
    return render_template('penjual/create.html', kota_list=kota_list)

@penjual_blueprint.route('/store', methods=['POST'])
def store():
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')
    kotaid = request.form.get('kotaid')
    
    if not nama or not alamat:
        flash("Nama dan alamat harus diisi!", "danger")
        return redirect(url_for('penjual.create'))
    
    if not kotaid:
        kotaid = None
    
    try:
        Penjual.create(nama=nama, alamat=alamat, kotaid=kotaid)
        flash("Penjual berhasil ditambahkan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index'))

@penjual_blueprint.route('/edit/<id>')
def edit(id):
    penjual = Penjual.get_by_id(id)
    kota_list = Kota.get_all()
    
    return render_template('penjual/edit.html', penjual=penjual, kota_list=kota_list)

@penjual_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')
    kotaid = request.form.get('kotaid')
    
    if not nama or not alamat:
        flash("Nama dan alamat harus diisi!", "danger")
        return redirect(url_for('penjual.edit', id=id))
    
    if not kotaid:
        kotaid = None
    
    try:
        penjual = Penjual.get_by_id(id)
        if penjual:
            penjual.update(nama=nama, alamat=alamat, kotaid=kotaid)
            flash("Penjual berhasil diupdate!", "success")
        else:
            flash("Penjual tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index'))

@penjual_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        penjual = Penjual.get_by_id(id)
        if penjual:
            penjual.delete()
            flash("Penjual berhasil dihapus!", "success")
        else:
            flash("Penjual tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index')) 