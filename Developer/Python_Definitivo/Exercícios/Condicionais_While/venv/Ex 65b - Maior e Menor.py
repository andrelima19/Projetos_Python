# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = soma = 0
n = 0
maior = 0
menor = 0
while True:
    n = int(input('Digite um número: '))
    if n == -1:
        break
    soma = soma + n
    c +=1
    maior = n
    #if maior >

'''
print(f'soma: {soma}\n'
      f'contador: {c}\n'
      f'media: {(soma/c)}')
'''
