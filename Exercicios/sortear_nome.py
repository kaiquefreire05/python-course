import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
n5 = input('Digite o quinto nome: ')

lista = [n1, n2, n3, n4, n5]

print(f'O aluno sorteado foi {random.choice(lista)}')