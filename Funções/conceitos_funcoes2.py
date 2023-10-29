def dobra_valores(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


valores = [2, 1, 6, 5, 7, 9, 11]
dobra_valores(valores)
print(valores)