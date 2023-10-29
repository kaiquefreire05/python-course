num = [2, 5, 9, 1] # Como criar a lista
num[2] = 3 # Na lista 'num' e a posição 2 eu substitui o valor pelo 3
num.append(7) # Comando para adicionar um número
num.sort(reverse=True) # O comando sort serve para organizar em ordem os valores, usando o reverse=True a lista fica em ordem decrescente
num.insert(2, 0) # Esse comando coloca um valor em tal posição sem substituir o valor antigo 
num.pop(2) # Exclui um valor da lista em tal posição, se ficar vazio ele tira o último valor

if 5 in num:
    num.remove(5) # Esse comando exclui um valor
    print('Número 5 foi excluido')
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista contém {len(num)} elementos')