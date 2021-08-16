'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)

'''
# função notas
# notas, várias notas
# alunos, vários alunos
# dicionário com:
    # Maior nota
    # menor nota
    # média da turma
    # situação

# Passando uma lista para um dic

turma = []
aluno = {}
maior = []
s = 0

for c in range(0,3):
     aluno['nome'] = input('Nome: ')
     aluno['nota1'] = int(input('Nota1: '))
     aluno['nota2'] = int(input('Nota2: '))
     turma.append(aluno.copy())

'''[{'nome': 'a', 'nota1': 3, 'nota2': 2}, {'nome': 'b', 'nota1': 6, 'nota2': 7}]'''

for n in range(len(turma)):
    maior.append(max(turma[n]['nota1'],turma[n]['nota2']))

print(maior)



















