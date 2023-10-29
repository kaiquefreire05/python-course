def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite o número inteiro: '))
        except (ValueError, TypeError):
            print('ERRO! Digite um valor inteiro válido.')
            continue # JOGA PARA O COMEÇO DO LAÇO NOVAMENTE

        except KeyboardInterrupt:
            print('Entrada de dados foi interrrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um valor real: '))

        except (ValueError, TypeError):
            print('ERRO! Digite um valor float válido.')
            continue # VAI VOLTAR PARA O COMEÇO DO LAÇO

        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar.')
            return 0

        else:
            return n


# PRGRAMA PRINCIPAL

inteiro = leiaInt('Digite o valor inteiro: ')
real = leiaFloat('Digite um valor real: ')
print(f'A soma entre {inteiro} e {real} é {inteiro + real}')



