from time import sleep
from random import randint

def sortear(lista):
    print('=-=' * 30)
    print(f'Sortando os valores da lista, aguarde: ', end='')
    for n in range(0, 5):
        num_aleatorio = randint(0, 1000000)
        numeros.append(num_aleatorio)
        print(f'{num_aleatorio} ', end='', flush=True)
        sleep(0.5)
    print('SORTEADO COM SUCESSO')

def somaPares(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'\nA soma dos números pares de {numeros}, temos {soma}')
    print('=-=' * 30)

# PROGRAMA PRINCIPAL

numeros = []
sortear(numeros)
somaPares(numeros)