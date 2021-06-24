#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

tabela = ('Bragantino', 'Athletico-PR', 'Fortaleza', 'Palmeiras', 'Atlético-GO',
          'Atlético-MG', 'Flamengo', 'Fluminense', 'Bahia', 'Santos',
          'Juventude', 'Corinthians', 'Ceará', 'Internacional', 'Sport',
          'Cuiabá', 'Chapecoense', 'São Paulo', 'América-MG', 'Grêmio')

#a) Os 5 primeiros times.
# Primeira forma
#print(tabela[0:5])

print('5 primeiros colocados')
for c in range(0, 5):
    print(f'{c+1}º - {tabela[c]}')

#b) Os últimos 4 colocados.
# Primeira forma
    #print(f'17 - {tabela[-4]}')
    #print(f'18 - {tabela[-3]}')
    #print(f'19 - {tabela[-2]}')
    #print(f'20 - {tabela[-1]}')

print('4 últimos colocados')
for c in range(16, 20):
    print(f'{c}º - {tabela[c]}')

#c) Times em ordem alfabética.
print(sorted(tabela))

#d) Em que posição está o time da Chapecoense.
print(tabela.index('Chapecoense'))