
'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

'''
'''
def ficha(jog = 'Desconhecido', gol = 0):
    print(f'O jogador {jog} fez gol(s): {gol}')

# Programa principal

n = str(input('Nome do jogador: '))
g = str(input('Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

ficha(n,g)
'''

def ficha(nome = '', gols = 0): # parametos opcionais - Por serem opcionais eu posso chamar a funçaõ sem eles.
    nome = str(input('Nome: '))
    gols = str(input('Gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador: {nome} fez {gols} gol(s).')

ficha()



