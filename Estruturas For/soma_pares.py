soma = 0
contador = 0
for numeros in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        contador += 1
        
print(f'A soma de todos os números pares é {soma}')
print(f'Foram mostrados {contador} numeros pares')