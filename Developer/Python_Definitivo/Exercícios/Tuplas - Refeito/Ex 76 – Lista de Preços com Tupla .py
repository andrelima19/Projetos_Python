#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Arroz', 'Macarrão', 'Tomate', 'Óleo', 'Pão')
Preco = ('5', '8', '4', '7', '3')

for c in range(0,4):
    print(f'{produtos[c]} ---- R${Preco[c]},00')