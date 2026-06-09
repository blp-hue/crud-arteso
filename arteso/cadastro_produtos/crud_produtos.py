# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================


# CREATE  |  cadastro de produto(s) 

#pensei em fazer um mini menu perguntando se quer criar ou nao, e provavelmente um while com uma condicional dentro pra criar um loop de cadastro de produto que pode ser interrompida

def adicionar_produtos(descricao_produtos):

    add_produto = input("\nDeseja adicionar produtos na loja? [S/N] ").strip().upper()

    while add_produto == "S":

        produto = input("\nDigite o nome do produto: ").strip().capitalize()

      
                    
        if not any(chave["nome"] == produto for chave in descricao_produtos): #evita duplicidade de dados para não criar outra lista
            print(f"\nProduto '{produto}' adicionado!")

            print(f"\nAdicione a descrição do produto: ") #criação do dicionário com a descrição do produto

            produtos = {
                "nome":     produto,
                "preço":    float(input("Valor do produto: R$ ")),
                "material": input("Material do produto: ").strip().capitalize(),
                "estoque":  int(input("Estoque do produto: "))
            }
            descricao_produtos.append(produtos) #adiciona o dicionário em uma lista para ter uma sequência de cadastros
        else:
            print("\nProduto já existe na loja.")

        add_produto = input("\nDeseja adicionar mais produtos? [S/N] ").strip().upper()

    return 0

# READ    |  listar produto(s)

# - poderia fazer um for para listar os produtos na lista e outro para o dicionário
# - um for para ver colocar o indice e/ou chave para acessar um produto específico na lista e/ou no dicionario

def consultar_produtos(descrição_produtos):

    print(f"Os produtos cadastrados são: ")

    #lista todos os produtos cadastrados com um número ordinal associado
    for i in range (len(descrição_produtos)):
        print(f"{i+1}º produto: {descrição_produtos[i]["nome"]}")

    consulta_produto = input("\nGostaria consultar um produto? [S/N] -> ").strip().upper()

    #condicional que valida o início do laço de repetição de consulta por produto
    if consulta_produto!="S":
        print(f"\nFim da consulta")
        return False
    

    #laço de repetição para consultar o dicionário de um produto específico de acordo com o número ordinal informado acima
    while True:

        num_produto = int(input("\nDigite o número do produto conforme a lista acima: "))

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

    consulta_geral = input("\nGostaria de fazer uma consulta geral? [S/N] -> ").strip().upper()

    #condicional que leva à lista de dicionários com todos os produtos e com print formatado auxiliado por um for
    if consulta_geral == "S":
        for g in range (len(descrição_produtos)):
            print(f"{g+1}º produto: {descrição_produtos[g]}")
        print("\nFim da consulta geral")
    else:
        print("\nVocê saiu da consulta geral")
    


print("="*30, "CONSULTA DE PRODUTOS", "="*30)

# UPDATE  |  atualizar produto() 

# - atualização de preço e estoque

def atualizar_produto(descricao_produtos):
    
    #condicional que verifica se existem produtos cadastrados
    if len(descricao_produtos) == 0:
        print("\nNão existem produtos cadastrados.")
        return

    print("\nProdutos cadastrados.")

    #retorna a lista de produtos 
    for i in range(len(descricao_produtos)):
            print(f"{i+1}º produto: {descricao_produtos[i]['nome']}")

    num_produto = int(input("\nDigite o número do produto que deseja atualizar: "))

    #verifica se o número ordinal associado ao produto é realmente válido
    if num_produto < 1 or num_produto > len(descricao_produtos):
            print("\nProduto inválido.")
            return

    produto = descricao_produtos[num_produto - 1]

    print(f"\nProduto selecionado: {produto['nome']}")

    print("\nO que deseja atualizar?")
    print("1 - Preço")
    print("2 - Estoque")
    print("3 - Tudo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
            produto["preço"] = float(input("Novo preço: R$ "))
            print("\nPreço atualizado com sucesso!")

    elif opcao == "2":
            produto["estoque"] = int(input("Novo estoque: "))
            print("\nEstoque atualizado com sucesso!")
        
    elif opcao == "3":
            produto["nome"] = input("Novo nome: ").strip().capitalize()
            produto["preço"] = float(input("Novo preço: R$ "))
            produto["material"] = input("Novo material: ").strip().capitalize()
            produto["estoque"] = int(input("Novo estoque: "))
            print("\nProduto atualizado com sucesso!")

    else:
            print("\nOpção inválida.")

print("="*30, "ATUALIZAÇÃO DE PRODUTOS", "="*30)

#DELETE | Excluir produto()
# - deletar produtos cadastrados

def excluir_produto(descricao_produtos):

    if len(descricao_produtos) == 0:
        print("\nNão há produtos cadastrados.")
        return

    print("\nProdutos cadastrados:")

    for i in range(len(descricao_produtos)):
        print(f"{i+1}º produto: {descricao_produtos[i]['nome']}")

    num_produto = int(input("\nDigite o número do produto que deseja excluir: "))

    if num_produto < 1 or num_produto > len(descricao_produtos):
        print("\nProduto inválido.")
        return

    produto_removido = descricao_produtos.pop(num_produto - 1)

    print(f"\nProduto '{produto_removido['nome']}' removido com sucesso!")

print("="*30, "EXCLUSÃO DE PRODUTOS", "="*30)
