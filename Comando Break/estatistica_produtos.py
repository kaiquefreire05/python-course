print('=-=' * 20)
print('REGISTRO DE PRODUTOS')
print('=-=' * 20)

total_gasto = 0
produtos_mil = 0
contador = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))
    total_gasto += preco
    op = ' '
    contador += 1

    if preco >= 1000:
        produtos_mil += 1

    if contador == 1 or preco < menor_valor:
        menor_valor = preco
        nome_menor_valor = nome
        
    while op not in 'SN':
        op = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if op == 'N':
        break

print(f'Fim do programa')
print(f'O total gasto na compra foi R${total_gasto}')
print(f'Tem {produtos_mil} produtos custando mais de R$1000')
print(f'o produto mais barato foi {nome_menor_valor} e custou R${menor_valor}')