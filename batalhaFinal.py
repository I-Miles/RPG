import random
global AzureVida, AzureMagia, AzureDefesa, AzureArco, AzurePoção, AzureAtaque, rvida, ReiDefesa, ReiMagia, ReiAtaque, defesaUsada, magiaUsada, qtdMagia, curaPocao, dificil, ataqueArco
AzureVida = random.randint(30, 50)
AzureAtaque = random.randint(10, 15)
AzureDefesa = random.randint(10, 15)
AzureMagia = random.randint(8, 10)
curaPocao = random.randint(1, 20)
ataqueArco = random.randint(2, 15)
AzurePoção = 1
AzureArco = 1
defesaUsada = 0
qtdMagia = 1
magiaUsada = False
# rei stats
ReiVida = random.randint(40,60)
ReiAtaque = random.randint(5, 10)
ReiDefesa = random.randint(10, 15)
ReiMagia = random.randint(8, 10)

def ataqueRei():
    global AzureVida, AzureMagia, AzureDefesa, AzureArco, AzurePoção, AzureAtaque, ReiVida, ReiDefesa, ReiMagia, ReiAtaque
    escolhaRei = random.randint(1, 3)
    if escolhaRei == 1:
        if AzureDefesa <= 0:
            AzureVida = AzureVida - ReiAtaque - AzureDefesa
            AzureDefesa = 0
            print(f"O rei atacou, o dano pegou na sua vida. Sua vida restante: {AzureVida}")
        else:
            AzureDefesa = AzureDefesa - ReiAtaque
            print(f"O rei atacou, o dano pegou na sua defesa. Sua defesa restante: {AzureDefesa}")
    if escolhaRei == 2:
        ReiDefesa +=2
        print(f"O rei se defendeu. Defesa total do rei: {ReiDefesa}")
    if escolhaRei == 3:
        if AzureDefesa <= 0:
            AzureVida = AzureVida - ReiMagia - AzureDefesa
            AzureDefesa = 0
            print(f"O rei atacou, o dano pegou na sua vida. Sua vida restante: {AzureVida}")
        else:
            AzureDefesa = AzureDefesa - ReiMagia
            print(f"O rei atacou, o dano pegou na sua defesa. Sua defesa restante: {AzureDefesa}")
def batalha():
    global AzureVida, AzureMagia, AzureDefesa, AzureArco, AzurePoção, AzureAtaque, ReiVida, ReiDefesa, ReiMagia, ReiAtaque, defesaUsada, magiaUsada, qtdMagia, curaPocao
    while True:
        print("Escolha uma das ações abaixo (1 a 6): ")
        print("1- Atacar o rei \n2- Defender-se(max: 2, Usado: %d) \n3- Usar magia(Dísponivel: %d) \n4- Se curar(Poções: %d) \n5- Usar arco e flecha(flechas: %d)\n6- Checar suas estatísticas" % (defesaUsada, qtdMagia, AzurePoção, AzureArco))
        escolha = int(input("Você irá: "))
        if escolha == 1:
            if ReiDefesa <= 0:
                ReiVida = ReiVida - AzureAtaque - ReiDefesa
                ReiDefesa = 0
                print(f"Você atacou, o dano pegou na vida do rei. Vida do rei restante: {ReiVida}")
                if ReiVida > 0:
                    ataqueRei()
                else:
                    break
            else:
                ReiDefesa = ReiDefesa - AzureAtaque
                print(f"Você atacou, o dano pegou na defesa do rei. Defesa do rei restante: {ReiDefesa}")
                if ReiVida > 0:
                    ataqueRei()
                else:
                    break
        if escolha == 2:
            if defesaUsada < 2:
                AzureDefesa += 2
                defesaUsada += 1
                print(f"Defesa total: {AzureDefesa}")
                ataqueRei()
            else:
                print("Você já usou o máximo de defesas.")
                ataqueRei()
        if escolha == 3:
            if magiaUsada == False:
                if ReiDefesa <= 0:
                    ReiVida = ReiVida - AzureMagia - ReiDefesa
                    ReiDefesa = 0
                    magiaUsada = True
                    qtdMagia -= 1
                    print(f"Você atacou, o dano pegou na vida do rei. Vida do rei restante: {ReiVida}")
                    if ReiVida > 0:
                        ataqueRei()
                    else:
                        break
                else:
                    ReiDefesa = ReiDefesa - AzureMagia
                    print(f"Você atacou, o dano pegou na defesa do rei. Defesa do rei restante: {ReiDefesa}")
                    magiaUsada = True
                    qtdMagia -= 1
                    if ReiVida > 0:
                        ataqueRei()
                    else:
                        break
            if magiaUsada == True:
                print("Você já usou o máximo de magia.")
        if escolha == 4:
            if AzurePoção > 0:
                AzureVida = AzureVida + curaPocao
                AzurePoção = 0
                print(f"Você utilizou a cura. Sua vida total foi para: {AzureVida}")
                ataqueRei()
            else:
                print("Acabou a poção.")
        if escolha == 5:
            if AzureArco >= 1:
                if ReiDefesa <= 0:
                    ReiVida = ReiVida - ataqueArco - ReiDefesa
                    ReiDefesa = 0
                    print(f"Você atacou, o dano pegou na vida do rei. Vida do rei restante: {ReiVida}")
                    if ReiVida > 0:
                        ataqueRei()
                    else:
                        break
                else:
                    ReiDefesa = ReiDefesa - ataqueArco
                    print(f"Você atacou, o dano pegou na defesa do rei. Defesa do rei restante: {ReiDefesa}")
                    if ReiVida > 0:
                        ataqueRei()
                    else:
                        break
        if escolha == 6:
            print(f"Sua vida: '{AzureVida}', sua defesa: '{AzureDefesa}', seu poder de ataque: '{AzureAtaque}' e seu poder de magia '{AzureMagia}'")
    if AzureVida <= 0:
        print("Você perdeu.")
        print("Obrigado por jogar.")
    else:
        print("Você GANHOU!!")
batalha()