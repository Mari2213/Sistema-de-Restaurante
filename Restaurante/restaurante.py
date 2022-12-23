from modulorestaurante import *
from dataclasses import dataclass
import pickle
from datetime import datetime

@dataclass
class Produtos: # Classes de produtos 
    Cod_prod: int
    Nome: str
    Qtd_estoque: int
    Preco: float

@dataclass
class Vendas: # Classes de vendas
    Num_comanda: int
    Cod_prod: int
    Qtd: int
    Valor: float
    Forma_pag: str
    Troco: float
    Total: float

produto= [] # Amazenar os produtos
venda= [] # Amazenar as vendas

print('|------------------------------------Bem Vindo--------------------------------------------------|')
print()

while True: # Menu do programa
    #Dia e horas
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    print(data_e_hora_em_texto)
    print()
    
    print('||||||| MENU PRINCINPAL |||||||||')
    print('1 - Menu de produtos')
    print('2 - Vender')
    print('3 - Pagar')
    print('4 - Excluir venda')
    print('5 - Pesquisar vendas')
    print('6 - Sair')
    op=int(input('Escolha umas das opções acima: '))
    print()

    if op == 6:
        break

    elif op == 1: # Cadastro dos produtos
        while True:
            print('|---------- MENU DE PRODUTOS ------------|')
            print('1 - Inserir produtos')
            print('2 - Atualizar produtos')
            print('3 - Pesquisar produto')
            print('4 - Excluir produtos')
            print('5 - Vizualizar tabelas de produtos')
            print('6 - Sair')
            opcao=int(input('Escolha umas das opções acima: '))
            print()

            if opcao == 6:
                break

            elif opcao == 1: # Inserir produtos
                #cadastro_produtos(produto, Produtos)
                with open('Produtos.txt', 'r+b') as arquivo:
                    cadastro_produtos(produto, Produtos)
                    pickle.dump(produto, arquivo)

            elif opcao == 2: # Atualizar produtos
                with open('Produtos.txt', 'rb') as arquivo:
                    produto = pickle.load(arquivo)
                atualiza_produtos(produto)
                with open('Produtos.txt', 'r+b') as arquivo:
                    pickle.dump(produto, arquivo)

            elif opcao == 3: # Pesquisar produto
                with open('Produtos.txt', 'rb') as arquivo:
                    produto = pickle.load(arquivo)
                pesquisa_produto(produto)

            elif opcao == 4: # Excluir produtos
                with open('Produtos.txt', 'rb') as arquivo:
                    produto = pickle.load(arquivo)
                exclui_produto(produto)
                with open('Produtos.txt', 'r+b') as arquivo:
                    pickle.dump(produto, arquivo)

            elif opcao == 5: # Vizualizar tabelas de produtos
                with open('Produtos.txt', 'rb') as arquivo:
                    produto = pickle.load(arquivo)
                visualizar_produtos(produto)
            else:
                print('Opção inválida!!!!')
                print()
        
    elif op == 2: # Opção de vender
        with open('Produtos.txt', 'rb') as arquivo:
            produto = pickle.load(arquivo)
        registro_vendas(venda,produto,Vendas)
        with open('Vendas.txt','r+b') as arquivo:
            pickle.dump(venda,arquivo)
        with open('Produtos.txt', 'r+b') as arquivo:
            pickle.dump(produto, arquivo)

    elif op == 3: # Opção para pagar
        with open('Produtos.txt', 'rb') as arquivo:
            produto = pickle.load(arquivo)
        with open('Vendas.txt', 'rb') as arquivo:
            venda = pickle.load(arquivo)
        pagamento(venda,produto)
        with open('Vendas.txt', 'r+b') as arquivo:
            pickle.dump(venda, arquivo)

    elif op == 4: # Excluir venda
        with open('Vendas.txt', 'rb') as arquivo:
            venda = pickle.load(arquivo)
        excluir_compra(venda)
        with open('Vendas.txt', 'r+b') as arquivo:
            pickle.dump(venda, arquivo)
        
    elif op == 5: # Pesquisa de venda
        with open('Vendas.txt', 'rb') as arquivo:
            venda = pickle.load(arquivo)
        pesquisa_venda(venda)
    else:
        print('Opção inválida!!!!!')