from flask import *
from app.models.product_details_model import ProductDetails
from app.models.product_model import Product
from app.models.penjual_model import Penjual
from app.models.kota_model import Kota
from app import db

product_details_blueprint = Blueprint('product_details', __name__, url_prefix='/product-details')

@product_details_blueprint.route('/')
def index():
    try:
        products = Product.get_all()
    except Exception as e:
        products = []
        flash(f"Error mengambil data produk: {str(e)}", "danger")
    
    return render_template('product_details/index.html', products=products)

@product_details_blueprint.route('/create')
def create():
    try:
        penjual_list = Penjual.get_all()
        kota_list = Kota.get_all()
    except Exception as e:
        penjual_list = []
        kota_list = []
        flash(f"Error mengambil data: {str(e)}", "danger")
    
    return render_template('product_details/create.html', penjual_list=penjual_list, kota_list=kota_list)

@product_details_blueprint.route('/store', methods=['POST'])
def store():
    product_name = request.form.get('product_name')
    harga = request.form.get('harga')
    seller_name = request.form.get('seller_name')
    seller_address = request.form.get('seller_address')
    city = request.form.get('city')
    
    if not product_name or not harga:
        flash("Nama produk dan harga harus diisi!", "danger")
        return redirect(url_for('product_details.create'))
    
    try:
        # First create or find the city
        city_obj = Kota.query.filter_by(nama=city).first()
        if not city_obj:
            city_obj = Kota.create(nama=city)
        
        # Then create or find the seller
        seller = Penjual.query.filter_by(nama=seller_name, alamat=seller_address, kotaid=city_obj.id).first()
        if not seller:
            seller = Penjual.create(nama=seller_name, alamat=seller_address, kotaid=city_obj.id)
        
        # Create the product
        product = Product.create(nama=product_name, harga=harga, penjualid=seller.id)
        
        # Create product details - now uses different field names
        if product:
            ProductDetails.create(
                product_name=product_name,
                harga=harga,
                seller_name=seller_name,
                seller_address=seller_address,
                city=city
            )
        
        flash("Data berhasil disimpan!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product_details.index'))

@product_details_blueprint.route('/edit/<id>')
def edit(id):
    try:
        product = Product.get_by_id(id)
        if not product:
            flash("Produk tidak ditemukan!", "danger")
            return redirect(url_for('product_details.index'))
        
        details = ProductDetails.get_by_product_id(product.id)
        penjual_list = Penjual.get_all()
        kota_list = Kota.get_all()
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('product_details.index'))
    
    return render_template('product_details/edit.html', 
                          product=product, 
                          details=details,
                          penjual_list=penjual_list, 
                          kota_list=kota_list)

@product_details_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    product_name = request.form.get('product_name')
    harga = request.form.get('harga')
    seller_name = request.form.get('seller_name')
    seller_address = request.form.get('seller_address')
    city = request.form.get('city')
    
    if not product_name or not harga:
        flash("Nama produk dan harga harus diisi!", "danger")
        return redirect(url_for('product_details.edit', id=id))
    
    try:
        # First create or find the city
        city_obj = Kota.query.filter_by(nama=city).first()
        if not city_obj:
            city_obj = Kota.create(nama=city)
        
        # Then create or find the seller
        seller = Penjual.query.filter_by(nama=seller_name, alamat=seller_address, kotaid=city_obj.id).first()
        if not seller:
            seller = Penjual.create(nama=seller_name, alamat=seller_address, kotaid=city_obj.id)
        
        # Update the product
        product = Product.get_by_id(id)
        if product:
            product.update(nama=product_name, harga=harga, penjualid=seller.id)
            
            # Update or create product details
            details = ProductDetails.get_by_product_id(product.id)
            if details:
                details.update(
                    product_name=product_name,
                    harga=harga,
                    seller_name=seller_name,
                    seller_address=seller_address,
                    city=city
                )
            else:
                ProductDetails.create(
                    product_name=product_name,
                    harga=harga,
                    seller_name=seller_name,
                    seller_address=seller_address,
                    city=city
                )
            
            flash("Data berhasil diupdate!", "success")
        else:
            flash("Produk tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product_details.index'))

@product_details_blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        product = Product.get_by_id(id)
        if product:
            # Delete associated product details first
            details = ProductDetails.get_by_product_id(product.id)
            if details:
                details.delete()
            
            # Then delete the product
            product.delete()
            flash("Data berhasil dihapus!", "success")
        else:
            flash("Produk tidak ditemukan!", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('product_details.index')) 