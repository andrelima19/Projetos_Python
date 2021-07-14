#Exercício 85 – Listas com pares e ímpares
# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

grupo_numeros = [[],[]]
num = 0

for c in range(1,8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        grupo_numeros[0].append(num)
    else:
        grupo_numeros[1].append(num)

# A - Lista de números:
print(grupo_numeros)

# B - Ordem crescente
print(f'Valores pares: {sorted(grupo_numeros[0])}\n'
      f'{30 * "*"}\n'
      f'Valores impares: {sorted(grupo_numeros[1])}')

