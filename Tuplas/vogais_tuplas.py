tupla_palavras = ('KAIQUE', 'FREIRE', 'PROGRAMADOR', 'CIENTISTA', 'COMPUTACAO', 'DESENVOLVEDOR')
vogais = ('A', 'E', 'I', 'O', 'U')

print('=-=' * 20)
for p in tupla_palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
print(f'\nFim das palavras')
print('=-=' * 20)