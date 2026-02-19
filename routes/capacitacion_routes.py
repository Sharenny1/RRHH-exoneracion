from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Capacitacion

capacitacion_bp = Blueprint("capacitacion", __name__)


@capacitacion_bp.route("/capacitaciones", methods=["GET", "POST"])
@login_required
def capacitaciones():

    if request.method == "POST":

        cap_id = request.form.get("id")
        nombre = request.form.get("nombre")
        estado = request.form.get("estado")

        # EDITAR
        if cap_id:
            cap = Capacitacion.query.get_or_404(cap_id)
            cap.nombre = nombre
            cap.estado = estado

        # CREAR
        else:
            nueva = Capacitacion(nombre=nombre, estado=estado)
            db.session.add(nueva)

        db.session.commit()
        return redirect(url_for("capacitacion.capacitaciones"))

    lista = Capacitacion.query.all()
    return render_template("capacitaciones.html", capacitaciones=lista)


@capacitacion_bp.route("/capacitaciones/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_capacitacion(id):
    cap = Capacitacion.query.get_or_404(id)
    db.session.delete(cap)
    db.session.commit()
    return redirect(url_for("capacitacion.capacitaciones"))
