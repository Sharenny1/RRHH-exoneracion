from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Puesto
from utils import solo_rh
from utils import solo_postulante
from flask_login import current_user


puesto_bp = Blueprint("puesto", __name__)


@puesto_bp.route("/puestos", methods=["GET", "POST"])
@login_required
@solo_rh
def puestos():

    if request.method == "POST":

        puesto_id = request.form.get("id")
        nombre = request.form.get("nombre")
        nivel_riesgo = request.form.get("nivel_riesgo")
        salario_min = float(request.form.get("salario_min"))
        salario_max = float(request.form.get("salario_max"))
        estado = request.form.get("estado")

        # Validación salario
        if salario_min > salario_max:
            return "El salario mínimo no puede ser mayor que el máximo"

        if puesto_id:
            puesto = Puesto.query.get_or_404(puesto_id)
            puesto.nombre = nombre
            puesto.nivel_riesgo = nivel_riesgo
            puesto.salario_min = salario_min
            puesto.salario_max = salario_max
            puesto.estado = estado
        else:
            nuevo = Puesto(
                nombre=nombre,
                nivel_riesgo=nivel_riesgo,
                salario_min=salario_min,
                salario_max=salario_max,
                estado=estado
            )
            db.session.add(nuevo)

        db.session.commit()
        return redirect(url_for("puesto.puestos"))

    lista = Puesto.query.all()
    return render_template("puestos.html", puestos=lista)


@puesto_bp.route("/puestos/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_puesto(id):
    puesto = Puesto.query.get_or_404(id)
    db.session.delete(puesto)
    db.session.commit()
    return redirect(url_for("puesto.puestos"))

@puesto_bp.route("/puestos_publicos")
@login_required
@solo_postulante
def puestos_publicos():

    lista = Puesto.query.all()

    return render_template("puestos_publicos.html", puestos=lista)