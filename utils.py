from functools import wraps
from flask import abort
from flask_login import current_user


def solo_rh(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # Verifica que esté autenticado primero
        if not current_user.is_authenticated:
            abort(401)

        # Verifica rol
        if current_user.rol != "RH":
            abort(403)

        return func(*args, **kwargs)

    return wrapper

def solo_postulante(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:
            abort(401)

        if current_user.rol != "POSTULANTE":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
