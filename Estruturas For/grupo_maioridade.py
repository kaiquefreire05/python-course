from datetime import date # Importação para o datetime
ano_atual = date.today().year # Importei datetime e peguei o ano atual
contagem_maior = 0 # Criei uma contagem para pessoas que atingiram a maioriadade
contagem_menor = 0 # Criei uma contagem para pessoas que ainda não são de maior
for ano_nasc in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: ')) # Input 7 vezes
    if ano_atual - ano >= 18:
        contagem_maior += 1
    else:
        contagem_menor += 1

print(f'{contagem_maior} pessoas atingiram a maioridade')      
print(f'{contagem_menor} pessoas não atingiram a maioridade')       