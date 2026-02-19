from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# -------------------------
# USUARIO (Login)
# -------------------------
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # "RH" o "POSTULANTE"



# -------------------------
# COMPETENCIAS
# -------------------------
class Competencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    estado = db.Column(db.String(20), default="Activo")



# -------------------------
# IDIOMAS
# -------------------------
class Idioma(db.Model):
    __tablename__ = "idiomas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.String(20))


# -------------------------
# CAPACITACIONES
# -------------------------
class Capacitacion(db.Model):
    __tablename__ = "capacitaciones"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(150), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)
    fecha_desde = db.Column(db.Date, nullable=False)
    fecha_hasta = db.Column(db.Date, nullable=False)
    institucion = db.Column(db.String(120), nullable=False)




# -------------------------
# PUESTOS
# -------------------------
class Puesto(db.Model):
    __tablename__ = "puestos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    nivel_riesgo = db.Column(db.String(20), nullable=False)
    salario_min = db.Column(db.Float, nullable=False)
    salario_max = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(20), default="Activo")



# -------------------------
# EXPERIENCIA LABORAL
# -------------------------
class ExperienciaLaboral(db.Model):
    __tablename__ = "experiencias"

    id = db.Column(db.Integer, primary_key=True)

    candidato_id = db.Column(
        db.Integer,
        db.ForeignKey("candidatos.id"),
        nullable=False
    )

    empresa = db.Column(db.String(120), nullable=True)
    puesto_ocupado = db.Column(db.String(120), nullable=True)
    fecha_desde = db.Column(db.Date, nullable=True)
    fecha_hasta = db.Column(db.Date, nullable=True)
    salario = db.Column(db.Float, nullable=True)

    candidato = db.relationship("Candidato", backref="experiencias")



# -------------------------
# CANDIDATOS
# -------------------------
class Candidato(db.Model):
    __tablename__ = "candidatos"

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    cedula = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    puesto_aspira = db.Column(db.String(120), nullable=False)
    departamento = db.Column(db.String(120), nullable=False)
    salario_aspira = db.Column(db.Float, nullable=False)
    


    competencias = db.Column(db.Text, nullable=True)
    capacitaciones = db.Column(db.Text, nullable=True)
    experiencia = db.Column(db.Text, nullable=True)
    recomendado_por = db.Column(db.String(120), nullable=True)

    estado = db.Column(db.String(20), default="Pendiente")
    fecha_proceso = db.Column(db.Date, nullable=True)




# -------------------------
# EMPLEADOS
# -------------------------
class Empleado(db.Model):
    __tablename__ = "empleados"

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    departamento = db.Column(db.String(120), nullable=False)
    puesto = db.Column(db.String(120), nullable=False)
    salario_mensual = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(20), default="Activo")

