def validar_email(email):
    # Verifica se tem arroba e ponto
    if "@" not in email or "." not in email:
        return False

    partes = email.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio = partes

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    if email.endswith("."):
        return False

    return True

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
        print("Erro: As senhas não coincidem.")
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


print("--- TESTE DE CADASTRO ---")
cadastrar_usuario("usuario.com", "123456", "123456")

cadastrar_usuario("teste@email.com", "123456", "654321")

cadastrar_usuario("joao@email.com", "senha123", "senha123")

cadastrar_usuario("joao@email.com", "outrasenha", "outrasenha")

print("\n--- TESTE DE LOGIN ---")

fazer_login("joao@email.com", "senha_errada")

fazer_login("joao@email.com", "senha123")
