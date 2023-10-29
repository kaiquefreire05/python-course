velocidade = int(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    print(f'VOCÊ FOI MULTADO!! O valor da sua multa será R${(velocidade - 80) * 7}, siga as leis de trânsito!!!!!')
else:
    print(f'Sua velocidade é de {velocidade}, tenha um bom dia e dirija com segurança!!!')