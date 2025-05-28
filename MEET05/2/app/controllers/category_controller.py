from flask import Blueprint, jsonify
from ..models import models

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = models.Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories]) 