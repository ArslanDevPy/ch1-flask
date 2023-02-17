from flask import Blueprint
from .. import app

account = Blueprint('account', __name__, url_prefix='/account')

from . import forms, routs

app.register_blueprint(account)
