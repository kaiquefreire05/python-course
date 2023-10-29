print('=-=' * 20)
print('10 Primeiros termos de uma PA')
print('=-=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
progressao = int(input('Digite a progressão da PA: '))

decimo_termo = primeiro_termo + (10 - 1) * progressao
for pa in range(primeiro_termo, decimo_termo, progressao):
    print(pa, end=' -> ')