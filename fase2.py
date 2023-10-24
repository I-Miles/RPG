import criarPocao
def main():
    ervas = int(input("Digite sua quantidade de ervas: "))
    agua = int(input("Digite sua quantidade de água: "))
    alquimia = int(input("A sua quantidade de alquimia é alta o suficiente?\nMe mostre: "))

    mensagem = criarPocao.fazerPocao(agua, alquimia, ervas)
    print(mensagem)

main()
