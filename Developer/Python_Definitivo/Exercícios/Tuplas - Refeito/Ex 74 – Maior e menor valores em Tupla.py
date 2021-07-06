# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

'''
from random import randint
lista = ()
for c in range(1,6):
    lista = (randint(1,23)),(randint(1,23)),(randint(1,23)),(randint(1,23)),(randint(1,23))

print(f'Numeros gerados: {lista}\n'
      f'Maior número: {max(lista)}\n'
      f'Menor número: {min(lista)}')


