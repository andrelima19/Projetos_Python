# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


valor = 0 # int
total_1 = 0
total_10 = 0

'''A ideia é quebrar o valor digitado e separar o dividendo (O valor inteiro da divisão) do resto da divisão'''

valor = int(input('Qual valor você quer sacar? '))
if valor < 10:
    total_1 = valor // 1
    print(f'Total de {total_1} cédulas de R$ 1,00')

elif valor >= 10 and valor <20:
    total_10 = valor // 10 # Valor inteiro
    resto = valor % 10   # Resto do valor
    total_1 = resto // 1

    print(f'Total de {total_10} cédulas de R$ 10,00\n'
          f'Total de {total_1} cédulas de R$ 1.00')
else:
    print('ERRO')
