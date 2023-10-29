largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

tinta = area / 2

print(f'Sua parede tem a dimensão de {largura} x {altura}, sua área é de {area}m²')
print(f'Voçê precisa de {tinta} litros de tinta para pintar a parede por completo')