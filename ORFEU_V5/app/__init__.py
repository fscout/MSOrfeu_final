from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from app.controllers.adm import adm

app = Flask(__name__)

# Passando o arquivo config.py para que o nosso app pegue as configurações.
app.config.from_object('config')

app.register_blueprint(adm)

db = SQLAlchemy(app)
# Para nos ajudar com as migrações do banco de dados, ou seja,
# sempre que mudarmos nossa tabela, devemos fazer a migração
migrate = Migrate(app, db)

# Muda a forma de aplicarmos os comandos, exemplo, antes para rodarmos
# a aplicação usávamos o comando python app.py e agora usaremo o comando
# python app.py runserver. Para mais detalhes consultar
# o arquivo bibliotecas.txt
manager = Manager(app)

manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)


from app.models import tables, forms
from app.controllers import default
