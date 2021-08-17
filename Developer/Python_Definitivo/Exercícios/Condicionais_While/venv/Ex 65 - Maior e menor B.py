## Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = media = c = 0
maior = menor = 0
while True:
    n = (int(input('Digite um número: ')))
    if n == 999:
        print('FIM')
        break
    c+=1
    soma = soma + n

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n

print(f'Maior: {maior}\n'
      f'Menor: {menor}')
'''
print(f'Valores digitados: {c}\n'
      f'Soma dos valores: {soma}'
      f'Maior: {n}'
      f'Menor: {n}')
'''