print('=-=' * 20)
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário?  '))
anos = int(input('Vai pagar em quantos anos? '))
print('=-=' * 20)

mensalidade = casa / (anos * 12)

print(f'\nO valor da mensalidade é de R${mensalidade:.2f}')
if mensalidade > (casa * 100 / 30):
    print('O seu empréstimo não foi aprovado, o valor excede 30% de seu salário')
else: 
    print('Emprestimo aprovado!!! Parabéns.')
