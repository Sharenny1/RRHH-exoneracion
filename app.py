from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, Usuario

# IMPORTAR BLUEPRINTS
from routes.auth_routes import auth_bp
from routes.candidato_routes import candidato_bp
from routes.empleado_routes import empleado_bp
from routes.competencia_routes import competencia_bp
from routes.idioma_routes import idioma_bp
from routes.puesto_routes import puesto_bp
from routes.capacitacion_routes import capacitacion_bp
from routes.dashboard_routes import dashboard_bp
from routes.experiencia_routes import experiencia_bp


# =========================
# CREAR APP
# =========================
app = Flask(__name__)
app.config.from_object(Config)

# =========================
# INICIALIZAR DB
# =========================
db.init_app(app)

# =========================
# LOGIN MANAGER
# =========================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))


# =========================
# REGISTRAR BLUEPRINTS
# =========================
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(candidato_bp)
app.register_blueprint(empleado_bp)
app.register_blueprint(competencia_bp)
app.register_blueprint(idioma_bp)
app.register_blueprint(puesto_bp)
app.register_blueprint(capacitacion_bp)
app.register_blueprint(experiencia_bp)




# =========================
# CREAR TABLAS
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


