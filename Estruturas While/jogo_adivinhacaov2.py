from random import randint
contagem_tentativas = 1
numero_aleatorio = randint(0, 10)

print(f'Sou seu computador...')
print(f'Pensei em um número entre 0 a 10')
print(f'Tente adivinhar...')
numero = int(input('Qual seu palpite? '))

while numero != numero_aleatorio:
    contagem_tentativas += 1
    if numero_aleatorio > numero:
        print(f'Mais...')
    else:
        print(f'Menos...')
    numero = int(input('Qual seu palpite? '))

print(f'Parabéns, você acertou com com {contagem_tentativas} tentativas.')    
