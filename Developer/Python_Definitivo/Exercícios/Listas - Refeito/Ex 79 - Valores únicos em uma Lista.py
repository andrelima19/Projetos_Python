# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numero = 0
lista = []

while True:
    numero = int(input('Digite um número menor que 100: '))
    if numero > 100:
        break
    else:
        lista.append(numero)

lista.sort()
print(f'Números digitados: {lista}')