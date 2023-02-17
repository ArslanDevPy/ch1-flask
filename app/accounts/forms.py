from flask_wtf import Form
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, StringField
from wtforms.validators import Length, InputRequired, Email


class Login(Form):
    email = EmailField(label='Email', validators=[InputRequired(), Length(5, 64), Email()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    remember_me = BooleanField(label='Keep me logged in')
    submit = SubmitField(label='Log In')


class Register(Form):
    name = StringField(label="Name", validators=(InputRequired(), Length(4, 60)))
    email = EmailField(label='Email', validators=[InputRequired(), Length(5, 64), Email()])
    password1 = PasswordField(label='Password', validators=[InputRequired(), Length(8, 40)])
    password2 = PasswordField(label='Confirm Password', validators=[InputRequired(), Length(8, 40)])
    agree = BooleanField(label='I accept the Terms of Use & Privacy Policy.', validators=[InputRequired()])
    submit = SubmitField(label='Register Now')
