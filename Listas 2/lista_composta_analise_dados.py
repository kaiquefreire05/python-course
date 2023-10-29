dados = []
pessoas = []

while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    dados.clear()

    op = str(input('Quer adicionar mais?[S/N]? ')).strip().upper()[0]

    if op == 'N':
        break

print(f'O número de pessoas cadastradas foram {len(pessoas)}.')

maior_peso = float('-inf') # Essa variável vai ter o menor valor possível, para não ocorrer erro.
menor_peso = float('inf') # Essa variável vai ter o maior valor possível, para não ocorrer erro.
nomes_maior_peso = []
nomes_menor_peso = []

for nome, peso in pessoas:
    # Maior peso

    if peso > maior_peso:
        maior_peso = peso
        nomes_maior_peso = [nome] # Vai apenas atualizar, não vai adicionar, só vai adicionar quando o elif for true.
    elif peso == maior_peso:
        nomes_maior_peso.append(nome)
    
    # Menor peso

    if peso < menor_peso:
        menor_peso = peso
        nomes_menor_peso = [nome]
    elif peso == menor_peso:
        nomes_menor_peso.append(nome)

print(f'O maior peso é {maior_peso}, e o/s nome/s são: {nomes_maior_peso}')
print(f'O menor peso é {menor_peso}, e o/s nome/s são: {nomes_menor_peso}')
