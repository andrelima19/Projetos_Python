# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. m
# ostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O número {n1} é maior.')
elif n1 < n2:
    print(f'O número {n2} é maior')
else:
    print(f'Os números {n1} e {n2} são iguais.')
