# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================
import json
from arteso.exception_value import *
ARQUIVO_PRODUTOS_JSON = "produtos.json" 

def carregar_produtos(): 
    # Carrega todo o dicionário master de produtos do arquivo JSON 
    try:
        with open(ARQUIVO_PRODUTOS_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_produtos(dicionario_master): 
    # Grava o dicionário mestre de produtos de volta no arquivo JSON
    with open(ARQUIVO_PRODUTOS_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dicionario_master, arquivo, indent=4, ensure_ascii=False)


# CREATE  |  cadastro de produto(s) 

def adicionar_produtos(email_logado):

    banco_geral = carregar_produtos()

    # Se a artesã já tiver produtos, pega a lista dela. Se não, cria uma lista nova vazia
    if email_logado not in banco_geral:
        banco_geral[email_logado] = []

    descricao_produtos = banco_geral[email_logado]

    add_produto = ler_decisao("\nDeseja adicionar produto(s) na loja? [S/N] ")

    while add_produto == "S":

        produto = ler_string("\nDigite o nome do produto: ").strip().capitalize()
                    
        if not any(chave["Nome"] == produto for chave in descricao_produtos): #evita duplicidade de dados para não criar outra lista
            print(f"\nProduto '{produto}' adicionado!")

            print(f"\nAdicione a descrição do produto: ") #criação do dicionário com a descrição do produto

            produtos = {
                "Nome":     produto,
                "Preço":    ler_real("Valor do produto: R$ "),
                "Material": ler_string("Material do produto: ").strip().capitalize(),
                "Estoque":  ler_inteiro("Estoque do produto: ")
            }
            descricao_produtos.append(produtos) #adiciona o dicionário em uma lista para ter uma sequência de cadastros
        else:
            print("\nProduto já existe na loja.")

        add_produto = ler_decisao("\nDeseja adicionar mais produtos? [S/N] ") 
    # salva no arquivo json
    banco_geral[email_logado] = descricao_produtos

    salvar_produtos(banco_geral)

    print("\nFim do cadastro de produtos")    

# READ    |  listar produto(s)

def consultar_produtos(email_logado):
    banco_geral = carregar_produtos()
    
    # Validação caso a artesã logada não possua nenhum produto registrado ainda
    if email_logado not in banco_geral or len(banco_geral[email_logado]) == 0:
        print("\nNão existem produtos cadastrados na sua loja.")
        return

    # Captura a lista de produtos específica desta artesã
    descrição_produtos = banco_geral[email_logado]
    print("="*30, "CONSULTA DE PRODUTOS", "="*30)
    print(f"Os produtos cadastrados são: ")

    #lista todos os produtos cadastrados com um número ordinal associado
    for i in range (len(descrição_produtos)):
        print(f"{i+1}º produto: {descrição_produtos[i]["Nome"]}")

    consulta_geral = ler_decisao("\nGostaria de fazer uma consulta geral? [S/N] -> ")

    #condicional que leva à lista de dicionários com todos os produtos e com print formatado auxiliado por um for
    if consulta_geral == "S":
        for g in range (len(descrição_produtos)):
            print(f"\n{g+1}º produto: ")
            for k, v in descrição_produtos[g].items():
                print(f"{k}: {v}")
            print("\n" + "-"*30)
        print("\nFim da consulta geral")
    else:
        print("\nVocê saiu da consulta geral")


    consulta_produto = ler_decisao("\nGostaria consultar um produto? [S/N] -> ")

    #condicional que valida o início do laço de repetição de consulta por produto
    if consulta_produto!="S":
        
        print(f"\nFim da consulta")
        return False
    

    #laço de repetição para consultar o dicionário de um produto específico de acordo com o número ordinal informado acima
    while True:

        num_produto = ler_inteiro("\nDigite o número do produto conforme a lista acima: ")

        #laço de repetição que itera a lista de dicionário até encontrar o produto indicado pelo número ordinal
        for n in range (len(descrição_produtos)):
            if n+1 == num_produto:
                print(f"\nDescrição do produto de número {num_produto}:")
                for k, v in descrição_produtos[n].items():
                    print(f"{k}: {v}")

        continuar_consulta = ler_decisao("\nGostaria de continuar a consulta por produto? [S/N] -> ")

        #condicional que quebra o laço de repetição caso não se deseje continuar a consulta por produto
        if continuar_consulta!="S":
            print("\nFim da consulta por produto")
            break



# UPDATE  |  atualizar produto() 

def atualizar_produto(email_logado):

    banco_geral = carregar_produtos()
    
    if email_logado not in banco_geral or len(banco_geral[email_logado]) == 0:
        print("\nNão existem produtos cadastrados na sua loja.")
        return

    descricao_produtos = banco_geral[email_logado]

    print("="*30, "ATUALIZAÇÃO DE PRODUTOS", "="*30)
    #condicional que verifica se existem produtos cadastrados
    if len(descricao_produtos) == 0:
        print("\nNão existem produtos cadastrados.")
        return

    att_produto = ler_decisao("\nDeseja atualizar produto(s) na loja? [S/N] ")

    while att_produto == "S":
        print("\nProdutos cadastrados.")
        #retorna a lista de produtos e o número ordinal associado ao produto
        for i in range(len(descricao_produtos)):
            print(f"\n{i+1}º produto: {descricao_produtos[i]['Nome']}")

        num_produto = ler_inteiro("\nDigite o número do produto que deseja atualizar: ")

        #verifica se o número colocado no input é realmente válido e associado a um produto
        if num_produto < 1 or num_produto > len(descricao_produtos):
            print("\nProduto inválido.")
            return

        #variável que recebe o dicionário do produto a ser atualizado
        produto = descricao_produtos[num_produto - 1]

        print(f"\nProduto selecionado: {produto['Nome']}")

        #menu que guia o usuário nas opções de atualização
        print("\nO que deseja atualizar?\n")
        print("1 - Nome")
        print("2 - Preço")
        print("3 - Material")
        print("4 - Estoque")
        print("5 - Tudo")

        opcao = ler_inteiro("\nEscolha o número da opção: ")

        if opcao == 1:
            produto["Nome"] = ler_string("Novo nome: ").strip().capitalize()
            print("\nNome atualizado com sucesso!")
        
        elif opcao == 2:
            produto["Preço"] = ler_real("Novo preço: R$ ")
            print("\nPreço atualizado com sucesso!")

        elif opcao == 3:
            produto["Material"] = ler_string("Novo material: ").strip().capitalize()
            print("\nMaterial atualizado com sucesso!")
    
        elif opcao == 4:
            produto["Estoque"] = ler_inteiro("Novo estoque: ")
            print("\nEstoque atualizado com sucesso!")
            
        elif opcao == 5:
            produto["Nome"] = ler_string("Novo nome: ").strip().capitalize()
            produto["Preço"] = ler_real("Novo preço: R$ ") 
            produto["Material"] = ler_string("Novo material: ").strip().capitalize()
            produto["Estoque"] = ler_inteiro("Novo estoque: ")
            print("\nProduto atualizado com sucesso!")

        else:
            print("\nOpção inválida.")

        att_produto = ler_decisao("\nDeseja atualizar mais algum produto? [S/N] ")

    # Atualiza os produtos no JSON
    banco_geral[email_logado] = descricao_produtos
    salvar_produtos(banco_geral)

    print("\nFim da atualização")

#DELETE | Excluir produto(s)

def excluir_produto(email_logado):

    banco_geral = carregar_produtos()
    
    if email_logado not in banco_geral or len(banco_geral[email_logado]) == 0:
        print("\nNão há produtos cadastrados na sua loja.")
        return

    descricao_produtos = banco_geral[email_logado]  

    print("="*30, "EXCLUSÃO DE PRODUTOS", "="*30)
    #verifica se há produtos cadastrados
    if len(descricao_produtos) == 0:
        print("\nNão há produtos cadastrados.")
        return

    del_produto = ler_decisao("\nDeseja excluir produto(s) na loja? [S/N] ")

    while del_produto == "S":
        print("\nProdutos cadastrados:")
        #laço de repetição que lista os produtos cadastrados e mostra os números ordinais associados a cada produto
        for i in range(len(descricao_produtos)):
            print(f"{i+1}º produto: {descricao_produtos[i]['Nome']}")

        num_produto = ler_inteiro("\nDigite o número do produto que deseja excluir: ")

        #verifica se o número do input é válido e corresponde a um dos produtos
        if num_produto < 1 or num_produto > len(descricao_produtos):
            print("\nProduto inválido.")
            return

        #variável que recebe o dicionário do produto que foi removido pelo método .pop()
        produto_removido = descricao_produtos.pop(num_produto - 1)

        print(f"\nProduto '{produto_removido['Nome']}' removido com sucesso!")

        del_produto = ler_decisao("\nDeseja excluir mais produtos na loja? [S/N] ")

    # Exclui o produto no JSON
    banco_geral[email_logado] = descricao_produtos
    salvar_produtos(banco_geral)

    print("\nFim da exclusão de produtos.")
