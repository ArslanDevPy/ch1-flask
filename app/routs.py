from flask import render_template
from . import app


@app.errorhandler(400)
def bad_request_error(e):
    context = {'title': "Error 400 – Bad Request", 'status_code': 400, 'message': "You've sent a bad request."}
    return render_template('error.html', **context), 400


@app.errorhandler(403)
def permission_denied_error(e):
    context = {'title': "Error 403 – Forbidden", 'status_code': 403,
               'message': "You don’t have permission to access this url on this server."}
    return render_template('error.html', **context), 403


@app.errorhandler(404)
def page_not_found(e):
    context = {'title': "Error 404 – Page Not Found", 'status_code': 404,
               'message': "The page you requested was not found."}
    return render_template('error.html', **context), 404


@app.errorhandler(500)
def internal_server_error(e):
    context = {'title': "Error 500 – Server Error", 'status_code': 500, 'message': "Oops, something went wrong."}
    return render_template('error.html', **context), 500
