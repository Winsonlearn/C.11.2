from flask import *
from app.models.product_details_model import ProductDetailsModel

product_details_blueprint = Blueprint('product_details', __name__, url_prefix='/product-details')

@product_details_blueprint.route('/')
def index():
    product_details_model = ProductDetailsModel()
    product_details = product_details_model.get_all_product_details()
    return render_template('product_details/index.html', product_details=product_details)

@product_details_blueprint.route('/create')
def create():
    return render_template('product_details/create.html')

@product_details_blueprint.route('/store', methods=['POST'])
def store():
    product_details_model = ProductDetailsModel()
    product_name = request.form.get('product_name')
    harga = request.form.get('harga')
    seller_name = request.form.get('seller_name')
    seller_address = request.form.get('seller_address')
    city = request.form.get('city')
    
    if not product_name or not harga:
        flash("Nama produk dan harga harus diisi!", "danger")
        return redirect(url_for('product_details.create'))
    
    try:
        product_details_model.insert_product_details(product_name, harga, seller_name, seller_address, city)
        flash("Detail produk berhasil disimpan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product_details.index'))

@product_details_blueprint.route('/edit/<id>')
def edit(id):
    product_details_model = ProductDetailsModel()
    product_detail = product_details_model.get_product_details_by_id(id)
    return render_template('product_details/edit.html', product_detail=product_detail)

@product_details_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    product_details_model = ProductDetailsModel()
    
    product_name = request.form.get('product_name')
    harga = request.form.get('harga')
    seller_name = request.form.get('seller_name')
    seller_address = request.form.get('seller_address')
    city = request.form.get('city')
    
    if not product_name or not harga:
        flash("Nama produk dan harga harus diisi!", "danger")
        return redirect(url_for('product_details.edit', id=id))
    
    try:
        product_details_model.update_product_details(id, product_name, harga, seller_name, seller_address, city)
        flash("Detail produk berhasil diupdate!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product_details.index'))

@product_details_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    product_details_model = ProductDetailsModel()
    try:
        product_details_model.delete_product_details(id)
        flash("Detail produk berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    return redirect(url_for('product_details.index')) 