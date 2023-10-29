lista_jogadores = [] # Lista principal
jogador = {} # Dicionário que armazena os jogadores
lista_gols = [] # Lista que é copiada para armazenar os gols

while True:
    jogador.clear() # Limpa o dicionário para começar um novo
    jogador['nome'] = str(input('Digite o nome do jogador: ')) # INPUT
    qtde_partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? ')) # INPUT

    for p in range(0, qtde_partidas): # Conforme a quantidade de partidas vai ser perguntado os gols por partida
        gols = int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida {p}? '))
        lista_gols.append(gols) # Cada gol vai ser adicionado nessa lista
        jogador['gols'] = lista_gols[:]  # Uma copia da lista para o dicionário

    lista_gols.clear() # Limpando a lista
    lista_jogadores.append(jogador.copy()) # Adicionando o dicionário na lista

    while True:
        op = str(input('Quer adicionar outro[S/N]? ')).strip().upper()[0]
        if op in 'SN':
            break
        else:
            print('Comando inválido. Digite novamente...')           
    if op == 'N':
        break

# Fazendo o topo da tabela com cod, nome e etc.
print('=-=' * 15)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<16}', end='')
print()

print('---' * 15)
for k, v in enumerate(lista_jogadores): # Key e value da lista de jogadores
    print(f'{k:>3}  ', end='') # Printando as keys frente a frente
    for d in v.values(): # Printando apenas os valores
        print(f'{str(d):<15} ', end='')
    print()
print('---' * 15)

while True:
    dados = int(input('Digite o número para fazer o levantamento do jogador:[999 encerra] '))

    if dados == 999: # 999 quebra a execução
        break

    if len(lista_jogadores) < dados: # Se tiver menos valores vai printar esse código
        print('Não existe jogador com o valor {op}. Tente novamente...')
    else:
        print(f' --- Levantamento do jogador {lista_jogadores[dados]["nome"]}: --- ')
        for i, g in enumerate(lista_jogadores[dados]['gols']):
            print(f'No jogo {i} marcou {g} gols.')
    print('---' * 15)
print('<<< VOLTE SEMPRE >>>')
    