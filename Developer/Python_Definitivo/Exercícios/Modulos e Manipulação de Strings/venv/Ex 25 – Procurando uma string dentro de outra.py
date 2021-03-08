# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: '))
verificacao = "SILVA" in nome

if verificacao == True:
    print('Tem SILVA no nome')
else:
    print('Não tem SILVA no nome')