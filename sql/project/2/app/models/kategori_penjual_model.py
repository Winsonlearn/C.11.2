import mysql.connector
from flask import current_app

class KategoriPenjualModel:
    def __init__(self):
        self.config = current_app.config
    
    def connect(self):
        return mysql.connector.connect(
            host = self.config["MYSQL_HOST"],
            database = self.config["MYSQL_DATABASE"],
            user = self.config["MYSQL_USER"],
            password = self.config["MYSQL_PASSWORD"],
        )
    
    def get_all_kategori_penjual(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT kp.id, kp.kategoriid, kp.penjualid, 
                   k.nama AS kategori_nama, 
                   p.nama AS penjual_nama
            FROM kategoripenjual kp
            LEFT JOIN kategori k ON kp.kategoriid = k.id
            LEFT JOIN penjual p ON kp.penjualid = p.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_kategori_penjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT kp.id, kp.kategoriid, kp.penjualid, 
                   k.nama AS kategori_nama, 
                   p.nama AS penjual_nama
            FROM kategoripenjual kp
            LEFT JOIN kategori k ON kp.kategoriid = k.id
            LEFT JOIN penjual p ON kp.penjualid = p.id
            WHERE kp.id = %s
        """, (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
        
    def insert_kategori_penjual(self, kategoriid, penjualid):
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO kategoripenjual (kategoriid, penjualid) VALUES (%s, %s)"
        data = (kategoriid, penjualid)  
        cursor.execute(query, data)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
        
    def update_kategori_penjual(self, id, kategoriid, penjualid):
        db = self.connect()
        cursor = db.cursor()
        query = "UPDATE kategoripenjual SET kategoriid = %s, penjualid = %s WHERE id = %s"
        cursor.execute(query, (kategoriid, penjualid, id))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows
        
    def delete_kategori_penjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        query = "DELETE FROM kategoripenjual WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows

    def get_all_kategori(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kategori")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_all_penjual(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM penjual")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data 