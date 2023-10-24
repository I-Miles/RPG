import cofreEncantado
def main():
    numero1 = int(input("Descubra o número secreto: "))
    numero2 = 12

    mensagem = cofreEncantado.cofreMIsterioso(numero1,numero2)
    print(mensagem)
main()
