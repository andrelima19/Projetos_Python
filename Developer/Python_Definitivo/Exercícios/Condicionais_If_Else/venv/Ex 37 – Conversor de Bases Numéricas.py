# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número e em seguida escolha a base em que deseja convertê-lo: '))
print(f'binario = 1\n'
      f'Octal = 2\n'
      f'Hexadecimal = 3')
base = int(input(f'Escolha uma das opções acima: '))

binario = 1
Octal = 2
Hexadecimal = 3

if base == 1:
    print(f'Binário de {numero}: {bin(numero)}')

elif base == 2:
    print(f'Octal de {numero}: {oct(numero)}')

elif base == 3:
    print(f'Hexadecimal de {numero}: {hex(numero)}')