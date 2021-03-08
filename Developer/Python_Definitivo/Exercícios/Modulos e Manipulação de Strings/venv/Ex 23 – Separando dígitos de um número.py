# Exercício Python 23: Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número: '))

div = str(numero)
print(f'Unidade: {div[0]}\n'
      f'Dezena: {div[1]}\n'
      f'Centena: {div[2]}\n'
      f'Milhar: {div[3]}')