from time import sleep
from random import randint
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogada = int(input('\nQual a sua opção? '))

escolha_pc = randint(0 , 2)

sleep(1)
print('\nJO!')
sleep(1)
print('KEN!')
sleep(1)
print('PÔ!')

print('=-=' * 20)
print(f'O computador jogou: {escolha_pc}')
print(f'Você jogou: {jogada}')
print('=-=' * 20)

if escolha_pc == 0: # PEDRA

    if jogada == 0:
        print(f'\nEMPATE')
    elif jogada == 1:
        print(f'\nVITÓRIA')
    elif jogada == 2:
        print(f'\nDERROTA')
    else:
        print(f'\nJOGADA INVÁLIDA')

elif escolha_pc == 1: # PAPEL
    if jogada == 0:
        print(f'\nDERROTA')
    elif jogada == 1:
        print(f'\nEMPATE')
    elif jogada == 2:
        print(f'\nVITÓRIA')
    else:
        print(f'\nJOGADA INVÁLIDA')

elif escolha_pc == 2: # TESOURA
    if jogada == 0:
        print(f'\nVITÓRIA')
    elif jogada == 1:
        print(f'\nDERROTA')
    elif jogada == 2:
        print('\nEMPATE')
    else:
        print(f'\nJOGADA INVÁLIDA')
