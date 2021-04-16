# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
        int(input('Digite um número: '))
       )
if 9 not in num:
    print('O numero 9 não aparece.')
else:
    print(f'O número 9 apareceu: {(num.count(9))}vezes')

if 3 not in num:
    print('Não há o número 3')
else:
    print(num.index(3))

print('Os valores pares digitados foram: ', end='')
for n in num: # Entendendo que os valores em num são copiados para n.
    if n %2 == 0:
        print(n, end=' ')
