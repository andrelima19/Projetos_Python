# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

PrecoProduto = float(input('Informe o preço do produto: '))
NovoPreco = (PrecoProduto - (PrecoProduto * 5/100))

print(f'O novo preço do produto com 5% de desconto é: R${(NovoPreco)},00')
