class Config:
    MYSQL_HOST = "localhost"
    MYSQL_DATABASE = "ecommerce"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    SECRET_KEY = "your_secret_key_here"
    
    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  