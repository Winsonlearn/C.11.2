from flask import *
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(seconds=5)
# session.permanent(True)

users = [
    {
    "username": "user1",
    "password": "1234",
    "role": "admin"
    },
    {
    "username": "user2",
    "password": "5678",
    "role": "user"
    },
    {
    "username": "user3",
    "password": "4321",
    "role": "guest"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bio', methods=["POST", "GET"])
def bio():
    return render_template("bio.html", 
                            nama=request.form.get("nama"),
                            kelas=request.form.get("kelas"),
                            email=request.form.get("email"),
                            tempat=request.form.get("tempat"),
                            tanggal=request.form.get("tanggal"),
                            cita_cita=request.form.get("cita_cita"),
                            agama=request.form.get("agama"),
                            tentang=request.form.get("tentang"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        for user in users:
            if user["username"] == username and user["password"] == password:
                session['user'] = username
                session.permanent = True
                session['role'] = user["role"]
                return redirect(url_for("admin"))
        # for user in users:
        #     if user["username"] == username and user["password"] == password:
        #         session['user'] = username
        #         session['role'] = user["role"]
        #         if user["role"] == "admin":
        #             return redirect(url_for("admin"))
        #         return redirect(url_for("anggota"))
        
        return render_template("login.html")
    return render_template("login.html")

@app.route("/admin")
def admin():
    # if session.get("user") and session.get("role") == "admin":
    #     return render_template("admin.html")
    if session.get("user"):
        return render_template("admin.html")
    return redirect(url_for("login"))

# @app.route("/anggota")
# def anggota():
#     if session.get("user") and session.get("role") == "user":
#         return render_template("user.html")
#     return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)  
    session.pop("role", None)  
    
    # destroy all session :
    # session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
