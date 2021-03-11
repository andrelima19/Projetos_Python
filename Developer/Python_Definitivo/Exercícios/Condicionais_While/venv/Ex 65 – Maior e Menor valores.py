# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = media = c = 0
maior = menor = 0
resp = ''
while resp in 'S':
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar inserindo valores? ')).strip().upper()[0]
    #soma = soma + n
    #media = (soma/c)
    c = c + 1
    if c ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(maior, menor)

