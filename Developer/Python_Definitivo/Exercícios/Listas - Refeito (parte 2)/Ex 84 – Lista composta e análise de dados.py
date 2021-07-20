#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
pessoas = []
maior = menor = 0

while True:
    nome = str(input('Informe seu nome: '))
    peso = float(input('Informe seu peso: '))

    pessoas.append(nome)
    pessoas.append(peso)

    if len(grupo_pessoas) == 0:
        pessoas[1] = maior = menor
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    grupo_pessoas.append(pessoas[:])
    pessoas.clear()  # Se não por o Clear o conteúdo de pessoas vai se repetir na lista principal

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break

'''A - Quantidade de pessoas cadastradas'''
print(f'Quantidade de pessoas cadastradas: {len(grupo_pessoas)}')

'''B - Listagem com as pessoas mais pesadas'''

for p in grupo_pessoas:
    if p[1] == maior:
        print(f'O mais pesado foi: {grupo_pessoas[0]} com {grupo_pessoas[1]}Kg')
    elif p[1] == menor:
        print(f'O mais leve foi: {grupo_pessoas[0]} com {grupo_pessoas[1]}Kg')

