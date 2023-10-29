print('=-=' * 20)
salario = float(input('Digite o valor do sálario para calcular o aumento: '))
print('=-=' * 20)

if salario > 1250.00:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100

print(f'O valor do seu aumento é de R${aumento}')
print(f'O valor do seu salario passará a ser R${salario + aumento}')