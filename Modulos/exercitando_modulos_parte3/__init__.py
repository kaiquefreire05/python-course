from Modulos.exercitando_modulos_parte3 import moeda


preco = float(input('Digite o preço: '))

print(f'Com aumento {moeda.formatar(preco)} passa a ser {moeda.aumenta(preco, 10, True)}')
print(f'Com a diminuição {moeda.formatar(preco)} passa a ser {moeda.diminuir(preco, 10, True)}')
print(f'O dobro de {moeda.formatar(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.formatar(preco)} é {moeda.metade(preco, True)}')