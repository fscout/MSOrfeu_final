# smtplib --> Será responsável por enviar o e-mail propriamente dito
import smtplib
import os
# email --> Será responsável por formatar a mensagem
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice
import string


def gerar_senha_aleatoria():
    tamanho = 8
    valores = string.ascii_letters + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    # print(type(senha), "Senha = ", senha)
    return senha


def enviar_senha_email(email, nova_senha):
    # E-mail que enviará a mensagem
    email_de = 'orfeu.bessa@gmail.com'
    # No terminal aplicar esse comando --> export EMAIL_PASSWORD='123@Orfeu'
    email_senha = '123@Orfeu'
    # email_senha = os.getenv('EMAIL_PASSWORD')
    # print('TESTE SENHA', email_senha)
    email_smtp_server = 'smtp.gmail.com'

    destino = [email]

    assunto = 'Recuperação de Senha!'

    mensagem = MIMEMultipart()  # Início do Cabeçalho da mensagem
    mensagem['From'] = email_de
    mensagem['Subject'] = assunto  # Fim do Cabeçalho da mensagem

    # print(mensagem)

    texto = f'Sua senha provisória é: {nova_senha}'
    # Abaixo temos que especificar o tipo do texto que enviaremos
    # e no nosso caso será em html.
    # Se formos enviar anexo, pdv, csv é nessa linha que modificaremos.
    mensagem_texto = MIMEText(texto, 'html')  # Habilitando no formato html

    # A linha abaixo anexa a nossa mensagem que está no formato html
    # no objeto mensagem
    mensagem.attach(mensagem_texto)

    # print(mensagem.as_string())

    try:
        smtp = smtplib.SMTP(email_smtp_server, 587)  # Porta do SRV: 587
        smtp.ehlo()  # Se identificando no servidor
        smtp.starttls()  # Indicando que é uma conexão segura
        smtp.ehlo()  # Se identificando no servidor novamente
        smtp.login(email_de, email_senha)  # Fazendo login
        # email_de = Quem envia, destino = Quem receberá e a mensagem a ser enviada
        smtp.sendmail(email_de, ','.join(destino), mensagem.as_string())
        smtp.quit()
        return f'Senha encaminhada para o e-mail {email}'
    except Exception as erro:
        return f'Falha ao enviar e-mail: {erro}'

    # https://www.youtube.com/watch?v=1VMWbbAGHkc


# print(enviar_senha_email('emprentime@gmail.com', '123@teste'))
