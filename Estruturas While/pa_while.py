print('=-=' * 20)
print(f'Progressão Aritmética com WHILE')
print('=-=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
progressao = int(input('Digite a progressão que você deseja: '))

cont = 1
valores = primeiro_termo

while cont < 10:
    valores += progressao
    print(valores)
    cont += 1