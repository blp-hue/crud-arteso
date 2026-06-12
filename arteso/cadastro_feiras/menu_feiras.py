# ==================================================
#   Imports iniciais
# ==================================================
from arteso.cadastro_feiras.menu_feiras import *
from arteso.cadastro_feiras.crud_feiras import *
from arteso.exception_value import *

# ==================================================
#   Main || LOOP INICIAL
# ==================================================
def menu_feiras(email_logado): # <- Recebe o e-mail vindo do main.py
    while True:
        print("\n======= MENU FEIRAS =======")
        print("1 - Inscrição nas Feiras")
        print("2 - Ler Inscrição")
        print("3 - Atualizar Inscrição")
        print("4 - Deletar Inscrição")
        print("5 - Voltar ao Menu Principal")
        print("===========================")
        
        opcao = ler_inteiro("\nEscolha uma opção: ")
        
        if opcao == 1:
            inscrever_feiras(email_logado) 
        elif opcao == 2:
            ler_inscricao(email_logado) 
        elif opcao == 3:
            atualizar_inscricao(email_logado) 
        elif opcao == 4:
            deletar_inscricao(email_logado) 
        elif opcao == 5:
            print("\nRetornando ao painel principal...")
            break
        else:
            print("\nOpção inválida.")
