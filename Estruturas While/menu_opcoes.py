from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

print('''Menu de opções: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
opcao = 0
lista_numeros = []

while opcao != 5:
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        print(f'A soma entre {v1} e {v2} é {v1 + v2}')
        print('=-=' * 20)
    elif opcao == 2:
        print(f'A multiplicação entre {v1} e {v2} é {v1 * v2}')
        print('=-=' * 20)
    elif opcao == 3:
        lista_numeros.append(v1)
        lista_numeros.append(v2)
        print(f'O maior número é {max(lista_numeros)}')
        print('=-=' * 20)
    elif opcao == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('=-=' * 20)
    elif opcao == 5:
        print(f'Finalizando...')
    else:
        print(f'Opção inválida')    
sleep(1)
print(f'Finalizado, volte sempre!')
print('=-=' * 20)     