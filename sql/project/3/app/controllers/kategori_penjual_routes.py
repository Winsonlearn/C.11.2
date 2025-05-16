from flask import *
from app.models.kategori_penjual_model import KategoriPenjual
from app.models.kategori_model import Kategori
from app.models.penjual_model import Penjual

kategori_penjual_blueprint = Blueprint('kategori_penjual', __name__, url_prefix='/kategori-penjual')

@kategori_penjual_blueprint.route('/')
def index():
    try:
        kategori_penjual_list = KategoriPenjual.get_all()
    except Exception as e:
        kategori_penjual_list = []
        flash(f"Error mengambil data: {str(e)}", "danger")
    return render_template('kategori_penjual/index.html', kategori_penjual_list=kategori_penjual_list)

@kategori_penjual_blueprint.route('/create')
def create():
    try:
        kategori_list = Kategori.get_all()
        penjual_list = Penjual.get_all()
        if not kategori_list:
            flash("Tidak ada data kategori tersedia. Silahkan tambahkan kategori terlebih dahulu.", "warning")
        if not penjual_list:
            flash("Tidak ada data penjual tersedia. Silahkan tambahkan penjual terlebih dahulu.", "warning")
    except Exception as e:
        kategori_list = []
        penjual_list = []
        flash(f"Error mengambil data: {str(e)}", "danger")
    
    return render_template('kategori_penjual/create.html', kategori_list=kategori_list, penjual_list=penjual_list)

@kategori_penjual_blueprint.route('/store', methods=['POST'])
def store():
    kategoriid = request.form.get('kategoriid')
    penjualid = request.form.get('penjualid')
    
    if not kategoriid or not penjualid:
        flash("Error: Kategori dan Penjual harus dipilih!", "danger")
        return redirect(url_for('kategori_penjual.create'))
    
    try:
        KategoriPenjual.create(kategoriid=kategoriid, penjualid=penjualid)
        flash("Data berhasil disimpan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        
    return redirect(url_for('kategori_penjual.index'))

@kategori_penjual_blueprint.route('/edit/<id>')
def edit(id):
    try:
        kategori_penjual = KategoriPenjual.get_by_id(id)
        if not kategori_penjual:
            flash("Data tidak ditemukan!", "danger")
            return redirect(url_for('kategori_penjual.index'))
            
        kategori_list = Kategori.get_all()
        penjual_list = Penjual.get_all()
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('kategori_penjual.index'))
    
    return render_template('kategori_penjual/edit.html', 
                          kategori_penjual=kategori_penjual,
                          kategori_list=kategori_list,
                          penjual_list=penjual_list)

@kategori_penjual_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    kategoriid = request.form.get('kategoriid')
    penjualid = request.form.get('penjualid')
    
    if not kategoriid or not penjualid:
        flash("Error: Kategori dan Penjual harus dipilih!", "danger")
        return redirect(url_for('kategori_penjual.edit', id=id))
    
    try:
        kategori_penjual = KategoriPenjual.get_by_id(id)
        if kategori_penjual:
            kategori_penjual.update(kategoriid=kategoriid, penjualid=penjualid)
            flash("Data berhasil diupdate!", "success")
        else:
            flash("Data tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        
    return redirect(url_for('kategori_penjual.index'))

@kategori_penjual_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        kategori_penjual = KategoriPenjual.get_by_id(id)
        if kategori_penjual:
            kategori_penjual.delete()
            flash("Data berhasil dihapus!", "success")
        else:
            flash("Data tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        
    return redirect(url_for('kategori_penjual.index')) 