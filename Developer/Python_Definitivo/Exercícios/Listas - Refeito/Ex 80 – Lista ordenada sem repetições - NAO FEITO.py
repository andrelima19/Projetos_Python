#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numero = 0
lista = []

for c in range(0,4):
    numero = int(input('Digite um número: '))
    if numero > lista[0]:
         lista.append(numero[1])
    else:
         lista.append(numero[0])

print(lista)
