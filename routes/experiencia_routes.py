from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, ExperienciaLaboral, Candidato
from datetime import datetime

experiencia_bp = Blueprint("experiencia", __name__)

# =====================================================
# VISTA PRINCIPAL (RH + POSTULANTE)
# =====================================================

@experiencia_bp.route("/experiencias", methods=["GET", "POST"])
@login_required
def experiencias():

    # =================================================
    # POST (CREAR / EDITAR)
    # =================================================
    if request.method == "POST":

        exp_id = request.form.get("id")

        # ---------------------------------------------
        # OBTENER CANDIDATO SEGÚN ROL
        # ---------------------------------------------
        if current_user.rol == "RH":
            candidato_id = request.form.get("candidato_id")
        else:
            candidato = Candidato.query.filter_by(
                usuario_id=current_user.id
            ).first()

            if not candidato:
                return redirect(url_for("candidato.candidatos"))

            candidato_id = candidato.id

        # ---------------------------------------------
        # FECHAS
        # ---------------------------------------------
        fecha_desde = datetime.strptime(
            request.form.get("fecha_desde"), "%Y-%m-%d"
        )

        fecha_hasta_str = request.form.get("fecha_hasta")
        fecha_hasta = datetime.strptime(fecha_hasta_str, "%Y-%m-%d") if fecha_hasta_str else None

        # ---------------------------------------------
        # EDITAR EXPERIENCIA
        # ---------------------------------------------
        if exp_id:
            experiencia = ExperienciaLaboral.query.get_or_404(exp_id)

            # Seguridad: si es postulante solo puede editar las suyas
            if current_user.rol == "POSTULANTE":
                candidato = Candidato.query.filter_by(
                    usuario_id=current_user.id
                ).first()

                if not candidato or experiencia.candidato_id != candidato.id:
                    return redirect(url_for("experiencia.experiencias"))

            empresa = request.form.get("empresa")
            puesto = request.form.get("puesto")

            experiencia.empresa = empresa if empresa else "Pendiente"
            experiencia.puesto_ocupado = puesto if puesto else "Pendiente"

            experiencia.fecha_desde = fecha_desde
            experiencia.fecha_hasta = fecha_hasta
            experiencia.salario = float(request.form.get("salario"))

        # ---------------------------------------------
        # CREAR EXPERIENCIA
        # ---------------------------------------------
        else:
            empresa = request.form.get("empresa")
            puesto = request.form.get("puesto")

            nueva = ExperienciaLaboral(
                candidato_id=candidato_id,
                empresa=empresa if empresa else "Pendiente",
                puesto_ocupado=puesto if puesto else "Pendiente",
                fecha_desde=fecha_desde,
                fecha_hasta=fecha_hasta,
                salario=float(request.form.get("salario"))
            )

            db.session.add(nueva)

        db.session.commit()
        return redirect(url_for("experiencia.experiencias"))

    # =================================================
    # GET (MOSTRAR EXPERIENCIAS)
    # =================================================

    # RH VE TODO
    if current_user.rol == "RH":
        lista = ExperienciaLaboral.query.all()
        candidatos = Candidato.query.all()

    # POSTULANTE VE SOLO LAS SUYAS
    else:
        candidato = Candidato.query.filter_by(
            usuario_id=current_user.id
        ).first()

        if candidato:
            lista = ExperienciaLaboral.query.filter_by(
                candidato_id=candidato.id
            ).all()
        else:
            lista = []

        candidatos = []

    return render_template(
        "experiencias.html",
        experiencias=lista,
        candidatos=candidatos
    )


# =====================================================
# ELIMINAR EXPERIENCIA
# =====================================================

@experiencia_bp.route("/experiencias/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_experiencia(id):

    exp = ExperienciaLaboral.query.get_or_404(id)

    # Si es postulante solo puede eliminar las suyas
    if current_user.rol == "POSTULANTE":
        candidato = Candidato.query.filter_by(
            usuario_id=current_user.id
        ).first()

        if not candidato or exp.candidato_id != candidato.id:
            return redirect(url_for("experiencia.experiencias"))

    db.session.delete(exp)
    db.session.commit()

    return redirect(url_for("experiencia.experiencias"))
