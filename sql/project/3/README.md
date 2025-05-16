# E-Commerce Project ORM Version

This project is an e-commerce web application that uses SQLAlchemy ORM (Object-Relational Mapping) instead of raw SQL queries for database operations.

## Features

- Products management
- Sellers management
- Categories management
- City management
- Product details management
- Seller-category associations

## Technology Stack

- Flask: Web framework
- SQLAlchemy: ORM library
- MySQL: Database
- PyMySQL: MySQL database adapter
- Flask-SQLAlchemy: Flask extension for SQLAlchemy

## Setup

1. Create a virtual environment:
   ```
   python -m venv myvenv
   ```

2. Activate the virtual environment:
   - Windows: `myvenv\Scripts\activate`
   - Linux/Mac: `source myvenv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Make sure MySQL is running and the database `ecommerce` exists

5. Run the application:
   ```
   python run.py
   ```

## ORM Benefits

- Cleaner code using Python classes to represent database tables
- Automatic table creation and schema management
- Built-in relationships between tables
- Improved protection against SQL injection
- Database-agnostic code (can easily switch database engines)
- Type safety and easier debugging

## Project Structure

- `app/`: Main application package
  - `models/`: SQLAlchemy ORM models
  - `controllers/`: Route controllers
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JS)
  - `__init__.py`: Application factory
  - `config.py`: Application configuration

## Database Schema

The database schema includes the following tables:
- produk (Product)
- penjual (Seller)
- kategori (Category)
- kategori_penjual (SellerCategory)
- kota (City)
- product_details (ProductDetails) 