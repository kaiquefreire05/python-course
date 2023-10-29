inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor final: '))

for c in range(inicio, fim + 1):
    if c % 2 == 0:
        print(c, end=' ')
print(f'\nAcabou')

for c in range(inicio, fim + 1, 2): # só funciona se o começo for == 0.
    print('.', end=' ')
    print(c, end=' ')
print(f'\nAcabou')