def linha():
    print('-' * 30)

def cabecalho(msg):
    linha()
    print(msg)
    linha()

def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite uma opção: '))
        except (ValueError, TypeError):
            print('ERRO! Digite um valor inteiro válido.')
            continue # JOGA PARA O COMEÇO DO LAÇO NOVAMENTE

        except KeyboardInterrupt:
            print('Entrada de dados foi interrrompida pelo usuário.')
            return 0
        else:
            return n

def menu(lista):
    arquivo = 'nomes_pessoas.txt'
    cabecalho('MENU PRINCIPAL')
    c = 1 # CONTADOR NORMAL
    for item in lista: # PARA CADA ITEM DA LISTA QUE EU COLOQUEI, VAI SER PRINTADO SEPARADO
        print(f'\033[36m{c} - {item}\033[m')
        c += 1
    linha()
    opc = leiaInt('Digite aqui sua opção: ') # USEI A DEF 'LEIAINT' PARA PEGAR EXCLUSIVAMENTE UM NÚMERO INTEIRO
    return opc