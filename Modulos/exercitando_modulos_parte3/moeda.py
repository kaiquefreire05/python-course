def aumenta (preco = 0, porcent = 0, format=False):
    porcent = porcent / 100
    preco_final = preco + (preco * porcent)
    return preco_final if format is False else formatar(preco_final)

def diminuir (preco = 0, porcent = 0, format=False):
    porcent = porcent / 100
    preco_final = preco - (preco * porcent)
    return preco_final if format is False else formatar(preco_final)

def dobro(preco = 0, format=False):
    dobro = preco * 2
    return dobro if not format else formatar(dobro)

def metade(preco = 0, format=False):
    metade = preco / 2
    return metade if not format else formatar(metade)

def formatar(preco = 0 ,moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.', ',')


