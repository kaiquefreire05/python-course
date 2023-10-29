print('=-=' * 20)
print('SAQUE DE BANCO')
print('=-=' * 20)

nota_um = 0
nota_dez = 0
nota_vinte = 0
nota_cinquenta = 0

valor = int(input('Digite o valor de saque: '))

while True:
    if valor >= 50: # Cédula de cinquenta
        nota_cinquenta += 1
        valor -= 50
    if valor >= 20 and valor < 50: # Cédula de vinte
        nota_vinte += 1
        valor -= 20
    if valor >= 10 and valor < 20: # Cédula de dez
        nota_dez += 1
        valor -= 10
    if valor >= 1 and valor < 10: # Cédula de um 
        nota_um += 1
        valor -= 1
    if valor == 0:
        break

print(f'Foram usados {nota_cinquenta} notas de 50')
print(f'Foram usados {nota_vinte} notas de 20')
print(f'Foram usados {nota_dez} notas de 10')
print(f'Foram usados {nota_um} notas de 1')
    