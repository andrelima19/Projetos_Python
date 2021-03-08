# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# km
# dia

km = float(input('Informe a quantidade de Quilometros percorridos: '))
dia = float(input('Informe quantos dias você alugou o carro: '))
preco = (dia * 60) + (km * 0.15)

print(f'Quilometros percorridos: {km} Km\n'
      f'Dias alugados: {dia}\n'
      f'Preço a pagar: R$ {preco},00')