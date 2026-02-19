from flask import Blueprint, render_template
from flask_login import login_required
from models import Empleado

empleado_bp = Blueprint('empleado', __name__)

@empleado_bp.route("/empleados")
@login_required
def empleados():
    lista = Empleado.query.all()
    return render_template("empleados.html", empleados=lista)
