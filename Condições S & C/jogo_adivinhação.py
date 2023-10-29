from random import randint
from time import sleep

aleatorio = randint(0, 5)

print('-=-' * 20)
print(f'Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-' * 20)

tentativa = int(input('\nEm que número eu pensei? '))
print(f'\nPROCESSANDO...')
sleep(3)


if tentativa > 5:
    print(f'\nEsse número não se encaixa...')

else:

    if tentativa == aleatorio:
        print(f'\nPARABENS!! Você conseguiu me vencer!')
    else:
        print(f'\nVocê errou! Tente novamente...')