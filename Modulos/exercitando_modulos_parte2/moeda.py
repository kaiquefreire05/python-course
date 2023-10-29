def aumenta (preco = 0, porcent = 0):
    porcent = porcent / 100
    preco_final = preco + (preco * porcent)
    return preco_final

def diminuir (preco = 0, porcent = 0):
    porcent = porcent / 100
    preco_final = preco - (preco * porcent)
    return preco_final

def dobro(preco = 0):
    dobro = preco * 2
    return dobro

def metade(preco = 0):
    metade = preco / 2
    return metade

def formatar(preco = 0 ,moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.', ',')