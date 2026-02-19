from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from models import db, Candidato, Empleado

candidato_bp = Blueprint("candidato_bp", __name__)

# ==============================
# LISTAR CANDIDATOS
# ==============================
@candidato_bp.route("/candidatos")
@login_required
def listar_candidatos():
    candidatos = Candidato.query.filter_by(estado="Postulante").all()
    return render_template("candidatos/listar.html", candidatos=candidatos)


# ==============================
# CREAR CANDIDATO
# ==============================
@candidato_bp.route("/candidatos/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_candidato():

    if request.method == "POST":
        nuevo = Candidato(
            cedula=request.form["cedula"],
            nombre=request.form["nombre"],
            puesto_aspira=request.form["puesto_aspira"],
            departamento=request.form["departamento"],
            salario_aspira=request.form["salario_aspira"],
            competencias=request.form["competencias"],
            capacitaciones=request.form["capacitaciones"],
            experiencia=request.form["experiencia"],
            recomendado_por=request.form["recomendado_por"],
            estado="Postulante"
        )

        db.session.add(nuevo)
        db.session.commit()

        flash("Candidato registrado correctamente", "success")
        return redirect(url_for("candidato_bp.listar_candidatos"))

    return render_template("candidatos/nuevo.html")


# ==============================
# PROCESO DE SELECCIÓN
# ==============================
@candidato_bp.route("/candidatos/seleccionar/<int:id>", methods=["POST"])
@login_required
def seleccionar_candidato(id):

    candidato = Candidato.query.get_or_404(id)

    # Crear nuevo empleado
    nuevo_empleado = Empleado(
        cedula=candidato.cedula,
        nombre=candidato.nombre,
        departamento=candidato.departamento,
        puesto=candidato.puesto_aspira,
        salario=candidato.salario_aspira,
        fecha_ingreso=datetime.utcnow(),
        estado="Activo"
    )

    # Cambiar estado del candidato
    candidato.estado = "Seleccionado"

    db.session.add(nuevo_empleado)
    db.session.commit()

    flash("Candidato seleccionado y convertido en empleado", "success")
    return redirect(url_for("candidato_bp.listar_candidatos"))


# ==============================
# ELIMINAR CANDIDATO
# ==============================
@candidato_bp.route("/candidatos/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_candidato(id):

    candidato = Candidato.query.get_or_404(id)
    db.session.delete(candidato)
    db.session.commit()

    flash("Candidato eliminado", "danger")
    return redirect(url_for("candidato_bp.listar_candidatos"))
