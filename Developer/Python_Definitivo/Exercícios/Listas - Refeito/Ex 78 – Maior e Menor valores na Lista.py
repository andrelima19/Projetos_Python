#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# a - Ler 5 valores e guardar numa lista
#b - Maior e menor
#c - Posições

valor = 0
lista = []

for c in range(0,5):
    valor = int(input('Digite um número: '))
    lista.append(valor)

print(f'Números inseridos: {lista}\n'
      f'Maior: {max(lista)} * Menor: {min(lista)}\n')

for cont in range (0,5):
        print(f'Número: {lista[cont]} -- Posição: {lista.index(lista[cont])}')