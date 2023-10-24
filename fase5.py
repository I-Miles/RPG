import mestreArqueiro
def main():
    habilidade = int(input("qual seu nivel de habilidade: "))
    flechas = int(input("qual o nivel de flechas "))
    minimo = 27

    mensagem = mestreArqueiro.treinoArqueiro(habilidade, flechas, minimo )
    print(mensagem)
main()
