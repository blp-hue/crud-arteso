# ==================================================
#   FLUXO PRINCIPAL DO SISTEMA - ARTESÔ
# ==================================================

# Importação de todas as funções e dados dos sub-módulos do sistema
from arteso.cadastro_feiras.menu_feiras import menu_feiras
from arteso.login.verificacao_email import *
from arteso.login.cadastro_login import *
from arteso.cadastro_produtos.dados_produtos import *
from arteso.cadastro_produtos.crud_produtos import *
from arteso.cadastro_feiras.crud_feiras import *
from arteso.cadastro_produtos.menu_produtos import menu_produtos
from arteso.exception_value import *


# SUB-MENU 1 | Gerenciamento de Produtos

def menu_produtos_principal():
    """ Controla o loop e as opções do CRUD de produtos """
    while True:
        print("="*30, "MENU DE PRODUTOS", "="*30)
        print("1 - Adicionar Produto")
        print("2 - Consultar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("5 - Voltar ao Menu Principal")
        print("=============================")
        
        # Tratamento de exceção para evitar que o programa quebre se o usuário digitar uma letra
        try:
            acao = int(input("\nEscolha sua ação (1 - 5): "))
        except:
            print("\nDigite apenas números.")
            continue
            
        # Condicionais que chamam as respectivas funções do CRUD de produtos passando a lista de dados
        if acao == 1:
            adicionar_produtos(descricao_produtos)
        elif acao == 2:
            consultar_produtos(descricao_produtos)
        elif acao == 3:
            atualizar_produto(descricao_produtos)
        elif acao == 4:
            excluir_produto(descricao_produtos)
        elif acao == 5:
            print("\nRetornando ao painel principal...")
            break # Quebra o laço atual para subir um nível no menu
        else:
            print("\nOpção inválida.")


# SUB-MENU 2 | Gerenciamento de Inscrições em Feiras

def menu_produtos_principal():
    """ Controla o loop e as opções do CRUD de produtos """
    while True:
        print("="*30, "MENU DE PRODUTOS", "="*30)
        print("1 - Adicionar Produto")
        print("2 - Consultar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("5 - Voltar ao Menu Principal")
        print("=============================")
        
        # Uso do ler_inteiro para blindar o menu de produtos também!
        acao = ler_inteiro("\nEscolha sua ação (1 - 5): ")
            
        # Comparação feita diretamente com números inteiros
        if acao == 1:
            adicionar_produtos(descricao_produtos)
        elif acao == 2:
            consultar_produtos(descricao_produtos)
        elif acao == 3:
            atualizar_produto(descricao_produtos)
        elif acao == 4:
            excluir_produto(descricao_produtos)
        elif acao == 5:
            print("\nRetornando ao painel principal...")
            break 
        else:
            print("\nOpção inválida.")


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
        
        # Correção: Tratando como inteiros
        if opcao == 1:
            menu_produtos_principal() 
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