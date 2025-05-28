from flask import Blueprint, jsonify
from ..models import models

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = models.Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'category_id': p.category_id
    } for p in products]) 