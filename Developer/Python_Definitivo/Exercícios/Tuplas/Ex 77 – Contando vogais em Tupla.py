#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('Andre','Maria', 'Ana', 'Joao')
vogais = ('a', 'e', 'i', 'o', 'u')

nome = 'Ana Maria'

if vogais[0] or vogais [1] or vogais [2] or vogais [3] or vogais [4] in nome:
    print(f'O nome: {nome} possui as vogais {vogais[0], vogais[1], vogais[2], vogais[3], vogais[4]}')
else:
    print('ERRO')