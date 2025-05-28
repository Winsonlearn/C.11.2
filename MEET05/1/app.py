from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

with app.app_context():
    db.create_all()
    if not Category.query.first():
        db.session.add_all([
            Category(name="makanan"),
            Category(name="minuman")
        ])
        db.session.commit()

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category_id = request.form["category_id"]
        product = Product(name=name, price=price, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        return redirect("/")
    # product_list = Product.query.all()
    # product_list = Product.query.get(1)
    # product_list = Product.query.filter(Product.price > 10).all()
    product_list = Product.query.filter_by(price=120).all()
    categories = Category.query.all()
    return render_template('index.html', product_list=product_list, categories=categories)

@app.route('/hapus/<id>')
def hapus(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")

@app.route('/update/<id>', methods=["POST", "GET"])
def update(id):
    product = Product.query.get(id)
    categories = Category.query.all()
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = request.form["price"]
        product.category_id = request.form["category_id"]
        db.session.commit()
        return redirect("/")
    return render_template("update.html", product=product, categories=categories)

@app.route('/kategori', methods=["POST", "GET"])
def kategori():
    if request.method == "POST":
        name = request.form["name"]
        db.session.add(Category(name=name))
        db.session.commit()
        return redirect("/kategori")
    kategori_list = Category.query.all()
    return render_template("kategori.html", kategori_list=kategori_list)

@app.route('/kategori/update/<id>', methods=["POST", "GET"])
def kategori_update(id):
    kategori = Category.query.get(id)
    if request.method == "POST":
        kategori.name = request.form["name"]
        db.session.commit()
        return redirect("/kategori")
    return render_template("update.html", kategori=kategori)

@app.route('/kategori/hapus/<id>')
def kategori_hapus(id):
    kategori = Category.query.get(id)
    db.session.delete(kategori)
    db.session.commit()
    return redirect("/kategori")

if __name__ == '__main__':
    app.run(debug=True)
