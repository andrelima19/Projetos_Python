# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

resp = ' '
masc = fem = adulto = menor_f = 0

while True:
    idade = int(input('Insira sua idade: '))
    if idade > 18:
        adulto = adulto + 1
    genero = str(input('Qual seu Sexo? [M / F]: ')).strip().upper()[0]
    if 'M' in genero:
        masc+=1
    if 'F' in genero:
        fem+=1
        if idade < 20:
            menor_f +=1

    resp = str(input('Deseja continuar? [S / N]: ')).strip().upper()[0]
    if 'N' in resp:
        print(f'A - Pessoas maiores de 18 anos: {adulto}\n'
              f'B - Quantidade de homens cadastrados: {masc}\n'
              f'C - Mulheres com menos de 20 anos: {menor_f}')
        break

