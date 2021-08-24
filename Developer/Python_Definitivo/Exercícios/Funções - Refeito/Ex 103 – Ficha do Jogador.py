# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    return f'O jogador {nome} fez {gols} gol(s).'

nome = str(input('Nome do jogador: '))
gol = input('Gol(s) feito(s): ')

if '' in nome:
    nome = 'Desconhecido'

if gol.isnumeric():
    gol = int(gol)

print(ficha(nome, gol))
