#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezesete', 'dezeoito', 'dezenove','vinte')

while True:
    n = int(input('Digite um número: '))
    if n >=0 and n<=20:
        print(f'{c[n]}')