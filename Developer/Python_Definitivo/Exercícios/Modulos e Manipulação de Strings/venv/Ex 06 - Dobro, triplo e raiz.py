# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import*

numero  = float(input('Digite um número: '))
print(f'O dobro de {numero} é: {numero * numero}.\nO triplo do número {numero} é: {numero * numero * numero}\n'
      f'A raiz de {numero} é: {(sqrt(numero))}')