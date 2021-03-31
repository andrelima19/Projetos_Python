# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
lista = (102, 1, 2, 11, 8, 19, 3, 3, 4.1, 4.2)
print(sorted(lista))
'''

lista_numeros = []
numeros = 0

for c in range(1,3):
    numeros = int(input('Digite um número: '))
    lista_numeros.append(numeros)

print(lista_numeros)