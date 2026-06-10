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

#função para verificar se o input é S ou N
def ler_decisao(mensagem):
    while True:
        try:
            opcao = input(mensagem).strip().upper()

            if opcao not in ("S", "N"):
                raise ValueError #cria uma excessão personalizada de ValueError

            return opcao

        except ValueError:
            print("Digite apenas [S] ou [N]")
