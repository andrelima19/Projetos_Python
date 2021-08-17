# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f'Área: {area}m²')

# programa principal
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)

