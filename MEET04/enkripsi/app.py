from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = secrets.token_hex(16)

db = SQLAlchemy(app)

class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(100), nullable=False)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(180), nullable=False)
    password = db.Column(db.String(180), nullable=False)
    
def cekuser():
    if not User.query.first():  
        newUser = User(username="admin")
        newUser.password = generate_password_hash("qwerty")
        db.session.add(newUser)
        db.session.commit()
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    if 'session' in session:
        if request.method == "POST":
            nama = request.form['nama']
            kelas = request.form['kelas']
            siswa = Siswa(nama=nama, kelas=kelas)
            db.session.add(siswa)
            db.session.commit()
            return redirect("/")
        siswa_list = Siswa.query.filter_by(kelas="12").all()
        # siswa_list = Siswa.query.all()
        
        return render_template('index.html', siswa_list=siswa_list)
    return render_template('login.html')


@app.route("/hapus/<int:id>")
def hapus(id):
    siswa = Siswa.query.get(id)
    db.session.delete(siswa)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    siswa = Siswa.query.get(id)
    
    if request.method == "GET":
        return render_template('update.html', siswa=siswa)
    
    if request.method == "POST":
        siswa.nama = request.form['nama']
        siswa.kelas = request.form['kelas']
        db.session.commit()
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['session'] = True
            return redirect("/")
        return redirect("/login")
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('session', None)
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        cekuser()
    app.run(debug=True)
