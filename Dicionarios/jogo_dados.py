from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []

sleep(1)
print('Números sorteados:')
print('=-=' * 11)
sleep(2)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-=' * 11)

print('  === RANKING DOS JOGADORES ===   ')
sleep(2)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
sleep(1)
print('=-=' * 11)
