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
        try:
            kota_model.insert_kota(nama)
            flash("Data kota berhasil ditambahkan!", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
    return redirect(url_for("routes.data_view"))

@routes_blueprint.route("/data_view")
def data_view():
    kota_model = KotaModel()
    try:
        data = kota_model.get_all_kota()
        if not data:
            flash("Belum ada data kota tersedia.", "info")
    except Exception as e:
        data = []
        flash(f"Error mengambil data: {str(e)}", "danger")
    return render_template("data_view.html", data=data)

@routes_blueprint.route("/hapus/<id>", methods=["GET", "POST"])  
def hapus(id):
    kota_model = KotaModel()
    try:
        kota_model.delete_kota(id)
        flash("Data kota berhasil dihapus!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    return redirect(url_for("routes.data_view"))

@routes_blueprint.route("/update/<id>", methods=["GET", "POST"])  
def update(id):
    kota_model = KotaModel()
    
    if request.method == "GET":
        try:
            value = kota_model.get_kota_by_id(id)
            if not value:
                flash("Data kota tidak ditemukan!", "danger")
                return redirect(url_for("routes.data_view"))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("routes.data_view"))
        return render_template("data_update.html", value=value)
    
    if request.method == "POST":
        nama = request.form.get("nama")
        try:
            kota_model.update_kota(id, nama)
            flash("Data kota berhasil diupdate!", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        return redirect(url_for("routes.data_view"))

