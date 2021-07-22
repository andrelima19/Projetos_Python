#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# a - Ler 5 valores e guardar numa lista
#b - Maior e menor
#c - Posições

lista = []

for c in range(1,6):
    num = int(input('Digite um valor: '))
    lista.append(num)

print(f'Valores da lista: {lista}')
print(f'O maior valor é: {max(lista)}\n'
      f'O menor valor é: {min(lista)}')

for i, v in enumerate(lista):
    print(f'No índice: {i} encontrei o valor: {v}')
