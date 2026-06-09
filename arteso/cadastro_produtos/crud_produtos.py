# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================

# CREATE  |  cadastro de produto(s) 

def adicionar_produtos(descricao_produtos):

    add_produto = input("\nDeseja adicionar produtos na loja? [S/N] ").strip().upper()#adicionar tratamento de exceção

    while add_produto == "S":

        produto = str(input("\nDigite o nome do produto: ")).strip().capitalize()#adicionar tratamento de exceção
                    
        if not any(chave["nome"] == produto for chave in descricao_produtos): #evita duplicidade de dados para não criar outra lista
            print(f"\nProduto '{produto}' adicionado!")

            print(f"\nAdicione a descrição do produto: ") #criação do dicionário com a descrição do produto

            produtos = {
                "nome":     produto,
                "preço":    float(input("Valor do produto: R$ ")),#adicionar tratamento de exceção
                "material": input("Material do produto: ").strip().capitalize(),
                "estoque":  int(input("Estoque do produto: "))#adicionar tratamento de exceção
            }
            descricao_produtos.append(produtos) #adiciona o dicionário em uma lista para ter uma sequência de cadastros
        else:
            print("\nProduto já existe na loja.")

        add_produto = input("\nDeseja adicionar mais produtos? [S/N] ").strip().upper()#adicionar tratamento de exceção

    return 0
# READ    |  listar produto(s)

def consultar_produtos(descrição_produtos):

    print("="*30, "CONSULTA DE PRODUTOS", "="*30)
    print(f"Os produtos cadastrados são: ")

    #lista todos os produtos cadastrados com um número ordinal associado
    for i in range (len(descrição_produtos)):
        print(f"{i+1}º produto: {descrição_produtos[i]["nome"]}")

    consulta_produto = input("\nGostaria consultar um produto? [S/N] -> ").strip().upper()#adicionar tratamento de exceção

    #condicional que valida o início do laço de repetição de consulta por produto
    if consulta_produto!="S":
        print(f"\nFim da consulta")
        return False
    

    #laço de repetição para consultar o dicionário de um produto específico de acordo com o número ordinal informado acima
    while True:

        num_produto = int(input("\nDigite o número do produto conforme a lista acima: ")) #adicionar tratamento de exceção

        #laço de repetição que itera a lista de dicionário até encontrar o produto indicado pelo número ordinal
        for n in range (len(descrição_produtos)):
            if n+1 == num_produto:
                print(f"\nDescrição do produto de número {num_produto}:")
                print(f"{descrição_produtos[n]}")

        continuar_consulta = input("\nGostaria de continuar a consulta por produto? [S/N] -> ").strip().upper()

        #condicional que quebra o laço de repetição caso não se deseje continuar a consulta por produto
        if continuar_consulta!="S":
            print("\nFim da consulta por produto")
            break

    consulta_geral = input("\nGostaria de fazer uma consulta geral? [S/N] -> ").strip().upper()#adicionar tratamento de exceção

    #condicional que leva à lista de dicionários com todos os produtos e com print formatado auxiliado por um for
    if consulta_geral == "S":
        for g in range (len(descrição_produtos)):
            print(f"{g+1}º produto: {descrição_produtos[g]}")
        print("\nFim da consulta geral")
    else:
        print("\nVocê saiu da consulta geral")
    



# UPDATE  |  atualizar produto() 

def atualizar_produto(descricao_produtos):
    
    print("="*30, "ATUALIZAÇÃO DE PRODUTOS", "="*30)
    #condicional que verifica se existem produtos cadastrados
    if len(descricao_produtos) == 0:
        print("\nNão existem produtos cadastrados.")
        return

    print("\nProdutos cadastrados.")

    #retorna a lista de produtos e o número ordinal associado ao produto
    for i in range(len(descricao_produtos)):
        print(f"{i+1}º produto: {descricao_produtos[i]['nome']}")

    num_produto = int(input("\nDigite o número do produto que deseja atualizar: ")) #adicionar tratamento de exceção

    #verifica se o número colocado no input é realmente válido e associado a um produto
    if num_produto < 1 or num_produto > len(descricao_produtos):
        print("\nProduto inválido.")
        return

    #variável que recebe o dicionário do produto a ser atualizado
    produto = descricao_produtos[num_produto - 1]

    print(f"\nProduto selecionado: {produto['nome']}")

    #menu que guia o usuário nas opções de atualização
    print("\nO que deseja atualizar?")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Material")
    print("4 - Estoque")
    print("5 - Tudo")

    opcao = int(input("Escolha o número da opção: ")) #adicionar tratamento de exceção

    if opcao == 1:
        produto["nome"] = input("Novo nome: ").strip().capitalize()
        print("\nNome atualizado com sucesso!")
    
    elif opcao == 2:
        produto["preço"] = float(input("Novo preço: R$ ")) #adicionar tratamento de exceção
        print("\nPreço atualizado com sucesso!")

    elif opcao == 3:
        produto["material"] = input("Novo material: ").strip().capitalize()
        print("\nMaterial atualizado com sucesso!")
  
    elif opcao == 4:
        produto["estoque"] = int(input("Novo estoque: "))#adicionar tratamento de exceção
        print("\nEstoque atualizado com sucesso!")
        
    elif opcao == 5:
        produto["nome"] = input("Novo nome: ").strip().capitalize()
        produto["preço"] = float(input("Novo preço: R$ ")) #adicionar tratamento de exceção
        produto["material"] = input("Novo material: ").strip().capitalize()
        produto["estoque"] = int(input("Novo estoque: ")) #adicionar tratamento de exceção
        print("\nProduto atualizado com sucesso!")

    else:
        print("\nOpção inválida.")


#DELETE | Excluir produto(s)

def excluir_produto(descricao_produtos):

    print("="*30, "EXCLUSÃO DE PRODUTOS", "="*30)
    #verifica se há produtos cadastrados
    if len(descricao_produtos) == 0:
        print("\nNão há produtos cadastrados.")
        return

    print("\nProdutos cadastrados:")

    #laço de repetição que lista os produtos cadastrados e mostra os números ordinais associados a cada produto
    for i in range(len(descricao_produtos)):
        print(f"{i+1}º produto: {descricao_produtos[i]['nome']}")

    num_produto = int(input("\nDigite o número do produto que deseja excluir: "))#adicionar tratamento de exceção

    #verifica se o número do input é válido e corresponde a um dos produtos
    if num_produto < 1 or num_produto > len(descricao_produtos):
        print("\nProduto inválido.")
        return

    #variável que recebe o dicionário do produto que foi removido pelo método .pop()
    produto_removido = descricao_produtos.pop(num_produto - 1)

    print(f"\nProduto '{produto_removido['nome']}' removido com sucesso!")

