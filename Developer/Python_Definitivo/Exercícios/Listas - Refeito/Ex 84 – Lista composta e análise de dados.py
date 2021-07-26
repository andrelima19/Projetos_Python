#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
dados = []
resp = ' '
maior = menor = 0
pesadas = []
leves = []

while True:
    n = str(input('Digite seu nome: '))
    dados.append(n)
    n = int(input('Digite seu peso: '))
    dados.append(n)

    if len(grupo_pessoas) == 0:
        dados[1] = maior = menor
    else:
        if dados[1] >  maior:
            pesadas.append(dados[1])
        if dados[1] < menor:
            leves.append(dados[1])

    grupo_pessoas.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break
print(f'Quantidade de pessoas cadastradas: {len(grupo_pessoas)}')

print(pesadas)
print(leves)