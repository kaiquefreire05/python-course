from interface import *
from time import sleep
from manipulacao_arquivo import *

# PROGRAMA PRINCIPAL

arq = 'pessoas_projeto.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não existe!')
    criarArquivo(arq)

while True: # Colquei tudo em um laço para pegar a resposta
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    # Chamei a def 'menu' e a variavel memoria recebe o própio menu.

    if resposta == 1:
        linha()
        # Opção de listar pessoas escritas no arquivos.
        print('\033[34mPrimeira opção - VER PESSOAS CADASTRADAS\033[m')
        lerArquivo(arq)
        linha()

    elif resposta == 2:
        linha()
        print('\033[34mSegunda opção - CADASTRAR NOVA PESSOA\033[m')
        linha()
        nome = str(input('Digite o nome da pessoa: '))
        idade = leiaInt('Digite a idade da pessoa: ')

        cadastrar_pessoa(arq, nome, idade)

    elif resposta == 3:
        linha()
        print('\033[34mSISTEMA ENCERRADO\033[m')
        linha()
        break

    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
