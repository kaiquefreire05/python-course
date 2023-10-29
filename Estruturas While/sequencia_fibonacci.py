n = int(input("Que termo deseja encontrar: "))

t1 = 0
t2 = 1
t3 = t1 + t2
contador = 3
print(f'{t1} -> {t2} -> ', end='')

while contador <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' ->')
    t1 = t2
    t2 = t3
    contador +=1
print('FIM')