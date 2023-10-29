pessoa = {}

pessoa['nome'] = str(input('Digite o nome: '))
pessoa['media'] = int(input('Digite a média: '))

if pessoa['media'] >= 6:
    pessoa['situacao'] = 'Aprovado'
else:
    pessoa['situacao'] = 'Reprovado'

print('=-=' * 10)
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')
print('=-=' * 10)
    