from flask import *
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    database="ecommerce",
    user="root",
    password=""
)

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route("/simpan", methods=["POST", "GET"])
def simpan():
    if request.method == "POST":
        cursor = mydb.cursor()
        nama = request.form.get("nama")
        q = "insert into kota (id, nama) values (%s, %s)"
        data = (None, nama)  
        cursor.execute(q, data)
        mydb.commit()
        cursor.close()
    return redirect(url_for("data_view"))

@app.route("/data_view")
def data_view():
    cursor = mydb.cursor()
    cursor.execute("select * from kota")
    data = cursor.fetchall()
    cursor.close()
    return render_template("data_view.html", data=data)

@app.route("/hapus/<id>")  
def hapus(id):
    cursor = mydb.cursor()
    q = "delete from kota where id = %s"
    cursor.execute(q, (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for("data_view"))

@app.route("/update/<id>", methods=["GET", "POST"])  
def update(id):
    cursor = mydb.cursor()
    
    if request.method == "GET":
        q = "select * from kota where id = %s"
        cursor.execute(q, (id,))
        value = cursor.fetchone()
        cursor.close()
        return render_template("data_update.html", value=value)
    
    if request.method == "POST":
        nama = request.form.get("nama")
        q = "update kota set nama = %s where id = %s"
        cursor.execute(q, (nama, id))
        mydb.commit()
        cursor.close()
        return redirect(url_for("data_view"))


if __name__ == "__main__":
    app.run(debug=True)
