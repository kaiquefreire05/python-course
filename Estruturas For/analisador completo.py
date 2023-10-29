soma_idades = 0 # Criei esta variável para coletar a soma das idades
contagem_mulheres20 = 0 # Variável para as mulheres com menos de 20 anos
homem_mvelho = '' # Variável para colocar o nome do homem mais velho
idade_hvelho = 0 # Variável para colocar a idade do homem mais velho

for p in range(1, 5): # Coloquei os inputs e as somas das idades
    print(f'=-=-=-=-=-=-=-= {p}/ª pessoa =-=-=-=-=-=-=-=')
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite aqui sua idade: '))
    sexo = str(input('Digite aqui seu sexo: ')).strip()
    soma_idades += idade

    if p == 1 and sexo in 'Mm': # Essa primeira parte coloca o primero nome e idade na variável do homem mais velho.
        idade_hvelho = idade
        homem_mvelho = nome
    if sexo in 'Mm' and idade > idade_hvelho: # Aqui já coloca o nome e a idade do mais velho, conforme os valores são adicionados
        idade_hvelho = idade
        homem_mvelho = nome

    if sexo in 'Ff' and idade <= 20: # Contagem das mulheres
        contagem_mulheres20 += 1

media_grupo = soma_idades / 4 # Variavel para calcular a média (soma_idades / 4 (são quatro pessoas))

print(f'\nA média de idade é {media_grupo} anos.')
print(f'O homem mais velho tem {idade_hvelho} e ele se chama {homem_mvelho}')
print(f'No grupo tem {contagem_mulheres20} mulheres com menos de 20 anos.')\

