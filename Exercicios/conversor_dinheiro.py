reais = float(input('Digite quantos R$, voçê tem: '))

dolarint = reais / 4.95
resdolar = reais % 4.95

print(f'Voçê pode trocar seus reais em: {dolarint:.0f}.{resdolar:.0f} U$')