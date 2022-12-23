def cadastro_produtos(produto, Produtos): # Função para cadastro de produtos
    achou= False
    while True:
        cod_produto=int(input('Digite o código do produto (Digite 0 para SAIR): '))
        if cod_produto == 0:
            break
        for i in range(len(produto)):
            if cod_produto == produto[i].Cod_prod:
                achou= True
                break
        if achou:
            print('Codigo já cadastrado para esse produto!!!')
            break
        else:
            nome=input('Nome produto: ')
            qtd_estoque=int(input('Quantidade: '))
            preco=float(input('Preço do produto: '))

            produto.append(Produtos(cod_produto,nome,qtd_estoque,preco))
            print('Produto cadastrado')
            print()

def atualiza_produtos(produto): # Função para atualizar produto
    achou= False
    cod_produto=int(input('Digite o código do produto: '))
    for i in range(len(produto)):
        if cod_produto == produto[i].Cod_prod:
            achou= True
            break
    if achou:
        atualizar=input('Deseja atualizar preço ou quantidade em estoque (1-preço ou 2-quantidade): ')
        if atualizar == '1':
            produto[i].Preco=float(input('Novo preço: '))
        else:
            produto[i].Qtd_estoque=int(input('Nova quantidade em estoque: '))
        print('Produto atualizado!!!')
    else:
        print('Produto não encontrado!!!!')
        print()

def pesquisa_produto(produto): # Função para pesquisa
    prod=int(input('Digite o código do produto: '))
    achou= False
    for i in range(len(produto)):
        if prod == produto[i].Cod_prod:
            achou= True
            break
    if achou == False:
        print('Produto não encontrado!!!')
    else:
        print(f'Cod_produto: {produto[i].Cod_prod} - Nome: {produto[i].Nome} - Estoque: {produto[i].Qtd_estoque} - Preço: {produto[i].Preco}')
        print()

def exclui_produto(produto): # Função para excluir produto
    achou= False
    cod_produto=int(input('Digite o código do produto: '))
    for i in range(len(produto)):
        if cod_produto == produto[i].Cod_prod:
            achou= True
            break
    if achou:
        del(produto[i])
        print('Produto Excluido')
    else:
        print('Produto não encontrado!!!!')
        print()

def visualizar_produtos(produto): # Função para visualizar todos os produtos
    print('|---------------Tabela de Produtos-----------------|')
    for i in range(len(produto)):
        print(f'Cod_produto: {produto[i].Cod_prod} - Nome: {produto[i].Nome} - Estoque: {produto[i].Qtd_estoque} - Preço: {produto[i].Preco}')
        print()

def registro_vendas(venda,produto,Vendas): # Função para vender
    acum= 0
    num_comanda=int(input('Número da comando: '))
    achou= False
    for l in range(len(venda)):
        if num_comanda == venda[l].Num_comanda:
            achou= True
            break
    if achou:
        print('Número da comanda já existenti')
    else:
        while True:
            cod_produto=int(input('Código do produto (Digite 0 para SAIR): '))
            if cod_produto == 0:
                break
            achou= False
            for i in range(len(produto)):
                if cod_produto == produto[i].Cod_prod:
                    achou= True
                    break
            if achou == False:
                print('Produto não encontrado!!!')
                break
            else:
                qtd=int(input('Quantidade: '))
                venda.append(Vendas(num_comanda,cod_produto,qtd,0,0,0,0))
                print()
        print('Nº comanda ---------> {}'.format(venda[i].Num_comanda))        
        for i in range(len(venda)):
            for j in range(len(produto)):
                if venda[i].Cod_prod == produto[j].Cod_prod:
                    print(f'Código do produto ------> {venda[i].Cod_prod}')
                    print(f'Nome produto ---> {produto[j].Nome}')
                    print(f'Qtd ------> {venda[i].Qtd}')
                    print(f'Preço unitario -----> R${produto[j].Preco}')
                    venda[i].Valor= venda[i].Qtd * produto[j].Preco
                    print(f'Preço total do produto -------> R${venda[i].Valor}')
                    acum+= venda[i].Valor
                    venda[i].Total= acum
                    if produto[j].Cod_prod == venda[i].Cod_prod:
                        produto[j].Qtd_estoque= produto[j].Qtd_estoque - venda[i].Qtd
        print('########################################')
        print(f'Valor total da venda ------> R${venda[i].Total}')
        print('########################################')
        print()

def pagamento(venda,produto): # Função de pagamento
    numcomanda=int(input('Nº da comanda: '))
    achou= False
    for i in range(len(venda)):
        if numcomanda == venda[i].Num_comanda:
            achou= True
            break
    if achou == False:
        print('Comanda não encontrada!!!')
    else:
        print()
        print(f'Nº comanda ---------> {venda[i].Num_comanda}')
        for i in range(len(venda)):
            print(f'Código do produto ------> {venda[i].Cod_prod}')
            print(f'Nome produto ---> {produto[i].Nome}')
            print(f'Qtd ------> {venda[i].Qtd}')
            print(f'Preço unitario -----> R${produto[i].Preco}')
            print(f'Preço total do produto -------> R${venda[i].Valor}')
        print('########################################')
        print(f'Valor total da venda ------> R${venda[i].Total}')
        print('########################################')
        venda[i].Forma_pag=input('Qual a forma de pagamento --> 1-Dinheiro, 2-Pix, 3-Cartão: ')
        if venda[i].Forma_pag == '1':
            dinheiro=float(input('Dinheiro: '))
            venda[i].Troco= dinheiro - venda[i].Total
            print(f'Forma de pagamento ------> {venda[i].Forma_pag} - Dinheiro')
            print(f'Troco ------> R${venda[i].Troco}')
            print()
        elif venda[i].Forma_pag == '2':
            print(f'Forma de pagamento ------> {venda[i].Forma_pag} - Pix')
            print('Chave Pix: 14589752')
        elif venda[i].Forma_pag == '3':
            cartao=input('1-Débito ou 2-Crédito: ')
            if cartao == '1' or cartao == '2':
                print(f'Forma de pagamento ------> {venda[i].Forma_pag} - Cartão')
                print('Insira o cartão ou Aproxime')
            else:
                print('Forma de pagamento inválida!!!')
        else:
            print('Forma de pagamento inválida!!!')
            print()

def excluir_compra(venda): # Função para excluir venda
    achou= False
    cod_comanda=int(input('Digite o código da comanda: '))
    for i in range(len(venda)):
        if cod_comanda == venda[i].Num_comanda:
            achou= True
            break
    if achou:
        del(venda[i])
        print('Venda Excluida!!!')
    else:
        print('Nº da comanda não encontrada!!!!')
        print()

def pesquisa_venda(venda): # Função para pesquisar venda
    vend=int(input('Digite o código da comanda: '))
    achou= False
    for i in range(len(venda)):
        if vend == venda[i].Num_comanda:
            achou= True
            break
    if achou == False:
        print('Comanda não encontrado!!!')
    else:
        print(f'Nº da comanda: {venda[i].Num_comanda}')
        for i in range(len(venda)):
            print(f'Cod do produto: {venda[i].Cod_prod}')
            print(f'Quantidade: {venda[i].Qtd}')
            print(f'Valor: R${venda[i].Valor}')  
        print(f'Pagamento: {venda[i].Forma_pag}') 
        print(f'Troco: R${venda[i].Troco}') 
        print(f'Total da venda: R${venda[i].Total}')
        print()