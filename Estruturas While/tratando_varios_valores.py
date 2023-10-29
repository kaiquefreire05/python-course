soma = 0
contador = 1

n = int(input('Digite um valor [999 para a execução]: '))

while not n == 999:
    soma += n
    contador += 1
    n = int(input('Digite um valor [999 para a execução]: '))
print(f'A execução parou, a soma de todos os valores são {soma} e você digitou {contador}')