def linha():
    print('-' * 20)

def area(l, c):
    a = l * c
    print(f'LARGURA(M): {l}')
    print(f'COMPRIMENTO(M): {c}')
    print(f'A área de um terreno {l} x {c} é {a}m²')

l = float(input('Digite a largura do terreno(m): '))
c = float(input('Digite o comprimento do terreno(m): '))

linha()
print('CONTROLE DE TERRENOS')
linha()
area(l, c)
linha()