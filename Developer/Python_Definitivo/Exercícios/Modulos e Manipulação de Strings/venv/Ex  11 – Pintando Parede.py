"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

"""

#largura = 0
#altura = 0
#area = 0
#QtdTinta = 0

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = altura * largura

print(f'Largura: {largura} metros\n'
      f'Altura: {altura} metros\n'
      f'Área: {area} metros²')

print(f'A quantidade de litros para pintar a parede será: {(area/2)}l')

