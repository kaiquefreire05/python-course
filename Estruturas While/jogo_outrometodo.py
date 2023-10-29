from random import randint
print(f'Sou seu computador...')
print(f'Pensei em um número entre 0 a 10')
print(f'Tente adivinhar...')

acertou = False
contagem_tentativas = 0
numero_aleatorio = randint(0, 10)

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    contagem_tentativas += 1
    if jogador == numero_aleatorio:
        acertou = True
    else:
        if numero_aleatorio > jogador:
            print(f'Menos...')
        else:
            print(f'Mais...')
            
print(f'Parabéns, você acertou com com {contagem_tentativas} tentativas.') 