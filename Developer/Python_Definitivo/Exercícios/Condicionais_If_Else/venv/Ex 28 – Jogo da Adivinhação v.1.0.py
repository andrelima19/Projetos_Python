# Exercício Python 28: Escreva um programa que faça o computador
# “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
usuario = int(input('Adivinhe o número que estou pensando: '))
computador = randint(0,5)

if usuario == computador:
    print('Você acertou!')
    print(f'Número que pensei: {computador}')
else:
    print('Você errou o número.')
    print(f'Número que pensei: {computador}')
