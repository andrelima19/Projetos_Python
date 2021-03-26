#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

classifica = ('Flamengo', 'Internacional', 'São Paulo', 'Cruzeiro', 'Palmeiras',
              'Avaí', 'Atlético-MG', 'Grêmio', 'Goiás', 'Corinthians', 'Chapecoense',
              'Santos', 'Santos', 'Vitória', 'Atlético-PR', 'Botafogo', 'Fluminense',
              'Coritiba', 'Santo André', 'Náutico', 'Sport')

# 5 Primeiros
print(f'1 - {classifica[0]}\n'
      f'2 - {classifica[1]}\n'
      f'3 - {classifica[2]}\n'
      f'4 - {classifica[3]}\n'
      f'5 - {classifica[4]}\n')

# Ultimos 4
print(f'17 - {classifica[-4]}\n'
      f'18 - {classifica[-3]}\n'
      f'19 - {classifica[-2]}\n'
      f'20 - {classifica[-1]}\n')

#c) Times em ordem alfabética.
print(sorted(classifica))

#d) Em que posição está o time da Chapecoense.
print(f'{classifica.index("Chapecoense")+1}')