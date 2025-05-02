from flask import *
from app.models.kota_model import KotaModel

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
@routes_blueprint.route('/home')
def home():
    return render_template('home.html')

@routes_blueprint.route('/data')
def data():
    return render_template('data.html')

@routes_blueprint.route("/simpan", methods=["POST", "GET"])
def simpan():
    if request.method == "POST":
        kota_model = KotaModel()
        nama = request.form.get("nama")
        kota_model.insert_kota(nama)
    return redirect(url_for("routes.data_view"))

@routes_blueprint.route("/data_view")
def data_view():
    kota_model = KotaModel()
    data = kota_model.get_all_kota()
    return render_template("data_view.html", data=data)

@routes_blueprint.route("/hapus/<id>")  
def hapus(id):
    kota_model = KotaModel()
    kota_model.delete_kota(id)
    return redirect(url_for("routes.data_view"))

@routes_blueprint.route("/update/<id>", methods=["GET", "POST"])  
def update(id):
    kota_model = KotaModel()
    
    if request.method == "GET":
        value = kota_model.get_kota_by_id(id)
        return render_template("data_update.html", value=value)
    
    if request.method == "POST":
        nama = request.form.get("nama")
        kota_model.update_kota(id, nama)
        return redirect(url_for("routes.data_view"))

