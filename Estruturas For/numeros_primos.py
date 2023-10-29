numero = int(input(f'\nDigite um valor para descobrir se ele é primo: '))

contagem_divisao = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        contagem_divisao += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c} ', end=' ')

print(f'\nO número {numero} foi dividido {contagem_divisao} vezes.')
if contagem_divisao == 2:
    print(f'Ele é primo')
else:
    print(f'Não é primo')
