from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

# link para esclarecimentos da classe FlaskForm
# https://flask-wtf.readthedocs.io/en/stable/


class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    lembrar_me = BooleanField('lembrar_me')
