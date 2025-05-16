from app import db
from datetime import datetime

class Penjual(db.Model):
    __tablename__ = 'penjual'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    alamat = db.Column(db.Text, nullable=True)
    kotaid = db.Column(db.Integer, db.ForeignKey('kota.id'), nullable=True)
    
    # Define relationship with Kota model
    kota = db.relationship('Kota', backref=db.backref('penjuals', lazy=True))
    
    # Define relationship with KategoriPenjual
    kategori_penjuals = db.relationship('KategoriPenjual', backref='penjual', lazy=True)
    
    def __repr__(self):
        return f'<Penjual {self.nama}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def create(cls, nama, alamat=None, kotaid=None):
        penjual = cls(nama=nama, alamat=alamat, kotaid=kotaid)
        db.session.add(penjual)
        db.session.commit()
        return penjual
    
    def update(self, nama, alamat=None, kotaid=None):
        self.nama = nama
        self.alamat = alamat
        self.kotaid = kotaid
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True 