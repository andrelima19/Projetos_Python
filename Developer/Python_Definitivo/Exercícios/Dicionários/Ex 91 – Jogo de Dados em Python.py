'''NÃO FEITO'''
#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

resultados = {'jogador1':0,'jogador2':0, 'jogador3':0,'jogador4':0}

for j in resultados:
    n = randint(1,7)
    resultados[j] = n
    print(f'O {j} tirou {n} no dado')

print('*=*' * 15)
print('RESULTADOS')
print('*=*' * 15)

print(sorted(resultados.values()))

