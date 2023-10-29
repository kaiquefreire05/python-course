'''
try:
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    r = a / b
except Exception as erro:  # VAI MOSTRAR UMA MENSAGEM DE ERRO E AINDA VAI MOSTRAR USANDO O {erro.__clas__}
    print(f'Problema encontrado foi {erro.__class__}')

else:   # SE NÃO TIVER ERRO VAI MOSTRAR O RESULTADO NORMALMENTE
    print(f'O resultado é {r:.1f}')

finally:   # ESTA MENSAGEM SEMPRE VAI APARECER, INDEPENDENTE DO QUE VAI ACONTECER.
    print(f'Volte sempre, obrigado!!!')
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# SÃO VARIOS TIPOS DE ERROS, MAS CADA UM COM UMA MENSAGEM DIFERENTE (É POSSÍVEL TRATAR CADA UM COMO CONFORME).

except (ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dados que você digitou.')

except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero.')

except KeyboardInterrupt:
    print(f'O usuário não preferiu informar os dados.')

except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')

else:   # SE NÃO TIVER ERRO VAI MOSTRAR O RESULTADO NORMALMENTE
    print(f'O resultado é {r:.1f}')

finally:   # ESTA MENSAGEM SEMPRE VAI APARECER, INDEPENDENTE DO QUE VAI ACONTECER.
    print(f'Volte sempre, obrigado!!!')

