# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()

while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'N':
            break
    else:
        print('Número já existe!')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'N':
            break

numeros.sort()
print(numeros)