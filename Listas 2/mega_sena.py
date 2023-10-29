from random import randint # Gerar valores inteiros aleatórios
from time import sleep # Usar o delay de 1 segundo

jogos = []

print('=' * 30)
print()
print(f'       SORTEIO MEGA-SENA            ')
print()
print('=' * 30)

numero_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'======== Sorteando {numero_jogos} jogos, aguarde... ========')

for j in range(numero_jogos): # Essa linha mostra quantas jogos vão ser gerados
    jogo_temp = []  # Essa vai ser uma lista tenmporária 
    for l in range(6): # Por padrão os jogos são de 6 números, então será sorteado 6
        numeros = randint(0, 99) # Vai gerar o número
        if numero_jogos not in jogo_temp: # Só vai adicionar números diferente nesse jogo
            jogo_temp.append(numeros) # Vai adicionar na lista temporaria
    jogos.append(jogo_temp[:]) # Vai copiar para a lista principal

for j in range(numero_jogos): # Vai simplesmente mostrar os jogos gerados.
        sleep(1)
        print(f'Jogo {j + 1}: [{jogos[j]}]')
print()