preco = float(input('Digite o preço do produto(R$): '))
desconto = int(input('Digite aqui a porcentagem do desconto: '))

porcent_desconto = desconto / 100

desconto_final = preco * porcent_desconto

# novo = preco - (preco * desconto / 100) ESSA FORMA É MAIS SIMPLES E ECONOMIZA MEMÓRIA

print(f'O seu produto com o valor de {preco}, com {desconto}% de desconto vai custar {preco - desconto_final:.2f} R$')