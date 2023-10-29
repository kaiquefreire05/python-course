from random import randint
print('=-=' * 20)
print('PAR OU ÍMPAR')
print('=-=' * 20)
contador = 0

while True:
    v = int(input('Digite um número: '))
    v_aleatorio = randint(1, 100)
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print('=-=' * 20)
    print(f'Você jogou {v} e o computador jogou {v_aleatorio}')
    print('=-=' * 20)

    if tipo == 'P':
        if v and v_aleatorio % 2 == 0:
            print(f'Vitória')
            contador += 1
        else:
            print(f'Derrota')
            break
    elif tipo == 'I':
        if v and v_aleatorio % 2 == 1:
            print(f'Vitória')
            contador += 1
        else:
            print(f'Derrota')
            break
print(f'Você perdeu mas ganhou {contador} vezes')

