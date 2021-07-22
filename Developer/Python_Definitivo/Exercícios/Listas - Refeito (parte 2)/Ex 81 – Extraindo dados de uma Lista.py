# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break

print(f'Quantidade de números digitados: {len(numeros)}\n'
      f'Números em ordem crescente: {sorted(numeros)}\n')

if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista.')