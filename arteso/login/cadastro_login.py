from arteso.login.verificacao_email import *
from arteso.cadastro_produtos.crud_produtos import *

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios():
    usuarios = {}

    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo: # Lê o arquivo de usuários e carrega os dados para um dicionário em memória
            for linha in arquivo:
                linha = linha.strip()

                if linha:
                    email, senha = linha.split(";")
                    usuarios[email] = senha

    except FileNotFoundError: # Se o arquivo não existir, ele será criado automaticamente
        open(ARQUIVO_USUARIOS, "a").close()

    return usuarios

banco_usuarios = carregar_usuarios() # Carrega os usuários do arquivo para o dicionário em memória

def salvar_usuario(email, senha): # Salva um novo usuário no arquivo de texto
    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{email};{senha}\n")

def cadastrar_usuario(email, senha, confirmar_senha): # Valida o e-mail, verifica se já existe e se a senha é válida antes de salvar o usuário

    if not validar_email(email): # Valida o formato do e-mail usando a função do arquivo verificacao_email.py
        print("Erro: O formato do e-mail é inválido.")
        return False

    if email in banco_usuarios: # Verifica se o e-mail já está cadastrado no dicionário em memória
        print("Erro: Este e-mail já está cadastrado.")
        return False

    if len(senha) < 6: #    Verifica se a senha tem pelo menos 6 caracteres
        print("Erro: A senha deve ter pelo menos 6 caracteres.")
        return False

    if senha != confirmar_senha: # Verifica se a senha e a confirmação de senha são iguais
        print("Erro: Senha incorreta.")
        return False

    banco_usuarios[email] = senha

    try: # Salva o novo usuário no arquivo de texto usando a função salvar_usuario do mesmo arquivo
        salvar_usuario(email, senha)
        print("Cadastro realizado com sucesso!")
        return True

    except Exception as e: # Tratamento de exceção para erros ao salvar o usuário no arquivo
        print(f"Erro ao salvar usuário: {e}")
        return False

def fazer_login(email, senha): # Verifica se o e-mail e senha correspondem a um usuário cadastrado

    if email in banco_usuarios and banco_usuarios[email] == senha: 
        print("Login efetuado com sucesso! Bem-vindo.")
        return True

    print("Erro: E-mail ou senha incorretos.")
    return False