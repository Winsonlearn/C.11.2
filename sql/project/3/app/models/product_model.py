from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'produk'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Float, nullable=False)
    penjualid = db.Column(db.Integer, db.ForeignKey('penjual.id'), nullable=True)
    
    # Define relationship with Penjual model
    penjual = db.relationship('Penjual', backref=db.backref('products', lazy=True))
    
    def __repr__(self):
        return f'<Product {self.nama}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def create(cls, nama, harga, penjualid=None):
        product = cls(nama=nama, harga=harga, penjualid=penjualid)
        db.session.add(product)
        db.session.commit()
        return product
    
    def update(self, nama, harga, penjualid=None):
        self.nama = nama
        self.harga = harga
        self.penjualid = penjualid
        db.session.commit()
        return self
    
    def delete(self):
        # Get product details
        from app.models.product_details_model import ProductDetails
        try:
            # Try to find and delete associated product details
            product_details = ProductDetails.query.filter_by(product_name=self.nama).first()
            if product_details:
                db.session.delete(product_details)
        except Exception as e:
            print(f"Error deleting associated product details: {e}")
        
        # Delete the product
        db.session.delete(self)
        db.session.commit()
        return True 