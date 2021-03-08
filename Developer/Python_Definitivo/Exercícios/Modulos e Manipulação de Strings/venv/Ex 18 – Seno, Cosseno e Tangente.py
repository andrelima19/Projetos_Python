# Exercício Python 18: Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Informe o ângulo do triângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Seno: {seno:.2f}\n'
      f'Coseno: {coseno:.2f}\n'
      f'Tangente: {tangente:.2f}')
