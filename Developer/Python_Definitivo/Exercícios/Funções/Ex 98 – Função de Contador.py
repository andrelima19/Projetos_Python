'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep

def contador(c):
    for c1 in range(1, 11, 1):
        print(c1, end=' ')
        sleep(0.5)
        c += 1
    print(' Fim')
    print()
    if c == 10:
        for c2 in range(10, 0, -2):
            print(c2, end=' ')
            sleep(0.5)
        print(' Fim')
        print()

        if c == 10:
            inicio = int(input('Inicio: '))
            fim = int(input('Fim: '))
            salto = int(input('Intervalo: '))

            for c3 in range(inicio, fim, salto):
                print(c3, end=' ')
                sleep(0.5)

contador(0)
