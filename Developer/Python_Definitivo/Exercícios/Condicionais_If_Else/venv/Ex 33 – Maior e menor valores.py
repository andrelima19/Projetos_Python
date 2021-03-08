# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Informe um primeiro número: '))
n2 = float(input('Informe um segundo número: '))
n3 = float(input('Informe um terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior')

elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior')

else:
    print(f'{n3} é o maior')