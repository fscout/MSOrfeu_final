# -*- coding: utf-8 -*-
#linha para que o codigo suporte acentos

#lib que permite o uso de comando via terminal
import os 

#lib que permite uso de funções relacioandas a tempo
from time import sleep


#aqui, coloque o nome da sua branch 
minha_branch = 'main'

#escreva a mensagem do commit nessta área
mensagem = input("Digite aqui a mensagem do commit:\n")

#sincroniza os repositórios
os.system('git pull --all')

#coloca na área de stag o seus arquivos
os.system('git add *')

#aplica o commit com a mensagem digitada acima
os.system('git commit -m "' + mensagem + '"')

#sobe para o devops
os.system('git push -u origin '  + minha_branch)
print('Commit realizado com sucesso e refletido também no DevOPS')
