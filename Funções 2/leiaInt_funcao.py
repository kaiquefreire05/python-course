def leiaInt(msg):
    ok = False # Vai servir como ponto de término
    valor = 0
    while True:
        n = str(input(msg)) # A várivel n vai ser inteiro (aqui que começa o código
        if n.isnumeric(): # Se o n for numérico o 'valor' vai receber um inteiro de 'n'
            valor = int(n)
            ok = True # Nesse ponto vai ser terminado o código
        else: # Mensagem de erro
            print(f'\033[0;31mERRO! Digite um número válido.\033[m')
        if ok: # Se o ok for 'true' BREAK
            break
    return valor # Tudo isso para retornar valor.
# Programa principal

n = leiaInt('Digite um número: ') # Mensagem qualquer para aparecer primeiro (vai tudo acontecer no código)
print(f'Você acabou de digitar o número {n}.')