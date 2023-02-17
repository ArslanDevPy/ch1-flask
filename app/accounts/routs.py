from flask import render_template
from . import account, forms


@account.route('/login')
def login():
    context = {}
    fm = forms.Login()
    context['form'] = fm
    context['title'] = "Login"
    return render_template("accounts/login.html", **context)


@account.route('/register')
def register():
    context = {}
    fm = forms.Register()
    context['form'] = fm
    context['title'] = "Register"
    return render_template("accounts/register.html", **context)
