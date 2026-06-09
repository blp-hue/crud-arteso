from login import *

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


print("--- TESTE DE CADASTRO ---")
cadastrar_usuario("usuario.com", "123456", "123456")

cadastrar_usuario("teste@email.com", "123456", "654321")

cadastrar_usuario("joao@email.com", "senha123", "senha123")

cadastrar_usuario("joao@email.com", "outrasenha", "outrasenha")

print("\n--- TESTE DE LOGIN ---")

fazer_login("joao@email.com", "senha_errada")

fazer_login("joao@email.com", "senha123")
