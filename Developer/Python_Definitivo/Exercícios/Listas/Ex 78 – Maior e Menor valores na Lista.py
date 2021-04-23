#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for c in range(1,6):
    valores.append(int(input('Digite um número: ')))

print(f'Número mais alto: {max(valores)}\n'
      f'Número mais baixo: {min(valores)}\n'
      f'Posição do número maior: {valores.index(max(valores))}\n'
      f'Posição do número menor: {valores.index(min(valores))}')
