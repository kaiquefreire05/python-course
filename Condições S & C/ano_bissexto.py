from datetime import date
ano = int(input('Digite o ano que você quer analisar? '))

if ano == 0: #Mostrando o ano atual se colocar o zero
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Calculando se o ano é bissexto !!!! (IMPORTANTE)
    print(f'O ano {ano} é bissexto')
else: 
    print(f'O ano não é bissexto')