# ==================================================
#   FLUXO PRINCIPAL DO SISTEMA - ARTESÔ
# ==================================================

# Importação de todas as funções e dados dos sub-módulos do sistema
from arteso.cadastro_feiras.menu_feiras import menu_feiras
from arteso.login.verificacao_email import *
from arteso.login.cadastro_login import *
from arteso.cadastro_produtos.crud_produtos import *
from arteso.cadastro_feiras.crud_feiras import *
from arteso.cadastro_produtos.menu_produtos import menu_produtos
from arteso.exception_value import *


# NÍVEL 2 | Painel do Usuário Autenticado

def sistema_logado(email_logado):
    """ Sub-menu intermediário acessado apenas após validação de login bem-sucedida """
    while True:
        print("\n" + "="*30, "PAINEL ARTESÔ", "="*30)
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Feiras")
        print("3 - Desconectar (Log out)")
        print("="*45)
        
        opcao = ler_inteiro("Escolha uma opção: ")
        
        if opcao == 1:
            # AJUSTE: Chama o menu de produtos externo passando o e-mail do usuário logado
            menu_produtos(email_logado) 
        elif opcao == 2:
            # Repassa o e-mail do usuário autenticado para o gerenciador de feiras externo
            menu_feiras(email_logado) 
        elif opcao == 3:
            print("\nSessão encerrada com sucesso.")
            break 
        else:
            print("\nOpção inválida.")


# NÍVEL 1 | Porta de Entrada e Autenticação

def main():
    """ Função mestra que inicializa o programa e gerencia o acesso à plataforma """
    while True:
        print("\n" + "="*30, "BEM VINDO AO ARTESÔ", "="*30)
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")
        print("="*45)
        
        opcao = ler_inteiro("Escolha uma opção: ")
        
        if opcao == 1:
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha: ")
            
            # Valida se os dados coincidem com o arquivo usuarios.txt
            if fazer_login(email, senha):
                sistema_logado(email) # Transmite o e-mail para abrir o painel logado
                
        elif opcao == 2:
            print("\n" + "="*30, "CADASTRO DE USUÁRIO", "="*30)
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha: ")
            confirmar_senha = input("Confirme sua senha: ")
            cadastrar_usuario(email, senha, confirmar_senha) 
            
        elif opcao == 3:
            print("Sistema encerrado. Até logo!")
            break 
        else:
            print("Opção inválida!")


# INICIALIZAÇÃO AUTOMÁTICA DO SISTEMA
if __name__ == "__main__":
    main()