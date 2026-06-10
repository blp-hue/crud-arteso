from arteso.login.verificacao_email import *
from arteso.cadastro_produtos.crud_produtos import *

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios():
    usuarios = {}

    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha:
                    email, senha = linha.split(";")
                    usuarios[email] = senha

    except FileNotFoundError:
        # Cria o arquivo caso ele não exista
        open(ARQUIVO_USUARIOS, "a").close()

    return usuarios

banco_usuarios = carregar_usuarios()

def salvar_usuario(email, senha):
    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{email};{senha}\n")

def cadastrar_usuario(email, senha, confirmar_senha):

    if not validar_email(email):
        print("Erro: O formato do e-mail é inválido.")
        return False

    if email in banco_usuarios:
        print("Erro: Este e-mail já está cadastrado.")
        return False

    if len(senha) < 6:
        print("Erro: A senha deve ter pelo menos 6 caracteres.")
        return False

    if senha != confirmar_senha:
        print("Erro: Senha incorreta.")
        return False

    banco_usuarios[email] = senha

    try:
        salvar_usuario(email, senha)
        print("Cadastro realizado com sucesso!")
        return True

    except Exception as e:
        print(f"Erro ao salvar usuário: {e}")
        return False

def fazer_login(email, senha):

    if email in banco_usuarios and banco_usuarios[email] == senha:
        print("Login efetuado com sucesso! Bem-vindo.")
        return True

    print("Erro: E-mail ou senha incorretos.")
    return False