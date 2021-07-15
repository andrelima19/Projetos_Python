
#  Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
#  lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))
print(f'Matriz [l]: {matriz[l]}')
print(f'Matriz [c]: {matriz[c]}')
print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(matriz[3])


#print('-=' * 30)

#for l in range(0,4):
#    for c in range(0,4):
#       print(f'[{matriz[l][c]:^5}]',end=' ')
#   print()

