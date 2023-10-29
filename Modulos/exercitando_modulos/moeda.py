def aumenta (preco, porcent):
    porcent = porcent / 100
    preco_final = preco + (preco * porcent)
    return preco_final


def diminuir (preco, porcent):
    porcent = porcent / 100
    preco_final = preco - (preco * porcent)
    return preco_final


def dobro(preco):
    dobro = preco * 2
    return dobro


def metade(preco):
    metade = preco / 2
    return metade
