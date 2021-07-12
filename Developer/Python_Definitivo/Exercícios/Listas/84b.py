#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
pessoas = []
mais_pesados = []
mais_leves = []

maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(grupo_pessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    grupo_pessoas.append(pessoas[:])

    pessoas.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

for p in grupo_pessoas:
    if p[1] == maior:
        print(f'{p[0]} foi o mais pesado com {p[1]}Kg\n')
    elif p[1] == menor:
        print(f'{p[0]} foi o mais leve com {p[1]}Kg\n')

print(f'Os dados foram: {grupo_pessoas}\n'
      f'As pessoas cadastradas foram: {len(grupo_pessoas)}\n'
      f'A pessoa mais pesada tem: {maior}Kg\n'
      f'A pessoa mais leve tem: {menor}Kg')

