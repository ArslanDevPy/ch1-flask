from flask import render_template
from . import main


@main.route('/')
@main.route('dashboard/')
def index():
    return render_template("main/index.html")
