nome = input('Digite o seu nome completo: ').strip()

maiusculo = nome.upper()
minusculo = nome.lower()
contagem = len(nome) - nome.count(' ')
quantidade = nome.find(' ')

print(f'Seu nome em maiúsculo fica: {maiusculo}')
print(f'Seu nome em minusculo fica: {minusculo}')
print(f'Seu nome tem: {contagem} letras sem os espaços')
# print(f'Seu primeiro nome tem: {quantidade} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')