matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_total = 0

for c in range(0, 3): # Adicionei os números na lista
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite o valor para a coluna [{c} e {l}]: '))

print('=-=' * 30)

for c in range(0, 3): # Printei em formato de matriz
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()

print('=-=' * 30)

for varrer_lista in matriz: # Pegando a soma total de todos os valores da matriz
    soma_total += sum(varrer_lista)
print(f'O valor da soma de todos os valores é {soma_total}')

segunda_linha = matriz[1] # Pegando o maior valor da segunda lista, para isso copiei apenas a segunda linha.
print(f'O maior valor da segunda linha é {max(segunda_linha)}')

terceira_linha = matriz[2] # Estou pegando a soma da terceira linha, copiei apenas a terceira linha e depos usei o comando sum()

soma_terceira_linha = sum(terceira_linha)

print(f'A soma de todos os valores da terceira linha é {soma_terceira_linha}')


