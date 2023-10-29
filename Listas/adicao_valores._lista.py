valores = []
opcao = ''

print('=-=' * 20)
print('Programa de inserção na lista')
print('=-=' * 20)

while True:
    valor = int(input('Digite o valor para adicionar na lista: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido! Não vou adicionar...')

    opcao = str(input('Quer continuar[S/N]? ')).upper().strip()
    if opcao in 'Nn':
        break

print('=-=' * 20)
print(f'Os valores adicionados foram {valores}')
print('=-=' * 20)