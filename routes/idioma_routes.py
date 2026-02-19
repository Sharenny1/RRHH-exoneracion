from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Idioma
from utils import solo_rh



idioma_bp = Blueprint("idioma", __name__)


@idioma_bp.route("/idiomas", methods=["GET", "POST"])
@login_required
@solo_rh
def idiomas():

    # CREAR o EDITAR
    if request.method == "POST":

        idioma_id = request.form.get("id")
        nombre = request.form.get("nombre")
        estado = request.form.get("estado")

        # EDITAR
        if idioma_id:
            idioma = Idioma.query.get_or_404(idioma_id)
            idioma.nombre = nombre
            idioma.estado = estado

        # CREAR
        else:
            nuevo = Idioma(nombre=nombre, estado=estado)
            db.session.add(nuevo)

        db.session.commit()
        return redirect(url_for("idioma.idiomas"))

    # GET
    lista = Idioma.query.all()
    return render_template("idiomas.html", idiomas=lista)


@idioma_bp.route("/idiomas/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_idioma(id):
    idioma = Idioma.query.get_or_404(id)
    db.session.delete(idioma)
    db.session.commit()
    return redirect(url_for("idioma.idiomas"))
