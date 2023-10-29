print('=-=' * 20, 'MÉTODOS PAGAMENTOS', '=-=' * 20)

valor = float(input('\nDIgite o valor da compra: '))

print(f'''\n[1]à vista dinheiro/cheque: 10% de desconto
[2]à vista no cartão: 5% de desconto
[3]em até 2x no cartão: preço formal 
[4]3x ou mais no cartão: 20% de juros''')

opcao = int(input('\nDigite a opção desejada(1 a 4): '))

if opcao == 1:
    desc = valor * (10 / 100)
    print(f'\nSua compra de {valor:.2f} com desconto vai ficar {valor - desc:.2f}')
          
elif opcao == 2:
    desc = valor * (5 / 100)
    print(f'\nSua compra de {valor:.2f} com desconto vai ficar {valor - desc:.2f}')

elif opcao == 3:
    parcela = valor / 2
    print(f'\nSua compra de R${valor:.2f} não vai ter desconte e nem aumento, cada parcela vai custar R${parcela:.2f}')

elif opcao == 4:
    qtde_parcela = int(input('\nDigite a quantidade de parcelas: '))

    aumento = valor * (20 / 100)
    parcela = (valor + aumento) / qtde_parcela
    print(f'\nSua compra de R${valor:.2f} divido em {qtde_parcela:.2f} vai custar R${parcela:.2f} por parcela(com aumento de 20%).')

else:
    print('\nOpção inválida')