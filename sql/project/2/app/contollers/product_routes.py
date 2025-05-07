from flask import *
from app.models.product_model import ProductModel

product_blueprint = Blueprint('product', __name__, url_prefix='/product')

@product_blueprint.route('/')
def index():
    product_model = ProductModel()
    products = product_model.get_all_products()
    return render_template('product/index.html', products=products)

@product_blueprint.route('/create')
def create():
    product_model = ProductModel()
    penjual_list = product_model.get_all_penjual()
    return render_template('product/create.html', penjual_list=penjual_list)

@product_blueprint.route('/store', methods=['POST'])
def store():
    product_model = ProductModel()
    nama = request.form.get('nama')
    harga = request.form.get('harga')
    penjualid = request.form.get('penjualid')
    
    if not nama or not harga:
        flash("Nama dan harga harus diisi!", "danger")
        return redirect(url_for('product.create'))
    
    if penjualid == "" or not penjualid:
        penjualid = None
    
    try:
        product_model.insert_product(nama, harga, penjualid)
        flash("Produk berhasil disimpan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product.index'))

@product_blueprint.route('/edit/<id>')
def edit(id):
    product_model = ProductModel()
    product = product_model.get_product_by_id(id)
    penjual_list = product_model.get_all_penjual()
    return render_template('product/edit.html', product=product, penjual_list=penjual_list)

@product_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    product_model = ProductModel()
    
    nama = request.form.get('nama')
    harga = request.form.get('harga')
    penjualid = request.form.get('penjualid')
    
    if not nama or not harga:
        flash("Nama dan harga harus diisi!", "danger")
        return redirect(url_for('product.edit', id=id))
    
    if penjualid == "" or not penjualid:
        penjualid = None
    
    try:
        product_model.update_product(id, nama, harga, penjualid)
        flash("Produk berhasil diupdate!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product.index'))

@product_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    product_model = ProductModel()
    try:
        product_model.delete_product(id)
        flash("Produk berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    return redirect(url_for('product.index')) 