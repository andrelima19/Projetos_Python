#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#nome, partidas, gols, gols feitos no campeonato, aproveitamento.

analise = dict()

analise['nome'] = str(input('Nome: '))
analise['partida'] = int(input('Jogos: '))

for n in analise['partida']:

    analise['gols'] = int(input(f'Partida: {n} - Gols feitos: {analise["gols"]}: '))
print(f'{analise["partidas"]} - {analise["gols"]}')