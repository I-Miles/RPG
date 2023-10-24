import enigmaMisterioso
def main():
    numero1 = int(input("Descubra o enigma secreto: "))
    numero2 = 12

    mensagem = enigmaMisterioso.descobrirEnigma(numero1,numero2)
    print(mensagem)
main()
