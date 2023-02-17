from flask import Blueprint
from .. import app

main = Blueprint('main', __name__, url_prefix='/')

from . import forms, routs

app.register_blueprint(main)
