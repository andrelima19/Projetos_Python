# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

A = float(input('Informe o lado A do triangulo: '))
B = float(input('informe o lado B do triângulo: '))
C = float(input('Informe o lado C do triângulo: '))

if (A + B) > C and (A + C ) > B and (B + C) > A:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
