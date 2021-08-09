#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(a,b,c,d):
    if a > b and a > c and a > d:
        print(f'{a} é maior')
    elif b > a and b > c and b > d:
        print(f'{b} é maior')
    elif c > a and c > b and c > d:
        print(f'{c} é maior')
    else:
        print(f'{d} é maior')

maior(a = int(input('Valor de A: ')),
    b = int(input('Valor de B: ')),
    c = int(input('Valor de C: ')),
    d = int(input('Valor de D: '))
)