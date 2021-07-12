#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

grupo_pessoas = []
pessoas = []
resp = ''
mais_pesado = mais_leve = 0
c = 0

while 'n' not in resp:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    grupo_pessoas.append(pessoas[:])
    c +=1

    if c == 1:
        mais_pesado = mais_leve = pessoas[1]
    else:
        if pessoas[1] > mais_pesado:
            mais_pesado = pessoas[1]
        if pessoas[1] < mais_leve:
            mais_leve = pessoas[1]

    resp = str(input('Deseja continuar? ')).strip().lower()
    pessoas.clear()

print(grupo_pessoas)

#  A) Quantas pessoas foram cadastradas.
print(f'Quantidade de pessoas: {c}')

print(f'Mais pesados: {mais_pesado} - Mais leves: {mais_leve}')