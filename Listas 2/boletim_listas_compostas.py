boletim = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    op = str(input('Quer continuar[S/N]? ')).strip().upper()[0]

    if 'N' in op:
        break

print(f'{"N°":<4}{"Nome":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, n in enumerate(boletim):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
print('-' * 30)

while True:

    opcao = int(input('Quer ver a nota de qual aluno?[999 INTERROMPE]'))
    if opcao == 999:
        print('FINALIZANDO...')
        break

    if opcao <= len(boletim) - 1:
        print(f'As notas de {boletim[opcao][0]} foram: {boletim[opcao][1]}')

