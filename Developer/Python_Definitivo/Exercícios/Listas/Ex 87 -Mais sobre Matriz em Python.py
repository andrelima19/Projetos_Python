
#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
soma = 0
soma2 = 0

# Bloco principal
# A Soma dos pares
print(20 * '+=')
print('Questão A - Soma dos pares')
print(20 * '+=')

for lin in range(0,3):
    for col in range(0,3):
        matriz[lin].append(int(input(f'Digite um valor em: [{lin}][{col}]: ')))
        if matriz[lin][col] % 2 == 0:
            soma = soma  + matriz[lin][col]

for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]',end='')
    print()

print(f'Soma dos pares: {soma}')

# B - Soma dos valores da coluna 2
print(20 * '+=')
print('Questão B - Soma dos valores da coluna 2')
print(20 * '+=')

for lin in range(0,3):
    for col in range(1,2):
        soma2 = soma2 + matriz[lin][col]


for lin in range(0,3):
    for col in range(1,2):
        print(f'[{matriz[lin][col]:^5}]',end='')
    print()

print(f'Soma dos valors da coluna 2: {soma2}')

# C - O maior valor da segunda linha.
print(20 * '+=')
print('Questão C - O maior valor da segunda linha.')
print(20 * '+=')

for lin in range(1,2):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]',end='')
    print()
print(f'O maior valor da segunda linha é: {max(matriz[1])}')