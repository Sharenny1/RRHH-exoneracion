from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Capacitacion
from datetime import datetime
from utils import solo_rh


capacitacion_bp = Blueprint("capacitacion", __name__)


@capacitacion_bp.route("/capacitaciones", methods=["GET", "POST"])
@login_required
@solo_rh
def capacitaciones():

    if request.method == "POST":

        cap_id = request.form.get("id")

        descripcion = request.form.get("descripcion")
        nivel = request.form.get("nivel")
        fecha_desde = datetime.strptime(request.form.get("fecha_desde"), "%Y-%m-%d")
        fecha_hasta = datetime.strptime(request.form.get("fecha_hasta"), "%Y-%m-%d")
        institucion = request.form.get("institucion")

        # EDITAR
        if cap_id:
            cap = Capacitacion.query.get_or_404(cap_id)
            cap.descripcion = descripcion
            cap.nivel = nivel
            cap.fecha_desde = fecha_desde
            cap.fecha_hasta = fecha_hasta
            cap.institucion = institucion

        # CREAR
        else:
            nueva = Capacitacion(
                descripcion=descripcion,
                nivel=nivel,
                fecha_desde=fecha_desde,
                fecha_hasta=fecha_hasta,
                institucion=institucion
            )
            db.session.add(nueva)

        db.session.commit()
        return redirect(url_for("capacitacion.capacitaciones"))

    lista = Capacitacion.query.all()
    return render_template("capacitaciones.html", capacitaciones=lista)


@capacitacion_bp.route("/capacitaciones/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_capacitacion(id):
    cap = Capacitacion.query.get_or_404(id)
    db.session.delete(cap)
    db.session.commit()
    return redirect(url_for("capacitacion.capacitaciones"))
