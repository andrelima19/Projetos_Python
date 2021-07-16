#  Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
#  lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[1,2],[3,4],[5,6]]
'''
Temos aqui uma lista principal chamada de matriz.
Nela possuímos 3 listas secundárias que servirão como as linhas da matriz
Dentro de cada sublista temos 2 valores que servirão como colunas na matriz
Logo, temos uma matriz com 3 linhas e 2 colunas - Matriz 3 x 2
'''

'''
soma1 = matriz[0][0] + matriz[0][1]
soma2 = matriz[1][0] + matriz[1][1]
soma3 = matriz[2][0] + matriz[2][1]
print(soma1)
print(soma2)
print(soma3)
'''

'''
soma =0
for lin in range(0,3):
    for col in range(0,2):
        soma = soma + matriz[lin][col]
        print(soma)
print(f'Total da soma dos valores: {soma}')

print(matriz)
'''

for lin in range(0,3):
    for col in range(0,2):
        print(f'[{matriz[lin][col]}]', end='')
    print()

