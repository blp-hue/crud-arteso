# ==================================================
#   Imports iniciais
# ==================================================
from menu_feiras import *
from crud_feiras import *
# ==================================================
#   Main || LOOP INICIAL
# ==================================================
def menu_feiras():
    """ Controla o loop e as opções do CRUD de feiras artesanais """
    while True:
        print("\n======= MENU FEIRAS =======")
        print("1 - Inscrição nas Feiras")
        print("2 - Ler Inscrição")
        print("3 - Atualizar Inscrição")
        print("4 - Deletar Inscrição")
        print("5 - Voltar ao Menu Principal")
        print("===========================")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            # Primeiro mostra o catálogo de feiras que guardamos na função
            painel_feiras() 
            # Depois faz a inscrição
            inscrever_feiras()
        elif opcao == "2":
            ler_inscricao(inscricao_feira)
        elif opcao == "3":
            atualizar_inscricao(inscricao_feira)
        elif opcao == "4":
            deletar_inscricao(inscricao_feira)
        elif opcao == "5":
            print("\nRetornando ao painel principal...")
            break 
        else:
            print("\nOpção inválida.")
