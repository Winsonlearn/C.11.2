import pymysql
from app.config import Config

def check_database_structure():
    """Check the actual structure of the product_details table."""
    # Connect to the database
    connection = pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE
    )
    
    try:
        with connection.cursor() as cursor:
            # Check if the product_details table exists
            cursor.execute("SHOW TABLES LIKE 'product_details'")
            table_exists = cursor.fetchone()
            
            if table_exists:
                # Show the table structure
                cursor.execute("DESCRIBE product_details")
                columns = cursor.fetchall()
                print("Product Details Table Structure:")
                for column in columns:
                    print(column)
            else:
                print("product_details table doesn't exist")
    finally:
        connection.close()

if __name__ == "__main__":
    check_database_structure() 