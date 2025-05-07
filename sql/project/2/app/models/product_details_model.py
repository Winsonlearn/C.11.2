import mysql.connector
from flask import current_app

class ProductDetailsModel:
    def __init__(self):
        self.config = current_app.config
    
    def connect(self):
        return mysql.connector.connect(
            host = self.config["MYSQL_HOST"],
            database = self.config["MYSQL_DATABASE"],
            user = self.config["MYSQL_USER"],
            password = self.config["MYSQL_PASSWORD"],
        )
    
    def get_all_product_details(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM product_details")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def get_product_details_by_id(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM product_details WHERE id = %s", (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
    
    def get_penjual_id_by_name_and_city(self, seller_name, seller_address, city):
        """Get or create a penjual record and return its ID"""
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        
        # First, try to find the kota ID
        cursor.execute("SELECT id FROM kota WHERE nama = %s", (city,))
        kota_result = cursor.fetchone()
        
        if not kota_result:
            # Create the city if it doesn't exist
            cursor.execute("INSERT INTO kota (nama) VALUES (%s)", (city,))
            kota_id = cursor.lastrowid
            db.commit()
        else:
            kota_id = kota_result['id']
        
        # Now try to find the existing penjual
        cursor.execute("SELECT id FROM penjual WHERE nama = %s AND alamat = %s AND kotaid = %s", 
                      (seller_name, seller_address, kota_id))
        penjual_result = cursor.fetchone()
        
        if not penjual_result:
            # Create the penjual if they don't exist
            cursor.execute("INSERT INTO penjual (nama, alamat, kotaid) VALUES (%s, %s, %s)", 
                          (seller_name, seller_address, kota_id))
            penjual_id = cursor.lastrowid
            db.commit()
        else:
            penjual_id = penjual_result['id']
        
        cursor.close()
        db.close()
        return penjual_id
        
    def insert_product_details(self, product_name, harga, seller_name, seller_address, city):
        # First get or create the penjual
        penjual_id = self.get_penjual_id_by_name_and_city(seller_name, seller_address, city)
        
        # Now insert into the produk table
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO produk (nama, harga, penjualid) VALUES (%s, %s, %s)"
        data = (product_name, harga, penjual_id)  
        cursor.execute(query, data)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
        
    def update_product_details(self, id, product_name, harga, seller_name, seller_address, city):
        # First get or create the penjual
        penjual_id = self.get_penjual_id_by_name_and_city(seller_name, seller_address, city)
        
        # Now update the produk table
        db = self.connect()
        cursor = db.cursor()
        query = "UPDATE produk SET nama = %s, harga = %s, penjualid = %s WHERE id = %s"
        cursor.execute(query, (product_name, harga, penjual_id, id))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows
        
    def delete_product_details(self, id):
        db = self.connect()
        cursor = db.cursor()
        # Delete from the base table (produk) instead of the view (product_details)
        query = "DELETE FROM produk WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        db.close()
        return affected_rows 