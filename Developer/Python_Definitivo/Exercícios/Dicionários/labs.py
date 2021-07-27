'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] <4:
    aluno['situacao'] = 'Reprovado'
elif aluno['media']>=4 and aluno['media'] <=7:
    aluno['situacao'] = 'Em Recuperação'
else:
    aluno['situacao'] = 'Aprovado'

print(aluno.items())
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
'''

