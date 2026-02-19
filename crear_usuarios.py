from app import app
from models import db, Usuario
from werkzeug.security import generate_password_hash

with app.app_context():

    admin = Usuario(
        username="admin",
        password=generate_password_hash("admin1234"),
        rol="RH"
    )

    postulante = Usuario(
        username="postulante",
        password=generate_password_hash("post1234"),
        rol="POSTULANTE"
    )

    db.session.add(admin)
    db.session.add(postulante)
    db.session.commit()

    print("Usuarios creados correctamente")
