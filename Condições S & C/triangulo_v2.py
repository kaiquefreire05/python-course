a = float(input('Digite o valor do primeiro seguimento: '))
b = float(input('Digite o valor do segundo seguimento: '))
c = float(input('Digite o valor do terceiro seguimento: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print(f'\nESSES VALORES PODEM FORMAR UM TRIÂNGULO')
    
    if (a == b) and (b == c):
        print(f'SEU TRIÂNGULO É EQUILÁTERO')
    elif (a == b) or (b == c) or (a == c):
        print(f'SEU TRIÂNGULO É ISÓSCELES')
    else:
        print(f'SEU TRIÂNGULO É ESCALENO')

else:
    print(f'NÃO PODE FORMAR UM TRIÂNGULO')