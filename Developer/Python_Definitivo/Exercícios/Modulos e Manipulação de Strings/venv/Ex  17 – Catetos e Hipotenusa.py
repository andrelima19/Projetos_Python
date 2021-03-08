# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# tg (hipotenusa) = CO/CA
from math import hypot

CO = float(input('Informe o comprimento do Cateto Oposto: '))
CA = float(input('Informe o comprimento do Cateto adjacente: '))

print(f'O comprimento da hipotenusa é: {hypot(CO,CA):.2f}')
