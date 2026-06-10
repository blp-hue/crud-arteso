# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================

# CREATE  |  inscrição na feira

import csv 
from datetime import date
from arteso.exception_value import *

info_feiras = [] #lista composta que contém as informações sobre as feiras retiradas do arquivo csv
inscricao_feira = {} #dicionário que irá conter as informações da inscrição nas feiras
tupla_feiras = () #tupla para guardar os nomes das feiras por serem imutáveis
data_inscricao = date.today() #retorna o dia que a inscrição será feita

def inscrever_feiras():

    print("="*30, "INFORMAÇÕES SOBRE AS FEIRAS", "="*30)

    for c in cabecalho: #divide as palavras presentes no cabeçalho para melhor visualização
        print(f"{c} \\ ", end=" ")

    for f in info_feiras: #uso da indexação para organizar melhor as informações sobre as feiras
        print(f"\n{f[0]}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")
    
    
    
    print("="*30, "INSCRIÇÃO NAS FEIRAS", "="*30)
    print("\nEm qual feira deseja se inscrever? ")

    #laço de repetição que retorna o nome de cada feira para facilitar a inscrição
    for f in tupla_feiras:
        print(f)

    print("OBSERVAÇÃO: Você só pode se inscrever em apenas uma feira a cada semana. Fique atenta aos prazos.")

    #adição do par chave-valor no dicionário que irá conter a inscrição da artesã
    inscricao_feira["Feira"] = input("\nDigite o nome da feira (igual ao da lista): ").strip().capitalize()
    inscricao_feira["Nome"] = input("Digite seu nome completo: ").strip().capitalize()
    inscricao_feira["Endereço"] = input("Digite seu endereço: ").strip().capitalize()
    inscricao_feira["Bairro"] = input("Digite seu bairro: ").strip().capitalize()
    inscricao_feira["Quantidade de produtos"] = ler_inteiro("Digite a quantidade de produtos: ")
    inscricao_feira["Data de inscrição"] = data_inscricao.strftime("%d/%m/%Y")

    #laço de repetição que itera a lista de feiras e encontra a feira que a artesã está inscrita para retornar informações específicas
    for f in info_feiras:
        if inscricao_feira["Feira"] in f[0].strip().capitalize():
            print(f"Informações sobre sua próxima feira, {inscricao_feira["Nome"]} -> {inscricao_feira["Feira"]}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")

with open("arteso/cadastro_feiras/informacao_feiras.csv", "r", encoding="utf-8") as arquivo:
    conteudo = csv.reader(arquivo, delimiter=',')
    cabecalho = next(conteudo)

#adiciona cada linha da planilha em uma lista:
    for linha in conteudo:
        info_feiras.append(linha)

#adiciona os nomes das feiras em uma tupla por concatenação
for f in info_feiras:
    tupla_feiras = tupla_feiras + (f[0],) 

#READ | ler a inscrição na feira -> iterar o dicionário e chamar as informações da feira inscrita 

def ler_inscricao(inscricao_feira):
    
    if len(inscricao_feira) == 0:
        print("\nVocê não realizou nenhuma inscrição.")
        return

    print("="*30, "INFORMAÇÕES SOBRE A INSCRIÇÃO", "="*30)
    print("As informações da sua inscrição: ")

    #laço de repetição que itera cada par chave-valor e printa na tela, gerando um formato de lista para leitura das informações cadastradas
    for k,v in inscricao_feira.items():
        print(f"{k}: {v}")

    #laço de repetição que retoma as principais informaçõoes sobre a feira inscrita -> ta no codigo acima também, acho q da pra deixar so aqui talvez
    for f in info_feiras:
        if inscricao_feira["Feira"] in f[0].strip().capitalize():
            print(f"Informações sobre sua próxima feira, {inscricao_feira["Nome"]} -> {inscricao_feira["Feira"]}: {f[1]} \\ {f[2]} \\ {f[3]} \\ {f[4]} \\ {f[5]} \\ {f[6]}")

#UPTADE | atualizar a inscrição na feira -> permite atualizar tudo ou só alguns campos.


def atualizar_inscricao(inscricao_feira):
    print("="*30, "ATUALIZAR INSCRIÇÃO", "="*30)

    #condicional para verificar se há inscrição
    if len(inscricao_feira) == 0:
        print("\nVocê não realizou nenhuma inscrição.")
        return

    while True:
        #menu que guia a opção do usuário para a atualização que deseja
        print("\nO que deseja atualizar?")
        print("1 - Feira")
        print("2 - Dados pessoais")
        print("3 - Tudo")
        try:
            opcao = int(input("Escolha o número da opção: "))
             
        except:
            print("Digite uma número válido.")
            continue
        #atualiza a feira que está inscrita
        if opcao == 1:
            print("\nFeiras disponíveis:")

            for f in tupla_feiras:
                print(f) 

            nova_feira = input("\nDigite a nova feira: ").strip().capitalize()

            #identifica se a nova feira digitada corresponde aos nomes de feira 
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

#DELETE | deletar a inscrição na feira 

def deletar_inscricao(inscricao_feira):
    print("="*30, "DELETAR INSCRIÇÃO", "="*30)

    #verificar se há inscrição 
    if len(inscricao_feira) == 0:
        print("\nNão há inscrições para deletar.")
        return
    
    confirmacao = ler_decisao("\nTem certeza que deseja deletar sua inscrição? [S/N] ")

    if confirmacao == "S":
        inscricao_feira.clear()
        print("\nInscrição deletada com sucesso!")
    else:
        print("\nOperação cancelada.")