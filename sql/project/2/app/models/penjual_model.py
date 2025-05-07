import mysql.connector
from flask import current_app

class PenjualModel:
    def __init__(self):
        self.config = current_app.config
    
    def connect(self):
        return mysql.connector.connect(
            host = self.config["MYSQL_HOST"],
            database = self.config["MYSQL_DATABASE"],
            user = self.config["MYSQL_USER"],
            password = self.config["MYSQL_PASSWORD"],
        )
    
    def get_all_penjual(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, k.nama as kota_nama 
            FROM penjual p
            LEFT JOIN kota k ON p.kotaid = k.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_penjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, k.nama as kota_nama 
            FROM penjual p
            LEFT JOIN kota k ON p.kotaid = k.id
            WHERE p.id = %s
        """, (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
        
    def insert_penjual(self, nama, alamat, kotaid=None):
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO penjual (nama, alamat, kotaid) VALUES (%s, %s, %s)"
        data = (nama, alamat, kotaid)  
        cursor.execute(query, data)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
        
    def update_penjual(self, id, nama, alamat, kotaid=None):
        db = self.connect()
        cursor = db.cursor()
        query = "UPDATE penjual SET nama = %s, alamat = %s, kotaid = %s WHERE id = %s"
        cursor.execute(query, (nama, alamat, kotaid, id))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows
        
    def delete_penjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        query = "DELETE FROM penjual WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows 