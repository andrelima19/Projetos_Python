#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_principal = [[],[]]

while True:
    n = int(input('Digite um número: '))
    lista_principal.append(n)

    if n % 2 == 0:
        lista_principal[0].append(n)
    else:
        lista_principal[1].append(n)

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if 'S' not in resp:
        break

print(f'Lista geral: {lista_principal}\n'
      f'Lista com os números pares: {sorted(lista_principal[0])}\n'
      f'Lista com os números impares: {sorted(lista_principal[1])}')