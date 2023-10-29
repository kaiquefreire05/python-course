valores_lista = []

while True:
    valor = int(input('Digite um valor para adicionar na lista: '))

    if valor not in valores_lista:
        valores_lista.append(valor)
    else:
        print('Valor repetido! Não vou adicionar...')

    opcao = str(input('Quer continuar[S/N]? ')).strip()[0]

    if opcao in 'Nn':
        print('Programa encerrado!')
        break
print(f'A lista em ordem numérica é {sorted(valores_lista)}')