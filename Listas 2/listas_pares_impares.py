numeros = [[], []]

for n in range(0, 8):
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(numeros)