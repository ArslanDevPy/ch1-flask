from flask import render_template, request, redirect, url_for
from . import account, forms


@account.route('/login', methods=['GET', 'POST'])
def login():
    context = {}
    fm = forms.LoginForm(request.form)
    context['title'] = "Login"
    if request.method == "POST":
        if fm.validate():
            print(fm.validate())
            return redirect(url_for('main.index'))
    context['form'] = fm
    return render_template("accounts/login.html", **context)


@account.route('/register', methods=['GET', 'POST'])
def register():
    context = {}
    fm = forms.RegisterForm(request.form)
    if request.method == "POST":
        if fm.validate():
            return redirect(url_for('account.login'))
    context['form'] = fm
    context['title'] = "Register"
    return render_template("accounts/register.html", **context)
