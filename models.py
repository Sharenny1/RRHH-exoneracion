from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# -------------------------
# USUARIO (Login)
# -------------------------
class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


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
    nombre = db.Column(db.String(120), nullable=False)
    estado = db.Column(db.String(20), default="Activo")
    descripcion = db.Column(db.String(255))
    nivel = db.Column(db.String(50))  # Grado, Post-grado, etc.
    fecha_desde = db.Column(db.Date)
    fecha_hasta = db.Column(db.Date)
    institucion = db.Column(db.String(255))


# -------------------------
# PUESTOS
# -------------------------
class Puesto(db.Model):
    __tablename__ = "puestos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    nivel_riesgo = db.Column(db.String(20))  # Alto, Medio, Bajo
    salario_min = db.Column(db.Float)
    salario_max = db.Column(db.Float)
    estado = db.Column(db.String(20))


# -------------------------
# EXPERIENCIA LABORAL
# -------------------------
class ExperienciaLaboral(db.Model):
    __tablename__ = "experiencias"
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(255))
    puesto = db.Column(db.String(150))
    fecha_desde = db.Column(db.Date)
    fecha_hasta = db.Column(db.Date)
    salario = db.Column(db.Float)


# -------------------------
# CANDIDATOS
# -------------------------
class Candidato(db.Model):
    __tablename__ = "candidatos"
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(20))
    nombre = db.Column(db.String(150))
    puesto_aspira = db.Column(db.String(150))
    departamento = db.Column(db.String(150))
    salario_aspira = db.Column(db.Float)
    competencias = db.Column(db.Text)
    capacitaciones = db.Column(db.Text)
    experiencia = db.Column(db.Text)
    recomendado_por = db.Column(db.String(150))


# -------------------------
# EMPLEADOS
# -------------------------
class Empleado(db.Model):
    __tablename__ = "empleados"
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(20))
    nombre = db.Column(db.String(150))
    fecha_ingreso = db.Column(db.Date, default=datetime.utcnow)
    departamento = db.Column(db.String(150))
    puesto = db.Column(db.String(150))
    salario = db.Column(db.Float)
    estado = db.Column(db.String(20))
