sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] # Strip tira os espaços, upper coloca em maiúsculo e [0] pega apenas a primeira letra.

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite corretamente: ')).strip().upper()[0]
print(f'Obrigado, sexo {sexo} registrado.')