# from flask import render_template, request, redirect, url_for, flash
# from flask_login import login_user, logout_user, login_required
# from app import app, db, login_manager
# from datetime import timedelta
# from app.models.forms import LoginForm
# from app.models.tables import NivelAcesso, Usuario
# from app.models.tables import Cliente
# from app.models.tables import Categoria, Marca, Medida, Produto
# from app.models.tables import Venda, TipoPagamento, DetalhesPagamento,\
#     DetalhesVenda
# from app.models.tables import Justificativa, MovimentacaoCaixa
# from datetime import datetime


# @login_manager.user_loader
# def get_user(user_id):
#     return Usuario.query.filter_by(id=user_id).first()


# '''
#     A linha abaixo direciona o usuário para tela de login, caso ele não tenha
#     logado, ou seja, tenha tentado acessar o conteúdo diretamente.
# '''
# login_manager.login_view = "login"

# '''
#     A linha abaixo nos permite personalizar a mensagem que o usuário receberá
#     após tentar acessar uma página privada sem logar.
# '''

# login_manager.login_message = u"Você precisa logar para acessar o conteúdo da página!"

# '''
#     A linha abaixo a evitar que as sessões dos usuários sejam roubadas.
# '''
# login_manager.session_protection = "strong"


# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template("index.html")


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         usuario = Usuario.query.filter_by(
#             login=form.login.data).first()
#         if usuario and usuario.descriptografar_senha(form.senha.data):
#             if form.lembrar_me.data:
#                 login_user(usuario, remember=True, duration=timedelta(days=2))
#             else:
#                 login_user(usuario)
#             return render_template('index.html')
#         else:
#             flash("Dados inválidos!")
#             return redirect(url_for('login'))
#     return render_template('login.html', form=form)


# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))