from random import sample

numeros_aleatorios = sample(range(0, 11), 10)

print('=-=' * 20)
print(f'Os números aleatórios são:')
print(numeros_aleatorios)
print('=-=' * 20)
print(f'O maior número é {max(numeros_aleatorios)}')
print('=-=' * 20)
print(f'O menor número é {min(numeros_aleatorios)}')
print('=-=' * 20)