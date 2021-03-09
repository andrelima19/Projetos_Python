# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
peso = []
for pessoa in range(1, 3):
    peso = int(input('Digite o peso: '))
    if maior > peso:
        maior = peso

print(maior)