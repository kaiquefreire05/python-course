def notas(* n, sit=False):
    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n) / len(n)
    if sit:
        if notas['media'] >= 7:
            notas['situação'] = 'BOA'
        elif notas['media'] > 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas


# Programa principal
resp = notas(5.5, 5.2, 1.0, 6.0, sit=True)
print(resp)