from flask import Blueprint, render_template, request
from flask_login import login_required
from models import Empleado
from datetime import datetime

reporte_bp = Blueprint('reporte', __name__)


@reporte_bp.route("/reportes", methods=["GET", "POST"])
@login_required
def reportes():

    empleados = []

    if request.method == "POST":
        fecha_desde = request.form.get("fecha_desde")
        fecha_hasta = request.form.get("fecha_hasta")

        if fecha_desde and fecha_hasta:
            fecha_desde = datetime.strptime(fecha_desde, "%Y-%m-%d")
            fecha_hasta = datetime.strptime(fecha_hasta, "%Y-%m-%d")

            empleados = Empleado.query.filter(
                Empleado.fecha_ingreso.between(fecha_desde, fecha_hasta)
            ).all()

    return render_template("reportes.html", empleados=empleados)
