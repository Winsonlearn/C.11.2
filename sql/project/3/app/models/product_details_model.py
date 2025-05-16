from app import db
from datetime import datetime

class ProductDetails(db.Model):
    __tablename__ = 'product_details'
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=True)
    harga = db.Column(db.Integer, nullable=True)
    seller_name = db.Column(db.String(100), nullable=True)
    seller_address = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f'<ProductDetails {self.id}>'
    
    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error querying ProductDetails: {e}")
            return []
    
    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.query.get(id)
        except Exception as e:
            print(f"Error querying ProductDetails by id: {e}")
            return None
    
    @classmethod
    def get_by_product_id(cls, product_id):
        """
        This method is different now as we don't have a direct foreign key relationship.
        We need to find the product details based on the product_name that matches the product.
        """
        from app.models.product_model import Product
        try:
            product = Product.get_by_id(product_id)
            if product:
                # Try to find product details with the same name
                return cls.query.filter_by(product_name=product.nama).first()
            return None
        except Exception as e:
            print(f"Error querying ProductDetails by product_id: {e}")
            return None
    
    @classmethod
    def create(cls, product_name, harga, seller_name=None, seller_address=None, city=None):
        try:
            product_details = cls(
                product_name=product_name,
                harga=harga,
                seller_name=seller_name,
                seller_address=seller_address,
                city=city
            )
            db.session.add(product_details)
            db.session.commit()
            return product_details
        except Exception as e:
            db.session.rollback()
            print(f"Error creating ProductDetails: {e}")
            return None
    
    def update(self, product_name=None, harga=None, seller_name=None, seller_address=None, city=None):
        try:
            if product_name:
                self.product_name = product_name
            if harga:
                self.harga = harga
            if seller_name:
                self.seller_name = seller_name
            if seller_address:
                self.seller_address = seller_address
            if city:
                self.city = city
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating ProductDetails: {e}")
            return None
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting ProductDetails: {e}")
            return False 