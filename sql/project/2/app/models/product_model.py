import mysql.connector
from flask import current_app

class ProductModel:
    def __init__(self):
        self.config = current_app.config
    
    def connect(self):
        return mysql.connector.connect(
            host = self.config["MYSQL_HOST"],
            database = self.config["MYSQL_DATABASE"],
            user = self.config["MYSQL_USER"],
            password = self.config["MYSQL_PASSWORD"],
        )
    
    def get_all_products(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pj.nama as penjual_nama
            FROM produk p
            LEFT JOIN penjual pj ON p.penjualid = pj.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_product_by_id(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pj.nama as penjual_nama
            FROM produk p
            LEFT JOIN penjual pj ON p.penjualid = pj.id
            WHERE p.id = %s
        """, (id,))
        data = cursor.fetchone()
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
        
    def check_penjual_exists(self, penjual_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT id FROM penjual WHERE id = %s", (penjual_id,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result is not None
        
    def insert_product(self, nama, harga, penjualid=None):
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO produk (nama, harga, penjualid) VALUES (%s, %s, %s)"
        data = (nama, harga, penjualid)  
        cursor.execute(query, data)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
        
    def update_product(self, id, nama, harga, penjualid=None):
        db = self.connect()
        cursor = db.cursor()
        query = "UPDATE produk SET nama = %s, harga = %s, penjualid = %s WHERE id = %s"
        cursor.execute(query, (nama, harga, penjualid, id))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows
        
    def delete_product(self, id):
        db = self.connect()
        cursor = db.cursor()
        query = "DELETE FROM produk WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows 