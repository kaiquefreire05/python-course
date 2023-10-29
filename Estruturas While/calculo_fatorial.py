fatorial = int(input('Digite o número para descobrir seu fatorial: '))
f = 1
c = fatorial
print(f'Calculando {fatorial}! = ', end= '')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= fatorial
    c -= 1
print(f'{f}')