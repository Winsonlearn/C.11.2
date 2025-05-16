from app import db
from datetime import datetime

class Kategori(db.Model):
    __tablename__ = 'kategori'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    
    # Define relationship with KategoriPenjual
    kategori_penjuals = db.relationship('KategoriPenjual', backref='kategori', lazy=True)
    
    def __repr__(self):
        return f'<Kategori {self.nama}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def create(cls, nama):
        kategori = cls(nama=nama)
        db.session.add(kategori)
        db.session.commit()
        return kategori
    
    def update(self, nama):
        self.nama = nama
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True 