melhores_times = ('Real Madrid', 'Milan', 'Bayer de Munique', 'Liverpool', 'Barcelona', 'Ajax', 'Manchester United','Inter de Milão', 
                  'Juventus', 'Benfica')

print('=-=' * 20)
print(f'Os primeiros três colocados são: {melhores_times[:3]}')
print('=-=' * 20)
print(f'Os três últimos são: {melhores_times[-3:]}')
print('=-=' * 20)
print(f'{sorted(melhores_times)}')
print('=-=' * 20)
print(f'O barcelona está na {melhores_times.index("Barcelona")} posição')
print('=-=' * 20)