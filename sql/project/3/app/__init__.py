from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    from app.config import Config
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)
    
    from app.controllers.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)
    
    from app.controllers.product_routes import product_blueprint
    from app.controllers.kategori_routes import kategori_blueprint
    from app.controllers.kategori_penjual_routes import kategori_penjual_blueprint
    from app.controllers.penjual_routes import penjual_blueprint
    from app.controllers.product_details_routes import product_details_blueprint
    from app.controllers.kota_routes import kota_blueprint
    
    app.register_blueprint(product_blueprint)
    app.register_blueprint(kategori_blueprint)
    app.register_blueprint(kategori_penjual_blueprint)
    app.register_blueprint(penjual_blueprint)
    app.register_blueprint(product_details_blueprint)
    app.register_blueprint(kota_blueprint)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    return app

