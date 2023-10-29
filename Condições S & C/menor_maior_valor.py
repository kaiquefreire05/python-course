v1 = int(input('Digite o primeio valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v1 < v2 and v1 < v3:
    print(f'O menor valor é {v1}')
elif v2 < v1 and v2 < v3:
    print(f'O menor valor é {v2}')
else:
    print(f'O menor valor é {v3}')

if v1 > v2 and v1 > v3:
    print(f'O maior valor é {v1}')
elif v2 > v1 and v2 > v3:
    print(f'O maior valor é {v2}')
else:
    print(f'O maior valor é {v3}')