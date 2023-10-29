tupla_precos_primeira_forma = (('Placa de Vídeo', 2000), ('Processador', 1500), ('Memória', 500), ('Placa Mãe', 1200), ('Fonte', 600), ('Gabinete', 200), 
                ('Water Cooler', 300))

# Acima da primeira forma 

tupla_precos = ('Placa de Vídeo', 2000, 'Processador', 1500, 'Memória', 500, 'Placa Mãe', 1200, 'Fonte', 600, 'Gabinete', 200, 
                'Water Cooler', 300)

print('=-=' * 20)
print('TABELA DE PREÇOS PC')
print('=-=' * 20)

for produto, valor in tupla_precos_primeira_forma:
   print(f'{produto} ------- R$ {valor}')
print('=-=' * 20)

# Acima da primeira forma

for c in tupla_precos:
    if type(c) == str: 
        print(f'{c:.<20} ', end='')
    else: 
        print(f'R$ {c}')