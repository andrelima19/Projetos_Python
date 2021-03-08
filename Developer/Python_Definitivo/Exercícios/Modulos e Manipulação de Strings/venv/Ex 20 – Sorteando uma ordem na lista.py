# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
# trabalhos dos alunos. # Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1 = str(input('Informe seu nome: '))
nome2 = str(input('Informe seu nome: '))
nome3 = str(input('Informe seu nome: '))
nome4 = str(input('Informe seu nome: '))

lista = [nome1, nome2, nome3, nome4] # Lista ordenada
shuffle(lista) # Lista embaralhada

print(f'A ordem sorteada foi: {lista}')