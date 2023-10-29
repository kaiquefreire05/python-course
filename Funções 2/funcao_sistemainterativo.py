def ajuda(com):
    help(com)

def mensagem(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(txt)
    print('~' * tamanho)



# Programa principal

comando = ''
while True:
    mensagem('  SISTEMA DE AJUDA PyHELP')
    comando = str(input('Digite a função ou biblioteca: '))
    if comando.upper().strip() == 'FIM':
        break
        print('PROGRAMA FINALIZADO')
    else:
        ajuda(comando)
mensagem('  ATÉ LOGO')