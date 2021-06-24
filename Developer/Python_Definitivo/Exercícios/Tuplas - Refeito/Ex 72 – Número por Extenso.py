#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

lista = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove','vinte')

while True:
    escolha = int(input('Digite um número que queira ver por extenso: '))
    if escolha < 0 or escolha > 20:
        break
    print(lista[escolha])

print('Fim')
