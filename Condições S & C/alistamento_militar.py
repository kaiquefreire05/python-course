
print('=-=' * 20)
ano = int(input('Digite seu ano de nascimento: '))
print('=-=' * 20)

idade = 2023 - ano

if idade <= 17:
    print(f'Você ainda não precisa fazer o alistamento')
    print(f'Faltam {18 - idade} anos aos para o alistamento')

elif idade >= 19:
    print(f'Você ja deveria ter se alistado a {idade - 18} anos')
    print(f'Seu alistamento foi em {2023 - (idade - 18)}')

else:
    print(f'Você ja tem 18, procure o quartel imediatamente!!!')
