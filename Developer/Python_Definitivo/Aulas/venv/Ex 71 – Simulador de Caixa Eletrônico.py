# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


valor = 0 # int
total_1 = 0
total_10 = 0
total_20 = 0
total_50 = 0

'''A ideia é quebrar o valor digitado e separar o dividendo (O valor inteiro da divisão) do resto da divisão'''

valor = int(input('Qual valor você quer sacar? R$ '))

# R$ 1,00
if valor < 10:
    total_1 = valor // 1
    print(f'Total de {total_1} cédulas de R$ 1,00')

# R$ 10,00
elif valor >= 10 and valor <20:
    total_10 = valor // 10 # Valor inteiro
    resto = valor % 10   # Resto do valor
    total_1 = resto // 1

    print(f'Total de {total_10} cédulas de R$ 10,00\n'
          f'Total de {total_1} cédulas de R$ 1.00')

# R$ 20,00
elif valor >=20 and valor <50:
    total_20 = valor // 20
    resto  = valor % 20

    if resto >= 10 and resto <50:
        total_10 = resto // 10
    total_1 = resto % 10

    print(f'20: {total_20}, Resto: {resto}, 10:{total_10}, 1:{total_1}')
    #total_1 = resto - total_10

# R$ 50,00
elif valor >50:
    total_50 = valor // 50
    resto = valor % 50

    if resto >=20 and resto <50:
        total_20 = resto // 20
        total_10 = resto % 20
    total_1 = resto % 10

    print(f'50: {total_50}, Resto: {resto}, 20:{total_20}, 10:{total_10}, 1:{total_1}')

'''
    print(f'Total de {total_20} cédulas de R$ 20,00\n'
          f'Total de {total_10} cédulas de R$ 10.00\n'
          f'Total de {total_1} cédulas de R$ 1.00')
else:
    print('ERRO')
    '''