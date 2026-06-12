# Dentro de arteso/cadastro_produtos/menu.py (ou crud.py)

from arteso.cadastro_produtos.crud_produtos import *

def menu_produtos(email_logado):
    """O antigo 'main interno' adaptado para ser uma função controladora"""
    while True:
        # Exibe o menu visual
        print("\n======= MENU =======")
        print("1 - Adicionar Produto")
        print("2 - Excluir Produto")
        print("3 - Atualizar Produto")
        print("4 - Ver Produtos")
        print("5 - Sair")
        print("====================")

        try:
            # Captura a ação do usuário tratando erros de digitação
            acao = int(input("\nEscolha sua ação (1 - 5): "))
        except ValueError:
            print("\nDigite apenas números.")
            continue
            
        # Estrutura match/case mapeando para as funções do seu CRUD
        match acao:
            case 1:
                adicionar_produtos(email_logado)
                
            case 2:
                excluir_produto(email_logado)
                
            case 3:
                # Corrigido aqui: sua função no crud.py está no singular (atualizar_produto)
                atualizar_produto(email_logado)
                
            case 4:
                # Corrigido aqui: sua função no crud.py usa descrição_produtos com Ç
                consultar_produtos(email_logado)
                
            case 5:
                print("\nVoltando ao menu principal do Artesô...")
                break # Quebra o while True e encerra a função, voltando para o main externo
                
            case _:
                print("\nOpção inválida. Escolha um número entre 1 e 5.")