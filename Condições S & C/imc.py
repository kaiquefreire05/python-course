print('=-=' * 25)
peso = float(input('Digite aqui seu peso: '))
altura = float(input('Digite aqui sua altura: '))
print('=-=' * 25)

imc = peso / (altura * 2)

print(f'\nSeu IMC é {imc}')

if imc < 18.5:
    print(f'Você está abaixo do peso.')

elif imc < 25:
    print(f'Você está no peso ideal.')

elif imc < 30:
    print(f'Você está com sobrepeso.')

elif imc < 40:
    print(f'Você está com obesidade.')

else:
    print('Você está com obesidade mórbida!!!!')
