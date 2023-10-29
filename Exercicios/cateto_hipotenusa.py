from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(ca, co)

print(f'O valor da hipotenusa é {hi:.2f}')