def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol/s no campeonato.')


# Programa principal

nome = str(input('Digite seu nome: '))
gols = str(input('Digite quantos gols você fez: ')) # Coloquei como string para analisar depois.

if gols.isnumeric(): # Se o gol tiver número essa string vai virar int.
    gols = int(gols)
else: # Senão vai ser igual a 0
    g = 0
if nome.strip() == '': # Se o nome com os espaços retirados não tiver nada vai exibir a mensagem abaixo
    print('<desconhecido>')
else: # Depois disso tudo vai chamar a função.
    ficha(nome, gols)
