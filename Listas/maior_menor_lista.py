valores = []

for val in range(0, 5):
    valores.append(int(input(f'Digite o valor que vai na posição {val}: ')))

print('=-=' * 20)

print(f'Você digitou valores {valores}')

maior_valor = max(valores)

posicoes_maior = [i for i, x in enumerate(valores) if x == maior_valor] # Código para descobrir as posições reptidas
# do maior, código muito versátil

menor_valor = min(valores)

posicoes_menor = [i for i, x in enumerate(valores) if x == menor_valor] # Código para descobrir as posições reptidas
# do menor, código muito versátil


print(f'O maior valor foi {maior_valor} e ele aparece nas posições: {posicoes_maior}')
print(f'O menor valor da lista foi {menor_valor} e ele aparce nas posições {posicoes_menor}')
