def soma(a, b): # Criando uma função para somar sem fazer um código extenso
    s = a + b
    print(f'A= {a}  B= {b}')
    print(f'A soma de A + B = {s}')
    print()

def contador(* num):
    print(num)
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

    tam = len(num)
    print(f'Recebi os valores {num}, e em quantidade tem {tam} números.')


# Prgrama principal 1
soma(1, 5)
soma(a=10, b=20)
soma(b=335356, a=20495)

#Programa principal 2
contador(8, 0, 1)
contador(12, 55, 33, 22)