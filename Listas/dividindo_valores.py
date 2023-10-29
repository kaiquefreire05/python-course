lista_numeros = []
lista_pares = []
lista_impar = []

while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    lista_numeros.append(n)

    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impar.append(n)

    op = str(input('Quer continuar[S/N]? ')).upper()[0] # Parar ou continuar a lista
    if op not in 'S':
        break

print(f'A lista completa é {sorted(lista_numeros)}')
print(f'A lista com os números pares são {sorted(lista_pares)}')
print(f'A lista com os números ímpares são {sorted(lista_impar)}')