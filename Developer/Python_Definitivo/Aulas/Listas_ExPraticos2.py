valores = []

valores.append(2)
valores.append(4)
valores.append(3)

print(valores)

for v in valores:
    print(f'{v}...')


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(10*'#')
# Lendo valores e colocando na lista

lista = []
#for cont in range(0,3):
#    lista.append(int(input('Informe um número: ')))

#for posicao, l, in enumerate(lista):
#    print(f'Na posição {posicao} encontrei o valor: {l}')
#print(lista)

# Fazendo uma LIGAÇÃO entre duas listas
a = [2,3,4,5]
b = a
b[2] = 11

print(f'Lista a: {a}\n'
      f'lista b: {b}')

a = [2,3,4,5]
b = a
b[2] = 11 # Como é uma ligação, o que o valor inserido numa lista é replicado na outra

print(a,b)

# Copiando os valores de uma lista e passando pra outra
#**************************#
#Ligando duas listas para mostrar a diferença
lista1 = [1,2,3,4]
lista2 = lista1
print(lista1, lista2)

#Copiando os valores de uma lista para outra
lista1 = [1,2,3,4]
lista2 = lista1[:]
lista2[2] = 8  # Como é uma cópia, o valor inserido numa lista não é replicado na outra
print(lista1,lista2)
