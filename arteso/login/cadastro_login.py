from arteso.login.verificacao_email import *
from arteso.cadastro_produtos.crud_produtos import *
#formato: {"email": "senha"}
banco_usuarios = {}

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
        print("Erro: Senha Incorreta.")
        return False

    banco_usuarios[email] = senha
    print("Cadastro realizado com sucesso!")
    return True

def fazer_login(email, senha):
    if email in banco_usuarios and banco_usuarios[email] == senha:
        print("Login efetuado com sucesso! Bem-vindo.")
        return True
    else:
        print("Erro: E-mail ou senha incorretos.")
        return False