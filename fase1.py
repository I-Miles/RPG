import forjarElfica
def main():
    nome = input("Qual o seu nome guerreiro? ")
    nivel = int(input("Me diga o seu nével guerreiro: "))
    magia = int(input("A sua quantidade de magia é alta o suficiente?\nMe mostre: "))

    mensagem = forjarElfica.forjarEspada(nome, nivel, magia)
    print(mensagem)

main()
