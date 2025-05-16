from app import db
from datetime import datetime

class KategoriPenjual(db.Model):
    __tablename__ = 'kategori_penjual'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kategoriid = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable=False)
    penjualid = db.Column(db.Integer, db.ForeignKey('penjual.id'), nullable=False)
    
    def __repr__(self):
        return f'<KategoriPenjual {self.id}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_by_penjual_id(cls, penjual_id):
        return cls.query.filter_by(penjualid=penjual_id).all()
    
    @classmethod
    def get_by_kategori_id(cls, kategori_id):
        return cls.query.filter_by(kategoriid=kategori_id).all()
    
    @classmethod
    def create(cls, kategoriid, penjualid):
        kategori_penjual = cls(kategoriid=kategoriid, penjualid=penjualid)
        db.session.add(kategori_penjual)
        db.session.commit()
        return kategori_penjual
    
    def update(self, kategoriid, penjualid):
        self.kategoriid = kategoriid
        self.penjualid = penjualid
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True 