pesos = []
for c in range(0,5):
    peso = float(input('Digite o seu peso: '))
    pesos.append(peso)

maior_valor = max(pesos)
menor_valor = min(pesos)

print(pesos)
print(f'O maior peso foi {maior_valor} KG')
print(f'O menor peso foi {menor_valor} KG')