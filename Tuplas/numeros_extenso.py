nome_valores = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez')

while True:

    numero = int(input('Digite o valor para saber seu extenso(0 a 10): '))

    if numero <= 10:
        print(f'Você digitou o número {nome_valores[numero]}')
        break
    else:
        print('Coloque um número permitido. ', end='')