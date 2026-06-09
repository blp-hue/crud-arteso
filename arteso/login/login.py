def validar_email(email):

    # Verifica se tem arroba e ponto
    if "@" not in email or "." not in email:
        return False
    
    # Divide em usuário e domínio
    partes = email.split("@")
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    
    # Verifica se usuário e domínio não estão vazios
    if not usuario or not dominio:
        return False
    
    # Verifica se o domínio tem um ponto
    if "." not in dominio:
        return False
        
    # Verifica se não termina com ponto
    if email.endswith("."):
        return False

    return True

#formato: {"email": "senha"}
banco_usuarios = {}

def fazer_login(email, senha):
    if email in banco_usuarios and banco_usuarios[email] == senha:
        print("Login efetuado com sucesso! Bem-vindo.")
        return True
    else:
        print("Erro: E-mail ou senha incorretos.")
        return False