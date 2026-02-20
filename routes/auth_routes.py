from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from models import Usuario

auth_bp = Blueprint("auth", __name__)

# --------------------
# LOGIN
# --------------------
@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Usuario.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get("next")

            
            if user.rol == "RH":
                return redirect(next_page or url_for("dashboard.dashboard"))

         
            return redirect(url_for("candidato.candidatos"))



        return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")


# --------------------
# LOGOUT
# --------------------
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
