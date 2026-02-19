from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Puesto

puesto_bp = Blueprint('puesto', __name__)


@puesto_bp.route("/puestos", methods=["GET", "POST"])
@login_required
def puestos():

    if request.method == "POST":
        puesto_id = request.form.get("id")
        nombre = request.form.get("nombre")
        nivel_riesgo = request.form.get("nivel_riesgo")
        salario_min = request.form.get("salario_min")
        salario_max = request.form.get("salario_max")
        estado = request.form.get("estado")

        if puesto_id:
            # EDITAR
            puesto = Puesto.query.get(puesto_id)
            puesto.nombre = nombre
            puesto.nivel_riesgo = nivel_riesgo
            puesto.salario_min = salario_min
            puesto.salario_max = salario_max
            puesto.estado = estado
        else:
            # CREAR NUEVO
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
