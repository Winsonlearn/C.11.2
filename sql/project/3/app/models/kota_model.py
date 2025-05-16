from app import db
from datetime import datetime

class Kota(db.Model):
    __tablename__ = 'kota'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Kota {self.nama}>'
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def create(cls, nama):
        kota = cls(nama=nama)
        db.session.add(kota)
        db.session.commit()
        return kota
    
    def update(self, nama):
        self.nama = nama
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True