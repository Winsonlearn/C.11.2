from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "password"

db = SQLAlchemy(app)

class ProfileUser(db.Model):
    __tablename__ = 'profile_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    jk = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(180), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    profile = db.relationship('ProfileUser', backref='user', uselist=False)

def cekuser():
    if not User.query.first():
        admin = User(
            username="admin",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)
        
        user = User(
            username="user",
            password=generate_password_hash("user123"),
            role="user"
        )
        db.session.add(user)
        db.session.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if 'user_id' not in session:
        return redirect("/login")
    
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return redirect("/login")
    
    return render_template('index.html', user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect("/")
        flash("Username atau password salah!")
    return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash("Username sudah digunakan!")
            return redirect("/register")
        
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            role="user" 
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registrasi berhasil! Silakan login.")
        return redirect("/login")
        
    return render_template('register.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'user_id' not in session:
        return redirect("/login")
    
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return redirect("/login")
    
    if request.method == "POST":
        if not user.profile:
            profile = ProfileUser(
                user_id=user.id,
                nama=request.form['nama'],
                jk=request.form['jk'],
                alamat=request.form['alamat']
            )
            db.session.add(profile)
        else:
            user.profile.nama = request.form['nama']
            user.profile.jk = request.form['jk']
            user.profile.alamat = request.form['alamat']
        
        db.session.commit()
        flash("Profil berhasil diperbarui!")
        return redirect("/profile")
    
    return render_template('profile.html', user=user)

@app.route("/data_customer")
def all_profiles():
    if 'user_id' not in session:
        return redirect("/login")
    
    user = User.query.get(session['user_id'])
    if not user or user.role != "admin":
        flash("Akses ditolak!")
        return redirect("/")
    
    users = User.query.all()
    return render_template('data_customer.html', users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        cekuser()
    app.run(debug=True)
