# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

'''
def area(largura, comprimento):
    largura = int(input('Informe a largura: '))
    comprimento = int(input('Informe o comprimento: '))

    print(f'A área do terreno é: {(largura * comprimento)} metros²')


area(largura=0,comprimento=0)
'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno é:{a}metros²')

larg = float(input('Lagura: '))
comp = float(input('Comprimento: '))

area(larg, comp)