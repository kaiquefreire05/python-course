def arquivoExiste(nome):
    try: # Verificando se o arquivo existe.
        a = open(nome, 'rt') # RD = Leitura em modo txt # Vai abrir em modo !!!!
        a.close() # Depois vai fechar
    except FileNotFoundError: # Se o arquivo não existir vai retornar False
        return False
    else: # Senão vai retornar verdadeiro
        return True

def criarArquivo(nome):
    try: # Função criar arquivo
        a = open(nome, 'wt+') # Escreve um arquivo e se ele não existir ele cria.
        a.close()
    except:
        print('Houve um erro na criação de um arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print('Pessoas cadastradas:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar_pessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na escrita no arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Erro ao escrever no arquivo!')
        else:
            print(f'{nome} adicionado com sucesso!')
            a.close()