# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================

# CREATE  |  inscrição na feira
import json
import csv 
from datetime import date
from arteso.exception_value import *

info_feiras = [] #lista composta que contém as informações sobre as feiras retiradas do arquivo csv
tupla_feiras = () #tupla para guardar os nomes das feiras por serem imutáveis
data_inscricao = date.today() #retorna o dia que a inscrição será feita

ARQUIVO_INSCRICOES_JSON = "inscricoes.json" #arquivo json para armazenar as inscrições feitas, caso queira persistir os dados mesmo após o programa ser fechado

def carregar_inscricoes(): #carrega as inscrições do arquivo JSON para um dicionário em memória, permitindo que os dados sejam acessados e manipulados durante a execução do programa
    try:
        with open(ARQUIVO_INSCRICOES_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver corrompido/vazio, retorna um dicionário vazio
        return {}

def salvar_todas_inscricoes_json(dicionario): #salva o dicionário mestre no arquivo JSON, garantindo que os dados sejam persistidos mesmo após o programa ser fechado
    with open(ARQUIVO_INSCRICOES_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)


# NOVO: Função utilitária interna para ler o catálogo do CSV sem rodar no import do main
def carregar_catalogo():
    global info_feiras, tupla_feiras
    info_feiras.clear()
    nomes_feiras = []
    
    with open("arteso/cadastro_feiras/informacao_feiras.csv", "r", encoding="utf-8") as arquivo:
        conteudo = csv.reader(arquivo, delimiter=',')
        cabecalho = next(conteudo)
        for linha in conteudo:
            info_feiras.append(linha)
            nomes_feiras.append(linha[0])
            
    tupla_feiras = tuple(nomes_feiras)
    return cabecalho


def inscrever_feiras(email_logado):
    # Carrega as tabelas do CSV de forma segura
    cabecalho = carregar_catalogo()

    banco_inscricoes = carregar_inscricoes()
    
    # Validação: Se o e-mail já existir nas chaves do JSON, barra a duplicidade
    if email_logado in banco_inscricoes:
        print(f"\nErro: Você já está inscrita na feira '{banco_inscricoes[email_logado]['Feira']}'.")
        return

    print("="*30, "INFORMAÇÕES SOBRE AS FEIRAS", "="*30)

    for c in cabecalho: #divide as palavras presentes no cabeçalho para melhor visualização
        print(f"{c} \\ ", end=" ")

    for f in info_feiras: #uso da indexação para organizar melhor as informações sobre as feiras
        print(f"\n{f[0]}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")
    
    print("\n" + "="*30, "INSCRIÇÃO NAS FEIRAS", "="*30)
    print("\nEm qual feira deseja se inscrever? ")

    #laço de repetição que retorna o nome de cada feira para facilitar a inscrição
    for f in tupla_feiras:
        print(f)

    print("OBSERVAÇÃO: Você só pode se inscrever em apenas uma feira a cada semana. Fique atenta aos prazos.")

    inscricao_feira = {} #dicionário local para armazenar as informações da inscrição da artesã, evitando mistura de dados de logins diferentes

    #adição do par chave-valor no dicionário que irá conter a inscrição da artesã
    inscricao_feira["Feira"] = input("\nDigite o nome da feira (igual ao da lista): ").strip().capitalize()
    inscricao_feira["Nome"] = input("Digite seu nome completo: ").strip().capitalize()
    inscricao_feira["Endereço"] = input("Digite seu endereço: ").strip().capitalize()
    inscricao_feira["Bairro"] = input("Digite seu bairro: ").strip().capitalize()
    inscricao_feira["Quantidade de produtos"] = ler_inteiro("Digite a quantidade de produtos: ")
    inscricao_feira["Data de inscrição"] = data_inscricao.strftime("%d/%m/%Y")

    # Insere/atualiza a chave do usuário logado no dicionário master
    banco_inscricoes[email_logado] = inscricao_feira
    
    # Salva o dicionário master atualizado de volta no arquivo JSON
    salvar_todas_inscricoes_json(banco_inscricoes)

    #laço de repetição que itera a lista de feiras e encontra a feira que a artesã está inscrita para retornar informações específicas
    for f in info_feiras:
        if inscricao_feira["Feira"] in f[0].strip().capitalize():
            print(f"\nInformações sobre sua próxima feira, {inscricao_feira['Nome']} -> {inscricao_feira['Feira']}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")


#READ | ler a inscrição na feira -> iterar o dicionário e chamar as informações da feira inscrita 

def ler_inscricao(email_logado):
    
    banco_inscricoes = carregar_inscricoes()

    if email_logado not in banco_inscricoes:
        print("\nVocê não realizou nenhuma inscrição.")
        return

    # AJUSTE: Mapeado para ler da variável correta que veio do JSON
    inscricao_usuario = banco_inscricoes[email_logado]

    print("="*30, "INFORMAÇÕES SOBRE A INSCRIÇÃO", "="*30)
    print("As informações da sua inscrição: ")

    #laço de repetição que itera cada par chave-valor e printa na tela
    for k,v in inscricao_usuario.items():
        print(f"{k}: {v}")

    # Carrega o catálogo do CSV para exibir os detalhes estruturais da feira associada
    carregar_catalogo()
    for f in info_feiras:
        if inscricao_usuario["Feira"] in f[0].strip().capitalize():
            print(f"Informações sobre sua próxima feira, {inscricao_usuario['Nome']} -> {inscricao_usuario['Feira']}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")


#UPTADE | atualizar a inscrição na feira -> permite atualizar tudo ou só alguns campos.

def atualizar_inscricao(email_logado):
    print("="*30, "ATUALIZAR INSCRIÇÃO", "="*30)

    banco_inscricoes = carregar_inscricoes()

    if email_logado not in banco_inscricoes:
        print("\nVocê não realizou nenhuma inscrição.")
        return

    inscricao_feira = banco_inscricoes[email_logado]
    carregar_catalogo()

    while True:
        #menu que guia a opção do usuário para a atualização que deseja
        print("\nO que deseja atualizar?")
        print("1 - Feira")
        print("2 - Dados pessoais")
        print("3 - Tudo")
        try:
            opcao = int(input("Escolha o número da opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue
            
        #atualiza a feira que está inscrita
        if opcao == 1:
            print("\nFeiras disponíveis:")

            for f in tupla_feiras:
                print(f) 

            nova_feira = input("\nDigite a nova feira: ").strip().capitalize()

            for f in info_feiras:
                if nova_feira in f[0].strip().capitalize():
                    inscricao_feira["Feira"] = nova_feira.strip().capitalize()

            print("\nAtualizado com sucesso!")
            break

        #atualiza os dados pessoais inscritos
        elif opcao == 2:
            inscricao_feira["Nome"] = input("\nDigite seu nome completo: ").strip().capitalize()
            inscricao_feira["Endereço"] = input("Digite o seu endereço: ").strip().capitalize()
            inscricao_feira["Bairro"] = input("Digite seu bairro: ").strip().capitalize()

            print("\nDados atualizados com sucesso!")
            break

        #atualiza todos os aspectos da inscrição
        elif opcao == 3:
            print("\nRefazendo inscrição...")

            for f in info_feiras:
                print(f[0])

            inscricao_feira["Feira"] = input("\nDigite o nome feira (igual ao da lista): ").strip().capitalize()
            inscricao_feira["Nome"] = input("Digite seu nome completo: ").strip().capitalize()
            inscricao_feira["Endereço"] = input("Digite seu endereço: ").strip().capitalize()
            inscricao_feira["Bairro"] = input("Digite seu bairro: ").strip().capitalize()
            inscricao_feira["Quantidade de produtos"] = ler_inteiro("Digite a quantidade de produtos: ")
            inscricao_feira["Data de inscrição"] = data_inscricao.strftime("%d/%m/%Y")

            print("\nInscrição atualizada com sucesso!")
            break

        else:
            print("\nOpção inválida.")

    # Salva o arquivo JSON atualizado
    banco_inscricoes[email_logado] = inscricao_feira
    salvar_todas_inscricoes_json(banco_inscricoes)


#DELETE | deletar a inscrição na feira 

def deletar_inscricao(email_logado):
    print("="*30, "DELETAR INSCRIÇÃO", "="*30)

    banco_inscricoes = carregar_inscricoes()

    if email_logado not in banco_inscricoes:
        print("\nNão há inscrições para deletar.")
        return
    
    confirmacao = ler_decisao("\nTem certeza que deseja deletar sua inscrição? [S/N] ")

    if confirmacao == "S":
        # Remove a chave do usuário logado do dicionário master
        del banco_inscricoes[email_logado]
        salvar_todas_inscricoes_json(banco_inscricoes)
        print("\nInscrição deletada com sucesso!")
    else:
        print("\nOperação cancelada.")