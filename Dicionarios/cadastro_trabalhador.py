from datetime import datetime

carteira_trabalho = {}

carteira_trabalho['nome'] = str(input('Nome: '))
carteira_trabalho['ano_nascimento'] = int(input('Digite a data de nascimento: '))
carteira_trabalho['codigo'] = int(input('Carteira de Trabalho[0 não tem]: '))
carteira_trabalho['idade'] = datetime.now().year - carteira_trabalho['ano_nascimento']

if carteira_trabalho['codigo'] == 0:

    print('=-=' * 15)
    for k, v in carteira_trabalho.items():
        print(f'{k} tem o valor de {v}')
    print('=-=' * 15)

else:
    carteira_trabalho['ano_contratação'] = int(input('Digite o que ano que foi contratado/a: '))
    carteira_trabalho['salario'] = float(input('Digite seu salário: '))
    carteira_trabalho['data_aposento'] = carteira_trabalho['idade'] + ((carteira_trabalho['ano_contratação'] + 35) - datetime.now().year)
    print('=-=' * 15)
    for k, v in carteira_trabalho.items():
        print(f'{k} tem o valor de {v}')
    print('=-=' * 15)