# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().capitalize()
nome = n.split()

print(f'O primeiro nome é: {nome[0]}\n'
      f'O último nome é: {nome[len(nome)-1]}')
