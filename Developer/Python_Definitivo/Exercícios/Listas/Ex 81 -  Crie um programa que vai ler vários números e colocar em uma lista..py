# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numero = 0
lista = []

for c in range(0,5):
    numero = int(input('Digite um número: '))
    lista.append(numero)


#A Quantos números foram digitados
print(len(lista))

#B Lista de valores, ordenada de forma crescente
print(sorted(lista))

# C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print('O número 5 se encontra na lista.')
else:
    print('O número 5 não está na lista')