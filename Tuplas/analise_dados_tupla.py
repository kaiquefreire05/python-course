contador = 0 # Contador para contas os números 9
lista_numeros = [] # Criei uma lista porque não tem como adicionar valores em uma tupla
lista_pares = [] # Criei uma lista para colocar os valores pares

for n in range(0, 4): # Gerando 4 inputs
    numeros = int(input(f'Digite um número({n + 1} de 4): '))
    lista_numeros.append(numeros) # Colocando os valores do input na lista

    if numeros == 9: # Contar quantos números 9 aparecem
        contador += 1

    if numeros % 2 == 0: # Adicionando os números pares em uma lista
        lista_pares.append(numeros)

tupla_numeros = tuple(lista_numeros) # Transformando a lista em tupla 
tupla_pares = tuple(lista_pares) # Transformando a lista dos pares em tupla

print('=-=' * 20)
print(f'O número 9 apareceu {contador} vezes')

if 3 in tupla_numeros: # Verificado se existe um 3 na tupla e mostra-lo
    print(f'O número 3 foi gerador na posição {tupla_numeros.index(3)}')
else:
    print(f'O número 3 não foi gerado.')

print(f'Os números pares são: {tupla_pares}')
print('=-=' * 20)
