lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis

#print(lanche[-1])
#print(lanche)
#print(len(lanche))

for comida in lanche:
   print(f'Eu vou comer {comida}')
   
for cont in range (0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for posicao, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posicao {posicao}')
print('Comi demais')