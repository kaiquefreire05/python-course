km = float(input('Digite a quantidade de quilômetros percorrido(KM): '))
dias = int(input('Digite a quantidade de dias usados: '))

preco_km = km * 0.15 # 15 CENTAVOS POR KM ANDADO
preco_dias = dias * 60 # 60 REAIS POR DIA USADO

print(f'O valor do aluguel é de {preco_km + preco_dias}')