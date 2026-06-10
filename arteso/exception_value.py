#função para verificar números inteiros
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")

#função para verificar números reais
def ler_real(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número Real válido.")

def ler_decisao (mensagem):
     while True:
        try:
            opcao = input(mensagem).strip().capitalize()
            return opcao
        except opcao !="S" and opcao!="N":
            print("Digite apenas [S] ou [N]")