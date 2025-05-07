import mysql.connector
from flask import current_app

class KategoriModel:
    def __init__(self):
        self.config = current_app.config
    
    def connect(self):
        return mysql.connector.connect(
            host = self.config["MYSQL_HOST"],
            database = self.config["MYSQL_DATABASE"],
            user = self.config["MYSQL_USER"],
            password = self.config["MYSQL_PASSWORD"],
        )
    
    def get_all_kategori(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kategori")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_kategori_by_id(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kategori WHERE id = %s", (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
        
    def insert_kategori(self, nama):
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO kategori (nama) VALUES (%s)"
        data = (nama,)  
        cursor.execute(query, data)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
        
    def update_kategori(self, id, nama):
        db = self.connect()
        cursor = db.cursor()
        query = "UPDATE kategori SET nama = %s WHERE id = %s"
        cursor.execute(query, (nama, id))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows
        
    def delete_kategori(self, id):
        db = self.connect()
        cursor = db.cursor()
        query = "DELETE FROM kategori WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows 