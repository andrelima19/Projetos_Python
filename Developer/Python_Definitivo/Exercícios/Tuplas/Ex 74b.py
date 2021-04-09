from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'{(lista)}\n', end=' ')

print(f'Maximo: {(max(lista))}\n'
      f'Mínimo: {min(lista)}')

