from Modulos.exercitando_modulos_parte2 import moeda

preco = float(input('Digite o preço: '))

print(f'Com aumento {moeda.formatar(preco)} passa a ser {moeda.formatar(moeda.aumenta(preco, 10))}')
print(f'Com a diminuição {moeda.formatar(preco)} passa a ser {moeda.formatar(moeda.diminuir(preco, 10))}')
print(f'O dobro de {moeda.formatar(preco)} é {moeda.formatar(moeda.dobro(preco))}')
print(f'A metade de {moeda.formatar(preco)} é {moeda.formatar(moeda.metade(preco))}')