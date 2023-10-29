n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))

m = (n1 + n2) / 2

print(f'\nA sua média foi {m}...')

if m < 5.0:
    print(f'\nVocê foi reprovado!!! Estude mais.')

elif m < 7.0:
    print(f'\nVocê está de recuperação!!! Não desista.')

else:
    print(f'\nParabéns!!! Você foi aprovado.')