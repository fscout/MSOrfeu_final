@app.route("/edit_categoria/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_categoria(id):
    categoria = Categoria.query.get(id)
    if request.method == 'POST':
        categorias = Categoria.query.all()
        for c in categorias:
            if c.id != categoria.id:
                if c.nome_categoria == request.form['nome_categoria']:
                    # print('Essa Categoria já foi cadastrada')
                    return redirect(url_for('listar_categorias'))
        categoria.nome_categoria = request.form['nome_categoria']
        # print('Categoria cadastrada com sucesso')
        db.session.commit()
        return listar_categorias()
    # return listar_categorias()

    if categoria:
        # categorias = Categoria.query.all()
        # marcas = Marca.query.all()
        # medidas = Medida.query.all()
        # # Verificar para criar uma função para as linhas abaixo pois estão se repetindo em outras partes do código
        # categoria = Categoria.query.get(produto.id_categoria_id)
        # marca = Marca.query.get(produto.id_marca_id)
        # medida = Medida.query.get(produto.id_medida_id)
        # produto.nome_categoria = categoria.nome_categoria
        # produto.nome_marca = marca.nome_marca
        # produto.nome_medida = medida.nome_medida
        return json.dumps(categoria.serialized())
        print('Não existe essa categoria método GET!!!')
    return redirect(url_for('produtos_cadastrados'))