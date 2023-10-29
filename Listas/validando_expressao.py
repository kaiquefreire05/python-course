expressao = str(input('Digite a sua expressão: '))
lista_parenteses = []

for simb in expressao: # Para cada símbolo em expressão
    if simb == '(':
        lista_parenteses.append('(')
    elif simb == ')':
        if len(lista_parenteses) > 0:
            lista_parenteses.pop()
        else: 
            lista_parenteses.append(')')
            break
if len(lista_parenteses) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é inválida!')
    
