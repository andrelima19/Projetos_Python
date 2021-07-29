
# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

    # O programa vai ler o nome do jogador e quantas partidas ele jogou.
    # # Depois vai ler a quantidade de gols feitos em cada partida.
    # # No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

cadastro = list()
jogador = dict()
total = 0

while True:
    jogador['nome'] = str(input('Nome: ')).capitalize()
    jogador['partidas'] = int(input('Partidas: '))

    for j in range(jogador['partidas']):
        jogador['gol'] = int(input(f'Gol(s) na Partida {j+1}: '))
        total = total + jogador['gol']
        jogador['total de gols'] = total

    cadastro.append(jogador.copy())
    total = total - total

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate()