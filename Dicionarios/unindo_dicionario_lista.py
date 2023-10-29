pessoa = {}
cadastradas = []
soma_idade = 0 

while True:
    pessoa.clear() # Limpar o dicionario para começar um novo
    pessoa['nome'] = str(input('Digite o nome: '))

    while True: # Enquanto for verdadeiro não vai deixae de perguntar o gênero
        pessoa['sexo'] = str(input('Digite seu genêro[F/M]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Inválido. Tente novamente...')

    pessoa['idade'] = int(input('Digite aqui a idade: ')) # Adicionado a idade
    soma_idade += pessoa['idade'] # Uma variável que vai receber a soma das idades
    cadastradas.append(pessoa.copy()) # Fazendo uma cópia do dicionario e adicionado na lista
    
    while True: # Fazendo a parte que pergunta se vai continuar
        op = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        if op in 'SN':
            break
        else:
            print('Inválido. Tente novamente...')

    if op == 'N': # Se a resposta for 'N' vai quebrar o código
        break

print('=-=' * 20)
print(f'Foram cadastradas {len(cadastradas)} pessoas.')
print(f'A média de idade é {soma_idade / len(cadastradas)} anos.')

print(f'As mulheres cadastradas são: ', end='') # Código para mostrar o nome das mulheres cadastradas
for p in cadastradas: 
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
    print()

for m in cadastradas: # Mostrar quem está acima da média 
    if m['idade'] >= (soma_idade / len(cadastradas)):
        for k, v in m.items():
            print(f'{k} = {v}; ', end='')
        print()