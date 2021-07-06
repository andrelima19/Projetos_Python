# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.
par = []
impar = []
lista = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))

print(lista)
# A) Quantas vezes apareceu o valor 9.

print(lista.count(9))

# B) Em que posição foi digitado o primeiro valor 3.
print(lista.index(3))

# C) Quais foram os números pares.
'''Primeira forma'''
'''
if lista[0] % 2 == 0:
    print(f'O número: {lista[0]} é PAR')
if lista[1] % 2 == 0:
    print(f'O número: {lista[0]} é PAR')
if lista[2] % 2 == 0:
    print(f'O número: {lista[0]} é PAR')
if lista[3] % 2 == 0:
    print(f'O número: {lista[0]} é PAR')
'''
for c in range(0,4):
    if lista[c] % 2 == 0:
        #print(f'Número: {lista[c]} é PAR')
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(f'Os numeros pares foram: {(par)} e os impares foram: {impar}')