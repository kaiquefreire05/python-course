while True: 
    n_tabuada = int(input('Digite o número da tabuada que você quer ver: ')) # Colocar dentro senão vai entrar em loop

    if n_tabuada < 0: # Colocar antes para que não execute primeiro e depois finalize
        break

    for c in range(0, 11): # Criando tabuada
        print(f'{n_tabuada} * {c} = {n_tabuada * c}')
print('Programa encerrado')