#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
dados = []

resp = ' '
maior = menor = 0

while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(int(input('Informe o peso: ')))
    if len(grupo_pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    grupo_pessoas.append(dados[:])
    dados.clear()

    resp = input('Deseja continuar? ').strip()
    if resp in 'Nn':
        break

# A) Quantas pessoas foram cadastradas.
print(f'Quantidade de pessoas cadastradas: {len(grupo_pessoas)}')

# B)
print(f'Mais pesado: {maior}\n'
      f'Mais leve: {menor}')