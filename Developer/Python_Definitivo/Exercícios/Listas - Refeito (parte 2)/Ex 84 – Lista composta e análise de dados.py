#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo_pessoas = [[],[],[],[]]
maior = menor = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    grupo_pessoas[0].append(nome)
    grupo_pessoas[1].append(peso)

    if len(grupo_pessoas) == 0:
        grupo_pessoas[1] = maior = menor
    else:
        if grupo_pessoas[1] > maior:
            maior = grupo_pessoas[1]
        if grupo_pessoas[1] < menor:
            menor = grupo_pessoas[1]

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

print(f'Lista de pessoas: {grupo_pessoas}\n'
      f'Nome: {grupo_pessoas[0]}\n'
      f'Peso: {grupo_pessoas[1]}\n')
print(grupo_pessoas)