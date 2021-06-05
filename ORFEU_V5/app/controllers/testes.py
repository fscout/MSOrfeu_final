# Adaptar a função abaixo para o novo cenário de inclusão de usuário
# @app.route('/login', methods=["GET", "POST"])
# def adicionar_usuario():
#     form = LoginForm()
#     if form.validate_on_submit():
#         usuario = Usuario.query.filter_by(
#             login=form.login.data).first()
#         if usuario and usuario.verify_password(form.senha.data):
#             if form.lembrar_me.data:
#                 login_user(usuario, remember=True, duration=timedelta(days=1))
#             else:
#                 login_user(usuario)
#             return render_template('index.html')
#         else:
#             flash("Dados inválidos!")
#             return redirect(url_for('login'))
#     return render_template('login.html', form=form)

# usuario01 = Usuario('marcio1', '007', 1) # Op. Caixa
# usuario02 = Usuario('marcio2', '007', 2) # Admin
# print(usuario01.login)
# print(usuario01.senha)
# print(usuario01.status)
# print(usuario01.id_nivel_acesso_id)

# print(usuario02.login)
# print(usuario02.senha)
# print(usuario02.status)
# print(usuario02.id_nivel_acesso_id)

# NivelAcesso
# Usuario
# Cliente
# Categoria
# Marca
# Medida
# Produto
# Venda
# TipoPagamento
# DetalhesPagamento
# DetalhesVenda
# Justificativa
# MovimentacaoCaixa

# select * from nivel_acesso; 
# select * from usuario;
# select * from cliente;
# select * from categoria;
# select * from marca;
# select * from medida;
# select * from produto;
# select * from venda;
# select * from tipo_pagamento;
# select * from detalhes_pagamento;
# select * from detalhes_venda;
# select * from justificativa;
# select * from movimentacao_caixa;

# Adionados os modais de editar e excluir na tela de produtos cadastrados

print()
print()
print()

print("# ********************** TESTES NÍVEL DE ACESSO ********************** #")
# nivel_acesso
# admin = NivelAcesso('admin')  # ID 1
# db.session.add(admin)
# db.session.commit()
admin = NivelAcesso.query.get(1)

print('ADMINISTRADOR: ', admin)
print('ADMINISTRADOR: ', admin.nivel_acesso)


# op_caixa = NivelAcesso('op_caixa')  # ID 2
# db.session.add(op_caixa)
# db.session.commit()
op_caixa = NivelAcesso.query.get(2)
print('OPERADOR DE CAIXA: ', op_caixa)
print('OPERADOR DE CAIXA: ', op_caixa.nivel_acesso)

print(100 * '*')
print()
print()
print()


print("# ********************** TESTES USUARIO ********************** #")
# nome, telefone, email, login, senha, id_nivel_acesso_id=2

# admin = NivelAcesso.query.get(1)
# user_maria = Usuario('Maria', '1199991111',
#                      'maria@email.com', 'maria.maria', '123', admin.id)
# db.session.add(user_maria)
# db.session.commit()
user_maria = Usuario.query.get(1)
print('USUÁRIO 01 ID: ', user_maria)
print('USUÁRIO 01 NOME: ', user_maria.nome)
print('USUÁRIO 01 TELEFONE: ', user_maria.telefone)
print('USUÁRIO 01 EMAIL: ', user_maria.email)
print('USUÁRIO 01 LOGIN: ', user_maria.login)
print('USUÁRIO 01 SENHA: ', user_maria.senha)
print('USUÁRIO 01 STATUS: ', user_maria.status)
print('USUÁRIO 01 ID_NIVEL_ACESSO_ID: ', user_maria.id_nivel_acesso_id)


print(100 * '*')

# op_caixa = NivelAcesso.query.get(2)
# user_joao = Usuario('Joao', '1199992222', 'joao@email.com',
#                     'joao.joao', '123', op_caixa.id)

# db.session.add(user_joao)
# db.session.commit()
user_joao = Usuario.query.get(2)
print('USUÁRIO 02 ID: ', user_joao)
print('USUÁRIO 02 NOME: ', user_joao.nome)
print('USUÁRIO 02 TELEFONE: ', user_joao.telefone)
print('USUÁRIO 02 EMAIL: ', user_joao.email)
print('USUÁRIO 02 LOGIN: ', user_joao.login)
print('USUÁRIO 02 SENHA: ', user_joao.senha)
print('USUÁRIO 02 STATUS: ', user_joao.status)
print('USUÁRIO 02 ID_NIVEL_ACESSO_ID: ', user_joao.id_nivel_acesso_id)

print(100 * '*')
print()
print()
print()


# ************************************************************************
# ************************************************************************
# ************************************************************************

print("# ********************** TESTES USUARIO 02********************** #")
user_maria = Usuario.query.get(1)
nivel_user = NivelAcesso.query.get(user_maria.id_nivel_acesso_id)
user_maria.nome_nivel_acesso = nivel_user.nivel_acesso
print('USUÁRIO 01 NOME ID_NIVEL_ACESSO_ID: ', user_maria.nome_nivel_acesso)

print(100 * '*')

user_joao = Usuario.query.get(2)
nivel_user = NivelAcesso.query.get(user_joao.id_nivel_acesso_id)
user_joao.nome_nivel_acesso = nivel_user.nivel_acesso
print('USUÁRIO 02 NOME ID_NIVEL_ACESSO_ID: ', user_joao.nome_nivel_acesso)


print("# ********************** TESTES CLIENTE ********************** #")

# Ajustar formato de data e hora

# nome, telefone, data_pagamento, cpf=None, observacao=None
# data_e_hora = datetime.strptime('20/04/2021 12:30', '%d/%m/%Y %H:%M')
# cli_jose = Cliente('Jose', '1199993333', data_e_hora,
#                    '11111111111', 'observacao 01')
# db.session.add(cli_jose)
# db.session.commit()
cli_jose = Cliente.query.get(1)

print('CLIENTE 01 ID: ', cli_jose)
print('CLIENTE 01 NOME: ', cli_jose.nome)
print('CLIENTE 01 TELEFONE: ', cli_jose.telefone)
print('CLIENTE 01 DATA_PAGAMENTO: ', cli_jose.data_pagamento)
print('CLIENTE 01 DATA_ULTIMA_COMPRA: ', cli_jose.data_ultima_compra)
print('CLIENTE 01 VALOR_DIVIDA: ', cli_jose.valor_divida)
print('CLIENTE 01 STATUS: ', cli_jose.status)
print('CLIENTE 01 CPF: ', cli_jose.cpf)
print('CLIENTE 01 OBSERVACAO: ', cli_jose.observacao)

print(100 * '*')

# data_e_hora = datetime.strptime('20/04/2021 12:30', '%d/%m/%Y %H:%M')
# cli_marta = Cliente('Marta', '1199994444', data_e_hora)

# db.session.add(cli_marta)
# db.session.commit()
cli_marta = Cliente.query.get(2)
print('CLIENTE 02 ID: ', cli_marta)
print('CLIENTE 02 NOME: ', cli_marta.nome)
print('CLIENTE 02 TELEFONE: ', cli_marta.telefone)
print('CLIENTE 02 DATA_PAGAMENTO: ', cli_marta.data_pagamento)
print('CLIENTE 02 DATA_ULTIMA_COMPRA: ', cli_marta.data_ultima_compra)
print('CLIENTE 02 VALOR_DIVIDA: ', cli_marta.valor_divida)
print('CLIENTE 02 STATUS: ', cli_marta.status)
print('CLIENTE 02 CPF: ', cli_marta.cpf)
print('CLIENTE 02 OBSERVACAO: ', cli_marta.observacao)

print(100 * '*')
print()
print()
print()

# TESTE PARA NÃO PERMIRTIR UM CLIENTE COM O MESMO TELEFONE
# data_e_hora = datetime.strptime('20/04/2021 12:30', '%d/%m/%Y %H:%M')
# cli_marta = Cliente('Paula', '1199994444', data_e_hora)
# db.session.add(cli_marta)
# db.session.commit()


print("# ********************** TESTES CATEGORIA ********************** #")
# nome_categoria
# categoria_01 = Categoria('GRÃOS')
# db.session.add(categoria_01)
# db.session.commit()
categoria_01 = Categoria.query.get(1)
print('CATEGORIA ID: ', categoria_01)
print('CATEGORIA NOME: ', categoria_01.nome_categoria)


print(100 * '*')
print()
print()
print()

print("# ********************** TESTES MARCA ********************** #")
# nome_marca
# marca_01 = Marca('CAMIL')
# db.session.add(marca_01)
# db.session.commit()
marca_01 = Marca.query.get(1)
print('MARCA ID: ', marca_01)
print('MARCA NOME: ', marca_01.nome_marca)

print(100 * '*')
print()
print()
print()

print("# ********************** TESTES MEDIDA ********************** #")
# nome_medida
# medida_01 = Medida('LITRO')
# db.session.add(medida_01)
# db.session.commit()
medida_01 = Medida.query.get(1)
print('MEDIDA ID: ', medida_01)
print('MEDIDA NOME: ', medida_01.nome_medida)


print(100 * '*')
print()
print()
print()


print("# ********************** TESTES PRODUTO ********************** #")
# codigo_barras, descricao_produto, quantidade_produto,
# quantidade_minima, preco_custo,
# preco_venda, quantidade_maxima = None, peso_liquido = None,
# peso_bruto = None, id_categoria_id = 1, id_marca_id = 1,
# id_medida_id = 1

# produto_01 = Produto('10', 'FEIJÃO', 200, 50, 5.00, 9.00, 300, 1, 1, 1, 1, 1)
# db.session.add(produto_01)
# db.session.commit()
produto_01 = Produto.query.get(1)

print('PRODUTO ID: ', produto_01)
print('PRODUTO CODIGO_BARRAS: ', produto_01.codigo_barras)
print('PRODUTO DESCRICAO_PRODUTO: ', produto_01.descricao_produto)
print('PRODUTO QUANTIDADE_PRODUTO: ', produto_01.quantidade_produto)
print('PRODUTO QUANTIDADE_MINIMA: ', produto_01.quantidade_minima)
print('PRODUTO PRECO_CUSTO: ', produto_01.preco_custo)
print('PRODUTO PRECO_VENDA: ', produto_01.preco_venda)
print('PRODUTO QUANTIDADE_MAXIMA: ', produto_01.quantidade_maxima)
print('PRODUTO PESO_LIQUIDO: ', produto_01.peso_liquido)
print('PRODUTO PESO_BRUTO: ', produto_01.peso_bruto)
print('PRODUTO ID_CATEGORIA_ID: ', produto_01.id_categoria_id)
print('PRODUTO ID_MARCA_ID: ', produto_01.id_marca_id)
print('PRODUTO ID_MEDIDA_ID: ', produto_01.id_medida_id)


print(100 * '*')

# codigo_barras, descricao_produto, quantidade_produto,
# quantidade_minima, preco_custo,
# preco_venda, quantidade_maxima = None, peso_liquido = None,
# peso_bruto = None, id_categoria_id = 1, id_marca_id = 1,
# id_medida_id = 1

# produto_02 = Produto('11', 'ARROZ', 300, 80, 3.50, 6.20)
# produto_02 = Produto('11', 'ARROZ', 300, 80, 3.50, 6.20, None, None, None)
# produto_02 = Produto('11', 'ARROZ', 300, 80, 3.50,
#                      6.20, None, None, None, 1, 1, 1)

# db.session.add(produto_02)
# db.session.commit()
produto_02 = Produto.query.get(2)

print('PRODUTO ID: ', produto_02)
print('PRODUTO CODIGO_BARRAS: ', produto_02.codigo_barras)
print('PRODUTO DESCRICAO_PRODUTO: ', produto_02.descricao_produto)
print('PRODUTO QUANTIDADE_PRODUTO: ', produto_02.quantidade_produto)
print('PRODUTO QUANTIDADE_MINIMA: ', produto_02.quantidade_minima)
print('PRODUTO PRECO_CUSTO: ', produto_02.preco_custo)
print('PRODUTO PRECO_VENDA: ', produto_02.preco_venda)
print('PRODUTO QUANTIDADE_MAXIMA: ', produto_02.quantidade_maxima)
print('PRODUTO PESO_LIQUIDO: ', produto_02.peso_liquido)
print('PRODUTO PESO_BRUTO: ', produto_02.peso_bruto)
print('PRODUTO ID_CATEGORIA_ID: ', produto_02.id_categoria_id)
print('PRODUTO ID_MARCA_ID: ', produto_02.id_marca_id)
print('PRODUTO ID_MEDIDA_ID: ', produto_02.id_medida_id)


print(100 * '*')

# produto_03 = Produto('12', 'ARROZ', 300, 80, 3.50, 6.20)

# db.session.add(produto_03)
# db.session.commit()
produto_03 = Produto.query.get(3)

print('PRODUTO ID: ', produto_03)
print('PRODUTO CODIGO_BARRAS: ', produto_03.codigo_barras)
print('PRODUTO DESCRICAO_PRODUTO: ', produto_03.descricao_produto)
print('PRODUTO QUANTIDADE_PRODUTO: ', produto_03.quantidade_produto)
print('PRODUTO QUANTIDADE_MINIMA: ', produto_03.quantidade_minima)
print('PRODUTO PRECO_CUSTO: ', produto_03.preco_custo)
print('PRODUTO PRECO_VENDA: ', produto_03.preco_venda)
print('PRODUTO QUANTIDADE_MAXIMA: ', produto_03.quantidade_maxima)
print('PRODUTO PESO_LIQUIDO: ', produto_03.peso_liquido)
print('PRODUTO PESO_BRUTO: ', produto_03.peso_bruto)
print('PRODUTO ID_CATEGORIA_ID: ', produto_03.id_categoria_id)
print('PRODUTO ID_MARCA_ID: ', produto_03.id_marca_id)
print('PRODUTO ID_MEDIDA_ID: ', produto_03.id_medida_id)


print(100 * '*')
print()
print()
print()


print("# ********************** TESTES VENDA ********************** #")
# data_venda
# valor_total
# id_usuario_id
# id_cliente_id

# venda_01 = Venda(user_joao.id, cli_jose.id)
# db.session.add(venda_01)
# db.session.commit()
venda_01 = Venda.query.get(1)

print('VENDA ID: ', venda_01)
print('VENDA DATA_VENDA: ', venda_01.data_venda)
print('VENDA VALOR_TOTAL: ', venda_01.valor_total)
print('VENDA ID_USUARIO_ID: ', venda_01.id_usuario_id)
print('VENDA ID_CLIENTE_ID: ', venda_01.id_cliente_id)


print(100 * '*')

# data_venda
# valor_total
# id_usuario_id
# id_cliente_id

# venda_02 = Venda(user_maria.id)
# db.session.add(venda_02)
# db.session.commit()
venda_02 = Venda.query.get(2)


print('VENDA ID: ', venda_02)
print('VENDA DATA_VENDA: ', venda_02.data_venda)
print('VENDA VALOR_TOTAL: ', venda_02.valor_total)
print('VENDA ID_USUARIO_ID: ', venda_02.id_usuario_id)
print('VENDA ID_CLIENTE_ID: ', venda_02.id_cliente_id)


print(100 * '*')
print()
print()
print()


print("# ********************** TESTES TIPO PAGAMENTO ********************** #")
# tipo_pagamento

# tipo_pagamento_dinheiro = TipoPagamento('DINHEIRO')  # ID 1
# db.session.add(tipo_pagamento_dinheiro)
# db.session.commit()
tipo_pagamento_dinheiro = TipoPagamento.query.get(1)

print('TIPO PAGAMENTO ID: ', tipo_pagamento_dinheiro)
print('TIPO PAGAMENTO NOME: ', tipo_pagamento_dinheiro.tipo_pagamento)

print(100 * '*')

# tipo_pagamento_cartao_debito = TipoPagamento('CARTÃO DÉBITO')  # ID 2
# db.session.add(tipo_pagamento_cartao_debito)
# db.session.commit()
tipo_pagamento_cartao_debito = TipoPagamento.query.get(2)

print('TIPO PAGAMENTO ID: ', tipo_pagamento_cartao_debito)
print('TIPO PAGAMENTO NOME: ', tipo_pagamento_cartao_debito.tipo_pagamento)

print(100 * '*')

# tipo_pagamento_cartao_credito = TipoPagamento('CARTÃO CRÉDITO')  # ID 3
# db.session.add(tipo_pagamento_cartao_credito)
# db.session.commit()
tipo_pagamento_cartao_credito = TipoPagamento.query.get(3)

print('TIPO PAGAMENTO ID: ', tipo_pagamento_cartao_credito)
print('TIPO PAGAMENTO NOME: ', tipo_pagamento_cartao_credito.tipo_pagamento)

print(100 * '*')

# tipo_pagamento_fiado = TipoPagamento('FIADO')  # ID 4
# db.session.add(tipo_pagamento_fiado)
# db.session.commit()
tipo_pagamento_fiado = TipoPagamento.query.get(4)

print('TIPO PAGAMENTO ID: ', tipo_pagamento_fiado)
print('TIPO PAGAMENTO NOME: ', tipo_pagamento_fiado.tipo_pagamento)


print(100 * '*')
print()
print()
print()


print("# ********************** TESTES DETALHES PAGAMENTO ********************** #")
# valor
# id_tipo_pagamento_id
# id_venda_id

# detalhes_pagamento_01 = DetalhesPagamento(
#     25.00, tipo_pagamento_dinheiro.id, venda_01.id)  # ID 1
# db.session.add(detalhes_pagamento_01)
# db.session.commit()
detalhes_pagamento_01 = DetalhesPagamento.query.get(1)

print('DETALHES PAGAMENTO ID: ', detalhes_pagamento_01)
print('DETALHES PAGAMENTO VALOR: ', detalhes_pagamento_01.valor)
print('DETALHES PAGAMENTO ID_TIPO_PAGAMENTO_ID: ',
      detalhes_pagamento_01.id_tipo_pagamento_id)
print('DETALHES PAGAMENTO ID_VENDA_ID: ', detalhes_pagamento_01.id_venda_id)

print(100 * '*')

# detalhes_pagamento_02 = DetalhesPagamento(
#     25.00, tipo_pagamento_cartao_debito.id, venda_01.id)  # ID 2
# db.session.add(detalhes_pagamento_02)
# db.session.commit()
detalhes_pagamento_02 = DetalhesPagamento.query.get(2)

print('DETALHES PAGAMENTO ID: ', detalhes_pagamento_02)
print('DETALHES PAGAMENTO VALOR: ', detalhes_pagamento_02.valor)
print('DETALHES PAGAMENTO ID_TIPO_PAGAMENTO_ID: ',
      detalhes_pagamento_02.id_tipo_pagamento_id)
print('DETALHES PAGAMENTO ID_VENDA_ID: ', detalhes_pagamento_02.id_venda_id)

print(100 * '*')

# detalhes_pagamento_03 = DetalhesPagamento(
#     25.00, tipo_pagamento_cartao_credito.id, venda_01.id)  # ID 3
# db.session.add(detalhes_pagamento_03)
# db.session.commit()
detalhes_pagamento_03 = DetalhesPagamento.query.get(3)

print('DETALHES PAGAMENTO ID: ', detalhes_pagamento_03)
print('DETALHES PAGAMENTO VALOR: ', detalhes_pagamento_03.valor)
print('DETALHES PAGAMENTO ID_TIPO_PAGAMENTO_ID: ',
      detalhes_pagamento_03.id_tipo_pagamento_id)
print('DETALHES PAGAMENTO ID_VENDA_ID: ', detalhes_pagamento_03.id_venda_id)

print(100 * '*')

# detalhes_pagamento_04 = DetalhesPagamento(
#     25.00, tipo_pagamento_fiado.id, venda_01.id)  # ID 4
# db.session.add(detalhes_pagamento_04)
# db.session.commit()
detalhes_pagamento_04 = DetalhesPagamento.query.get(4)

print('DETALHES PAGAMENTO ID: ', detalhes_pagamento_04)
print('DETALHES PAGAMENTO VALOR: ', detalhes_pagamento_04.valor)
print('DETALHES PAGAMENTO ID_TIPO_PAGAMENTO_ID: ',
      detalhes_pagamento_04.id_tipo_pagamento_id)
print('DETALHES PAGAMENTO ID_VENDA_ID: ', detalhes_pagamento_04.id_venda_id)


print(100 * '*')
print()
print()
print()


print("# ********************** TESTES DETALHES VENDA ********************** #")
# quantidade_produto, id_venda_id, id_produto_id

# detalhes_venda_01 = DetalhesVenda(1, venda_01.id, produto_01.id)  # ID 1
# db.session.add(detalhes_venda_01)
# db.session.commit()
detalhes_venda_01 = DetalhesVenda.query.get(1)

print('DETALHES VENDA ID: ', detalhes_venda_01)
print('DETALHES QUANTIDADE_PRODUTO: ', detalhes_venda_01.quantidade_produto)
print('DETALHES VALOR_PRODUTO: ', detalhes_venda_01.valor_produto)
print('DETALHES VALOR_DESCONTO: ', detalhes_venda_01.valor_desconto)
print('DETALHES TROCA: ', detalhes_venda_01.troca)
print('DETALHES DEVOLUCAO: ', detalhes_venda_01.devolucao)
print('DETALHES ID_VENDA_ID: ', detalhes_venda_01.id_venda_id)
print('DETALHES ID_PRODUTO_ID: ', detalhes_venda_01.id_produto_id)

print(100 * '*')

# detalhes_venda_02 = DetalhesVenda(1, venda_01.id, produto_02.id)  # ID 2
# db.session.add(detalhes_venda_02)
# db.session.commit()
detalhes_venda_02 = DetalhesVenda.query.get(2)

print('DETALHES VENDA ID: ', detalhes_venda_02)
print('DETALHES QUANTIDADE_PRODUTO: ', detalhes_venda_02.quantidade_produto)
print('DETALHES VALOR_PRODUTO: ', detalhes_venda_02.valor_produto)
print('DETALHES VALOR_DESCONTO: ', detalhes_venda_02.valor_desconto)
print('DETALHES TROCA: ', detalhes_venda_02.troca)
print('DETALHES DEVOLUCAO: ', detalhes_venda_02.devolucao)
print('DETALHES ID_VENDA_ID: ', detalhes_venda_02.id_venda_id)
print('DETALHES ID_PRODUTO_ID: ', detalhes_venda_02.id_produto_id)

print(100 * '*')

# detalhes_venda_03 = DetalhesVenda(1, venda_01.id, produto_03.id)  # ID 3
# db.session.add(detalhes_venda_03)
# db.session.commit()
detalhes_venda_03 = DetalhesVenda.query.get(3)

print('DETALHES VENDA ID: ', detalhes_venda_03)
print('DETALHES QUANTIDADE_PRODUTO: ', detalhes_venda_03.quantidade_produto)
print('DETALHES VALOR_PRODUTO: ', detalhes_venda_03.valor_produto)
print('DETALHES VALOR_DESCONTO: ', detalhes_venda_03.valor_desconto)
print('DETALHES TROCA: ', detalhes_venda_03.troca)
print('DETALHES DEVOLUCAO: ', detalhes_venda_03.devolucao)
print('DETALHES ID_VENDA_ID: ', detalhes_venda_03.id_venda_id)
print('DETALHES ID_PRODUTO_ID: ', detalhes_venda_03.id_produto_id)

print(100 * '*')

print()
print()
print()


print("# ********************** TESTES JUSTIFICATIVA ********************** #")


# justificativa_01 = Justificativa("01 - OUTROS")  # ID 01
# db.session.add(justificativa_01)
# db.session.commit()
justificativa_01 = Justificativa.query.get(1)

# justificativa_02 = Justificativa("02 - TROCO")  # ID 02
# db.session.add(justificativa_02)
# db.session.commit()
justificativa_02 = Justificativa.query.get(2)

# justificativa_03 = Justificativa("03 - PAGAMENTO DE DÉBITO")  # ID 03
# db.session.add(justificativa_03)
# db.session.commit()
justificativa_03 = Justificativa.query.get(3)

# justificativa_04 = Justificativa("04 - PAGAMENTO PARA FORNECEDOR")  # ID 04
# db.session.add(justificativa_04)
# db.session.commit()
justificativa_04 = Justificativa.query.get(4)

# justificativa_05 = Justificativa(
#     "05 - PAGAMENTO DE CONTA (ÁGUA, LUZ, TELEFONE)")  # ID 05
# db.session.add(justificativa_05)
# db.session.commit()
justificativa_05 = Justificativa.query.get(5)

# justificativa_06 = Justificativa("06 - VALE PARA FUNCIONÁRIO")  # ID 06
# db.session.add(justificativa_06)
# db.session.commit()
justificativa_06 = Justificativa.query.get(6)

# justificativa_07 = Justificativa("07 - VENDA")  # ID 07
# db.session.add(justificativa_07)
# db.session.commit()
justificativa_07 = Justificativa.query.get(7)


print('JUSTIFICATIVA ID: ', justificativa_01)
print('JUSTIFICATIVA NOME: ', justificativa_01.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_02)
print('JUSTIFICATIVA NOME: ', justificativa_02.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_03)
print('JUSTIFICATIVA NOME: ', justificativa_03.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_04)
print('JUSTIFICATIVA NOME: ', justificativa_04.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_05)
print('JUSTIFICATIVA NOME: ', justificativa_05.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_06)
print('JUSTIFICATIVA NOME: ', justificativa_06.justificativa)
print(100 * '*')

print('JUSTIFICATIVA ID: ', justificativa_07)
print('JUSTIFICATIVA NOME: ', justificativa_07.justificativa)
print(100 * '*')

print()
print()
print()


print("# ********************** TESTES MOVIMENTACAO CAIXA ********************** #")
# valor_movimentacao=0, observacao=None, id_venda_id=None, id_justificativa_id=1

# movimentacao_caixa_01 = MovimentacaoCaixa(
#     100.00, 'Vale para Maria Souza', None, justificativa_06.id)
# db.session.add(movimentacao_caixa_01)
# db.session.commit()
movimentacao_caixa_01 = MovimentacaoCaixa.query.get(1)

print('MOVIMENTACAO CAIXA ID: ', movimentacao_caixa_01)
print('MOVIMENTACAO CAIXA VALOR_MOVIMENTACAO: ',
      movimentacao_caixa_01.valor_movimentacao)
print('MOVIMENTACAO CAIXA DATA_MOVIMENTACAO: ',
      movimentacao_caixa_01.data_movimentacao)
print('MOVIMENTACAO CAIXA STATUS: ', movimentacao_caixa_01.status)
print('MOVIMENTACAO CAIXA OBSERVACAO: ', movimentacao_caixa_01.observacao)
print('MOVIMENTACAO CAIXA ID_VENDA_ID: ', movimentacao_caixa_01.id_venda_id)
print('MOVIMENTACAO CAIXA ID_JUSTIFICATIVA_ID: ',
      movimentacao_caixa_01.id_justificativa_id)

print(100 * '*')


# movimentacao_caixa_02 = MovimentacaoCaixa(
#     50.00, 'Pagamento para Italac', None, justificativa_04.id)
# db.session.add(movimentacao_caixa_02)
# db.session.commit()
movimentacao_caixa_02 = MovimentacaoCaixa.query.get(2)

print('MOVIMENTACAO CAIXA ID: ', movimentacao_caixa_02)
print('MOVIMENTACAO CAIXA VALOR_MOVIMENTACAO: ',
      movimentacao_caixa_02.valor_movimentacao)
print('MOVIMENTACAO CAIXA DATA_MOVIMENTACAO: ',
      movimentacao_caixa_02.data_movimentacao)
print('MOVIMENTACAO CAIXA STATUS: ', movimentacao_caixa_02.status)
print('MOVIMENTACAO CAIXA OBSERVACAO: ', movimentacao_caixa_02.observacao)
print('MOVIMENTACAO CAIXA ID_VENDA_ID: ', movimentacao_caixa_02.id_venda_id)
print('MOVIMENTACAO CAIXA ID_JUSTIFICATIVA_ID: ',
      movimentacao_caixa_02.id_justificativa_id)
print(100 * '*')


# movimentacao_caixa_03 = MovimentacaoCaixa(venda_01.valor_total, None, venda_01.id, 7)

# movimentacao_caixa_03 = MovimentacaoCaixa(venda_01.valor_total, None, venda_01.id, justificativa_07.id)
# db.session.add(movimentacao_caixa_03)
# db.session.commit()
movimentacao_caixa_03 = MovimentacaoCaixa.query.get(3)

print('MOVIMENTACAO CAIXA ID: ', movimentacao_caixa_03)
print('MOVIMENTACAO CAIXA VALOR_MOVIMENTACAO: ',
      movimentacao_caixa_03.valor_movimentacao)
print('MOVIMENTACAO CAIXA DATA_MOVIMENTACAO: ',
      movimentacao_caixa_03.data_movimentacao)
print('MOVIMENTACAO CAIXA STATUS: ', movimentacao_caixa_03.status)
print('MOVIMENTACAO CAIXA OBSERVACAO: ', movimentacao_caixa_03.observacao)
print('MOVIMENTACAO CAIXA ID_VENDA_ID: ', movimentacao_caixa_03.id_venda_id)
print('MOVIMENTACAO CAIXA ID_JUSTIFICATIVA_ID: ',
      movimentacao_caixa_03.id_justificativa_id)
print(100 * '*')


print(100 * '*')
print()
print()
print()

''''''

# FIM DOA TESTES


# @app.route('/login', methods=["GET", "POST"]) # --- BKP ---
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         usuario = Usuario.query.filter_by(
#             nome_usuario=form.nome_usuario.data).first()
#         if usuario and usuario.verify_password(form.senha_usuario.data):
#             if form.lembrar_me.data:
#                 login_user(usuario, remember=True, duration=timedelta(days=2))
#             else:
#                 login_user(usuario)
#             return render_template('index.html')
#         else:
#             flash("Dados inválidos!")
#             return redirect(url_for('login'))
#     return render_template('login.html', form=form)


# @app.route("/nivel_acesso")  # TESTE
# def nivel_acesso():
#     niveis_acesso = NivelAcesso.query.all()
#     lista = []
#     for nivel in niveis_acesso:
#         lista.append(nivel.nivel_acesso)
#     print(lista)
#     return str(lista)



'''
@app.route("/exibir_categorias")
@login_required
def exibir_categorias():
    categorias = Categoria.query.all()
    return render_template('add_produto.html', categorias=categorias)


@app.route("/categorias_cadastradas")
@login_required
def categorias_cadastradas():
    categorias = Categoria.query.all()
    return render_template('categorias_cadastradas.html', categorias=categorias)


@app.route("/teste_add_categoria")
def teste_add_categoria():
    categoria = Categoria('Teste Categ')
    db.session.add(categoria)
    db.session.commit()
    return "Ok"


@app.route("/teste_add_marca")
def teste_add_marca():
    marca = Marca('Nestle')
    db.session.add(marca)
    db.session.commit()
    return "Ok"


@app.route("/teste_add_medida")
def teste_add_medida():
    medida = Medida('Litro')
    db.session.add(medida)
    db.session.commit()
    return "Ok"


@app.route("/teste_add_produto")
def teste_add_produto():
    produto = Produto(30, '01256666', 'Espaguete 007', 60, 20, 250, 1.60, 3.90)
    db.session.add(produto)
    db.session.commit()
    return "Ok"


@app.route("/teste_add_produto_full")
def teste_add_produto_full():
    categoria = Categoria('Bebidas 05')
    db.session.add(categoria)
    db.session.commit()
    # marca = Marca('Camil')
    # db.session.add(marca)
    # medida = Medida('KG')
    # db.session.add(medida)
    produto = Produto('0155567121004', 'Teste Bebida 05',
                      60, 20, 250, 1.60, 4.50)
    db.session.add(produto)
    db.session.commit()
    return "Ok"

#     produto = Produto(1, '1234567891001', 'Feijão', 100, 50, 250, 5.25, 9.75, 1, 1, 1)
#     produto = Produto(2, '1234567891002', 'Arroz', 120, 50, 300, 2.70, 5.50, 1, 1, 1)
#     produto = Produto(3, '1234567891003', 'Espaguete', 60, 20, 250, 1.60, 3.90)
# select * from categoria;
# select * from marca;
# select * from medida;
# select * from produto;
'''

'''  DESCOMENTAR ESSA PARTE DO CÓDIGO PARA CRIAR O O PRIMEIRO USUÁRIO
@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    teste_ = Usuario('marcio', '007', 'Marcio', '09419076432', 'adm')
    db.session.add(teste_)
    db.session.commit()
    return "Ok"



@app.route("/teste")
def teste():
    teste_ = Usuario('marcio', '007', 'Marcio', '09419076432', 'adm')
    db.session.add(teste_)
    db.session.commit()
    return "Ok"


@app.route("/ler_produto/<info>")
@app.route("/ler_produto", defaults={"info": None})
def ler_produto(info):
    # usuario_ = Usuario.query.filter_by(nome_usuario="marcio.teste").all()
    usuario_ = Usuario.query.filter_by(nome_usuario="marcio.teste1").first()
    print(usuario_.senha_usuario)
    return usuario_.senha_usuario
'''


# @app.route("/teste")
# def teste():
#     teste_ = Usuario('marcio1', '007', 'Marcio1', '09419016432', 'Op. Caixa')
#     db.session.add(teste_)
#     db.session.commit()
#     return "Ok"


# @app.route('/recebe_dados_jquery', methods=['POST'])
# def receive_data():
#     if request.method == 'POST':
#         dados = request.form['meus_dados']
#         print(dados)


# @app.route('/testes_v1')
# def testes_v1():
#     return render_template('testes_v1.html')


# @app.route('/signUpUser', methods=['POST'])
# def signUpUser():
#     if request.method == 'POST':
#         user = request.form['username']
#         password = request.form['password']
#         return json.dumps({'status': 'OK', 'user': user, 'pass': password})



@app.route("/edit_usuario/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuarios = Usuario.query.all()
        for u in usuarios:
            if u.id != usuario.id:
                #  Se o email já existir mandar de volta para o index
                if u.email == request.form['email']:
                    # print('Esse e-mail já foi cadastrado')
                    return redirect(url_for('index'))
                #  Se o login já existir mandar de volta para o index
                if u.login == request.form['login']:
                    # print('Esse login já foi cadastrado')
                    return redirect(url_for('index'))
        usuario.nome = request.form['nome']
        usuario.telefone = request.form['telefone']
        usuario.email = request.form['email']
        usuario.login = request.form['login']
        usuario.senha = request.form['senha']
        usuario.id_nivel_acesso_id = request.form['id_nivel_acesso_id']
        db.session.commit()
        return usuarios_cadastrados()
    return render_template('edit_usuario.html', usuario=usuario)