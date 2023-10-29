print('=-=' * 20)
print('- ANALISADOR DE TRIANGULOS - ')
print('=-=' * 20)

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('\nPode formar um triângulo!!!')
else:
    print('\nNão pode formar um triângulo')