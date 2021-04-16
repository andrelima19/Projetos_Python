#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Carne', 30.00,
            'Feijão', 5.65,
            'Arroz', 7.00,
            'Margarina', 5.60,
            'Biscoito', 3.00,
            'Alface', 2.50,
            'Maçã', 6.00)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<25}', end=' ')
    else:
        print(f'R$ {produtos[pos]:.2f}')

