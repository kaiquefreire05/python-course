salario = float(input('Digite o valor do salário do funcionário: '))
desc_aum = int(input('Digite o valor do desconto ou do aumento: '))

aumento = salario + (salario * desc_aum / 100)
desconto = salario - (salario * desc_aum / 100)

print(f'O valor do aumento com o salário de {salario} e aumento de {desc_aum}% é {aumento:.2f}')
print(f'O valor do desconto com o salário de {salario} e com o desconto de {desc_aum}% é {desconto:.2f}')