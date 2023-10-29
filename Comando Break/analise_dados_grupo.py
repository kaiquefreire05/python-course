print('=-=' * 20)
print('CADASTRO DE PESSOAS')
print('=-=' * 20)

pessoas_mais18 = 0
homem_cadastrados = 0
mulheres_menos20 = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
    op = ' '
    while op not in 'SN':
        print('=-=' * 20)
        op = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        print('=-=' * 20)
    if sexo == 'F' and idade <= 20:
        mulheres_menos20 += 1
    if sexo == 'M':
        homem_cadastrados += 1
    if idade >= 18:
        pessoas_mais18 += 1
    if op == 'N':
        break 
print('=-=' * 20)
print(f'O total de pessoas com mais de 18 foi {pessoas_mais18}')
print(f'O total de homens cadastrados foi {homem_cadastrados}')
print(f'Tem {mulheres_menos20} mulheres com menos de 20 anos')
print('=-=' * 20)