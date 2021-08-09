#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e  vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# numeros = []
# def sorteio() - Sortear 5 números e colocar dentro da lista
# def somaPar() - Somar valores pares

from random import randint
from time import sleep
'''
numeros = []
def sorteio(soma):
    for n in range(0,5):
        print(n)
        numeros.append(randint(1, 10))
        if numeros[n] % 2 == 0:
            soma = soma + numeros[n]
    print(f'Números gerados: {numeros}\n'
          f'Soma dos números pares: {soma}')

sorteio(soma=0)
'''

numeros = []
soma = 0
def sorteio():
    for n in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Números gerados: {numeros}')


def somaPar(sorteio, soma):
    for n in range(0, 5):
        if numeros[n] % 2 == 0:
            soma = soma + numeros[n]
    print(f'Soma dos valores pares: {soma}')

somaPar(sorteio(), soma)