#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#nome, partidas, gols, gols feitos no campeonato, aproveitamento.

analise = dict()
partida = 1

analise['total de gols'] = 0
analise['nome'] = str(input('Nome: '))
analise['total partida'] = int(input('Jogos: '))

while partida <= analise['total partida']:
    analise['gols feitos'] = int(input(f'Gol(s) feito na partida {partida}: '))
    partida +=1
    analise['total de gols'] = analise['gols feitos'] + analise['total de gols']

print(f'Total de partidas disputadas: {analise["total partida"]}\n'
      f'Total de gols feitos: {analise["total de gols"]}')
