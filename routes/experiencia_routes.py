from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Experiencia

experiencia_bp = Blueprint('experiencia', __name__)


@experiencia_bp.route("/experiencias", methods=["GET", "POST"])
@login_required
def experiencias():

    if request.method == "POST":
        exp_id = request.form.get("id")
        empresa = request.form.get("empresa")
        puesto = request.form.get("puesto")
        fecha_desde = request.form.get("fecha_desde")
        fecha_hasta = request.form.get("fecha_hasta")
        salario = request.form.get("salario")

        if exp_id:
            # EDITAR
            experiencia = Experiencia.query.get(exp_id)
            experiencia.empresa = empresa
            experiencia.puesto = puesto
            experiencia.fecha_desde = fecha_desde
            experiencia.fecha_hasta = fecha_hasta
            experiencia.salario = salario
        else:
            # CREAR
            nueva = Experiencia(
                empresa=empresa,
                puesto=puesto,
                fecha_desde=fecha_desde,
                fecha_hasta=fecha_hasta,
                salario=salario
            )
            db.session.add(nueva)

        db.session.commit()
        return redirect(url_for("experiencia.experiencias"))

    lista = Experiencia.query.all()
    return render_template("experiencias.html", experiencias=lista)
