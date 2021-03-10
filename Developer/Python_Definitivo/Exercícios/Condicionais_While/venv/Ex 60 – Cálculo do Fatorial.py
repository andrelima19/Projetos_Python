#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120


n = int(input('Insira um número: '))
c = n
fat = 1
while c > 0:
    print(c)
    fat = fat * c
    c -= 1

print(fat)


    