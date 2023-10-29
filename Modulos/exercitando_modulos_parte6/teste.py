from Modulos.exercitando_modulos_parte6.utilidadescev import dados
from Modulos.exercitando_modulos_parte6.utilidadescev import moeda

p = dados.leiaDinheiro('Digite o preço: R$ ')
aumento = int(input('Digite  o aumento: '))
reducao = int(input('Digite a reduçao: '))

moeda.resumo(p, aumento, reducao)