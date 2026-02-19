from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Empleado
from datetime import datetime
from utils import solo_rh
from sqlalchemy import extract
from models import Candidato


empleado_bp = Blueprint("empleado", __name__)


@empleado_bp.route("/empleados", methods=["GET", "POST"])
@login_required
@solo_rh
def empleados():

    if request.method == "POST":

        empleado_id = request.form.get("id")

        cedula = request.form.get("cedula")
        nombre = request.form.get("nombre")
        fecha_ingreso = datetime.strptime(
            request.form.get("fecha_ingreso"), "%Y-%m-%d"
        )
        departamento = request.form.get("departamento")
        puesto = request.form.get("puesto")
        salario = float(request.form.get("salario"))
        estado = request.form.get("estado")

        if empleado_id:
            empleado = Empleado.query.get_or_404(empleado_id)

            empleado.cedula = cedula
            empleado.nombre = nombre
            empleado.fecha_ingreso = fecha_ingreso
            empleado.departamento = departamento
            empleado.puesto = puesto
            empleado.salario_mensual = salario
            empleado.estado = estado

        else:
            nuevo = Empleado(
                cedula=cedula,
                nombre=nombre,
                fecha_ingreso=fecha_ingreso,
                departamento=departamento,
                puesto=puesto,
                salario_mensual=salario,
                estado=estado
            )
            db.session.add(nuevo)

        db.session.commit()
        return redirect(url_for("empleado.empleados"))

    lista = Empleado.query.all()
    return render_template("empleados.html", empleados=lista)


@empleado_bp.route("/empleados/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_empleado(id):

    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for("empleado.empleados"))

@empleado_bp.route("/reporte/nuevo-ingreso", methods=["GET", "POST"])
@login_required
@solo_rh
def reporte_nuevo_ingreso():

    empleados = []

    if request.method == "POST":

        fecha_inicio = datetime.strptime(
            request.form.get("fecha_inicio"), "%Y-%m-%d"
        )

        fecha_fin = datetime.strptime(
            request.form.get("fecha_fin"), "%Y-%m-%d"
        )

        empleados = Empleado.query.filter(
            Empleado.fecha_ingreso.between(fecha_inicio, fecha_fin)
        ).all()

    return render_template(
        "reporte_nuevo_ingreso.html",
        empleados=empleados
    )

@empleado_bp.route("/reporte/proceso-mensual", methods=["GET", "POST"])
@login_required
@solo_rh
def reporte_proceso_mensual():

    datos = []

    if request.method == "POST":

        mes = int(request.form.get("mes"))
        anio = int(request.form.get("anio"))

        contratados = Candidato.query.filter(
            extract('month', Candidato.id) == mes,
            extract('year', Candidato.id) == anio,
            Candidato.estado == "Contratado"
        ).count()

        rechazados = Candidato.query.filter(
            Candidato.estado == "Rechazado"
        ).count()

        pendientes = Candidato.query.filter(
            Candidato.estado == "Pendiente"
        ).count()

        datos = {
            "contratados": contratados,
            "rechazados": rechazados,
            "pendientes": pendientes
        }

    return render_template("reporte_proceso_mensual.html", datos=datos)
