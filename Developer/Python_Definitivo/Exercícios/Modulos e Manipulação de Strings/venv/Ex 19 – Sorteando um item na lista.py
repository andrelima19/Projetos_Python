# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
# choice: Sorteia elementos numa sequencia. Podem ser numericos ou strings.

nome01 = input('Digite seu nome: ')
nome02= input('Digite seu nome: ')
nome03 = input('Digite seu nome: ')
nome04 = input('Digite seu nome: ')

lista = [nome01, nome02, nome03, nome04]

print(f'O nome sorteado foi: {random.choice(lista)}')