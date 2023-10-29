valores = []

for cont in range (0, 5):
    valores.append(int(input('Digite um valor para ser adicionado a lista: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final do código')

# A linguagem Python cria uma ligação entre listas, então se eu quiser mudar o valor da lista b sem interferir na a tem que ser assim:

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Todos os valores da lista A: {a}')
print(f'Todos os valores da lista B: {b}')