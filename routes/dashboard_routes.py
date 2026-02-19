from flask import Blueprint, render_template
from flask_login import login_required
from models import (
    Candidato,
    Empleado,
    Puesto,
    Competencia,
    Idioma,
    Capacitacion
)

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        total_candidatos=Candidato.query.count(),
        total_empleados=Empleado.query.count(),
        total_puestos=Puesto.query.count(),
        total_competencias=Competencia.query.count(),
        total_idiomas=Idioma.query.count(),
        total_capacitaciones=Capacitacion.query.count()
    )
