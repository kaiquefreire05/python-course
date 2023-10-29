import urllib.request, urllib.error

def verificar_conexao(url):
    try:
        urllib.request.urlopen(url)
        print('Conexão bem sucedida!')
    except urllib.error.URLError:
        print('Não foi possível estabelecer uma conexão. Verifique sua conexão de internet.')
    except Exception as erro:
        print(f'Ocorreu um erro na requisição: {erro}')


# PROGRAMA PRINCIPAL

url = str(input('Digite aqui o site: '))
verificar_conexao(url)