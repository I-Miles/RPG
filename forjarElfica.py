def forjarEspada(nome, nivel, magia):
    forjarElfica = lambda nivel, magia: nivel>=20 and magia >=250
    if forjarElfica(nivel,magia):
        return f'Cavaleiro {nome}, você pode tomar no seu cu!'
    else:
        return f'Cavaleiro {nome}, você é noob!'




