numeros = []

while True:
    valor = int(input('Digite um valor para adicionar na lista: '))
    numeros.append(valor)
    op = str(input('Quer continuar [S/N]? ')).upper()[0]
    if op not in 'S':
        break
numeros.sort(reverse=True)

print('=-=' * 20)
print(f'Nesta lista contém {len(numeros)} elementos.')
print(f'Os valores da lista em ordem decrescente são: {numeros}')

if 5 in numeros:
    print(f'O número 5 está inserido nesta lista.')
else:
    print(f'O número 5 não está inserido nesta lista.')
print('=-=' * 20)
