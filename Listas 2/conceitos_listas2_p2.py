pessoas = []
dados_adicionar = []
totmaior = totmenor = 0

for c in range(0, 3):
    dados_adicionar.append(str(input('Digite seu nome: ')))
    dados_adicionar.append(int(input('Digite sua idade: ')))
    pessoas.append(dados_adicionar[:])
    dados_adicionar.clear()


for p in pessoas:
    if p[1] >= 18:
        print(f'\n{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'\n{p[0]} é menor de idade.')
        totmenor += 1

print(f'\n{totmaior} pessoas são maiores de idade, {totmenor} são menores de idade.')