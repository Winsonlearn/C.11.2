from flask import *
from app.models.product_model import Product
from app.models.penjual_model import Penjual

product_blueprint = Blueprint('product', __name__, url_prefix='/product')

@product_blueprint.route('/')
def index():
    products = Product.get_all()
    return render_template('product/index.html', products=products)

@product_blueprint.route('/create')
def create():
    penjual_list = Penjual.get_all()
    return render_template('product/create.html', penjual_list=penjual_list)

@product_blueprint.route('/store', methods=['POST'])
def store():
    nama = request.form.get('nama')
    harga = request.form.get('harga')
    penjualid = request.form.get('penjualid')
    
    if not nama or not harga:
        flash("Nama dan harga harus diisi!", "danger")
        return redirect(url_for('product.create'))
    
    if penjualid == "" or not penjualid:
        penjualid = None
    
    try:
        Product.create(nama=nama, harga=harga, penjualid=penjualid)
        flash("Produk berhasil disimpan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product.index'))

@product_blueprint.route('/edit/<id>')
def edit(id):
    product = Product.get_by_id(id)
    penjual_list = Penjual.get_all()
    return render_template('product/edit.html', product=product, penjual_list=penjual_list)

@product_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    product = Product.get_by_id(id)
    
    if not product:
        flash("Produk tidak ditemukan!", "danger")
        return redirect(url_for('product.index'))
    
    nama = request.form.get('nama')
    harga = request.form.get('harga')
    penjualid = request.form.get('penjualid')
    
    if not nama or not harga:
        flash("Nama dan harga harus diisi!", "danger")
        return redirect(url_for('product.edit', id=id))
    
    if penjualid == "" or not penjualid:
        penjualid = None
    
    try:
        product.update(nama=nama, harga=harga, penjualid=penjualid)
        flash("Produk berhasil diupdate!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product.index'))

@product_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    product = Product.get_by_id(id)
    
    if not product:
        flash("Produk tidak ditemukan!", "danger")
        return redirect(url_for('product.index'))
    
    try:
        product.delete()
        flash("Produk berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        
    return redirect(url_for('product.index')) 