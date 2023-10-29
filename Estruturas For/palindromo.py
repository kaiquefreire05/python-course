frase = str(input('Digite aqui a frase ou nome: ')).strip().lower() # Escrevi a frase removendo espaços(strip) e 
#(colocar todas as letras em minusculos)
palavras = frase.split() # Usei o split para gerar uma lista 
tudo_junto = ''.join(palavras) # Juntei tudo em uma única string
inverso = ''

for f in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[f]
print(f'\n{frase}, {inverso}')
if frase == inverso:
    print(f'\nÉ um palíndromo!')
else: 
    print(f'\nNão é um palíndromo')
