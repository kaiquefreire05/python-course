n = int(input('Digite um valor: '))
op = str(input('Quer continuar [S/N]:')).lower().strip()
media = 0
contador = 1
numeros = []

while not op =='N':
    n = int(input('Digite um valor: '))
    media += n
    numeros.append(n)
    contador += 1
    op = str(input('Quer continuar [S/N]:')).upper().strip()
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')
print(f'A média foi {media / contador}')