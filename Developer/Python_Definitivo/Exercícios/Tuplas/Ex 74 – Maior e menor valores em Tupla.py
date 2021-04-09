# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
lista = (102, 1, 2, 11, 8, 19, 3, 3, 4.1, 4.2)
print(sorted(lista))
'''
import random

lista_numeros = []
lista_tupla = ()
numeros = 0

maior = menor = 0

for c in range(1,6):
    numeros = random.randint(1,500)
    lista_tupla = lista_numeros
    lista_tupla.append(numeros)

    if c == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros


print(lista_tupla)
print(sorted(lista_tupla))
print(maior, menor)