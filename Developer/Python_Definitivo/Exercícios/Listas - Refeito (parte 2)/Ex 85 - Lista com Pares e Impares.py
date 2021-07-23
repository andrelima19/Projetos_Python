#Exercício 85 – Listas com pares e ímpares
# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

lista_princ = [[],[]]

while True:
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        lista_princ[0].append(n)
    else:
        lista_princ[1].append(n)

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

print(lista_princ)




