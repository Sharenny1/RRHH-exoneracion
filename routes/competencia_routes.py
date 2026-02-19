from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Competencia
from utils import solo_rh


competencia_bp = Blueprint('competencia', __name__)


@competencia_bp.route("/competencias", methods=["GET", "POST"])
@login_required
@solo_rh
def competencias():

    if request.method == "POST":
        comp_id = request.form.get("id")
        descripcion = request.form.get("descripcion")
        estado = request.form.get("estado")

        if comp_id:
            competencia = Competencia.query.get(comp_id)
            competencia.nombre = descripcion
            competencia.estado = estado
        else:
            nueva = Competencia(nombre=descripcion, estado=estado)
            db.session.add(nueva)

        db.session.commit()
        return redirect(url_for("competencia.competencias"))

    lista = Competencia.query.all()
    return render_template("competencias.html", competencias=lista)

@competencia_bp.route("/competencias/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_competencia(id):
    competencia = Competencia.query.get_or_404(id)
    db.session.delete(competencia)
    db.session.commit()
    return redirect(url_for("competencia.competencias"))
