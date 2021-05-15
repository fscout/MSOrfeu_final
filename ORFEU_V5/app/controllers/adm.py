from flask import Blueprint, render_template
from flask_login import login_required

adm = Blueprint('adm', __name__, url_prefix="/adm")


@adm.route("/")
@login_required
def index():
    return render_template('admin.html')


@adm.route("/usuarios")
def usuarios():
    return "Essa e a pagina onde o adm gerencia os usuarios"
