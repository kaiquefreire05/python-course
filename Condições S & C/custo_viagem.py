distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f'O valor da sua passagem será de R$ {valor:.2f}')