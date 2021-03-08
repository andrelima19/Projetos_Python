# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira =  float(input('Informe quanto você tem na carteira: '))

print(f'O dolar está valendo $ 5,44  você tem R${carteira},00 e pode comprar R${(carteira/5.44)},00')