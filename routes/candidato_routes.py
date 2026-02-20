from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Candidato, Empleado
from utils import solo_rh
from datetime import datetime

candidato_bp = Blueprint("candidato", __name__)

# ==========================================
# VISTA COMPARTIDA (RH + POSTULANTE)
# ==========================================

@candidato_bp.route("/candidatos", methods=["GET", "POST"])
@login_required
def candidatos():

    # =========================
    # POST (CREAR / EDITAR)
    # =========================
    if request.method == "POST":

        candidato_id = request.form.get("id")

        cedula = request.form.get("cedula")
        nombre = request.form.get("nombre")
        puesto = request.form.get("puesto")
        departamento = request.form.get("departamento")
        salario = abs(float(request.form.get("salario")))
        competencias = request.form.get("competencias")
        capacitaciones = request.form.get("capacitaciones")
        experiencia = request.form.get("experiencia")
        recomendado = request.form.get("recomendado")

        # =====================
        # SI ES RH
        # =====================
        if current_user.rol == "RH":

            estado = request.form.get("estado")

            if candidato_id:
                candidato = Candidato.query.get_or_404(candidato_id)

                candidato.cedula = cedula
                candidato.nombre = nombre
                candidato.puesto_aspira = puesto
                candidato.departamento = departamento
                candidato.salario_aspira = salario
                candidato.competencias = competencias
                candidato.capacitaciones = capacitaciones
                candidato.experiencia = experiencia
                candidato.recomendado_por = recomendado
                candidato.estado = estado

            else:
                nuevo = Candidato(
                    usuario_id=current_user.id,
                    cedula=cedula,
                    nombre=nombre,
                    puesto_aspira=puesto,
                    departamento=departamento,
                    salario_aspira=salario,
                    competencias=competencias,
                    capacitaciones=capacitaciones,
                    experiencia=experiencia,
                    recomendado_por=recomendado,
                    estado=estado
                )
                db.session.add(nuevo)

        # =====================
        # SI ES POSTULANTE
        # =====================
        else:

            existente = Candidato.query.filter_by(
                usuario_id=current_user.id
            ).first()

            if existente:
                existente.cedula = cedula
                existente.nombre = nombre
                existente.puesto_aspira = puesto
                existente.departamento = departamento
                existente.salario_aspira = salario
                existente.competencias = competencias
                existente.capacitaciones = capacitaciones
                existente.experiencia = experiencia
                existente.recomendado_por = recomendado
                existente.estado = "Pendiente"

            else:
                nuevo = Candidato(
                    usuario_id=current_user.id,
                    cedula=cedula,
                    nombre=nombre,
                    puesto_aspira=puesto,
                    departamento=departamento,
                    salario_aspira=salario,
                    competencias=competencias,
                    capacitaciones=capacitaciones,
                    experiencia=experiencia,
                    recomendado_por=recomendado,
                    estado="Pendiente"
                )
                db.session.add(nuevo)

        db.session.commit()
        return redirect(url_for("candidato.candidatos"))

    # =========================
    # GET CON FILTROS
    # =========================

    query = Candidato.query

    # FILTRO POR PUESTO
    puesto = request.args.get("puesto")
    if puesto:
        query = query.filter(Candidato.puesto_aspira.ilike(f"%{puesto}%"))

    # FILTRO POR COMPETENCIA
    competencia = request.args.get("competencia")
    if competencia:
        query = query.filter(Candidato.competencias.ilike(f"%{competencia}%"))

    # FILTRO POR CAPACITACION
    capacitacion = request.args.get("capacitacion")
    if capacitacion:
        query = query.filter(Candidato.capacitaciones.ilike(f"%{capacitacion}%"))

    # FILTRO SEGÚN ROL
    if current_user.rol == "POSTULANTE":
        query = query.filter_by(usuario_id=current_user.id)

    lista = query.all()

    return render_template("candidatos.html", candidatos=lista)


# ==========================================
# ELIMINAR (SOLO RH)
# ==========================================

@candidato_bp.route("/candidatos/eliminar/<int:id>", methods=["POST"])
@login_required
@solo_rh
def eliminar_candidato(id):

    candidato = Candidato.query.get_or_404(id)
    db.session.delete(candidato)
    db.session.commit()

    return redirect(url_for("candidato.candidatos"))


# ==========================================
# SELECCIONAR (CONTRATAR)
# ==========================================

@candidato_bp.route("/candidatos/seleccionar/<int:id>")
@login_required
@solo_rh
def seleccionar_candidato(id):

    candidato = Candidato.query.get_or_404(id)

    nuevo_empleado = Empleado(
        cedula=candidato.cedula,
        nombre=candidato.nombre,
        fecha_ingreso=datetime.today(),
        departamento=candidato.departamento,
        puesto=candidato.puesto_aspira,
        salario_mensual=candidato.salario_aspira,
        estado="Activo"
    )

    db.session.add(nuevo_empleado)

    candidato.estado = "Contratado"
    candidato.fecha_proceso = datetime.today()

    db.session.commit()

    return redirect(url_for("candidato.candidatos"))


# ==========================================
# RECHAZAR
# ==========================================

@candidato_bp.route("/candidatos/rechazar/<int:id>")
@login_required
@solo_rh
def rechazar_candidato(id):

    candidato = Candidato.query.get_or_404(id)

    candidato.estado = "Rechazado"
    candidato.fecha_proceso = datetime.today()

    db.session.commit()

    return redirect(url_for("candidato.candidatos"))
