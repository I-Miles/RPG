def fazerPocao(ervas, agua, alquimia):
    fazerPocao = lambda agua, alquimia, ervas: alquimia>=5 and agua>=3 and ervas>=6
    if fazerPocao(agua,alquimia,ervas):
        return f'Você pode preparar a poção!'
    else:
        return f'Mete o pé!'




