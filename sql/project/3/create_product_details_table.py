import pymysql
from app import create_app
from app.config import Config

def create_product_details_table():
    """Create the product_details table if it doesn't exist."""
    app = create_app()
    with app.app_context():
        # Connect to the database
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE
        )
        
        try:
            with connection.cursor() as cursor:
                # Check if the table exists
                cursor.execute("SHOW TABLES LIKE 'product_details'")
                table_exists = cursor.fetchone()
                
                if not table_exists:
                    # Create the table if it doesn't exist
                    cursor.execute("""
                    CREATE TABLE product_details (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        produk_id INT NOT NULL,
                        weight FLOAT NULL,
                        description TEXT NULL,
                        FOREIGN KEY (produk_id) REFERENCES produk(id) ON DELETE CASCADE
                    )
                    """)
                    connection.commit()
                    print("Successfully created product_details table")
                else:
                    # Check if the produkid column exists
                    cursor.execute("SHOW COLUMNS FROM product_details LIKE 'produkid'")
                    produkid_exists = cursor.fetchone()
                    
                    if produkid_exists:
                        # Rename the column if it exists
                        cursor.execute("ALTER TABLE product_details CHANGE produkid produk_id INT NOT NULL")
                        connection.commit()
                        print("Successfully renamed 'produkid' to 'produk_id'")
                    
                    # Check if the produk_id column exists
                    cursor.execute("SHOW COLUMNS FROM product_details LIKE 'produk_id'")
                    produk_id_exists = cursor.fetchone()
                    
                    if not produk_id_exists:
                        # Add the column if it doesn't exist
                        cursor.execute("ALTER TABLE product_details ADD COLUMN produk_id INT NOT NULL")
                        cursor.execute("ALTER TABLE product_details ADD FOREIGN KEY (produk_id) REFERENCES produk(id) ON DELETE CASCADE")
                        connection.commit()
                        print("Successfully added 'produk_id' column")
                        
                    print("product_details table already exists, structure updated if needed")
        finally:
            connection.close()

if __name__ == "__main__":
    create_product_details_table()
    print("Database structure update completed") 