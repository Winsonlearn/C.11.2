from app import create_app, db
from app.models.product_model import Product
from app.models.penjual_model import Penjual
from app.models.kota_model import Kota
from app.models.kategori_model import Kategori
from app.models.kategori_penjual_model import KategoriPenjual
from app.models.product_details_model import ProductDetails

def create_tables():
    """Create all database tables."""
    app = create_app()
    with app.app_context():
        # Drop the product_details table if it exists
        try:
            # If the table exists but has a wrong structure, drop it
            db.engine.execute("DROP TABLE IF EXISTS product_details")
            print("Dropped existing product_details table")
        except Exception as e:
            print(f"Error dropping product_details table: {e}")
        
        # Create all tables
        db.create_all()
        print("All tables created successfully")

if __name__ == "__main__":
    create_tables()
    print("Database structure update completed") 