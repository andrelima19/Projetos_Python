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
nota = []
aluno = []
boletim = {}

c = 0
while c < 3:
    c+=1
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota: ')))


print(aluno, nota)
