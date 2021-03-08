# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

# math.ceil(x)
# Retorna o teto de x, o menor inteiro maior ou igual a x.

from math import ceil

numero = float(input('Digite um número qualquer: '))

print(f'Número: {ceil(numero)}')