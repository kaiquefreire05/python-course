ano = int(input('Digite seu ano de nascimento: '))

idade = 2023 - ano

if idade <= 9:
    print(f'\nSua categoria é MIRIM')

elif idade <= 14:
    print(f'\nSua categoria é INFANTIL')

elif idade <= 19:
    print(f'\nSua categoria é JÚNIOR')

elif idade <= 25:
    print(f'\nSua categoria é SÊNIOR')

else:
    print(f'\nSua categoria é MASTER')