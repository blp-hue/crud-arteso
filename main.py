# ==================================================
#   FLUXO PRINCIPAL DO SISTEMA - ARTESÔ
# ==================================================

# Importação de todas as funções e dados dos sub-módulos do sistema
from arteso.login.verificacao_email import *
from arteso.login.cadastro_login import *
from arteso.cadastro_produtos.dados_produtos import *
from arteso.cadastro_produtos.crud_produtos import *
from arteso.cadastro_feiras.crud_feiras import *
from arteso.cadastro_produtos.menu_produtos import menu_produtos


# SUB-MENU 1 | Gerenciamento de Produtos

def menu_produtos_principal():
    """ Controla o loop e as opções do CRUD de produtos """
    while True:
        print("="*30, "MENU DE PRODUTOS", "="*30)
        print("1 - Adicionar Produto")
        print("2 - Excluir Produto")
        print("3 - Atualizar Produto")
        print("4 - Ver Produtos")
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
            excluir_produto(descricao_produtos)
        elif acao == 3:
            atualizar_produto(descricao_produtos)
        elif acao == 4:
            consultar_produtos(descricao_produtos)
        elif acao == 5:
            print("\nRetornando ao painel principal...")
            break # Quebra o laço atual para subir um nível no menu
        else:
            print("\nOpção inválida.")


# SUB-MENU 2 | Gerenciamento de Inscrições em Feiras

def menu_feiras_principal():
    """ Controla o loop e as opções do CRUD de feiras artesanais """
    while True:
        print("="*30, "MENU DE FEIRAS", "="*30)
        print("1 - Inscrição nas Feiras")
        print("2 - Ler Inscrição")
        print("3 - Atualizar Inscrição")
        print("4 - Deletar Inscrição")
        print("5 - Voltar ao Menu Principal")
        print("===========================")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        # Condicionais que chamam as funções do arquivo crud_feiras.py
        if opcao == "1":
            inscrever_feiras()
        elif opcao == "2":
            ler_inscricao(inscricao_feira)
        elif opcao == "3":
            atualizar_inscricao(inscricao_feira)
        elif opcao == "4":
            deletar_inscricao(inscricao_feira)
        elif opcao == "5":
            print("\nRetornando ao painel principal...")
            break # Quebra o laço atual para voltar ao painel do usuário
        else:
            print("\nOpção inválida.")


# NÍVEL 2 | Painel do Usuário Autenticado

def sistema_logado():
    """ Sub-menu intermediário acessado apenas após validação de login bem-sucedida """
    while True:
        print("="*30, "PAINEL ARTESÔ", "="*30)
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Feiras")
        print("0 - Desconectar (Log out)")
        
        opcao = input("Escolha uma opção: ").strip()
        
        # Redireciona o fluxo para o módulo escolhido ou encerra a sessão atual
        if opcao == "1":
            menu_produtos_principal() # Direciona para o fluxo de produtos
        elif opcao == "2":
            menu_feiras_principal() # Direciona para o fluxo de feiras
        elif opcao == "0":
            print("\nSessão encerrada com sucesso.")
            break # Quebra o laço e faz o usuário voltar para a tela de autenticação inicial
        else:
            print("\nOpção inválida.")


# NÍVEL 1 | Porta de Entrada e Autenticação

def main():
    """ Função mestra que inicializa o programa e gerencia o acesso à plataforma """
    while True:
        print("="*30, "BEM VINDO AO ARTESÔ", "="*30)
        print("1 - Login")
        print("2 - Cadastro")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        # Fluxo de verificação de credenciais
        if opcao == "1":
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha: ")
            
            # Valida se os dados coincidem com o dicionário de usuários cadastrados
            if fazer_login(email, senha):
                sistema_logado() # Só concede acesso se a função retornar True
                
        # Fluxo para criação de novas contas
        elif opcao == "2":
            print("="*30, "CADASTRO DE USUÁRIO", "="*30)
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha: ")
            confirmar_senha = input("Confirme sua senha: ")
            cadastrar_usuario(email, senha, confirmar_senha) # Invoca a rotina de criação de conta e senha
            
        # Encerramento definitivo da aplicação
        elif opcao == "0":
            print("Sistema encerrado. Até logo!")
            break # Quebra o loop principal e finaliza o script de vez
        else:
            print("Opção inválida!")


# INICIALIZAÇÃO AUTOMÁTICA DO SISTEMA
if __name__ == "__main__":
    main()
