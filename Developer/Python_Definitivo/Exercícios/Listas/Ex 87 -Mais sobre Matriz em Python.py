
#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
soma = 0
for lin in range(0,3):
    for col in range(0,3):
        matriz[lin].append(int(input(f'Insira os valores em [{lin}][{col}]: ')))
    if matriz[[]] % 2 == 0:



print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])




for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()

# A - Soma dos valores


