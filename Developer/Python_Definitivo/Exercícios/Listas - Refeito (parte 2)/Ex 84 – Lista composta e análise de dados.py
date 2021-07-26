#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
dados = []
maior = menor = 0
resp = ''

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if len(grupo_pessoas) == 0:
        maior = menor = dados[1]

    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    grupo_pessoas.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

for pessoas in grupo_pessoas:
    if pessoas[1] == maior:
        print(f'{pessoas[0]} foi o/a Mais pesado com {maior}kg')
    if pessoas[1] == menor:
        print(f'{pessoas[0]} foi o/a Mais leve com {menor}kg')

print(f'Quantidade de pessoas cadastradas: {len(grupo_pessoas)}')

