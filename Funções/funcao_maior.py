from time import sleep

def maior(* numeros):
    print('~' * 30)
    print('Analisando os valores passados')
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor foi {max(numeros)}.')


# PROGRAMA PRINCIPAL

maior(0, 2, 3, 6, 4, 5)
maior(89, 36, 25, 488, 123, 584)
maior(58, 63, 51 ,78, 298, 51915, 8489516)
maior(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
