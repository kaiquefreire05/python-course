cadastro_jogador = {}
lista_gol = []

cadastro_jogador['nome'] = str(input('Digite o nome do jogador: '))
cadastro_jogador['partidas'] = int(input('Quantas partidas o jogador jogou? '))
cadastro_jogador['total'] = 0

for c in range(0, cadastro_jogador['partidas']):
    gols = int(input(f'Digite o números de gols na partida {c}: '))
    lista_gol.append(gols)
    cadastro_jogador['total'] += gols

print('=-=' * 11)
print(cadastro_jogador)
print('=-=' * 11)
for k, v in cadastro_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-=' * 11)

print(f'O jogador {cadastro_jogador["nome"]} jogou {cadastro_jogador["partidas"]} partidas')
for g in range(0, len(lista_gol)):
    print(f'Na partida {g}, fez {lista_gol[g]} gols.')
print('=-=' * 11)