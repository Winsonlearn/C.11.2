from flask import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

users = [
    {
        "username" : "user",
        "password" : "1234",
        "role" : "admin"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bio', methods = ["POST", "GET"])
def bio():
    return render_template("bio.html", 
                            nama = request.form["nama"],
                            kelas = request.form["kelas"],
                            email = request.form["email"],
                            tempat = request.form["tempat"],
                            tanggal = request.form["tanggal"],
                            cita_cita = request.form["cita_cita"],
                            agama = request.form["agama"],
                            tentang = request.form["tentang"])
    
if __name__ == "__main__":
    app.run(debug=True)