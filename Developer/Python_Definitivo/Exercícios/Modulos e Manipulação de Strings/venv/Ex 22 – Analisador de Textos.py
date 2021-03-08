'''

Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''



nome = str(input('Digite seu nome completo: '))

print(f'{nome.upper()}\n'
      f'{nome.lower()}\n'
      f'Quantidade de letras c/ espaço: {len(nome)}\n')

div = nome.split() # Criei uma lista com os nomes
print(len(div[4])) # Peguei o tamanho verificando a posição de cada palavra.

