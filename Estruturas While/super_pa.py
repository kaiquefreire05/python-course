print('=-=' * 20)
print(f'Super Progressão Aritmética com WHILE')
print('=-=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
progressao = int(input('Digite a progressão que você deseja: '))

contador = 1 # Váriavel para repetir
valores = primeiro_termo # Valores é a variavel que vai receber os valores da PA
total = 0 # Recebe os valores inicias e os que vão vir depois caso o usuário quiser
mais_valores = 10 # Esse recebe 10 porque a PA inicialmente começa com 10 valores

while mais_valores != 0: # Enquanto ele não recebe 0 ele continua gerando valores
    total += mais_valores # Total recebe mais valores
    while contador < total: # Inicial mente o total começa com 10
        valores += progressao
        print(valores, end='->')
        contador += 1
    print('PAUSA')
    mais_valores = int(input('Você quer mais valores? ')) # Aqui eu decido quantos valores vão receber a mais 
print(f'Prograssão finalizada com {total} valores')



    