from math import cos, tan, sin, radians

angulo = float(input(f'Digite o valor do ângulo a calcular: '))

cos = cos(radians(angulo))
tan = tan(radians(angulo))
seno = sin(radians(angulo))

print(f'O cosseno de {angulo} é {cos:.2f}')
print(f'A tangente de {angulo} é {tan:.2f}')
print(f'O seno de {angulo} é {seno:.2f}')