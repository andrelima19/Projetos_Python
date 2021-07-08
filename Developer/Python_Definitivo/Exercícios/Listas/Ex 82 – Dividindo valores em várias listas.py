#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numero = 0
lista1 = []
lista_par = []
lista_impar = []

# Criação de lista padrão
for c in range(0,5):
    numero = int(input('Digite um número: '))
    lista1.append(numero)

# Distribuição dos conteúdos da lista1 para as demais listas
for cont in range(0,5): # laço for criado
    if lista1[cont] % 2 == 0: # Se o valor que estiver na lista 1 f
        lista_par.append(lista1[cont])
    else:
        lista_impar.append(lista1[cont])

print(f'Números da lista: {lista1}\n'
      f'Números da lista de pares: {lista_par}\n'
      f'Números da lista de impares: {lista_impar}')