def linha():
    print('~' * 35)

def contador(i, f, p):
    # CONTADOR

    if i > f:
        p = -p

    for c in range(i, f, p):
        print(c, end=' ')

    if f > i:
        print(f)
    elif f < 0:
        print(f)
    else:
        print(0)

# PROGRAMA PRINCIPAL

linha()
contador(1, 10 , 1)
linha()
contador(10, 0, 2)
linha()
print('Contador personalizado.')
i = int(input('Agora você escolhe. Digite o início: '))
f = int(input('Agora você escolhe. Digite o fim: '))
p = int(input('Agora você escolhe. Digite o passo: '))
contador(i, f, p)
linha()

