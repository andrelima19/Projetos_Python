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

turma = []
aluno = []
boletim = {}

for n in range(0,3):
    # Cadastro de boletim dos alunos
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append(float(input('Nota 3: ')))

    # media de cada aluno
    media = (aluno[1] + aluno[2] + aluno[3])/3

    boletim['media'] = media
    aluno.append(boletim.copy())

    turma.append(aluno[:])
    aluno.clear()

    # Situação da turma

    print()

    #turma.append(aluno.copy())# Adicionando o dicionário a lista "turma"
    #aluno['Nota 1'] = float(input('Nota 1: '))

print(turma)

# Média da turma
