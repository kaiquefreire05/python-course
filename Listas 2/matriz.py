matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3): # Serve para colocar os valores na matriz
    for p in range(0, 3):
        matriz[l][p] = int(input(f'Digite um valor para [{l} e {p}]: '))

for l in range(0, 3): # Serve para formatar e mostrar os valores na matriz
    for p in range(0, 3):
        print(f'[{matriz[l][p]:^5}]', end= '')
    print()