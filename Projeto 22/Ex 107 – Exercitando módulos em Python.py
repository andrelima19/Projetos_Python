'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

import moeda

n = float(input('Digite o preço: R$ '))
print(f'O valor: {n} acrescido de 10% é: {moeda.aumentar(n)}\n'
      f'O valor: {n} reduzido de 15% é: {moeda.diminuir(n)}\n'
      f'O dobro de {n} é: {moeda.dobro(n)}\n'
      f'A metade de {n} é {moeda.metade(n)}')