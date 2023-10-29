pessoas = {'nome': 'Kaíque', 'sexo': 'M', 'idade': 22}

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# print(pessoas.keys())

# print(pessoas.values())

# print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

# del pessoas['sexo']

pessoas['nome'] = 'Felipe'
pessoas['peso'] = 78.5