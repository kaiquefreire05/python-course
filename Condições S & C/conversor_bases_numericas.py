valor = int(input('Digite o valor para ser convertido: '))

print('''São três opções:
1° opção: Base binário
2° opção: Base octal
3° opção: Base hexadecimal 
''')

opcao = int(input('Digite a opção desejada(1 a 3): '))

if opcao == 1:
    binario = format(valor, 'b')
    print(f'\nO valor {valor} covertido para binário é {binario}')

elif opcao == 2:
    octal = format(valor, 'o')
    print(f'\nO valor {valor} covertido para octadecimal é {octal}')

elif opcao == 3:
    hexa = format(valor, 'x')
    print(f'\nO valor {valor} covertido para hexadecimal é {hexa}')

else:
    print('\nOpção inválida')