#Exercício 85 – Listas com pares e ímpares
# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

grupo_numeros = []
temp = []
pares = []
impares = []

grupo_numeros.append(pares)
grupo_numeros.append(impares)

for c in range(0,6):
   temp.append(int(input('Digite um número: '))) # Lista "temporaria" recebe os valores
   grupo_numeros.append(temp[:]) # Lista "temporaria" é copiada sem vinculo [:] para a lista principal



print(f'Todos os números: {grupo_numeros}')
print(pares)
#print(pares)
#print(impares)
