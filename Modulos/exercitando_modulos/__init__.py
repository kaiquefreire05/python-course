from Modulos.exercitando_modulos import moeda

p = int(input('Digite o preço: '))

print(f'Com aumento {p} passa a ser {moeda.aumenta(p, 10)}')
print(f'Com a diminuição {p} passa a ser {moeda.diminuir(p, 10)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')