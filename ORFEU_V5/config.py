DEBUG = True  # Habilitando o debug, para recebermos as informações de debugs,
# assim não precisamos reiniciar toda hora o servidor
POSTGRES = {
    'user': 'postgres',  # Deixar dessa forma
    'pw': '123@Impacta',  # Colocar a senha do banco de dados
    'db': 'orfeu_vendas',  # Colocar o nome do banco de dados
    'host': 'localhost',  # Deixar dessa forma
    'port': '5432',  # Deixar dessa forma
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# Se quisermos usar o banco de dados do SQLALCHEMY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '123@Impacta'  # Senha para o formulário de login