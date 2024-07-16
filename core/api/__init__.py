from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import views  # noqa: F401 E402
