from flask import *
from app.models.penjual_model import PenjualModel
from app.models.kota_model import KotaModel

penjual_blueprint = Blueprint('penjual', __name__, url_prefix='/penjual')

@penjual_blueprint.route('/')
def index():
    penjual_model = PenjualModel()
    penjual_list = penjual_model.get_all_penjual()
    return render_template('penjual/index.html', penjual_list=penjual_list)

@penjual_blueprint.route('/create')
def create():
    kota_model = KotaModel()
    kota_list = kota_model.get_all_kota()
    return render_template('penjual/create.html', kota_list=kota_list)

@penjual_blueprint.route('/store', methods=['POST'])
def store():
    penjual_model = PenjualModel()
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')
    kotaid = request.form.get('kotaid')
    
    if not nama or not alamat:
        flash("Nama dan alamat harus diisi!", "danger")
        return redirect(url_for('penjual.create'))
    
    if not kotaid:
        kotaid = None
    
    try:
        penjual_model.insert_penjual(nama, alamat, kotaid)
        flash("Penjual berhasil ditambahkan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index'))

@penjual_blueprint.route('/edit/<id>')
def edit(id):
    penjual_model = PenjualModel()
    kota_model = KotaModel()
    
    penjual = penjual_model.get_penjual_by_id(id)
    kota_list = kota_model.get_all_kota()
    
    return render_template('penjual/edit.html', penjual=penjual, kota_list=kota_list)

@penjual_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    penjual_model = PenjualModel()
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')
    kotaid = request.form.get('kotaid')
    
    if not nama or not alamat:
        flash("Nama dan alamat harus diisi!", "danger")
        return redirect(url_for('penjual.edit', id=id))
    
    if not kotaid:
        kotaid = None
    
    try:
        penjual_model.update_penjual(id, nama, alamat, kotaid)
        flash("Penjual berhasil diupdate!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index'))

@penjual_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    penjual_model = PenjualModel()
    
    try:
        penjual_model.delete_penjual(id)
        flash("Penjual berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('penjual.index')) 