# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = int(input('Informe um valor em metros: '))
print(f'Convsão em centímetros: {(medida/100)} cm\n'
      f'Conversão em milímetros: {(medida/1000)} mm')