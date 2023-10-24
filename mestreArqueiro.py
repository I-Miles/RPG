def treinoArqueiro(flechas, habilidade, minimo):
    treinoArqueiro = lambda flechas, habilidade: flechas, habilidade
    print(f"você tem {flechas} flechas e possui {habilidade} de habilidade")

    treinoArqueiro = lambda habilidade, minimo: habilidade >= minimo
    if habilidade >= minimo:
        return f"vamos para o treinamento"
    else:
        return f"você precisa evoluir mais para o treinamento"