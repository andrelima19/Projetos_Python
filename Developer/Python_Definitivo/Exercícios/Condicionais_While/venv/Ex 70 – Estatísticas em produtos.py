# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

nome = resp = ' '
preco = total = 0
produto = 0
barato = caro = 0

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço: '))
    
    if total > 1000:
        produto +=1
    total = total + preco


    resp = str(input('Deseja continuar comprando? ')).strip().upper()[0]
    if 'N' in resp:
        print(f'A - Total gasto na compra: {total}\n'
              f'B - Qtd de produtos que custam mais de R$ 1000,00: {produto}')
        break