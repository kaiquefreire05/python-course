def voto(ano_nasc):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano_nasc
    if idade < 16:
        return f'Com a idade de {idade} anos: Negado'
    elif idade < 65:
        return f'Com a idade de {idade} anos: Obrigatório'
    else:
        return f'Com a idade de {idade} anos: Opcional'
    
# Programa princial:

ano_nasc = int(input('Digite aqui seu ano de nascimento: '))

print(voto(ano_nasc))